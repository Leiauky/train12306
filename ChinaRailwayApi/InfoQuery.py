from requests import Session

from Other.Config import UrlConfig
from Other.MyError import CreateObjectError


class InfoQuery(object):
    def __init__(self):
        raise CreateObjectError(self.__class__.__name__)

    @classmethod
    def get_train_search(cls, session: Session, train_code: str, train_date: str) -> list:
        params = {
            'keyword': train_code,
            'date': train_date
        }
        train_search_response = session.get(url=UrlConfig.get_train_search_url(), params=params)
        train_search_json = train_search_response.json()
        return train_search_json['data']
