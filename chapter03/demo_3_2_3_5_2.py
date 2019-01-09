#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:25

"""
Cookie处理:设置cookie
"""

import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
cookies = dict(name='qiye', age='10')
r = requests.get('http://www.baidu.com', headers=headers, cookies=cookies)
print r.text