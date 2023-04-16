import base64
import time
from io import BytesIO

from PIL import Image
from requests import Session
from selenium.webdriver import ActionChains
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.Config import UrlConfig
from utils.MyError import MyError


class Login(object):
    def __init__(self):
        raise MyError(error_messages="Login对象不能被创建。")

    @classmethod
    def password_selenium_login(cls, username: str, password: str, browser: Edge, headless: bool) -> bool:
        """
        12306滑块验证登录
        :param headless:
        :param password:
        :param username:
        :param browser:
        :return: 登录成功 True
        """
        if headless:
            return False
        # 填写username
        username_locator = (By.XPATH, '//input[@id="J-userName"]')
        WebDriverWait(driver=browser, timeout=3, poll_frequency=0.5).until(
            EC.presence_of_element_located(locator=username_locator)).send_keys(username)
        # browser.find_element(By.XPATH, '//input[@id="J-userName"]').send_keys(username)
        # 填写password
        password_locator = (By.XPATH, '//input[@id="J-password"]')
        WebDriverWait(driver=browser, timeout=3, poll_frequency=0.5).until(
            EC.presence_of_element_located(locator=password_locator)).send_keys(password)
        # browser.find_element(By.XPATH, '//input[@id="J-password"]').send_keys(password)

        # 点击登录
        login_locator = (By.XPATH, '//a[@id="J-login"]')
        WebDriverWait(driver=browser, timeout=3, poll_frequency=0.5).until(
            EC.element_to_be_clickable(mark=login_locator)).click()
        # browser.find_element(By.XPATH, '//a[@id="J-login"]').click()

        # 获取滑块
        slide_locator = (By.XPATH, '//span[@id="nc_1_n1z"]')
        btn_slide = WebDriverWait(driver=browser, timeout=3, poll_frequency=0.5).until(
            EC.presence_of_element_located(locator=slide_locator))
        # btn_slide = browser.find_element(By.XPATH, '//span[@id="nc_1_n1z"]')
        # 按住滑块
        ActionChains(browser).click_and_hold(on_element=btn_slide).perform()
        # 滑动滑块
        ActionChains(browser).move_to_element_with_offset(to_element=btn_slide, xoffset=300,
                                                          yoffset=0).perform()
        return True

    @classmethod
    def password_message_login(cls, username: str, password: str,
                               cast_num: str, session: Session, browser: Edge) -> bool:
        """
        12306短信验证登录
        :param browser:
        :param session:
        :param password:
        :param username:
        :param cast_num: 身份证后四位
        :return: 登录成功 True
        """
        # 获取短信验证码并判断是否获取成功
        if not cls.__message_code(session=session, username=username, cast_num=cast_num):
            # 获取失败
            return False
        # 输入短信验证码
        rand_code = input("请输入短信验证码：")
        # 密码加密
        password = '@' + browser.execute_script("return encrypt_ecb('%s', SM4_key)" % password)
        # 发送登录请求
        data = {
            'sessionId': '',
            'sig': '',
            'if_check_slide_passcode_token': '',
            'scene': '',
            'checkMode': '0',
            'randCode': rand_code,  # 验证码
            'username': username,  # 用户名 手机号 邮箱
            'password': password,  # 密码
            'appid': 'otn'
        }
        passport_login_response = session.post(url=UrlConfig.get_passport_login_url(), data=data)
        # 处理请求的响应信息
        passport_login_json = passport_login_response.json()
        # 判断是否验证通过
        if passport_login_json['result_code'] != 0:
            return False
        # 设置登录cookies
        new_app_tk = cls.__get_uam_tk(session=session)
        return cls.__get_uam_auth_client(session=session, tk=new_app_tk)

    @classmethod
    def __message_code(cls, session: Session, username: str, cast_num: str) -> bool:
        """
        请求12306发送短信验证码
        :param session:
        :param username: 用户名 or 手机号 or 邮箱
        :param cast_num: 身份证后四位
        :return: 12306发送短信验证码 True
        """
        # 发送获取短信验证码请求
        data = {
            'appid': 'otn',
            'username': username,  # 用户名 手机号 邮箱
            'castNum': cast_num  # 身份证后四位
        }
        message_code_response = session.post(url=UrlConfig.get_message_code_url(), data=data)
        # 处理请求的响应信息
        message_code_json = message_code_response.json()
        return True if message_code_json['result_message'] == '获取手机验证码成功！' else False

    @classmethod
    def qr_login(cls, session: Session) -> bool:
        """
        12306扫描二维码登录
        :param session:
        :return: 登录成功 True
        """
        # 发送获取获取二维码请求
        data = {
            'appid': 'otn'
        }
        qr64_response = session.post(url=UrlConfig.get_qr64_url(), data=data)
        # 处理请求的响应信息
        qr64_json = qr64_response.json()
        # 展示二维码图片
        Image.open(BytesIO(base64.b64decode(qr64_json['image']))).show()
        #
        data = {
            'RAIL_DEVICEID': session.cookies["RAIL_DEVICEID"],
            'RAIL_EXPIRATION': session.cookies["RAIL_EXPIRATION"],
            'uuid': qr64_json['uuid'],
            'appid': 'otn'
        }

        return cls.__check_qr_login(session=session, data=data)

    @classmethod
    def __check_qr_login(cls, session: Session, data: dict) -> bool:
        """
        检测二维码是否已识别且已授权
        :param data: 发送检测二维码状态请求的post参数
        :return: 登录成功 True
        """
        # 发送检测二维码状态请求
        check_qr_response = session.post(url=UrlConfig.get_check_qr_url(), data=data)
        # 处理请求的响应信息
        check_qr_json = check_qr_response.json()
        # result_code 0：未识别 1：已识别，暂未授权（未点击授权或不授权） 2：登录成功，（已识别且已授权）3：已失效 5：系统异常
        result_code = check_qr_json['result_code']
        if result_code == '0' or result_code == '1':
            time.sleep(1)
            return cls.__check_qr_login(session=session, data=data)
        elif result_code == '2':
            # 设置登录cookies
            new_app_tk = cls.__get_uam_tk(session=session)
            return cls.__get_uam_auth_client(session=session, tk=new_app_tk)
        elif result_code == '3':
            # 二维码失效，重新获取二维码
            return cls.qr_login(session=session)
        else:
            return False

    @classmethod
    def __get_uam_tk(cls, session: Session) -> str:
        """
        登录成功后设置cookies_uamtk并获取newapptk
        :param session:
        :return: 成功返回 tk
        """
        # 发送设置cookies_uamtk并获取newapptk的请求
        data = {
            'appid': 'otn'
        }
        uam_tk_response = session.post(url=UrlConfig.get_uam_tk_url(), data=data)
        # 处理请求响应的信息
        uam_tk_json = uam_tk_response.json()
        if uam_tk_response.cookies.get('uamtk'):
            return uam_tk_json['newapptk']

    @classmethod
    def __get_uam_auth_client(cls, session: Session, tk: str) -> bool:
        """
        登录成功后设置cookies_tk
        :param session:
        :param tk:
        :return: 设置成功 True
        """
        # 发送设置cookies_tk的请求
        data = {
            'tk': tk
        }

        uam_auth_client_response = session.post(url=UrlConfig.get_uam_auth_client_url(),
                                                data=data)
        # 处理请求响应的信息
        if uam_auth_client_response.cookies.get('tk'):
            return True
        return False


if __name__ == '__main__':
    pass
