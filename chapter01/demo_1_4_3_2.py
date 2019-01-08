#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/8 下午10:52

"""
gevent pool对象使用
"""

from gevent import monkey
monkey.patch_all()
import urllib2
from gevent.pool import Pool

def run_task(url):
    print 'Visit --> %s' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), url)
    except Exception, e:
        print e
    return 'url:%s ---> finish' % url

if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    results = pool.map(run_task, urls)
    print results