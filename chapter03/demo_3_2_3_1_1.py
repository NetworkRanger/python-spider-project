#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:07

"""
实现一个完整的请求与响应模型:GET
"""

import requests
r = requests.get('http://www.baidu.com')
print r.content