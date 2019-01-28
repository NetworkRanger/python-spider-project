#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 8:45 PM

import random

"""
这个类主要用于产生随机代理
"""


class RandomProxy(object):

    def __init__(self, iplist):  # 初始化一下数据库连接
        self.iplist = iplist

    @classmethod
    def from_crawler(cls, crawler):
        # 从Setting中加载IPLIST的值
        return cls(crawler.settings.getlist('IPLIST'))

    def process_request(self, request, spider):
        """
        在请求上添加代理
        :param request:
        :param spider:
        :return:
        """
        proxy = random.choice(self.iplist)
        request.meta['proxy'] = proxy
