#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:13

"""
请求headers处理:add_header来添加请求头信息
"""

import urllib
import urllib2
url = 'http://www.xxxxxx.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://www.xxxxxx.com/'
postdata = {
    'username': 'qiye',
    'password': 'qiye_pass'
}
data = urllib.urlencode(postdata)
req = urllib2.Request(url)
# 将user_agent,referer写入头信息
req.add_header('User-Agent', user_agent)
req.add_header('Referer', referer)
req.add_header(data)
response = urllib2.urlopen(req)
html = response.read()

print html