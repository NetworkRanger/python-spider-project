#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/7 下午11:12

"""
第二种方法：使用multiprocessing模块创建多进程
"""
import os
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print 'Child process %s (%s) Running...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p_list = []
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        p_list.append(p)
        print 'Process will start.'
        p_list[i].start()
    for p in p_list:
        p.join()
    print 'Process end.'

