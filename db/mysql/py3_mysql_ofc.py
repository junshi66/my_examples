#!/usr/bin/env python
# -*- coding:utf-8 -*-

'Python连接到MySQL数据及相关的操作（基于Python3）'

import pymysql

# 打开数据库连接
conn = pymysql.connect(host='192.168.80.191', user="root", passwd="HiSQL2019", port=6666)
conn.select_db('employees')
# 获取游标
cur = conn.cursor()
##执行单个SQL语句
cur.execute("select count(*) from employees;")
while 1:
    res = cur.fetchone()
    if res is None:
        # 表示已经取完结果集
        break
    print(res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')
