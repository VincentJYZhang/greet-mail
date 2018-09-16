"""
    程序配置文件
    
    这个文件用于配置一些固定设置，如网址等。
    如果它改了登陆方式或者格式就没办法了呢  :)

    write on 2018.09.13
"""


import security

weather_api = "http://v.juhe.cn/weather/index?format=1&cityname={cityname}&key={appkey}"
weather_api_key = security.weather_api_key

# 废弃
# news_api = "http://v.juhe.cn/toutiao/index?type={type}&key={appkey}"
# news_api_key = security.news_api_key

weibo_api = "https://m.weibo.cn/api/container/getIndex?type=uid&value={uid}&containerid=107603{uid}"

today_api = "http://www.ipip5.com/today/api.php?type=json"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept':'application/json, text/plain, */*',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'gzip',
    'Connection':'close',
    'Referer':'http://www.baidu.com/'
    }

uid = {"danxiang":1673965152}