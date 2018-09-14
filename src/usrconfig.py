"""
    用户自定义文件

    这个文件用于用户自定义设置，包括用户名密码和邮箱设置

    write on 2018.09.13
"""

import security


users = security.users

myname = security.myname


FOLDER_PATH_ = "./pictures/"


# ==== 以下是邮箱设置 ====

# 是否发送邮件
MAIL_MODE = True
# 发送邮件完成后是否保存文件
SAVE_IMG = True


MODEL_TODAY = True

ZHANKU_IMG = "https://www.zcool.com.cn/top/index.do"


# 邮箱服务器地址
MAIL_HOST = 'smtp.163.com'
# 邮箱用户及密码
MAIL_USR = security.MAIL_USR
MAIL_PWD = security.MAIL_PWD

# 发件人
SEND_MAIL = ""
# 收件人，数组支持多个发送
RECE_MAIL = [""]

# 邮件整体模板
MESS_TEMP = """{head}
{body}
{tail}"""

# 邮件正文
MESS_BODY = """{weather}
{news}
{calendar}
"""

# 邮件头部
MESS_HEAD = """From: From Person <{sender}>
To: To Person <{receiver}>
Subject: {subject}"""

# 邮件结尾
MESS_TAIL = ""

MESS_WEATHER = ""

MESS_NEWS = ""

MESS_CALENDAR = ""

NEWS_CARD_TEMP = """<div class="card m-panel card9 f-weibo"><div class="card-wrap">
<header class="weibo-top m-box">
<div class="m-box-col">
<div class="m-text-box">
<div class="f-r"  style="font-size:10">{data_time}</div>
<div class="inline-block anim-load" style="font-size:10">
{author_name}
</div>
</div>
</div>
</header>
<article class="weibo-main">
<div class="weibo-og">
<p class="txt-margin anim-load">{title}</p>
</div>
<div class="m-avatar-box">
原文链接：<a href="{news_link}">{news_link}</a>
</div>
</article>
<p></p>
</div>
</div>"""
