"""
    weather.py

    获取天气信息，转换成问候语
    调用格式 WeatherAcquirer.getWeatherMess(cityname)

    write on 2018.09.14
"""


__author__ = "Vincent Zhang"


import pgconfig
import usrconfig
import requests
import json


class WeatherAcquirer:

    @staticmethod
    def getJson(city_name):

        url = pgconfig.weather_api.format(cityname=city_name,appkey=pgconfig.weather_api_key)
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
        today = data["today"]

        mess = "你所在的" + today["city"] + \
        "今天的天气是" + today["weather"] + "，" +\
        "气温" + today["temperature"] + "（当前" + data["sk"]["temp"] + "℃），" + \
        "紫外线强度" + today["uv_index"] + "。" + \
        "天气" + today["dressing_index"] + "，" + \
        today["dressing_advice"]

        return mess

    @staticmethod
    def getWeatherMess(city_name):
        return WeatherAcquirer.transMESS(WeatherAcquirer.getJson(city_name))


if __name__ == '__main__':
    print(WeatherAcquirer.getWeatherMess("北京"))