import json
import re
import threading
import time

import requests
from requests import Session
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions

from Login.Login import Login
from Ticket.OrderTicket import OrderTicket
from Ticket.PayTicket import PayTicket
from Ticket.QueryTicket import QueryTicket
from utils import Utils
from utils.Config import GlobalConfig, UrlConfig, PathConfig, TicketType, SeatType
from utils.MyError import MyError


class User(object):
    """
    私人配置类
    """

    def __init__(self, username: str = None, password: str = None, cast_num: str = None,
                 headless: bool = False) -> None:
        self.__username = username
        self.__password = password
        self.__cast_num = cast_num
        self.__headless = headless
        self.__session = self.__init_session()
        self.__browser = self.__init_browser()
        self.__session_and_browser_init()
        self.__tokens = None
        # self.__init_dc_path = None
        # self.__order_id = None
        self.__lock = threading.Lock()

    def get_username(self) -> str:
        """
        返回用户账号
        :return:
        """
        return self.__username

    def get_password(self) -> str:
        """
        返回用户密码
        :return:
        """
        return self.__password

    def get_cast_num(self) -> str:
        """
        返回身份证后四位
        :return:
        """
        return self.__cast_num

    def get_headless(self) -> bool:
        """
        返回headless属性
        :return:
        """
        return self.__headless

    def __init_session(self) -> Session:
        """
        为每一位用户初始化request_session
        :return:
        """
        self.__session = requests.Session()
        self.__session.headers.update(GlobalConfig.get_headers())
        self.__session.get(url=UrlConfig.get_index_url())
        return self.__session

    def __init_browser(self) -> Edge:
        """
        为每一位用户初始化selenium_browser
        :return:
        """
        edge_options = EdgeOptions()
        if self.__headless:
            edge_options.add_argument('--headless')

        edge_options.add_argument('--window-size=1920,1080')
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.95')
        # 开启开发者模式
        edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 将参数传给浏览器
        self.__browser = Edge(executable_path=PathConfig.get_ms_edge_driver_path(), options=edge_options)

        with open(PathConfig.get_stealth_min_js_path(), mode='r', encoding='utf-8') as stealth_min_js_file:
            stealth_min_js = stealth_min_js_file.read()
            self.__browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": stealth_min_js})
            stealth_min_js_file.close()

        self.__browser.get(UrlConfig.get_index_url())

        return self.__browser

    def __session_and_browser_init(self) -> None:
        """
        通过browser获取cookies_RAIL_DEVICEID、cookies_RAIL_EXPIRATION
        :return:
        """

        # browser访问12306登录页面
        self.__browser.get(UrlConfig.get_login_url())
        # 将browser的cookies更新为session的cookies
        Utils.update_selenium_browser_cookies_from_requests_session_cookies(selenium_browser=self.__browser,
                                                                            requests_session=self.__session)
        # 更新session的请求头
        headers = {
            'Host': 'kyfw.12306.cn',
        }
        self.__session.headers.update(headers)

    def get_session(self) -> Session:
        """
        返回session属性
        :return:
        """
        return self.__session

    def get_browser(self) -> Edge:
        """
        返回browser属性
        :return:
        """
        return self.__browser

    def update_tokens(self, tokens: dict) -> None:
        """
        更新tokens属性
        :param tokens:
        :return:
        """
        threading_name = threading.current_thread().name
        self.__lock.acquire()
        if not self.__tokens:
            self.__tokens = {}
        if threading_name not in self.__tokens.keys():
            self.__tokens[threading_name] = tokens
        else:
            self.__tokens[threading_name].update(tokens)
        self.__lock.release()

    def get_tokens(self) -> dict:
        """
        返回tokens属性
        :return:
        """
        self.__lock.acquire()
        tokens = self.__tokens[threading.current_thread().name]
        self.__lock.release()
        return tokens

    # def update_init_dc_path(self, init_dc_path: str) -> None:
    #     self.__init_dc_path = init_dc_path
    #
    # def get_init_dc_path(self) -> str:
    #     return self.__init_dc_path
    #
    # def update_order_id(self, order_id: str) -> None:
    #     self.__order_id = order_id
    #
    # def get_order_id(self) -> str:
    #     return self.__order_id

    def password_slider_login(self, timeout: int = 60) -> bool:
        """
        12306滑块验证登录
        :return:
        """
        if not self.__username or not self.__password:
            return False
        start_time = time.time()
        Login.password_selenium_login(username=self.__username, password=self.__password, browser=self.__browser,
                                      headless=self.__headless)
        # 判断是否登录成功
        while True:
            if self.__browser.get_cookie("tk"):
                break
            elif time.time() - start_time > timeout:
                return False
            time.sleep(1)
        # 获取selenium_cookies
        browser_cookies = self.__browser.get_cookies()
        # selenium_cookies 转成 requests_session_cookies
        requests_session_cookies = Utils.selenium_browser_cookies2requests_session_cookies(browser_cookies)
        # 更新requests_session_cookies
        self.__session.cookies.update(requests_session_cookies)
        return True

    def password_message_login(self) -> bool:
        """
        12306短信验证登录
        :return:
        """
        if not self.__username or not self.__password or not self.__cast_num:
            return False
        return Login.password_message_login(username=self.__username, password=self.__password,
                                            cast_num=self.__cast_num,
                                            session=self.__session, browser=self.__browser)

    def qr_login(self) -> bool:
        """
        12306扫描二维码登录
        :return:
        """
        return Login.qr_login(session=self.__session)

    def get_tickets_info(self, train_date: str, from_station: str, to_station: str, station_train_codes: list,
                         seats_type: list,
                         purpose_codes: str = TicketType.ADULT_TICKETS) -> list:
        """

        :return:
        """

        def show_tickets_info(tickets_info: list) -> None:
            ticket_num = 0
            for ticket in tickets_info:
                message = '序号：%d，车次：%s，%s-->%s，%s--%s，全程耗时：%s，是否可以购买：%s，选择座位为%s' % (
                    ticket_num,  # 序号
                    ticket['queryLeftNewDTO']['station_train_code'],  # 车次
                    ticket['queryLeftNewDTO']['from_station_name'],  # 出发站
                    ticket['queryLeftNewDTO']['to_station_name'],  # 到达站
                    ticket['queryLeftNewDTO']['start_time'],  # 出发时间
                    ticket['queryLeftNewDTO']['arrive_time'],  # 到达时间
                    ticket['queryLeftNewDTO']['lishi'],  # 历时
                    ticket['queryLeftNewDTO']['canWebBuy'],  # 是否可以购买
                    SeatType.get_seat_type_str_cn()[ticket['seat_type']]  # 座位

                )
                print(message)
                ticket_num += 1

        pattern = '(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)'
        if not re.compile(pattern=pattern, flags=re.S).findall(train_date):
            raise MyError(error_messages='乘车日期输入错误')
        tickets_info = QueryTicket.get_left_ticket_query(session=self.__session, train_date=train_date,
                                                         from_station=from_station, to_station=to_station,
                                                         purpose_codes=purpose_codes)
        is_tickets_info = []
        seat_type_str_en = SeatType.get_seat_type_str_en()
        for ticket_info in tickets_info:
            if ticket_info['queryLeftNewDTO']['station_train_code'] in station_train_codes:
                for seat_type in seats_type:
                    seat_num = ticket_info['queryLeftNewDTO'][seat_type_str_en[seat_type]]
                    if seat_num != '无' and seat_num != '--':
                        ticket_info['seat_type'] = seat_type
                        is_tickets_info.append(ticket_info)
                        break
        show_tickets_info(tickets_info=is_tickets_info)
        # QueryTicket.update_tickets_price(session=self.__session, tickets_info=tickets_info)
        # ticket_id = int(input('选择购买的票ID：'))
        return is_tickets_info

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

        self.update_tokens(tokens=tokens)

        pattern = re.compile(r'<title>中国铁路12306网站</title>')
        repl = r'<title>中国铁路12306网站</title>\n<base href="https://kyfw.12306.cn/" target="_blank">'
        init_dc_text = re.sub(pattern=pattern, repl=repl, string=init_dc_text)

        # self.update_init_dc_path(init_dc_path=init_dc_path)

        with open(init_dc_path, 'w+', encoding='utf-8') as init_dc_html:
            init_dc_html.write(init_dc_text)

    def __clean_normal_passengers(self, is_normal_passengers: list, normal_passengers: list, seat_type: str) -> None:
        """

        :return:
        """
        for normal_passenger in normal_passengers:
            if normal_passenger['passenger_name'] in is_normal_passengers:
                normal_passenger['seat_type'] = seat_type
                normal_passenger['ticker_type'] = TicketType.ADULT_TICKETS
                is_normal_passengers.remove(normal_passenger['passenger_name'])
                is_normal_passengers.append(normal_passenger)
                continue
        passenger_ticket_str = ''
        old_passenger_str = ''
        for normal_passenger in is_normal_passengers:
            passenger_ticket_str += '%s,0,%s,%s,%s,%s,%s,N,%s,' % (
                normal_passenger['seat_type'],
                normal_passenger['ticker_type'],
                normal_passenger['passenger_name'],
                normal_passenger['passenger_id_type_code'],
                normal_passenger['passenger_id_no'],
                normal_passenger['mobile_no'],
                normal_passenger['allEncStr'])
            old_passenger_str += '%s,%s,%s,%s_' % (normal_passenger['passenger_name'],
                                                   normal_passenger['passenger_id_type_code'],
                                                   normal_passenger['passenger_id_no'],
                                                   normal_passenger['passenger_type'])
        passenger_ticket_str = passenger_ticket_str[:-1]
        tokens = {'passenger_ticket_str': passenger_ticket_str, 'old_passenger_str': old_passenger_str}
        self.update_tokens(tokens=tokens)

    def order2pay(self, ticket: dict, is_normal_passengers: list,
                  purpose_codes: str = TicketType.ADULT_TICKETS) -> None:
        """

        :return:
        """
        if not QueryTicket.get_check_user(session=self.__session):
            raise MyError(error_messages='用户未登录')

        if not QueryTicket.submit_order(session=self.__session, ticket=ticket, purpose_codes=purpose_codes):
            raise MyError(error_messages='预约失败')

        init_dc_text = OrderTicket.get_init_dc(session=self.__session)

        self.__clean_init_dc_text(init_dc_text=init_dc_text)

        tokens = self.get_tokens()
        passenger_dtos_data = OrderTicket.get_passenger_dtos(session=self.__session,
                                                             tokens=tokens)
        if passenger_dtos_data['isExist']:
            normal_passengers = passenger_dtos_data['normal_passengers']
            seat_type = ticket['seat_type']
            if seat_type == '11':
                seat_type = '1'
            self.__clean_normal_passengers(is_normal_passengers=is_normal_passengers,
                                           normal_passengers=normal_passengers, seat_type=seat_type)
            OrderTicket.get_check_order_info(session=self.__session, tokens=tokens)
            OrderTicket.get_queue_count(session=self.__session, tokens=tokens)

        init_dc_path = tokens['init_dc_path']
        if PayTicket.get_confirm_single_for_queue(session=self.__session, browser=self.__browser,
                                                  init_dc_path=init_dc_path, tokens=tokens):
            order_id = PayTicket.get_query_order_wait_time(session=self.__session, tokens=tokens)
            message = '订单号：%s，车次为%s的车票已下单，请十分钟内完成付款~' % (order_id, ticket['queryLeftNewDTO']['station_train_code'])
            Utils.sendmail(message)


if __name__ == '__main__':
    pass
