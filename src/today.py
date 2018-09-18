"""
    获得历史上的今天

    write on 2018.09.14
"""

__author__ = "Vincent Zhang"

import template
import pgconfig
import usrconfig
import template
import requests
import json


class HistoryAcquirer:

    @staticmethod
    def getJson():
        url = pgconfig.today_api
        r = requests.get(url)

        try_count = pgconfig.try_count

        while (r.status_code != 200 and try_count > 0):
            r = requests.get(url)
            try_count -= 1

        r.raise_for_status()

        return json.loads(r.text)

    @staticmethod
    def transMESS(json_data):
        
        data = json_data["result"]
        mess = """"""
        temp = """<tr><td style="white-space:nowrap;text-align:center">{year}</td><td style="text-align:left">{event}</td></tr>"""
        
        for i in range(len(data)):
            mess = mess + temp.format(year=data[i]["year"], event=data[i]["title"])

        return mess

    @staticmethod
    def getTodayMess():
        
        json_data = HistoryAcquirer.getJson()
        table = HistoryAcquirer.transMESS(json_data)

        return template.TODAY_TEMP.format(mess=table)


