from requests import Session, Response
from selenium.webdriver import ActionChains
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Other.Config import UrlConfig
from Other.MyError import MyError


class Login(object):
    def __init__(self):
        raise MyError(error_messages="Login对象不能被创建。")

    @classmethod
    def password_slider_login(cls, username: str, password: str, browser: Edge) -> bool:
        """
        12306滑块验证登录
        :param username: eg: '18322******'
        :param password: eg: '123456'
        :param browser: eg: Edge()
        :return: 登录成功 True
        """
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
                               rand_code: str, session: Session, browser: Edge) -> dict:
        """
        12306短信验证登录
        :param username: eg: '18322******'
        :param password: eg: '123456'
        :param rand_code: eg: '1234'
        :param session: eg: Session()
        :param browser: eg: Edge()
        :return: 登录成功 True
        """
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
        return passport_login_json

    @classmethod
    def message_code(cls, session: Session, username: str, cast_num: str) -> dict:
        """
        请求12306发送短信验证码
        :param session:
        :param username: 用户名 or 手机号 or 邮箱
        :param cast_num: 身份证后四位
        :return: {"result_message":"获取手机验证码成功！","result_code":0} {"result_message":"身份证后四位不匹配!","result_code":11}
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
        return message_code_json

    @classmethod
    def qr_login(cls, session: Session) -> dict:
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
        return qr64_json

    @classmethod
    def check_qr_login(cls, session: Session, data: dict) -> dict:
        """
        检测二维码是否已识别且已授权
        :param session:
        :param data: 发送检测二维码状态请求的post参数
        :return: 登录成功 True
        """
        # 发送检测二维码状态请求
        check_qr_response = session.post(url=UrlConfig.get_check_qr_url(), data=data)
        # 处理请求的响应信息
        check_qr_json = check_qr_response.json()
        return check_qr_json

    @classmethod
    def get_uam_tk(cls, session: Session) -> dict:
        """
        登录成功后设置cookies_uamtk并获取newapptk
        :param session:
        :return: {"apptk":null,"result_message":"验证通过","result_code":0,"newapptk":"abAKLJqkTeDMVkjCeiFts0xV95W_NKguh5KgHqBro78koZ1Z0"}
        """
        # 发送设置cookies_uamtk并获取newapptk的请求
        data = {
            'appid': 'otn'
        }
        uam_tk_response = session.post(url=UrlConfig.get_uam_tk_url(), data=data)
        # 处理请求响应的信息
        uam_tk_json = uam_tk_response.json()
        return uam_tk_json

    @classmethod
    def get_uam_auth_client(cls, session: Session, tk: str) -> Response:
        """
        登录成功后设置cookies_tk
        :param session:
        :param tk:
        :return:
        """
        # 发送设置cookies_tk的请求
        data = {
            'tk': tk
        }

        uam_auth_client_response = session.post(url=UrlConfig.get_uam_auth_client_url(),
                                                data=data)

        return uam_auth_client_response


if __name__ == '__main__':
    pass
