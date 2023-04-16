import threading
import time
import uuid

from User.User import User
from utils.Config import SeatType, UserConfig

if __name__ == '__main__':
    username = UserConfig.USERNAME
    password = UserConfig.PASSWORD
    cast_num = UserConfig.CAST_NUM
    user = User(username=username, password=password, cast_num=cast_num, headless=False)
    isLogin = user.password_slider_login()
    # isLogin = user.password_message_login()
    # isLogin = user.qr_login()
    print(isLogin)
    if isLogin:
        train_date = '2023-04-29'
        from_station = '南昌'
        to_station = '哈尔滨'
        station_train_codes = ['Z112', 'K726']
        is_normal_passengers = ['张三']
        seats_type = [SeatType.NO_SEAT, SeatType.HARD_SLEEPER]
        tickets = []
        while not tickets:
            time.sleep(1)
            tickets = user.get_tickets_info(train_date=train_date, from_station=from_station, to_station=to_station,
                                            station_train_codes=station_train_codes, seats_type=seats_type)

        threads = []
        for ticket in tickets:
            threads.append(threading.Thread(target=user.order2pay, name=str(uuid.uuid1()),
                                            args=(ticket, is_normal_passengers)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
