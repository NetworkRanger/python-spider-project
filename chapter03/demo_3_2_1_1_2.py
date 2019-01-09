#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:03

"""
上面对http://www.zhihu.com的请求响应分为两步，一步是请求，一步是响应
"""

import urllib2

# 请求
request = urllib2.Request('http://www.zhihu.com')
# 响应
response = urllib2.urlopen(request)
html = response.read()
print html
