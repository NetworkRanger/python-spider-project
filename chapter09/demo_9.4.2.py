#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 7:24 PM

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
assert u'百度' in driver.title
elem = driver.find_element_by_name('wd')
elem.clear()
elem.send_keys(u'网络爬虫')
time.sleep(3)
assert u'网络爬虫.' not in driver.page_source
driver.close()
