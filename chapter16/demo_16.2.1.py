#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 9:17 PM

import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('name', 'qiye')
print r.get('name')

'''
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'qiye')
print r.get('name')
'''