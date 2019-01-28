#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 9:25 PM

import redis
from BloomfilterOnRedis import BloomFilter
from scrapy.utils.request import request_fingerprint
from scrapy import Request

rconn = redis.Redis('172.16.188.121', 6379)
bf = BloomFilter(rconn, 'spider_1:dupefilter')


if __name__ == '__main__':
    # while True:
        url = 'http://www.x14hack.com/'
        request = Request(url)
        fp = request_fingerprint(request)
        print fp,
        if bf.isContains(fp):
            print 'exist!'
        else:
            print 'not exist!'
