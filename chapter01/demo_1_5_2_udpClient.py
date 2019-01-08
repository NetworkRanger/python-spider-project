#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/8 下午11:53

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for data in [b'Hello', b'World']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据
    print s.recv(1024).decode('utf-8')
s.close()