import threading
import time
import uuid

from User.Ticket import Ticket
from User.User import User
from Other.Config import SeatType, UserConfig, TicketType
from Other.MyError import MyError


def buy_ticket(train_date: str, from_station: str, to_station: str, trains_code: list, passengers: dict):
    tickets = []
    for train_code in trains_code:
        ticket = Ticket(session=user.get_session(), train_date=train_date, from_station=from_station,
                        to_station=to_station, train_code=train_code,
                        passengers=passengers)
        tickets.append(ticket)

    tasks = []
    for ticket in tickets:
        tasks.append(threading.Thread(target=ticket.order2pay, name=uuid.uuid1().__str__(),
                                      args=(user.get_session(), user.get_browser())))

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()


if __name__ == '__main__':
    # 用户名
    username = UserConfig.USERNAME
    # 密码
    password = UserConfig.PASSWORD
    # 身份证后四位
    cast_num = UserConfig.CAST_NUM
    user = User(username=username, password=password, cast_num=cast_num, headless=False)
    isLogin = user.password_slider_login()
    # isLogin = user.password_message_login()
    # isLogin = user.qr_login()
    if not isLogin:
        raise MyError('登录失败')
    # 乘车日期
    train_date = '2023-04-25'
    # 上车地点
    from_station = '南昌'
    # 下车地点
    to_station = '上海'
    # 车次
    trains_code = ['K353', 'K1558']
    # 乘客
    # passengers = {'名字': (座位类型, 车票类型), }
    passengers = {'张三': (SeatType.HARD_SEAT, TicketType.ADULT_TICKETS), }
    buy_ticket(train_date=train_date, from_station=from_station, to_station=to_station, trains_code=trains_code,
               passengers=passengers)
    pass
