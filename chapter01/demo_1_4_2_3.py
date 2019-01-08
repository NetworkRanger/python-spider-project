#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/7 下午11:41

"""
线程同步
"""

import threading
mylock = threading.RLock()
num = 0

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '%s locked, Number: %d' % (threading.current_thread().name, num)
            if num>=4:
                mylock.release()
                print '%s released, Number: %d' % (threading.current_thread().name, num)
                break
            num += 1
            print '%s released, Number: %d' % (threading.current_thread().name, num)
            mylock.release()

if __name__ == '__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()
