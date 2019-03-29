安装
Pip install celery   (4.2)
Pip install redis
Pip install eventlet


https://www.cnblogs.com/cwp-bg/p/8759638.html celery参数详解
https://www.cnblogs.com/huang-yc/p/10073167.html 参数个数不对

先启动redis_server, 再启动celery, 再运行app
celery -A async:celery worker -l info -P eventlet

连续两个同样的定时任务只会进入一个，原因待读celery实现代码
