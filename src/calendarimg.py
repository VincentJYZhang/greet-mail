"""
    calendarimg.py

    获取单向历

    write on 2018.09.15
"""


__author__ = "Vincent Zhang"


import pgconfig
import usrconfig
import requests
import json
import re
import time
import os


class calendarAcquirer:

    @staticmethod
    def getUrl():
        
        headers = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate, br",
            "Connection":"keep-alive",
            "Origin":"http://web.okjike.com",
            "platform":"web",
            "Referer":"https://m.weibo.cn/u/1673965152",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }

        url = "https://m.weibo.cn/api/container/getIndex?type=uid&value=1673965152&containerid=1076031673965152"

        r = requests.get(url, headers=headers)

        data = json.loads(r.text)

        imgUrl = ""
        for card in data['data']['cards']:
            if card['mblog']['page_info']['page_title'] == "#单向历#":
                imgUrl = card['mblog']['original_pic']
                break

        return imgUrl

    @staticmethod
    def saveImg(url):
        
        folder_path = usrconfig.FOLDER_PATH_

        if folder_path[-1] != '/':
            folder_path = folder_path + '/'

		# 格式化成2018-09-12形式
        time_str = time.strftime("%Y-%m-%d", time.localtime())

        if os.path.exists(folder_path) == False:
            os.makedirs(folder_path)

        img_html = requests.get(url)
        img_name = folder_path + 'calendar-' + time_str + '.jpg'

        with open(img_name, 'wb') as file:
            file.write(img_html.content)
            file.flush()
        file.close()

    @staticmethod
    def getImg():
        calendarAcquirer.saveImg(calendarAcquirer.getUrl())


if __name__ == '__main__':
        calendarAcquirer.saveImg(calendarAcquirer.getUrl())