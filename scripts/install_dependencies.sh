#!/bin/bash
codepath=/data/apps/lex/python/es_to_xls
echo install dependencies
if [ -d $codepath ];then
    echo $codepath exists
else
    mkdir -p $codepath
fi
echo install dependencies done!
