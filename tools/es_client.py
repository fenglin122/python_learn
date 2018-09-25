#!/usr/bin/env python
# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch


# es_client = Elasticsearch(host='172.29.19.44', port=9200)

es_client = Elasticsearch(
    ['172.29.19.44', '172.29.19.45'],
    # sniff before doing anything
    sniff_on_start=True,
    # refresh nodes after a node fails to respond
    sniff_on_connection_fail=True,
    # and also every 60 seconds
    sniffer_timeout=60
)
