#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午12:57

"""
httplib/urllib实现:GET请求
"""

import httplib
conn = None
try:
    conn = httplib.HTTPConnection('www.zhihu.com')
    conn.request('GET', '/')
    response = conn.getresponse()
    print response.status, response.reason
    print '-'*40
    headers = response.getheaders()
    for h in headers:
        print h
    print '-'*40
    print response.msg
except Exception, e:
    print e
finally:
    if conn:
        conn.close()

