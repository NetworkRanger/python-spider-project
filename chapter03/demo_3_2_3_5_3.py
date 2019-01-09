#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:27

"""
Cookie处理:自动化
"""

import requests

loginUrl = 'http://www.xxxxxx.com/login'
s = requests.Session()
# 首先访问登录界面，作为游客，服务器会先分配一个cookie
r = s.get(loginUrl, allow_redirects=True)
datas = {'name': 'qiye', 'passwd': 'qiye'}
# 向登录链接发送post请求，验证成功，游客权限转为会员权限
r = s.post(loginUrl, data=datas, allow_redirects=True)
print r.text
