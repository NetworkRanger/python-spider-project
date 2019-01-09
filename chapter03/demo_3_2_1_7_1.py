#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:35

"""
使用ProxyHandler在程序中动态设置代理
"""

import urllib2
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener([proxy])
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.zhichu.com/')
print response.read()