#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:26

"""
获取HTTP响应码
"""

import urllib2
try:
    response = urllib2.urlopen('http://www.google.com')
    print response
except urllib2.HTTPError as e:
    if hasattr(e, 'code'):
        print 'Error code:', e.code