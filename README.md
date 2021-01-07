# Tmall_spider
> 天猫评论爬虫极简版

使用前请将cfg.py中的参数换成需要的。其中:
- url_ori:指的是商品原始的链接。
- url_comment:指的是商品评论的链接。这个需要点击评价中的下一页按钮，抓取数据包中的headers部分，将其补充完整。
- cookie:与上述操作一样，抓取到的cookie部分填入即可。如果失效再来一次。

<br>

使用时运行以下命令即可:
```console
python tmall_spider.py
```