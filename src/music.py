"""
    music.py

    获取音乐榜

    write on 2018.09.15
"""


__author__ = "Vincent Zhang"

import template
import requests
import json
import re


class musicAcquirer:

    @staticmethod
    def getJson():
        
        url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_opt.fcg?page=index&format=html&tpl=macv4&v8debug=1&jsonCallback=jsonCallback'

        headers = {
            "Accept":"*/*",
            "Cookie":"pt2gguin=o1403992259; tvfe_boss_uuid=89f10642caa894f6; pgv_pvid=3655342803; o_cookie=812400875; ptcz=536f26fa29dc70ef67e4f18279cbbcde8070af3602495e881b611fe8e9f1cf5e; pgv_pvi=9640849408; RK=JO0aPTrbYW; yqq_stat=0",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-Hans-CN, zh-Hans; q=0.8, ja; q=0.6, en-US; q=0.4, en; q=0.2",
            "Cache-Control": "no-cache",
            "Host": "c.y.qq.com",
            "Referer":"https://y.qq.com/n/yqq/toplist/4.html",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }

        r = requests.get(url,headers=headers)
        return json.loads(r.text[14:-1])

    @staticmethod
    def transMess(data):

        temp = "<li>{value}</li>"

        popular_mess = """ """

        for song in data[0]['List'][0]['songlist']:
            popular_mess = popular_mess + temp.format(value=song['songname'] + ' - ' + song['singername'])
            

        hot_mess = """ """

        for song in data[0]['List'][1]['songlist']:
            hot_mess = hot_mess + temp.format(value=song['songname'] + ' - ' + song['singername'])


        new_mess = """ """
        for song in data[0]['List'][2]['songlist']:
            new_mess = new_mess + temp.format(value=song['songname'] + ' - ' + song['singername'])

        return template.MUSIC_TEMP.format(popular=popular_mess, hot=hot_mess, new=new_mess)
     

    @staticmethod
    def getMusic():
        return musicAcquirer.transMess(musicAcquirer.getJson())


if __name__ == '__main__':
        print(musicAcquirer.getMusic())