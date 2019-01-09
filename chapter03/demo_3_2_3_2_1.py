#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:13

"""
响应与编码
"""

import requests
r = requests.get('http://www.baidu.com')
print 'content-->' + r.content
print 'text-->' + r.text
print 'encoding-->'+r.encoding
r.encoding='utf-8'
print 'new text -->'+r.text