#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:31

"""
重定向与历史
"""

import requests
r = requests.get('http://github.com')
print r.url
print r.status_code
print r.history