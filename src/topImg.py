"""
    topImg.py

    获取站酷排名第一的图片

    write on 2018.09.14
"""


__author__ = "Vincent Zhang"


import pgconfig
import usrconfig
import requests
import json
import re
import time
import os

class imgAcquirer:

    @staticmethod
    def getUrl():
        
        r = requests.get(usrconfig.ZHANKU_IMG, headers = pgconfig.headers)
        data = r.text
        index = re.search(r'https://img\.zcool\.cn/community/.*?"', data).span()

        return data[index[0]:index[1]-1]

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
        img_name = folder_path + time_str + '.jpg'

        with open(img_name, 'wb') as file:
            file.write(img_html.content)
            file.flush()
        file.close()

    @staticmethod
    def getImg():
        imgAcquirer.saveImg(imgAcquirer.getUrl())


if __name__ == '__main__':
        imgAcquirer.saveImg(imgAcquirer.getUrl())