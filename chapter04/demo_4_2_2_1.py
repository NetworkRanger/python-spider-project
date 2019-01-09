#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:39

import re
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d+')
# 使用re.match匹配文本，获取匹配结果，无法匹配时将返回None
result1 = re.match(pattern, '192abc')
if result1:
    print result1.group()
else:
    print '匹配失败1'
result2 = re.match(pattern, 'abc192')
if result2:
    print result2.group()
else:
    print '匹配失败2'