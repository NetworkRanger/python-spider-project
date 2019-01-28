#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 9:11 PM

from scrapy.dupefilter import RFPDupeFilter

class URLFilter(RFPDupeFilter):
    """
    根据url过滤
    """
    def __init__(self, path=None, debug=False):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)

