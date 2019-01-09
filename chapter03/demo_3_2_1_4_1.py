#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:23

"""
Timeout设置超时:更改Socket的全局Timeout值
"""

import urllib2
import socket
socket.setdefaulttimeout(10) # 10称后超时
urllib2.socket.setdefaulttimeout(10) # 另一种方式