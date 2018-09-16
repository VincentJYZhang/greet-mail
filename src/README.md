# 一点小的说明

## 关于无法找到security

我从中拔除了`security.py`文件，里面主要是我的邮箱、密码、API KEY等，所以你只需要将文件中含有security文件的配置（好像只有四个地方），改成自己的设置即可。


## 关于users的配置

users主要是邮件的接收方，用数组存储，可以给多人发送，主要格式如下所示：

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

配置中`weibo_fellow`是还没做的功能（不影响运行，只是留个位置）

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
