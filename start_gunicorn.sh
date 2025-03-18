#!/bin/bash

/home/muellerkev/venv/bin/gunicorn \
  --bind 127.0.0.1:8000 \
  --workers 5 \
  --access-logfile /var/log/coderr/gunicorn_access.log \
  --error-logfile /var/log/coderr/gunicorn_err.log \
  --access-logformat "%(h)s %(l)s %(u)s %(t)s \"%r\" %(s)s %(b)s %(f)s \"%a\""
