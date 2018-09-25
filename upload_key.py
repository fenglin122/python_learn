#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.Connect(host='rm-2zexpn42j6ymkk9j5.mysql.rds.aliyuncs.com', port=3306, user='smart_lex', passwd='3e4r5t6y7u2wSMART', db='video_phoenix', charset='utf8')
#conn = pymysql.Connect(host='172.29.2.167', port=3306, user='root', passwd='Lenovo', db='video_phoenix', charset='utf8')
cursor = conn.cursor()
f = open('keyno.txt', 'r')
f1 = open('output.txt', 'w')
lines = f.readlines()
sn = []
i = 0
for line in lines:
    print(line)
    sn.append(line.rstrip('\n'))
    i = i + 1
    if i % 10 == 0:
        select_str = 'select lps_did from device_detail_formal where lps_did in (%s)' % ','.join(['%s'] * len(sn))
        print(select_str)
        count = cursor.execute(select_str, sn)
        results = cursor.fetchall()
        for r in results:
            print(r)
            f1.write(str(r) + '\n')
        sn = []
f.close()
f1.close()
