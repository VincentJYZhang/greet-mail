"""
    news.py

    获取新闻信息，转换为网页代码块
    调用格式 NewsAcquirer.getNewsMess()

    write on 2018.09.14
"""


__author__ = "Vincent Zhang"

import template
import pgconfig
import usrconfig
import requests
import json
import re


class NewsAcquirer:

    @staticmethod
    def getJson():
        
        headers = {
            "Accept":"application/json",
            "App-Version":"4.1.0",
            "Content-Type":"application/json",
            "DNT":"1",
            "Origin":"http://web.okjike.com",
            "platform":"web",
            "Referer":"http://web.okjike.com/topic/553870e8e4b0cafb0a1bef68/official",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "x-jike-access-token":""
        }

        body = {
            "loadMoreKey":"",
            "topic":"553870e8e4b0cafb0a1bef68",
            "limit":20
        }

        url = "https://app.jike.ruguoapp.com/1.0/messages/history"

        r = requests.post(url, headers=headers, data=json.dumps(body))

        try_count = pgconfig.try_count

        while (r.status_code != 200 and try_count > 0):
            r = requests.post(url, headers=headers, data=json.dumps(body))
            try_count -= 1

        r.raise_for_status()

        return json.loads(r.text)

    @staticmethod
    def transMESS(json_data):
        
        # 因为月初有个月初加餐，所以这里得进行一下过滤
        for card in json_data['data']:
            if 'content' in card:
                news = card['content']
                if 'https://www.okjike.com/medium/' in news:
                    break

        news = news.replace("(欢迎到评论区理性发言，友好讨论)","")

        pattern = re.compile(r'\d\. .+?\n')
        result = pattern.findall(news)

        mess = ""

        for res in result:
            mess = mess + "<li>" + res[2:] + "</li>"

        mess = "<ol>" + mess + "</ol>"

        index = re.search(r'https://www.okjike.com/medium/',news).span()
        url = news[index[0]+12:]

        return template.NEWS_TEMP.format(mess=mess,url=url)


    @staticmethod
    def getNewsMess():
        return NewsAcquirer.transMESS(NewsAcquirer.getJson())


    @staticmethod
    def getInfo():
        """
        uniform interface
        """
        return NewsAcquirer.getNewsMess()


if __name__ == '__main__':
    print(NewsAcquirer.getNewsMess())