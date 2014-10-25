# -*- coding: utf-8 -*-  
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

reload(sys)
sys.setdefaultencoding('utf-8')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), os.pardir)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "templates"),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=ul@%az6pud#52n)7*0a*fi&%ol1c(ik)+j=6^k#e5b2+xi$n1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = '*'


DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'south',
    'django_cron',
    'cron',
    'xadmin',
    'crispy_forms',
    'quanlin',
    'oa',
    'vir2real',
)



# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CRON_CLASSES = [
    "quanlin.down_trade_engins.taobao_engin.TaobaoDownTradeCronJob",
    "quanlin.mycron.MyCronJob",
]

FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[likangwei@quanlinbense.com]: 3632840aa"

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES_SQLIT = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': os.path.join(PROJECT_ROOT, 'data.db'), 
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',                      
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#本地数据库
DATABASES_LOCAL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quanlin3',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1'
    }
}
#阿里云 RDS
DATABASES_RDS = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quanlin',
        'USER': 'kangwei',
        'PASSWORD': '3632840aa',
        'HOST': 'testkangwei.mysql.rds.aliyuncs.com'
    }
}

#DATABASES = DATABASES_LOCAL
DATABASES = DATABASES_RDS
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'
# LANGUAGE_CODE ='en-us'
TIME_ZONE = 'Asia/Shanghai'
#TIME_ZONE = 'UTC'
STATIC_ROOT = 'static/'
SITE_ID = 1
USE_I18N = True

USE_L10N = True

USE_TZ = False
MEDIA_ROOT = ''
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)
STATIC_URL = '/static/'
