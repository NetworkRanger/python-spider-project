#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:33

"""
Timeouts超时设置
"""

import requests
requests.get('http://github.com', timeout=2)