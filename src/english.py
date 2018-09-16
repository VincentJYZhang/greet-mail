"""
    english.py

    获取每日英语
    调用方式: englishAcquirer.getEnglish()

    write on 2018.09.15
"""


__author__ = "Vincent Zhang"

import template
import requests
import json
import re
import time

class englishAcquirer:

    @staticmethod
    def getJson():  
        time_str = time.strftime("%Y-%m-%d", time.localtime())
        url = "http://sentence.iciba.com/index.php?callback=jQuery19007435210156345391_1537015701618&c=dailysentence&m=getdetail&title={date}&_=1537015701624"
        url = url.format(date = time_str)

        headers = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Host":"sentence.iciba.com",
            "DNT":"1",
            "Cookie":"UM_distinctid=165dd44bd7cd8-0e97780ebe5833-9393265-144000-165dd44bd7d39",
            "Referer":"http://news.iciba.com/views/dailysentence/daily.html",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }

        r = requests.get(url,headers=headers)
        index = re.search(r'\(.+\)',r.text).span()
        return json.loads(r.text[index[0]+1:index[1]-1])

    @staticmethod
    def transMess(data):

        mess_en = data['content']
        mess_ch = data['note']
        mess_tr = data['translation']
        
        return template.ENGLISH_TEMP.format(sentence_en=mess_en,sentence_ch=mess_ch,comment=mess_tr)
    
    @staticmethod
    def getEnglish():
        return englishAcquirer.transMess(englishAcquirer.getJson())


if __name__ == '__main__':
        print(englishAcquirer.getEnglish())