import os
import smtplib
from email.mime.text import MIMEText

import requests
from requests import Session
from requests.cookies import RequestsCookieJar
from selenium.webdriver.edge.webdriver import WebDriver

from utils.Config import MailConfig


def requests_session_cookies2selenium_browser_cookies(requests_session_cookies: RequestsCookieJar) -> list:
    """
    将requests.Session的cookies转化为WebDriver的cookies
    :param requests_session_cookies: requests.Session的cookies eg: requests.Session.cookies
    :return: [{"domain": ,"name": ,"value": ,},{},...]
    """
    selenium_browser_cookies = []
    for requests_session_cookie in requests_session_cookies:
        selenium_browser_cookie = {'domain': requests_session_cookie.domain, 'name': requests_session_cookie.name,
                                   'value': requests_session_cookie.value}
        selenium_browser_cookies.append(selenium_browser_cookie)

    return selenium_browser_cookies


def selenium_browser_cookies2requests_session_cookies(selenium_browser_cookies: list) -> RequestsCookieJar:
    """
    将WebDriver的cookies转化为requests.Session的cookies
    :param selenium_browser_cookies: WebDriver的cookies eg: selenium.webdriver.Edge.get_cookies()
    :return: requests.Session的cookies
    """
    requests_session_cookies = {}

    for selenium_browser_cookie in selenium_browser_cookies:
        requests_session_cookies[selenium_browser_cookie['name']] = selenium_browser_cookie['value']
        requests_session_cookies['domain'] = selenium_browser_cookie['domain']
    requests_session_cookies = requests.utils.cookiejar_from_dict(requests_session_cookies)

    return requests_session_cookies


def update_selenium_browser_cookies_from_requests_session_cookies(selenium_browser: WebDriver,
                                                                  requests_session: Session) -> bool:
    """
    将WebDriver的cookies更新为Session的cookies
    :param selenium_browser: selenium下的浏览器 eg: selenium.webdriver.Edge
    :param requests_session: requests下的会话 eg: requests.Session
    :return: 更新成功 True
    """
    # 获取browser_cookies
    selenium_browser_cookies = selenium_browser.get_cookies()
    # selenium_cookies 转成 requests_session_cookies
    requests_session_cookies = selenium_browser_cookies2requests_session_cookies(
        selenium_browser_cookies=selenium_browser_cookies)
    # 更新requests_session_cookies
    requests_session.cookies.update(requests_session_cookies)
    return True


def update_requests_session_cookies_from_selenium_browser_cookies(requests_session: Session,
                                                                  selenium_browser: WebDriver) -> bool:
    """
    将Session的cookies更新为WebDriver的cookies
    :param requests_session: selenium下的浏览器 eg: selenium.webdriver.Edge
    :param selenium_browser: requests下的会话 eg: requests.Session
    :return: 更新成功 True
    """
    # 获取requests_session_cookies
    requests_session_cookies = requests_session.cookies
    # requests_session_cookies 转成 selenium_cookies
    selenium_browser_cookies = requests_session_cookies2selenium_browser_cookies(
        requests_session_cookies=requests_session_cookies)
    # 更新selenium_browser_cookies
    for selenium_browser_cookie in selenium_browser_cookies:
        selenium_browser.add_cookie(cookie_dict=selenium_browser_cookie)
    return True


def get_encrypted_data(selenium_browser: WebDriver, path: str) -> str:
    selenium_browser.get(path)
    encrypted_data = selenium_browser.execute_script("return window.json_ua.toString()")
    os.remove(path)
    return encrypted_data


def sendmail(message: str) -> None:
    # 服务器
    smtp_server = MailConfig.SMTP_SERVER
    # 发送邮件的地址
    sender = MailConfig.USER
    # 授权密码(不等同于登录密码)
    password = MailConfig.PASSWORD
    # 转为邮件文本
    msg = MIMEText(_text=message)
    # 邮件主题
    msg["Subject"] = "Train12306"
    # 邮件的发送者
    msg["From"] = sender
    # 连接服务器
    mail_sever = smtplib.SMTP(host=smtp_server, port=587)
    mail_sever.ehlo()
    mail_sever.starttls()
    # 登录
    mail_sever.login(user=sender, password=password)
    # 发送邮件
    mail_sever.sendmail(from_addr=sender, to_addrs=MailConfig.TO_ADDRS, msg=msg.as_string())
    mail_sever.quit()


if __name__ == '__main__':
    sendmail('Test')
