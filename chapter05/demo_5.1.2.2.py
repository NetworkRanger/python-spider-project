#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 2:17 PM

import csv

headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
rows = [{'ID': 1001, 'UserName': "qiye", 'Password': "qiye_pass", 'Age': 24, 'Country': "China"},
    {'ID': 1002, 'UserName': "Mary", 'Password': "Mary_pass", 'Age': 20, 'Country': "USA"},
    {'ID': 1003, 'UserName': "Jack", 'Password': "Jack_pass", 'Age': 20, 'Country': "USA"},
]

with open('qiye.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

