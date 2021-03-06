"""
    app.py

    整个程序的调度系统

    GitHub: https://github.com/VincentJYZhang/greet-mail
    write on 2018.09.14
"""

__author__ = 'Vincent Zhang'

import security
import usrconfig
import pgconfig
import template
from mail import MailSender
from weather import WeatherAcquirer
from news import NewsAcquirer
from today import HistoryAcquirer
# from topImg import imgAcquirer
from calendarimg import calendarAcquirer
from bingImg import bingAcquirer
from music import musicAcquirer
from english import englishAcquirer
from holidaytts import HolidayAcquirer
import time

__author__ = 'Vincent Zhang'


def start():

    time_str = time.strftime("%Y-%m-%d", time.localtime())
    
    if usrconfig.MODEL_TODAY == True:
        today_mess = HistoryAcquirer.getTodayMess()
    else:
        today_mess = ""

    news_mess = NewsAcquirer.getNewsMess()
    music_mess = musicAcquirer.getMusic()
    bing_mess = bingAcquirer.getBing()
    eng_mess = englishAcquirer.getEnglish()
    calendarAcquirer.getImg()
    holiday_mess = HolidayAcquirer.getHolidayMess()

    usr = {}
    cities = []

    for usr in usrconfig.users:
        if usr["city_ch"] not in cities:
            cities.append(usr["city_ch"])

    weather_greets = {}

    for city in cities:
        weather_greets[city] = WeatherAcquirer.getWeatherMess(city)


    # imgAcquirer.getImg()

    for usr in usrconfig.users:
        # weather_mess = WeatherAcquirer.getWeatherMess(usr["city_ch"])
        greet_mess = "早上好，" + usr["full_name"] + "！" + weather_greets[usr["city_ch"]]
        mess = template.MAIL_TEMP.format(date=time_str, \
                                    greet=greet_mess, \
                                    today=today_mess, \
                                    news=news_mess, \
                                    music=music_mess, \
                                    english=eng_mess, \
                                    img_description=bing_mess, \
                                    myname=security.myname, \
                                    holiday=holiday_mess)

        MailSender.sendmail(usr["full_name"], usr["mail"], mess)
        time.sleep(5)


if __name__ == '__main__':
    start()
