import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing
bind = '127.0.0.1:7000'
backlog = 512
timeout = 30
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = "./gunicorn_access.log"      # 访问日志文件
errorlog = "./gunicorn_error.log"
