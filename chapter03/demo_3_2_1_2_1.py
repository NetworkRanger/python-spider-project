#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:09

"""
请求headers处理:设置一下请求头中的User-Agent域和Referer域信息
"""

import urllib
import urllib2
url = 'http://www.xxxxxx.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://www.xxxxxx.com/'
postdata = {
    'username': 'qiyie',
    'password': 'qiye_pass'
}
# 将user_agent,referer写入头信息
headers = {'User-Agent': user_agent, 'Referer': referer}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
html = response.read()

print html