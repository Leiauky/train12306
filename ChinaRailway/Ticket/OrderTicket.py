import datetime

from requests import Session

from utils.Config import UrlConfig
from utils.MyError import MyError


class OrderTicket(object):

    def __init__(self):
        raise MyError(error_messages="OrderTicket对象不能被创建。")

    @classmethod
    def get_init_dc(cls, session: Session) -> str:
        """
        
        :return: 
        """

        data = {
            '_json_att': ''
        }
        init_dc_response = session.post(url=UrlConfig.get_init_dc_url(), data=data)
        return init_dc_response.text

    @classmethod
    def get_passenger_dtos(cls, session: Session, tokens: dict) -> dict:
        """
        获取乘客信息
        :param tokens:
        :type session: object
        :return:
        """
        data = {
            '_json_att': tokens['_json_att'],
            'REPEAT_SUBMIT_TOKEN': tokens['globalRepeatSubmitToken']
        }
        passenger_dtos_response = session.post(url=UrlConfig.get_passenger_dtos_url(), data=data)
        passenger_dtos_json = passenger_dtos_response.json()

        return passenger_dtos_json['data']

    @classmethod
    def get_check_order_info(cls, session: Session, tokens: dict) -> dict:
        """
        获取订单信息
        :param session:
        :param tokens:
        :return:
        """

        data = {
            'cancel_flag': tokens['cancel_flag'],
            'bed_level_order_num': tokens['bed_level_order_num'],
            'passengerTicketStr': tokens['passenger_ticket_str'],
            'oldPassengerStr': tokens['old_passenger_str'],
            'tour_flag': tokens['tour_flag'],
            'randCode': '',
            'whatsSelect': '1',
            'sessionId': '',
            'sig': '',
            'scene': 'nc_login',
            '_json_att': tokens['_json_att'],
            'REPEAT_SUBMIT_TOKEN': tokens['globalRepeatSubmitToken']
        }

        check_order_info_response = session.post(url=UrlConfig.get_check_order_info_url(),
                                                 data=data)
        check_order_info_json = check_order_info_response.json()
        return check_order_info_json['data']

    @classmethod
    def get_queue_count(cls, session: Session, tokens: dict) -> dict:
        """

        :param tokens:
        :param session:
        :return:
        """
        fmt = '%a %b %d %Y %H:%M:%S GMT+0800 (中国标准时间)'
        year = tokens['train_date']['year']
        month = tokens['train_date']['month']
        day = tokens['train_date']['day']
        hour = tokens['train_date']['hours']
        minute = tokens['train_date']['minutes']
        second = tokens['train_date']['seconds']
        train_date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute,
                                       second=second).strftime(fmt)

        date = {
            'train_date': train_date,
            'train_no': tokens['train_no'],
            'stationTrainCode': tokens['station_train_code'],
            'seatType': tokens['passenger_ticket_str'][:1],
            'fromStationTelecode': tokens['from_station_telecode'],
            'toStationTelecode': tokens['to_station_telecode'],
            'leftTicket': tokens['leftTicketStr'],
            'purpose_codes': tokens['purpose_codes'],
            'train_location': tokens['train_location'],
            '_json_att': tokens['_json_att'],
            'REPEAT_SUBMIT_TOKEN': tokens['globalRepeatSubmitToken']
        }
        queue_count_response = session.post(url=UrlConfig.get_queue_count_url(), data=date)
        queue_count_json = queue_count_response.json()
        return queue_count_json['data']


if __name__ == '__main__':
    pass
