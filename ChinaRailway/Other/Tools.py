import os
import smtplib
import threading
from datetime import date, datetime
from email.mime.text import MIMEText

from selenium.webdriver.edge.webdriver import WebDriver

from Other.Config import MailConfig, GlobalConfig

from Other.MyError import MyError


def get_encrypted_data(selenium_browser: WebDriver, path: str) -> str:
    selenium_browser.get(path)
    encrypted_data = selenium_browser.execute_script("return window.json_ua.toString()")
    os.remove(path)
    return encrypted_data


def clean_tickets_info(result: list, map: dict) -> list:
    """
    车票信息格式化
    :param result:
    :param map:
    :return:
    """
    cX = []
    for i in result:
        c1 = {}
        cV = i.split('|')
        c1['secretStr'] = cV[0]
        c1['buttonTextInfo'] = cV[1]
        cZ = {'train_no': cV[2], 'station_train_code': cV[3], 'start_station_telecode': cV[4],
              'end_station_telecode': cV[5], 'from_station_telecode': cV[6], 'to_station_telecode': cV[7],
              'start_time': cV[8], 'arrive_time': cV[9], 'lishi': cV[10], 'canWebBuy': cV[11],
              'yp_info': cV[12],
              'start_train_date': cV[13], 'train_seat_feature': cV[14], 'location_code': cV[15],
              'from_station_no': cV[16], 'to_station_no': cV[17], 'is_support_card': cV[18],
              'controlled_train_flag': cV[19], 'gg_num': cV[20] if cV[20] else "--",
              'gr_num': cV[21] if cV[21] else "--", 'qt_num': cV[22] if cV[22] else "--",
              'rw_num': cV[23] if cV[23] else "--", 'rz_num': cV[24] if cV[24] else "--",
              'tz_num': cV[25] if cV[25] else "--", 'wz_num': cV[26] if cV[26] else "--",
              'yb_num': cV[27] if cV[27] else "--", 'yw_num': cV[28] if cV[28] else "--",
              'yz_num': cV[29] if cV[29] else "--", 'ze_num': cV[30] if cV[30] else "--",
              'zy_num': cV[31] if cV[31] else "--", 'swz_num': cV[32] if cV[32] else "--",
              'srrb_num': cV[33] if cV[33] else "--", 'yp_ex': cV[34], 'seat_types': cV[35],
              'exchange_train_flag': cV[36], 'houbu_train_flag': cV[37], 'houbu_seat_limit': cV[38],
              'yp_info_new': cV[39]}
        if len(cV) > 46:
            cZ['dw_flag'] = cV[46]

        if len(cV) > 48:
            cZ['stopcheckTime'] = cV[48]

        if len(cV) > 49:
            cZ['country_flag'] = cV[49]
            cZ['local_arrive_time'] = cV[50]
            cZ['local_start_time'] = cV[51]

        cZ['from_station_name'] = map[cV[6]]
        cZ['to_station_name'] = map[cV[7]]
        c1['queryLeftNewDTO'] = cZ

        cX.append(c1)
    return cX


def check_date(train_date: str) -> str:
    try:
        format = '%Y-%m-%d'
        train_date = datetime.strptime(train_date, format).date()

        if train_date < date.today():
            raise ValueError('输入的日期不能小于今天的日期！')

        train_date = date.strftime(train_date, format)
    except ValueError:
        raise MyError(error_messages='日期输入错误！')
    return train_date


def check_station_name(station_name: str) -> str:
    try:
        station_name = GlobalConfig.get_station_name()[station_name]
    except KeyError:
        raise MyError(error_messages='站点输入错误！')
    return station_name


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
    pass
