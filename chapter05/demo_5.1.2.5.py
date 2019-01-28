#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 2:25 PM

import csv

with open('qiye.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print row.get('UserName'), row.get('Password')