"""
    bingImg.py

    获取bing壁纸

    write on 2018.09.15
"""


__author__ = "Vincent Zhang"


import pgconfig
import usrconfig
import requests
import re
import time
import os

class bingAcquirer:

    @staticmethod
    def bingSave():
        
        headers = {
            "Accept":"application/json",
            "App-Version":"4.1.0",
            "Content-Type":"application/json",
            "DNT":"1",
            "Origin":"http://web.okjike.com",
            "platform":"web",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "x-jike-access-token":""
        }

        url = "https://cn.bing.com/?FORM=BEHPTB"

        r = requests.get(url, headers=headers)

        index = re.search(r'/az/hprichbg.+?.jpg',r.text).span()
        imgUrl = 'https://cn.bing.com' + r.text[index[0]:index[1]]
        index = re.search(r'class=\"sc_light\" title=\".+?\"',r.text).span()

        imgName = r.text[index[0]:index[1]]
        index = re.search(r'\".+?\"',imgName[::-1]).span()
        imgName = imgName[-index[1] + 1:-index[0] - 1]

        bingAcquirer.saveImg(imgUrl)

        return imgName

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
        img_name = folder_path + "bing-" + time_str + '.jpg'

        with open(img_name, 'wb') as file:
            file.write(img_html.content)
            file.flush()
        file.close()

    @staticmethod
    def getBing():
        return bingAcquirer.bingSave()


if __name__ == '__main__':
        print(bingAcquirer.getBing())