"""
    holidaytts.py

    得到节日信息
    调用格式 HolidayAcquirer.getHolidayMess(cityname)

    write on 2018.09.14
"""


__author__ = "Vincent Zhang"

import pgconfig
import requests
import json


class HolidayAcquirer:

    @staticmethod
    def getJson():
        url = "http://lanfly.vicp.io/api/holiday/tts"
        r = requests.get(url)

        try_count = pgconfig.try_count

        while (r.status_code != 200 and try_count > 0):
            r = requests.get(url)
            try_count -= 1

        r.raise_for_status()

        return json.loads(r.text)

    @staticmethod
    def transMESS(json_data):

        mess = ""

        # 获取正常正常
        if json_data['code'] == 0:
            mess = json_data['tts']

        return mess

    @staticmethod
    def getHolidayMess():
        return HolidayAcquirer.transMESS(HolidayAcquirer.getJson())


    @staticmethod
    def getInfo():
        """
        uniform interface
        """
        return HolidayAcquirer.getHolidayMess()


if __name__ == '__main__':
    print(HolidayAcquirer.getHolidayMess())