#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 2:36 PM

import urllib
from lxml import etree
import requests


def Schedule(blocknum, blocksize, totalsize):
    """
    :param blocknum: 已经下载的数据块
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件的大小
    :return:
    """

    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print '当前下载进度: %d' % per


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
# 使用lxml解析网页
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')  # 先找到所有的img
i = 0
for img_url in img_urls:
    urllib.urlretrieve(img_url, 'img' + str(i) + '.jpg', Schedule)
    i += 1
