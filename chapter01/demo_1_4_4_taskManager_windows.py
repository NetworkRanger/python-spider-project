#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/8 下午11:25

import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 任务个数
task_number = 10
# 定义收发队列
task_queue = Queue.Queue(task_number)
result_queue = Queue.Queue(task_number)

def get_task():
    return task_queue

def get_result():
    return result_queue

# 创建类似的QueueManager:
class QueueManger(BaseManager):
    pass

def win_run():
    # windows下绑定调用接口不能使用lambda, 所以只能定义函数再绑定
    QueueManger.register('get_task_queue', callable=get_task)
    QueueManger.register('get_result_queue', callable=get_result)
    # 绑定端口并设置验证口令，windows下需要填写ip地址，linux下不填默认为本地
    manager = QueueManger(address=('127.0.0.1', 8001), authkey=b'qiye')
    # 启动
    manager.start()
    try:
        # 通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 添加任务
        for url in ['ImageUrl_' + str(i) for i in range(10)]:
            print 'put task %s ...' % url
            task.put(url)
        print 'try get result ...'
        for i in range(10):
            print 'result is %s' % result.get(timeout=10)
    except:
        print 'Manager error'
    finally:
        # 一定要关闭，否则会爆管道未关闭的错误
        manager.shutdown()

if __name__ == '__main__':
    # windows 下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()
