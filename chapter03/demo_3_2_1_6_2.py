#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/9 上午12:31

"""
自定义HTTPRedirectHandler类
"""

import urllib2


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result


opener = urllib2.build_opener(RedirectHandler)
opener.open('http://www.zhihu.cn')
