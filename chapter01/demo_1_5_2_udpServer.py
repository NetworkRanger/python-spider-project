#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/8 下午11:50

"""
UDP服务端创建和运行
"""

import socket
# 创建socket,绑定指定的ip端口
# SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9000))
print 'Bind UDP on 9999...'
while True:
    # 直接发送数据和接收数据
    data, addr = s.recvfrom(1024)
    print 'Received from %s.' % addr
    s.sendto(b'Hello, %s!', data, addr)


