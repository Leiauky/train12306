import time

from requests import Session
from selenium.webdriver import Edge

from Other import Tools
from Other.Config import UrlConfig
from Other.MyError import CreateObjectError


class PayTicket(object):
    def __init__(self):
        raise CreateObjectError(class_name=self.__class__.__name__)

    @classmethod
    def get_confirm_single_for_queue(cls, session: Session, browser: Edge, tokens: dict) -> dict:
        """

        :param session:
        :param browser:
        :param tokens:
        :return:
        """

        encrypted_data = Tools.get_encrypted_data(selenium_browser=browser, path=tokens['init_dc_path'])

        data = {
            'passengerTicketStr': tokens['passenger_ticket_str'],
            'oldPassengerStr': tokens['old_passenger_str'],
            'randCode': '',
            'purpose_codes': tokens['purpose_codes'],
            'key_check_isChange': tokens['key_check_isChange'],
            'leftTicketStr': tokens['leftTicketStr'],
            'train_location': tokens['train_location'],
            'choose_seats': tokens['choose_seat'],
            'seatDetailType': '000',
            'is_jy': tokens['is_jy'],
            'is_cj': tokens['is_cj'],
            'encryptedData': encrypted_data,
            'whatsSelect': '1',
            'roomType': '00',
            'dwAll': 'N',
            '_json_att': tokens['_json_att'],
            'REPEAT_SUBMIT_TOKEN': tokens['globalRepeatSubmitToken']
        }
        confirm_single_for_queue_response = session.post(
            url=UrlConfig.get_confirm_single_for_queue_url(), data=data)
        confirm_single_for_queue_json = confirm_single_for_queue_response.json()
        return confirm_single_for_queue_json


    @classmethod
    def get_query_order_wait_time(cls, session: Session, tokens: dict) -> dict:
        """

        :param session:
        :param tokens:
        :return:
        """
        random = time.time() * 1000
        params = {
            'random': random,
            'tourFlag': tokens['tour_flag'],
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': tokens['globalRepeatSubmitToken']
        }
        query_order_wait_time_response = session.get(url=UrlConfig.get_query_order_wait_time_url(),
                                                     params=params)
        query_order_wait_time_json = query_order_wait_time_response.json()
        return query_order_wait_time_json


    @classmethod
    def get_result_order_for_dc_queue(cls, session: Session, order_id: str, tokens: dict) -> dict:
        """

        :param tokens:
        :param order_id:
        :param session:
        :return:
        """
        data = {
            'orderSequence_no': order_id,
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': tokens['globalRepeatSubmitToken']
        }
        result_order_for_dc_queue_response = session.post(url=UrlConfig.get_result_order_for_dc_queue_url(),
                                                          data=data)
        result_order_for_dc_queue_json = result_order_for_dc_queue_response.json()
        return result_order_for_dc_queue_json
