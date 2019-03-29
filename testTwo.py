#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__mtime__ = '2019/3/22'
"""
import async
import datetime

print(datetime.datetime.now())
async.hello.delay("abc")
print(datetime.datetime.now())