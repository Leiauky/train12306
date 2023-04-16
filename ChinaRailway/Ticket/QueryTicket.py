import random
import time
from datetime import date
from urllib import parse

from requests import Session

from utils.Config import GlobalConfig, UrlConfig, TicketType
from utils.MyError import MyError


class QueryTicket(object):

    def __init__(self):
        raise MyError(error_messages="QueryTicket对象不能被创建。")

    @classmethod
    def get_left_ticket_query(cls, session: Session, train_date: str, from_station: str, to_station: str,
                              purpose_codes: str = TicketType.ADULT_TICKETS) -> list:
        """
        获取车票信息
        :param session:
        :param train_date: 乘坐火车日期 eg：2023-04-08
        :param from_station: 乘坐火车站点 eg：南昌
        :param to_station: 火车下车站点 eg：哈尔滨
        :param purpose_codes: 成人票 True 学生票 False
        :return: 火车票信息[{},{}...]
        """

        def __clean_tickets_info(result: list, map: dict) -> list:
            """
            格式化车票信息
            :param result:
            :param map:
            :return: 车票信息
            """
            cX = []
            for i in result:
                c1 = {}
                cV = i.split('|')
                c1['secretStr'] = cV[0]
                c1['buttonTextInfo'] = cV[1]
                cZ = {'train_no': cV[2], 'station_train_code': cV[3], 'start_station_telecode': cV[4],
                      'end_station_telecode': cV[5], 'from_station_telecode': cV[6], 'to_station_telecode': cV[7],
                      'start_time': cV[8], 'arrive_time': cV[9], 'lishi': cV[10], 'canWebBuy': cV[11],
                      'yp_info': cV[12],
                      'start_train_date': cV[13], 'train_seat_feature': cV[14], 'location_code': cV[15],
                      'from_station_no': cV[16], 'to_station_no': cV[17], 'is_support_card': cV[18],
                      'controlled_train_flag': cV[19], 'gg_num': cV[20] if cV[20] else "--",
                      'gr_num': cV[21] if cV[21] else "--", 'qt_num': cV[22] if cV[22] else "--",
                      'rw_num': cV[23] if cV[23] else "--", 'rz_num': cV[24] if cV[24] else "--",
                      'tz_num': cV[25] if cV[25] else "--", 'wz_num': cV[26] if cV[26] else "--",
                      'yb_num': cV[27] if cV[27] else "--", 'yw_num': cV[28] if cV[28] else "--",
                      'yz_num': cV[29] if cV[29] else "--", 'ze_num': cV[30] if cV[30] else "--",
                      'zy_num': cV[31] if cV[31] else "--", 'swz_num': cV[32] if cV[32] else "--",
                      'srrb_num': cV[33] if cV[33] else "--", 'yp_ex': cV[34], 'seat_types': cV[35],
                      'exchange_train_flag': cV[36], 'houbu_train_flag': cV[37], 'houbu_seat_limit': cV[38],
                      'yp_info_new': cV[39]}
                if len(cV) > 46:
                    cZ['dw_flag'] = cV[46]

                if len(cV) > 48:
                    cZ['stopcheckTime'] = cV[48]

                if len(cV) > 49:
                    cZ['country_flag'] = cV[49]
                    cZ['local_arrive_time'] = cV[50]
                    cZ['local_start_time'] = cV[51]

                cZ['from_station_name'] = map[cV[6]]
                cZ['to_station_name'] = map[cV[7]]
                c1['queryLeftNewDTO'] = cZ

                cX.append(c1)
            return cX

        # 发送获取车票信息的请求
        params = {
            'leftTicketDTO.train_date': train_date if train_date else date.today().strftime('%Y-%m-%d'),  # 出发日期
            'leftTicketDTO.from_station': GlobalConfig.get_station_name()[from_station],  # 上车车站
            'leftTicketDTO.to_station': GlobalConfig.get_station_name()[to_station],  # 下车车站
            'purpose_codes': 'ADULT' if purpose_codes == TicketType.ADULT_TICKETS else '0X00'  # 成人票：ADULT，学生票：0X00
        }
        left_ticket_query_response = session.get(url=UrlConfig.get_left_ticket_query_url(),
                                                 params=params)
        # 处理请求响应的信息
        left_ticket_query_json = left_ticket_query_response.json()
        result = left_ticket_query_json['data']['result']
        map = left_ticket_query_json['data']['map']
        return __clean_tickets_info(result, map)

    @classmethod
    def update_tickets_price(cls, session: Session, tickets_info: dict or list) -> list:
        """
        获取多个车票价格
        :param session:
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
        elif "p" in data.keys():
            price["swz_num"] = data["p"]
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
    def get_check_user(cls, session: Session) -> bool:
        """
        检测用户是否登录
        :param session:
        :return: 已登录 True
        """
        # 发送检测用户是否登录的请求
        data = {
            '_json_att': ''
        }
        check_user_response = session.post(url=UrlConfig.get_check_user_url(), data=data)
        # 处理请求响应的信息
        check_user_json = check_user_response.json()
        return check_user_json['data']['flag']

    @classmethod
    def submit_order(cls, session: Session, ticket: dict, purpose_codes: str = TicketType.ADULT_TICKETS) -> bool:
        """
        下单
        :param session:
        :param ticket:
        :param purpose_codes:
        :return:
        """
        start_train_date = '%s-%s-%s' % (ticket['queryLeftNewDTO']['start_train_date'][:4],
                                         ticket['queryLeftNewDTO']['start_train_date'][4:6],
                                         ticket['queryLeftNewDTO']['start_train_date'][6:])
        data = {
            'secretStr': parse.unquote(ticket['secretStr']),
            'train_date': start_train_date,
            'back_train_date': start_train_date,
            'tour_flag': 'dc',
            'purpose_codes': 'ADULT' if purpose_codes == TicketType.ADULT_TICKETS else '0X00',
            'query_from_station_name': ticket['queryLeftNewDTO']['from_station_name'],
            'query_to_station_name': ticket['queryLeftNewDTO']['to_station_name'],
            'undefined': ''
        }

        submit_order_request_response = session.post(url=UrlConfig.get_submit_order_request_url(),
                                                     data=data)
        submit_order_request_json = submit_order_request_response.json()
        return submit_order_request_json['status']


if __name__ == '__main__':
    pass
