# 一点小的说明

## 如何运行

单独一次发送：`python app.py` 或者 `python3 app.py`

如果想设置定时发送，建议使用Linux的crontab命令来实现定时运行，比如想每天早上8:30发送就在终端输入：

```
$ crontab -e   # 第一次使用会让你选择编辑器，自己选择常用的，然后输入
30 * * * * python3 .../app.py   # 在...中输入文件路径
```

## 关于部署到服务器 socket.connect(sa) 没有响应

如果部署在服务器上，部分提供商不开放25端口（说是为了提高IP段发邮件的质量）。有两种解决方案（个人推荐第二种）：

- 可以对服务商申请解封25端口（一般要求只能使用第三方SMTP服务器而不能直接发送SMTP邮件）
- 但是针对我们的程序，还有一种更为便捷的解决方案，把 `mail.py` 文件中的 `server = smtplib.SMTP(smtp_server, 25)` 这一行注释了，改成: `server = smtplib.SMTP_SSL(smtp_server, 465)`即可。

## 关于无法找到security

我从中拔除了`security.py`文件，里面主要是我的邮箱、密码、API KEY和接受方信息等，所以你只需要将文件中含有security文件的配置（好像只有四个地方），改成自己的设置即可。


## 关于users的配置

`usrconfig.py`里有个users的对象，主要是邮件的接收方信息，用数组存储，个人信息存为字典，可以给多人发送，主要格式如下所示：

```
users = [
    {
        "first_name":"某某",
        "last_name":"张",
        "full_name":"张某某",
        "first_name_en":"Vincent",
        "last_name_en":"Zhang",
        "mail":"xxxxxx@xx.com",
        "city_ch":"北京",        # 我也想在北上广有房，可惜
        "city_en":"Beijing",
        "weibo_fellow":{},
        "news_type":"top,keji,guoji"
    },
    {
        ...
    }
]
```

配置中`weibo_fellow`是还没做的功能（不影响运行，只是留个位置，以后抓微博信息用）

(*已弃用，可删*)`news_type`是聚合数据新闻头条的新闻类型（之后版本会爬取微博等热门新闻，但说实话不好做分类），具体如下：

- top(头条，默认)
- shehui(社会)
- guonei(国内)
- guoji(国际)
- yule(娱乐)
- tiyu(体育)
- junshi(军事)
- keji(科技)
- caijing(财经)
- shishang(时尚)

设置多个新闻分类的时候请用逗号（英文）隔开。
