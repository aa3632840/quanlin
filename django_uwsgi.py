#!/usr/bin/env python
# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
application = django.core.handlers.wsgi.WSGIHandler()
