#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:28

"""
检测是否发生了重定向动作
"""

import urllib2
response = urllib2.urlopen('http://www.zhihu.cn')
isRedirected = response.geturl() == 'http://www.zhihu.cn'
print isRedirected