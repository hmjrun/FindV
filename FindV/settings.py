"""
Django settings for FindV project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import environ

env = environ.Env(DEBUG=(bool, False)) # set default values and casting
environ.Env.read_env('FindV.env') # reading .env file

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hy38x6a6s%0ag5z^^e6zsp3c3p*0v2^h9v^^g&sy5tc(020$km'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wechat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'FindV.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FindV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': env.db()
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/data/dists/static_files/FindV/static'


#Abourt Logging 
#https://docs.djangoproject.com/en/1.10/topics/logging/
#DJANGO_LOG_LEVEL = 'DEBUG' to see all of Django’s debug logging 
#which is very verbose as it includes all database queries
import os
DJANGO_LOG_LEVEL = 'DEBUG'
LOGGING = {
    'version': 1, # 标示配置模板版本，int 类型，目前只接收 `1`这个值。
    'disable_existing_loggers': False,#default True，all loggers from the default configuration will be disabled.设置成false就对了，
    'formatters': {
        'verbose': {#详细日志格式
            'format': '%(levelname)s %(asctime)s %(pathname)s %(funcName)s : %(lineno)d : %(process)d %(thread)d %(message)s'
        },
        'simple': {#简单日志格式
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        # 这里是定义过滤器，需要注意的是，
        #由于 'filters' 是 logging.config.dictConfig 方法要求在配置字典中必须给订的 key ,
        #所以即使不使用过滤器也需要明确给出一个空的结构。
    },
    'handlers': {
        'mail_admins': {#发送错误的日志信息给admin，需要用到filters
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter':'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'tofile': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter':'verbose',#日志格式
            'maxBytes': 5 * 1024 * 1024,  # 5M
            'backupCount': 5,
            'filename': '/var/log/django/findv.log',#日志文件保存地址
        },
    },
    'loggers': {
        'django': {
            'handlers': ['tofile','console'],#写入文件和输出控制台
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
