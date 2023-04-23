import requests
from requests import Session
from requests.cookies import RequestsCookieJar
from selenium.webdriver.edge.webdriver import WebDriver


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


if __name__ == '__main__':
    pass
