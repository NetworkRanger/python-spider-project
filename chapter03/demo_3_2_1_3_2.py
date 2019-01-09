#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:20

"""
CookieJar函数进行Cookie的管理:设置Cookie值
"""

import urllib2
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'email=' + 'xxxxxx@163.com'))
req = urllib2.Request('http://www.zhihu.com/')
response = opener.open(req)
print response.headers
retdata = response.read()
print '-'*10
print retdata