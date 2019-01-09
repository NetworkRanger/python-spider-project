#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:42

import re
# 将正则表达式编码成Pattern对象
pattern = re.compile(r'\d+')
# 将使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.search(pattern, 'abc192edf')
if result1:
    print result1.group()
else:
    print '匹配失败1'