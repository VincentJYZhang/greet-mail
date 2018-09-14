"""
    news.py

    获取新闻信息，转换为网页代码块
    调用格式 NewsAcquirer.getNewsMess(news_type)

    write on 2018.09.14
"""


__author__ = "Vincent Zhang"


import pgconfig
import usrconfig
import requests
import json


class NewsAcquirer:

    @staticmethod
    def getJson(news_type):
        url = pgconfig.news_api.format(type=news_type,appkey=pgconfig.news_api_key)
        r = requests.get(url)
        return json.loads(r.content)

    @staticmethod
    def transMESS(json_data):

        data = json_data["result"]["data"]  # list of dict

        data = data[:8]

        mess = """"""
        temp = usrconfig.NEWS_CARD_TEMP

        for one_news in data:
            mess = mess + temp.format(data_time=one_news["date"],author_name=one_news["author_name"],title=one_news["title"],news_link=one_news["url"])
            temp = usrconfig.NEWS_CARD_TEMP

        return mess

    @staticmethod
    def getNewsMess(news_type):
        return NewsAcquirer.transMESS(NewsAcquirer.getJson(news_type))


if __name__ == '__main__':
    print(NewsAcquirer.getNewsMess("keji,top"))