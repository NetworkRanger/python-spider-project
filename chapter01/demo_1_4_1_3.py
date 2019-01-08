#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/7 下午11:16

"""
multiporcessing模块提供了一个Pool类来代表进程池对象
"""

from multiprocessing import Pool
import os, time, random

def run_task(name):
    print 'Task %s (pid = %s) is running...' % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' % name

if __name__ == '__main__':
    print 'Current process %s.' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print 'Waiting for all subprocess done...'
    p.close()
    p.join()
    print 'All subprocess done.'


