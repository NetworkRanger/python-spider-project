#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:20

"""
响应码code和响应头headers处理
"""

import requests
r = requests.get('http://www.baidu.com')
if r.status_code == requests.codes.ok:
    print r.status_code # 响应码
    print r.headers # 响应头
    print r.headers.get('content-type') # 推荐使用这种获取方式，获取其中的某个字段
    print r.headers['content-type'] # 不推荐使用这种获取方式
else:
    r.raise_for_status()