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

# 功能废弃
# ZHANKU_IMG = "https://www.zcool.com.cn/top/index.do"


# 邮箱服务器地址
MAIL_HOST = 'smtp.163.com'
# 邮箱用户及密码
MAIL_USR = security.MAIL_USR
MAIL_PWD = security.MAIL_PWD