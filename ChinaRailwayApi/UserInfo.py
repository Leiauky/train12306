from requests import Session

from Other.Config import UrlConfig
from Other.MyError import CreateObjectError


class UserInfo(object):
    def __init__(self):
        raise CreateObjectError(class_name=self.__class__.__name__)

    @classmethod
    def get_passengers_query(cls, session: Session, passenger_name: str):
        data = {
            'pageIndex': '1',
            'pageSize': '10',
            'passengerDTO.passenger_name': passenger_name
        }
        passengers_query_response = session.post(url=UrlConfig.get_passengers_query_url(), data=data)
        passengers_query_json = passengers_query_response.json()
        return passengers_query_json['data']
