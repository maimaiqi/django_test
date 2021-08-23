from .base import *   #NOQA  指PEP8规范检测工具，这个地方不需要检测

DEBUG = True  #线上不得为true

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}