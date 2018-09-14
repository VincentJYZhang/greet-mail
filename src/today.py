"""
    获得历史上的今天

    write on 2018.09.14
"""

__author__ = "Vincent Zhang"


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
        return json.loads(r.content)

    @staticmethod
    def transMESS(json_data):
        
        data = json_data["result"]
        mess = """"""
        temp = """<tr><td style="white-space:nowrap">{year}</td><td style="text-align:left">{event}</td></tr>"""
        
        for i in range(len(data)):
            mess = mess + temp.format(year=data[i]["year"], event=data[i]["title"])
        
        mess = "<table style=\"margin-left:auto;margin-right:auto;width:80%\" border=\"1\">" + mess + "</table>"

        return mess

    @staticmethod
    def getTodayMess():
        
        json_data = HistoryAcquirer.getJson()
        table = HistoryAcquirer.transMESS(json_data)

        mess = """
        <div style="text-align:center;">
        <h3 class="news-wrap-title" style="font-size:20px">
        历史上的今天<br><p></p>
        </h3> <div style="text-align:center">
        {table}
        </div>
        <p></p>
        <p></p>
        </div>
        """

        return mess.format(table=table)


