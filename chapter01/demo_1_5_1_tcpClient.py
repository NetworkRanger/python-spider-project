#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/8 下午11:43

"""
TCP客户端的创建和运行
"""

import socket

# 初始化Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接目标的ip和端口
s.connect(('127.0.0.1', 9999))
# 接收消息
print '--->>' + s.recv(1024).decode('utf-8')
# 发送消息
s.send(b'Hello, I am a client')
print '--->>' + s.recv(1024).decode('utf-8')
s.send(b'text')
# 关闭套接字
s.close()