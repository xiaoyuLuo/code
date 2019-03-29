#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__mtime__ = '2019/3/21'
"""
from flask import Flask
from celery import Celery
import requests
import time

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://user:password@host:port/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
celery.conf.update(
    ACCEPT_CONTENT=['pickle'],
    TASK_SERIALIZER='pickle'
)


@celery.task
def hello(resContent):
    time.sleep(3)
    response = notifyRequest(resContent)
    return response.status_code


def notifyRequest(resContent):
    # 异步通知地址
    notifyUrl = "http://host:post/uri"

    headers = {
        "Content-Type": "application/xml",
        "Authorization": "Basic c3podDolMSEjRWQ0NHRJRHI="
    }
    response = requests.request("POST", notifyUrl, data=resContent, headers=headers)
    return response
