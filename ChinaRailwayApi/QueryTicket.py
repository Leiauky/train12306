import random
import time
from datetime import date, datetime
from urllib import parse

from requests import Session

from Other.Config import UrlConfig
from Other.MyError import MyError, CreateObjectError


class QueryTicket(object):

    def __init__(self):
        raise CreateObjectError(class_name=self.__class__.__name__)

    @classmethod
    def get_left_ticket_query(cls, session: Session, train_date: str, from_station: str, to_station: str,
                              is_student: bool = False) -> dict:
        """
        获取车票信息
        :param session: eg: Session()
        :param train_date: eg：'2023-04-08'
        :param from_station: eg：'NCG'
        :param to_station: eg：'HBB'
        :param is_student: eg: False
        :return: 车票信息[{},{}...]
        """

        # 发送获取车票信息的请求
        params = {
            'leftTicketDTO.train_date': train_date,  # 出发日期
            'leftTicketDTO.from_station': from_station,  # 上车车站
            'leftTicketDTO.to_station': to_station,  # 下车车站
            'purpose_codes': '0X00' if is_student else 'ADULT'  # 成人票：ADULT，学生票：0X00
        }
        left_ticket_query_response = session.get(url=UrlConfig.get_left_ticket_query_url(),
                                                 params=params)

        # 处理请求响应的信息
        left_ticket_query_json = left_ticket_query_response.json()
        return left_ticket_query_json

    @classmethod
    def update_tickets_price(cls, session: Session, tickets_info: dict or list) -> list:
        """
        获取多个车票价格
        :param session: eg: Session()
        :param tickets_info:
        :return: 传dict返回dict，传list返回list
        """
        tickets_list = []
        if type(tickets_info) == list:
            for ticket_info in tickets_info:
                ticket_info = cls.__get_query_ticket_price(session=session, ticket_info=ticket_info)
                tickets_list.append(ticket_info)
        else:
            ticket_info = cls.__get_query_ticket_price(session=session, ticket_info=tickets_info)
            tickets_list.append(ticket_info)
        return tickets_list

    @classmethod
    def __get_query_ticket_price(cls, session: Session, ticket_info: dict) -> dict:
        """
        获取车票价格
        :param session:
        :param ticket_info: 车票信息
        :return: 包含价格的车票信息
        """
        # 发送获取车票价格的请求
        start_train_date = '%s-%s-%s' % (ticket_info['queryLeftNewDTO']['start_train_date'][:4],
                                         ticket_info['queryLeftNewDTO']['start_train_date'][4:6],
                                         ticket_info['queryLeftNewDTO']['start_train_date'][6:])

        params = {
            'train_no': ticket_info['queryLeftNewDTO']['train_no'],
            'from_station_no': ticket_info['queryLeftNewDTO']['from_station_no'],
            'to_station_no': ticket_info['queryLeftNewDTO']['to_station_no'],
            'seat_types': ticket_info['queryLeftNewDTO']['seat_types'],
            'train_date': start_train_date
        }
        headers = {
            "If-Modified-Since": "0",
            "Cache-Control": "no-cache"
        }

        query_ticket_price_response = session.get(url=UrlConfig.get_query_ticket_price_url(),
                                                  params=params, headers=headers)

        # 处理请求响应的信息
        query_ticket_price_json = query_ticket_price_response.json()
        data = query_ticket_price_json['data']

        '''
        'gg_num': , 'gr_num': 高级软座, 'qt_num': 其他, 'rw_num': 软卧, 'rz_num': 软座,
         'tz_num': 特等座, 'wz_num': 无座, 'yb_num': , 'yw_num': 硬卧, 'yz_num': 硬座,
          'ze_num': 二等座, 'zy_num': 一等座, 'swz_num': 商务座, 'srrb_num': 动卧 
        '''
        price = {
            'gg_num': None, 'gr_num': None, 'qt_num': None, 'rw_num': None, 'rz_num': None,
            'tz_num': None, 'wz_num': None, 'yb_num': None, 'yw_num': None, 'yz_num': None,
            'ze_num': None, 'zy_num': None, 'swz_num': None, 'srrb_num': None
        }
        # 商务座、特等座*
        if "A9" in data.keys():
            price["swz_num"] = data["A9"]
        if "P" in data.keys():
            price["tz_num"] = data["P"]
        # 一等座
        if "M" in data.keys():
            price["yz_num"] = data["M"]
        # 二等座、二等包座
        if "O" in data.keys():
            price["ze_num"] = data["O"]
        # 高级软卧
        if "A6" in data.keys():
            price["gr_num"] = data["A6"]
        # 软卧、一等卧
        if "A4" in data.keys():
            price["rw_num"] = data["A4"]
        # 动卧
        if "F" in data.keys():
            price["srrb_num"] = data["F"]
        # 硬卧、二等卧
        if "A3" in data.keys():
            price["yw_num"] = data["A3"]
        # 软座
        if "A2" in data.keys():
            price["rz_num"] = data["A2"]
        # 硬座
        if "A1" in data.keys():
            price["yz_num"] = data["A1"]
        # 无座
        if "WZ" in data.keys():
            price["wz_num"] = data["WZ"]
        ticket_info['price'] = price
        time.sleep(random.randint(1, 4))
        return ticket_info

    @classmethod
    def get_check_user(cls, session: Session) -> dict:
        """
        检测用户是否登录
        :param session: Session()
        :return: 已登录 True
        """
        # 发送检测用户是否登录的请求
        data = {
            '_json_att': ''
        }
        check_user_response = session.post(url=UrlConfig.get_check_user_url(), data=data)

        # 处理请求响应的信息
        check_user_json = check_user_response.json()
        return check_user_json

    @classmethod
    def submit_order(cls, session: Session, ticket_info: dict, train_date: str, back_train_date: str,
                     is_dc: bool = True, is_student: bool = False,
                     ) -> dict:
        """
        预订
        :param session:
        :param ticket_info:
        :param train_date:
        :param back_train_date:
        :param is_dc:
        :param is_student:
        :return:
        """

        data = {
            'secretStr': parse.unquote(ticket_info['secretStr']),
            'train_date': train_date,
            'back_train_date': back_train_date,
            'tour_flag': 'dc' if is_dc else 'wc',
            'purpose_codes': '0X00' if is_student else 'ADULT',
            'query_from_station_name': ticket_info['queryLeftNewDTO']['from_station_name'],
            'query_to_station_name': ticket_info['queryLeftNewDTO']['to_station_name'],
            'undefined': ''
        }

        submit_order_request_response = session.post(url=UrlConfig.get_submit_order_request_url(),
                                                     data=data)

        submit_order_request_json = submit_order_request_response.json()
        return submit_order_request_json


if __name__ == '__main__':
    pass
