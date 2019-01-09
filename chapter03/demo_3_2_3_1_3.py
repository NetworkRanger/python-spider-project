#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:10

"""
带参数的GET请求
"""

import requests
payload = {'Keywords': 'blog:qiyeboy', 'pageindex': 1}
r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=payload)
print r.url