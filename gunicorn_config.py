import multiprocessing
import gevent.monkey

gevent.monkey.patch_all()

# debug = True

# log日志
loglevel = 'debug'
accesslog = "log/gunicorn_access.log"
errorlog = "log/gunicorn_debug.log"

# 意味着开启后台运行 默认为False
daemon = False

workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
worker_class = 'gevent'

bind = '0.0.0.0:2001'
pid = '/tmp/bbs.pid'