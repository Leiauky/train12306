import json
import re
import threading
import time

from requests import Session
from selenium.webdriver import Edge

from ChinaRailwayApi.InfoQuery import InfoQuery
from ChinaRailwayApi.OrderTicket import OrderTicket
from ChinaRailwayApi.PayTicket import PayTicket
from ChinaRailwayApi.QueryTicket import QueryTicket
from ChinaRailwayApi.UserInfo import UserInfo
from Other import Tools
from Other.Config import GlobalConfig, PathConfig
from Other.MyError import PassengerError, MyError
from Other.Tools import check_station_name


class Ticket(object):
    def __init__(self, session: Session, train_date: str, from_station: str, to_station: str, train_code: str,
                 passengers: dict) -> None:
        """

        :param train_date: eg: '2023-04-19'
        :param from_station: eg: '南昌'
        :param to_station: eg: '哈尔滨'
        :param train_code: eg: 'Z112'
        :param passengers: eg: {'张三': (SeatType.HARD_SLEEPER, TicketType.ADULT_TICKETS),'李四': (SeatType.HARD_SEAT, TicketType.ADULT_TICKETS),...}
        """
        # 乘车日期
        self.__train_date = self.__set_train_date(train_date=train_date)
        # 上车车站
        self.__from_station = self.__set_from_station(from_station=from_station)
        # 下车车站
        self.__to_station = self.__set_to_station(to_station=to_station)
        # 车次
        self.__train_code = self.__set_train_code(session=session, train_code=train_code)
        # 乘车人信息
        self.__passengers_info = self.__set_passengers_info(session=session, passengers=passengers)
        # 车票信息
        self.__ticket_info = self.__set_ticket_info(session=session)
        #
        self.__tokens = None

    def __update_tokens(self, tokens: dict) -> None:
        """
        更新tokens
        :param tokens:
        :return:
        """
        if not self.__tokens:
            self.__tokens = {}
        self.__tokens.update(tokens)

    def __clean_init_dc_text(self, init_dc_text: str) -> None:
        """

        :param init_dc_text:
        :return:
        """
        init_dc_path = r'%s\%s.html' % (PathConfig.get_init_dc_root_path(), threading.current_thread().name)
        global_repeat_submit_token = re.findall(r"globalRepeatSubmitToken = '(.*)?';", init_dc_text)[0]
        _json_att = re.findall(r'name="_json_att" value="(.*)?"', init_dc_text)[0]
        _json_att = _json_att if _json_att else ''

        ticket_info_for_passenger_form_str = re.findall(r"ticketInfoForPassengerForm=(.*)?;", init_dc_text)[0].replace(
            "'", '"')
        ticket_info_for_passenger_form = json.loads(ticket_info_for_passenger_form_str)

        cancel_flag = ticket_info_for_passenger_form['orderRequestDTO']['cancel_flag']
        cancel_flag = cancel_flag if cancel_flag else '2'

        bed_level_order_num = ticket_info_for_passenger_form['orderRequestDTO']['bed_level_order_num']
        bed_level_order_num = bed_level_order_num if bed_level_order_num else '000000000000000000000000000000'

        choose_seat = ticket_info_for_passenger_form['orderRequestDTO']['choose_seat']
        choose_seat = choose_seat if choose_seat else ''

        is_jy = re.findall(r"is_jy = '(.*)?';", init_dc_text)[0]
        is_cj = re.findall(r"is_cj = '(.*)?';", init_dc_text)[0]

        tokens = {'globalRepeatSubmitToken': global_repeat_submit_token,
                  '_json_att': _json_att,
                  'cancel_flag': cancel_flag,
                  'bed_level_order_num': bed_level_order_num,
                  'tour_flag': ticket_info_for_passenger_form['tour_flag'],
                  'train_date': ticket_info_for_passenger_form['orderRequestDTO']['train_date'],
                  'train_no': ticket_info_for_passenger_form['orderRequestDTO']['train_no'],
                  'station_train_code': ticket_info_for_passenger_form['orderRequestDTO'][
                      'station_train_code'],
                  'from_station_telecode': ticket_info_for_passenger_form['orderRequestDTO'][
                      'from_station_telecode'],
                  'to_station_telecode': ticket_info_for_passenger_form['orderRequestDTO'][
                      'to_station_telecode'],
                  'leftTicketStr': ticket_info_for_passenger_form['leftTicketStr'],
                  'purpose_codes': ticket_info_for_passenger_form['purpose_codes'],
                  'train_location': ticket_info_for_passenger_form['train_location'],
                  'key_check_isChange': ticket_info_for_passenger_form['key_check_isChange'],
                  'choose_seat': choose_seat,
                  'is_jy': is_jy,
                  'is_cj': is_cj,
                  'init_dc_path': init_dc_path}

        self.__update_tokens(tokens=tokens)

        pattern = re.compile(r'<title>中国铁路12306网站</title>')
        repl = r'<title>中国铁路12306网站</title>\n<base href="https://kyfw.12306.cn/" target="_blank">'
        init_dc_text = re.sub(pattern=pattern, repl=repl, string=init_dc_text)

        with open(init_dc_path, 'w+', encoding='utf-8') as init_dc_html:
            init_dc_html.write(init_dc_text)

    def __clean_normal_passengers(self, passengers_info: dict) -> None:
        """

        :return:
        """
        passenger_ticket_str = ''
        old_passenger_str = ''
        for passenger_name, passenger_info in passengers_info.items():
            passenger_ticket_str += '%s,0,%s,%s,%s,%s,%s,N,%s,' % (
                passenger_info['seat_type'],
                passenger_info['ticker_type'],
                passenger_info['passenger_name'],
                passenger_info['passenger_id_type_code'],
                passenger_info['passenger_id_no'],
                passenger_info['mobile_no'],
                passenger_info['allEncStr'])
            old_passenger_str += '%s,%s,%s,%s_' % (passenger_info['passenger_name'],
                                                   passenger_info['passenger_id_type_code'],
                                                   passenger_info['passenger_id_no'],
                                                   passenger_info['passenger_type'])
        passenger_ticket_str = passenger_ticket_str[:-1]

        tokens = {'passenger_ticket_str': passenger_ticket_str, 'old_passenger_str': old_passenger_str}
        self.__update_tokens(tokens=tokens)

    def order2pay(self, session: Session, browser: Edge) -> None:
        """

        :param session:
        :param browser:
        :return:
        """
        check_user_json = QueryTicket.get_check_user(session=session)
        if not check_user_json['data']['flag']:
            raise MyError(error_messages='用户未登录')

        submit_order_request_json = QueryTicket.submit_order(session=session, ticket_info=self.__ticket_info,
                                                             train_date=self.__train_date,
                                                             back_train_date=self.__train_date, is_dc=True,
                                                             is_student=False)
        if not submit_order_request_json['status']:
            time.sleep(0.5)
            return self.order2pay(session=session, browser=browser)
            # raise MyError(error_messages='预约失败')

        init_dc_text = OrderTicket.get_init_dc(session=session).text
        self.__clean_init_dc_text(init_dc_text=init_dc_text)
        self.__clean_normal_passengers(passengers_info=self.__passengers_info)

        tokens = globals().get(threading.current_thread().name)
        check_order_info_json = OrderTicket.get_check_order_info(session=session, tokens=tokens)
        queue_count_json = OrderTicket.get_queue_count(session=session, tokens=tokens)
        confirm_single_for_queue_json = PayTicket.get_confirm_single_for_queue(session=session, browser=browser,
                                                                               tokens=tokens)
        if not confirm_single_for_queue_json['status'] or not confirm_single_for_queue_json['data']['submitStatus']:
            raise MyError(error_messages='下单失败')
        order_id = self.__check_order_success(session=session, tokens=tokens)
        result_order_for_dc_queue_json = PayTicket.get_result_order_for_dc_queue(session=session, order_id=order_id,
                                                                                 tokens=tokens)
        if result_order_for_dc_queue_json['data']['submitStatus']:
            message = '订单号：%s，车次为%s的车票已下单，请十分钟内完成付款~' % (order_id, self.__train_code)
            Tools.sendmail(message=message)

    def __check_order_success(self, session: Session, tokens: dict) -> str:
        query_order_wait_time_json = PayTicket.get_query_order_wait_time(session=session, tokens=tokens)
        order_id = query_order_wait_time_json['data']['orderId']
        messages = query_order_wait_time_json['messages']
        if order_id:
            return order_id
        elif messages:
            raise MyError(error_messages=messages)
        time.sleep(4)
        return self.__check_order_success(session=session, tokens=tokens)

    def get_train_date(self) -> str:
        """
        获取乘车日期
        :return:
        """
        return self.__train_date

    def __set_train_date(self, train_date: str) -> str:
        """
        设置乘车日期
        :param train_date:
        :return:
        """

        return Tools.check_date(train_date=train_date)

    def get_from_station(self) -> str:
        """
        获取上车车站
        :return:
        """
        return self.__from_station

    def __set_from_station(self, from_station: str) -> str:
        """
        设置上车车站
        :param from_station:
        :return:
        """
        return check_station_name(station_name=from_station)

    def get_to_station(self) -> str:
        """
        获取下车车站
        :return:
        """
        return self.__to_station

    def __set_to_station(self, to_station: str) -> str:
        """
        设置下车车站
        :param to_station:
        :return:
        """

        return check_station_name(station_name=to_station)

    def get_train_code(self) -> str:
        """
        获取车次
        :return:
        """
        return self.__train_code

    def __set_train_code(self, session: Session, train_code: str) -> str:
        """
        设置车次
        :param session:
        :param train_code:
        :return:
        """
        data = InfoQuery.get_train_search(session=session, train_code=train_code, train_date=self.__train_date)
        if not data:
            raise MyError(error_messages='车次输入错误！')
        return train_code

    def get_passengers_info(self) -> dict:
        """
        获取乘车人信息
        :return:
        """
        return self.__passengers_info

    def __set_passengers_info(self, session: Session, passengers: dict) -> dict:
        """
        设置乘车人信息
        :param session:
        :param passengers:
        :return:
        """
        passengers_info = {}
        for passenger, ticket_seat_type in passengers.items():
            data = UserInfo.get_passengers_query(session=session, passenger_name=passenger)
            datas = data['datas']
            if not datas:
                raise PassengerError(passenger_name=passenger)
            for _ in datas:
                if passenger == _['passenger_name']:
                    _['seat_type'] = ticket_seat_type[0]
                    _['ticket_type'] = ticket_seat_type[1]
                    passengers_info[passenger] = _

        return passengers_info

    def get_ticket_info(self) -> dict:
        """
        获取车次信息
        :return:
        """
        return self.__ticket_info

    def __set_ticket_info(self, session: Session) -> dict:
        """
        设置车次信息
        :param session:
        :return:
        """
        tickets_info = QueryTicket.get_left_ticket_query(session=session, train_date=self.__train_date,
                                                         from_station=self.__from_station, to_station=self.__to_station)
        for ticket_info in tickets_info:
            if self.__train_code == ticket_info['queryLeftNewDTO']['station_train_code']:
                return ticket_info
        raise MyError(error_messages='%s车次信息未找到！' % self.__train_code)
