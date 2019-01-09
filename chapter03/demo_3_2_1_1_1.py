#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:02

"""
最简单的形式
"""
import urllib2
response = urllib2.urlopen('http://www.zhihu.com')
html = response.read()
print html