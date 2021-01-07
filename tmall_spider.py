# -*- coding: utf-8 -*-
import requests
import re
import time
import pandas as pd
import cfg

#需要修改的参数位于cfg.py

def set_up(times, url_ori, a, b,cookie):
    #找到评论接口,构造相应页数的接口
    url_comment_list = []
    for i in range(int(page)):
        url_comment_list.append(a + str(i) + b)
    
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Host': 'rate.tmall.com',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': url_ori,
        'Connection': 'keep-alive',
        'Cookie' : cookie ,
        'TE': 'Trailers'
    }

    spider(times, url_comment_list, headers)

def spider(times, url_2,headers):
    for y in range(len(url_2)):
        response = requests.get(url_2[y], headers=headers, timeout=30).content.decode()
        # 初次评价
        evaluate = re.findall(',"rateContent":"(.*?)"',response)
        # 分类
        kinds = re.findall('"auctionSku":"(.*?)",',response)
        for i in range(len(evaluate)):
            # 将每一页的评论添加到总评论里面
            Evaluate.append({'商品的种类': kinds[i],'商品的评价': evaluate[i],})
        print('第'+str(y+1)+'页的评论获取成功')
        # 延时，防止检测
        time.sleep(5)

    print('一共获取了'+str(len(Evaluate))+'评论')
    for i in Evaluate:
        print(i)
    df = pd.DataFrame(Evaluate)
    df.to_csv('./rst%d.csv' % (times))


if __name__ == '__main__':
    page = 10
    Evaluate =[]

    url_ori_list = cfg.url_ori_list
    url_comment_list = cfg.url_comment_list
    cookie = cfg.cookie

    for i in range(len(url_ori_list)):
        url_ori = url_ori_list[i]
        url_comment_split = url_comment_list[i].split('currentPage=2')
        url_before_curPage = url_comment_split[0] + 'currentPage='
        url_after_curPage = url_comment_split[1]

        set_up(i, url_ori, url_before_curPage, url_after_curPage, cookie)
