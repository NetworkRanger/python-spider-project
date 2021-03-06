#!/usr/bin/python2.7
# -*- coding:utf-8 -*-

# Author: NetworkRanger
# Date: 2019/1/28 4:38 PM

import sqlite3

con = sqlite3.connect('./test.db') # con = sqlite2.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE person (id integer primary key, name varchar(20), age integer)')

data  = '0, "qiye", 20'
cur.execute('INSERT INTO person VALUES (%s)' % data)
# cur.execute('INSERT INTO person VALUES (?,?,?)', (0, 'qiye', 20))
cur.executemany('INSERT INTO person VALUES(?,?,?)', [(3, 'marry', 20), (4, 'jack', 20)])

cur.execute('SELECT * FROM person')
res = cur.fetchall()
for line in res:
    print(line)
    cur.execute('SELECT * FROM person')
    res = cur.fetchone()
    print(res)

cur.execute('UPDATE person SET name=? WHERE id=?', ('rose', 1))
cur.execute('DELETE FROM person WHERE id=?', (0,))
con.commit()
con.close()