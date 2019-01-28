#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 9:15 PM
import hashlib

from pybloom import ScalableBloomFilter
from scrapy.dupefilters import RFPDupeFilter
from w3lib.url import canonicalize_url


class URLBloomFilter(RFPDupeFilter):
    """根据urlhash_bloom过滤"""

    def __init__(self, path=None, debug=False):
        self.urls_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        RFPDupeFilter.__init__(self, path)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.urls_sbf:
            return True
        else:
            self.urls_sbf.add(url_sha1)
