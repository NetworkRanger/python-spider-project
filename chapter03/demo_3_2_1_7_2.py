#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:37

"""
直接调用opener的open方法代替全局的urlopen方法
"""

import urllib2
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy,)
response = opener.open('http://www.zhihu.com/')
print response.read()