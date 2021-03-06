#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/10 上午1:45

import re

# re.split(pattern, string[, maxsplit])

pattern = re.compile(r'\d+')
print re.split(pattern, 'A1B2C3D4')


# re.findall(pattern, string[, flags])

pattern = re.compile(r'\d+')
print re.findall(pattern, 'A1B2C3D4')

# re.finditer(pattern, string[, flags])

p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)') # 使用名称引用
s = 'i say, hello word!'
print p.sub(r'\g<word2> \g<word1>', s)
p = re.compile(r'(\w+) (\w+)') # 使用编号
print p.sub(r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.sub(func, s)

# re.subn(pattern, repl, string[, count])

s = 'i say, hello world!'
p = re.compile(r'(\w+) (\w+)')
print p.subn(r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.subn(func, s)

pattern = re.compile(r'(\w+) (\w+) (?P<word>.*)')
match = pattern.match('I love you!')

print 'mathing.string', match.string
print 'mathing.re', match.re
print 'mathing.pos', match.pos
print 'mathing.endpos', match.endpos
print 'mathing.lastindex', match.lastindex
print 'mathing.lastgroup', match.lastgroup

print 'match.group(1,2):', match.group(1, 2)
print 'match.groups():', match.groups()
print 'match.groupdict():', match.groupdict()
print 'match.start(2):', match.start(2)
print 'match.end(2):', match.end(2)
print 'match.span(2):', match.span(2)
print r"match.expand(r'\2 \1 \3')", match.expand(r'\2 \1 \3')
