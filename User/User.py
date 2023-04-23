import base64
import time
from io import BytesIO

import requests
from PIL.Image import Image
from requests import Session
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options as EdgeOptions

from ChinaRailwayApi.Login import Login
from ChinaRailwayApi.QueryTicket import QueryTicket
from Other import Utils
from Other.Config import GlobalConfig, UrlConfig, PathConfig, SeatType
from Other.MyError import MyError
from Other.Tools import check_date, clean_tickets_info, check_station_name


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

    def password_slider_login(self, timeout: int = 60) -> bool:
        """
        12306滑块验证登录
        :return:
        """
        if not self.__username or not self.__password:
            return False
        start_time = time.time()
        Login.password_slider_login(username=self.__username, password=self.__password, browser=self.__browser)
        # 判断是否登录成功
        while True:
            if self.__browser.get_cookie("tk"):
                break
            elif time.time() - start_time > timeout:
                return False
            time.sleep(0.5)
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
        :return: {"result_message":"获取手机验证码成功！","result_code":0}
        """
        if not self.__username or not self.__password or not self.__cast_num:
            return False
        # 获取短信验证码并判断是否获取成功
        message_code_json = Login.message_code(session=self.__session, username=self.__username,
                                               cast_num=self.__cast_num)

        if message_code_json['result_code'] != 0:
            raise MyError(message_code_json['result_message'])
        rand_code = input('请输入短信验证码：')
        passport_login_json = Login.password_message_login(username=self.__username, password=self.__password,
                                                           rand_code=rand_code, session=self.__session,
                                                           browser=self.__browser)
        # 判断是否验证通过
        if passport_login_json['result_code'] != 0:
            return False
        # 设置登录cookies
        return self.__set_login_cookies()

    def qr_login(self) -> bool:
        """
        12306扫描二维码登录
        :return:
        """

        qr64_json = Login.qr_login(session=self.__session)
        # 展示二维码图片
        Image.open(BytesIO(base64.b64decode(qr64_json['image']))).show()
        #
        data = {
            'RAIL_DEVICEID': self.__session.cookies["RAIL_DEVICEID"],
            'RAIL_EXPIRATION': self.__session.cookies["RAIL_EXPIRATION"],
            'uuid': qr64_json['uuid'],
            'appid': 'otn'
        }
        return self.__check_qr_login(data=data)

    def __check_qr_login(self, data: dict) -> bool:
        check_qr_json = Login.check_qr_login(session=self.__session, data=data)
        # result_code 0：未识别 1：已识别，暂未授权（未点击授权或不授权） 2：登录成功，（已识别且已授权）3：已失效 5：系统异常
        result_code = check_qr_json['result_code']
        if result_code == '0' or result_code == '1':
            time.sleep(1)
            return self.__check_qr_login(data=data)
        elif result_code == '2':
            return self.__set_login_cookies()
        elif result_code == '3':
            # 二维码失效，重新获取二维码
            return self.qr_login()
        else:
            return False

    def __set_login_cookies(self) -> bool:
        # 设置登录cookies
        uam_tk_json = Login.get_uam_tk(session=self.__session)
        uam_auth_client_response = Login.get_uam_auth_client(session=self.__session,
                                                             tk=uam_tk_json['newapptk'])
        # 处理请求响应的信息
        if uam_auth_client_response.cookies.get('tk'):
            return True
        return False

    def get_tickets_info(self, train_date: str, from_station: str, to_station: str) -> None:
        """

        :param train_date: eg：'2023-04-08'
        :param from_station: eg: 南昌
        :param to_station: eg: 哈尔滨
        :return:
        """

        train_date = check_date(train_date=train_date)
        from_station = check_station_name(from_station)
        to_station = check_station_name(to_station)

        left_ticket_query_json = QueryTicket.get_left_ticket_query(session=self.__session, train_date=train_date,
                                                                   from_station=from_station, to_station=to_station)
        result = left_ticket_query_json['data']['result']
        map = left_ticket_query_json['data']['map']
        tickets_info = clean_tickets_info(result=result, map=map)

        self.__show_tickets_info(tickets_info=tickets_info)

    def __show_tickets_info(self, tickets_info: list) -> None:
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


if __name__ == '__main__':
    pass
