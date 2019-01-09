#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:04

"""
httplib/urllib实现:POST请求
"""

import httplib, urllib

conn = None
try:
    params = urllib.urlencode({'name': 'qiye', 'age': 22})
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = httplib.HTTPConnection('www.zhihu.com', headers)
    response = conn.getresponse()
    print response.getheaders() # 获取头信息
    print response.status
    print response.read()
except Exception, e:
    print e
finally:
    if conn:
        conn.close()
