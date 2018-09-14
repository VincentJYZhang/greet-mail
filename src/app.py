"""
    app.py

    整个程序的调度系统

    write on 2018.09.14
"""

__author__ = 'Vincent Zhang'


import usrconfig
import pgconfig
import template
from mail import MailSender
from weather import WeatherAcquirer
from news import NewsAcquirer
from today import HistoryAcquirer
from topImg import imgAcquirer
import time

__author__ = 'Vincent Zhang'


def start():

    if usrconfig.MODEL_TODAY == True:
        today_mess = HistoryAcquirer.getTodayMess()
    else:
        today_mess = ""

    imgAcquirer.getImg()

    for usr in usrconfig.users:
        temp = template.MAIL_TEMP
        weather_mess = WeatherAcquirer.getWeatherMess(usr["city_ch"])
        news_mess = NewsAcquirer.getNewsMess(usr["news_type"])
        greet_mess = "早上好，" + usr["full_name"] + "！" + weather_mess
        mess = temp.format(greet=greet_mess,today=today_mess,news=news_mess)
        MailSender.sendmail(usr["full_name"], usr["mail"], mess)
        time.sleep(5)


if __name__ == '__main__':
    start()
