#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/17 下午9:23

import csv

headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
rows = [
    (1001, 'qiye', 'qiye_pass', 24, 'China'),
    (1002, 'Mary', 'Mary_pass', 20, 'China'),
]

with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
