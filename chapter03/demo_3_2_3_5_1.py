#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:23

"""
Cookie处理:获取cookie
"""

import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.baidu.com', headers=headers)
# 遍历出所有的cookie字段的值
for cookie in r.cookies.keys():
    print cookie+':'+r.cookies.get(cookie)