#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:25

"""
urlopen函数提供了对timeout的设置
"""

import urllib2
request = urllib2.Request('http://www.zhihu.com')
response = urllib2.urlopen(request, timeout=2)
html = response.read()
print html