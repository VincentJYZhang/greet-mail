"""
    template.py

    存储邮件内容模板
"""

__author__ = 'Vincent Zhang'


MAIL_TEMP = """<!doctype html>
<html lang="zh-cn">
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width initial-scale=1'>
    <title></title>
</head>
<body style="width:100%;height: 100%;">

    <div style="height:100%;width:95%;margin-right:auto;margin-left:auto;border: 1px solid #d8d8d8;">
        <div style="height:100%;width:90%;margin-right:auto;margin-left:auto;margin-top:10px;word-break:break-all;">
            <h1>{date} 的问候</h1>
            <p style="word-wrap:break-word;text-indent:40px;">{greet}</p>
            <p>&nbsp;</p>
            <h2>一觉醒来世界发生了什么</h2>
            {news}
            <p>&nbsp;</p>
            <h2>历史上的今天</h2>
            <div style="margin-right:auto;margin-left:auto;width:90%">
                <table border="1px" style="width:100%">
                {today}
                </table>
            </div>
            <p>&nbsp;</p>
            <h2>单向历 {date}</h2>
            <p style="text-align:center;width:100%"><img src="cid:0" style="max-width:100"></p>
            <p>&nbsp;</p>
            <h2>腾讯音乐榜</h2>
            <p>数据更新于{date}</p>
            {music}
            <p>&nbsp;</p>
            <h2>每日英语</h2>
            {english}
            <p>&nbsp;</p>
            <h2>每日bing壁纸</h2>
            <p>{img_description}</p>
            <p style="text-align:center;width:100%"><img src="cid:1" style="max-width:100"></p>
            <p>&nbsp;</p>
            <div style="margin-top:20px;text-align:center">
            <p style="text-align:center">- From {myname} on {date} -</p>
            <p style="text-align:center">Have a good day!</p>
            </div>
        </div>
    </div>
</body>
</html>"""

NEWS_TEMP = """{mess}<blockquote><p>更多请看：{url}</p></blockquote>"""

TODAY_TEMP = """<tbody>{mess}</tbody>"""

MUSIC_TEMP = """<h3>流行指数</h3><ol>{popular}</ol>
<h3>热歌榜</h3><ol>{hot}</ol>
<h3>新歌榜</h3><ol>{new}</ol>"""

ENGLISH_TEMP = """<blockquote><p>{sentence_en}</p><p>{sentence_ch}</p></blockquote><p>{comment}</p>"""