#!/usr/bin/env python
# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()