#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:08

"""
实现一个完整的请求与响应模型:POST
"""

import requests
postdata = {'key': 'value'}
r = requests.post('http://www.xxxxxx.com/login', data=postdata)
print r.content

