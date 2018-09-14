

MAIL_TEMP = """
    <!DOCTYPE html>
    <html lang="zh-cn">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
        <meta name="format-detection" content="telephone=no">
        <title>来自Vincent Zhang的问候</title>
        <meta name="theme-color" content="#F3F3F3">
        <meta name="apple-mobile-web-app-status-bar-style" content="white">
        <style>
            html,
            body {{
                height: 100%;
            }}

            #app {{
                width: 95%;
                margin-right: auto;
                margin-left: auto;
                border: 1px solid #d8d8d8;
            }}

            [v-cloak] {{
                display: none;
            }}

            .wb-item-wrap .card9.card {{
                margin: 0
            }}

            .f-weibo .m-img-box {{
                background-color: #e6e6e6
            }}

            .empty-bg {{
                width: 100%;
                background-color: #e6e6e6;
                height: .375rem;
            }}

            .inline-block {{
                display: inline-block
            }}

            .txt-margin {{
                margin: 0 0 1rem 0
            }}

            .width-min {{
                width: 4.375rem
            }}

            .anim-load {{
                animation: load .5s ease-out;
                -moz-animation: load .5s ease-out;
                -webkit-animation: load .5s ease-out;
                -o-animation: load .5s ease-out
            }}

            @keyframes load {{
                0% {{
                    background-color: #fff
                }}
                100% {{
                    background-color: #e6e6e6
                }}
            }}

            @-moz-keyframes load {{
                0% {{
                    background-color: #fff
                }}
                100% {{
                    background-color: #e6e6e6
                }}
            }}

            @-webkit-keyframes load {{
                0% {{
                    background-color: #fff
                }}
                100% {{
                    background-color: #e6e6e6
                }}
            }}

            .f-more {{
                letter-spacing: .1rem
            }}

            .f-weibo .f-card-title {{
                margin: -1rem -1rem .5rem -1rem;
                padding: 0 1rem;
                border-width: 0
            }}

            .f-weibo .m-avatar-box .m-img-box .m-icon {{
                font-size: 10px;
                margin-left: .75rem
            }}

            .iosx3 .card9 .f-card-title {{
                border-width: 0
            }}

            .iosx2 .card9 .f-card-title {{
                border-width: 0
            }}

            .f-weibo.card9 {{
                border-bottom: 1px solid #e6e6e6
            }}

            .iosx3 .f-weibo.card9 {{
                border-bottom: .36px solid #e6e6e6
            }}

            .iosx2 .f-weibo.card9 {{
                border-bottom: .5px solid #e6e6e6
            }}

            .f-weibo.card9>.card-wrap {{
                margin-left: .75rem;
                margin-right: .75rem
            }}

            .f-weibo.card9.m-panel {{
                border-top-width: 0
            }}

            .f-weibo.card .card-wrap .f-col-wrap {{
                padding: 0 .9375rem
            }}

            .f-weibo.card9 .m-box-col {{
                min-width: 0
            }}

            .f-weibo.card9 .weibo-top {{
                padding: 0 0 0 .25rem
            }}

            .f-weibo.card9 .weibo-top .m-box-col .m-icon {{
                margin-left: 1px
            }}

            .f-weibo.card9 .weibo-main .weibo-og {{
                padding: .5rem 0 0 .25rem
            }}

            .f-weibo.card9 .weibo-main .card-wrap~.weibo-rp {{
                margin-top: 0.5rem
            }}

            .f-weibo.card9 .weibo-main .media-b {{
                margin: .25rem 0 -.375rem
            }}

            .f-weibo.card9 .weibo-main .media-b .m-auto-list {{
                margin: 0 0 -.25rem
            }}

            .f-weibo .weibo-top .m-text-box {{
                margin: .15rem 0 .5rem .1rem
            }}

            .f-weibo .f-r {{
                float: right
            }}

            .f-weibo .weibo-main .weibo-og {{
                font-size: .5000rem
            }}

            .f-weibo .weibo-rp .weibo-text {{
                font-size: .5000rem
            }}

            .f-weibo .weibo-rp .f-footer-ctrl {{
                padding: 0.625rem 0 0
            }}

            .f-weibo .f-bg-img {{
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                position: absolute;
                width: 100%;
                height: 100%
            }}

            .f-footer-ctrl {{
                border-top-width: 0;
                height: 1.1rem;
                padding: 1rem .375rem 1rem 0;
                margin: 0 0.75rem
            }}

            .f-footer-ctrl .m-diy-btn {{
                color: rgba(40, 47, 60, 0.8);
                height: 100%;
                float: left
            }}

            .f-footer-ctrl .m-diy-btn+.m-diy-btn {{
                margin-left: 1.6875rem
            }}

            .f-footer-ctrl .m-diy-btn .m-icon {{
                font-size: 12px
            }}

            .f-footer-ctrl aside {{
                float: right;
                color: rgba(40, 47, 60, 0.8)
            }}

            .f-footer-ctrl .m-font {{
                font-size: 1rem;
                vertical-align: middle
            }}

            .f-footer-ctrl .m-diy-btn h4 {{
                display: inline-block;
                margin-top: 0;
                margin-left: .0rem
            }}

            .all-wrap {{
                margin-top: 20px;
                height: 100%;
                width: 90%;
                margin-left: auto;
                margin-right: auto;
                word-break: break-all;
            }}

            .weather-wrap {{
                width: 95%;
                margin-left: auto;
                margin-right: auto;
                margin-bottom: 30px;
            }}

            .news-wrap-title {{
                text-align: center;
                margin-top: 20px;
                margin-bottom: 30px;
                font-size: 25px
            }}
        </style>

    </head>

    <body>
        <div class="all-wrap">
            <div class="weather-wrap">
                <p style="width:100%;font-size:20px;text-indent:50px">{greet}</p>
            </div>
            <div id="app" class="m-container-max">
                <div class="wb-item-wrap">
                    <div class="wb-item">

                    <h3 class="news-wrap-title" style="font-size:20px;text-align:center">
                            站酷今日榜首<br><p></p>
                    </h3>
                    <p style="text-align:center"><img src="cid:0"></p>
                    <br><p></p>

                    {today}
                        <h3 class="news-wrap-title" style="font-size:20px;text-align:center">
                            每日新闻<br><p></p>
                        </h3>{news}
                    </div>
                </div>
            </div>
        </div>
    </body>

    </html>
    """