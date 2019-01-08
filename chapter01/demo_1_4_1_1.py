#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/7 下午11:06

"""
第一种方式：使用os模块中的fork方式实现多进程
"""

import os

if __name__ == '__main__':
    print 'current Process (%s) start ...' % (os.getpid)
    pid = os.fork()
    if pid < 0:
        print 'error in fork'
    elif pid == 0:
        print 'I am child process(%s) and my parent process is (%s)', (os.getpid, os.getppid())