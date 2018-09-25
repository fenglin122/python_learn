#!/usr/bin python
# -*- coding:utf-8 -*-
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.0.51:9092', api_version='2.0.0')

def log(str):
    t = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
    print("[%s]%s"%(t, str))
for i in range(2):
    producer.send('test31', bytes('data' + str(i), encoding='utf8'), i,None,None)
    log('data' + str(i))
producer.close(5000)