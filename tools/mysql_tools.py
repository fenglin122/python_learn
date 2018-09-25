#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


def get_mysql_conn(host='rm-2zexpn42j6ymkk9j5.mysql.rds.aliyuncs.com'):
    conn = pymysql.Connect(host=host, port=3306, user='lex_pyramid', passwd='lex_qwerty!@#', db='pyramid', charset='utf8')
    return conn

def get_mysql_conn_dev(host='172.29.2.167'):
    conn = pymysql.Connect(host=host, port=3306, user='root', passwd='Lenovo', db='pyramid', charset='utf8')
    return conn


def insert_update(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

