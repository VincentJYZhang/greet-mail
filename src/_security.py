"""

    使用时除了填写这个文件以外，还需要将文件名前的下划线删去

    如果users较多，可以单独简历一个users.json文件存储，删去本文件的users列表后，使用如下代码：    
    users = []
    with open("./users.json",'r', encoding='utf-8') as load_f:
        users = json.load(load_f)

"""


MAIL_USR = ''
MAIL_PWD = ''

weather_api_key = ""   # 从聚合数据中申请的，可以换源然后修改weather.py文件

# news_api_key = ""   # 废弃功能


myname = ''


users = [
    {
        "first_name":"某某",
        "last_name":"张",
        "full_name":"张某某",
        "first_name_en":"Vincent",
        "last_name_en":"Zhang",
        "mail":"xxxxxx@xx.com",
        "city_ch":"北京",
        "city_en":"Beijing",
        "weibo_fellow":{},
        "news_type":""
    },
    {
        "first_name":"某某",
        "last_name":"李",
        "full_name":"李某某",
        "first_name_en":"Moumou",
        "last_name_en":"Li",
        "mail":"xxxxxx@xx.com",
        "city_ch":"北京",
        "city_en":"Beijing",
        "weibo_fellow":{},
        "news_type":""
    }
]
