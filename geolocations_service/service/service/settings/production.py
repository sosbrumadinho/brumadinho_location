import os
from service.settings.common import *

flag = """
              +-+-+-+-+-+               
              |U|s|i|n|g|               
 +-+-+-+-+-+-+-+-+-+-+++-+-+-+-+-+-+-+-+
 |P|r|o|d|u|c|t|i|o|n| |S|e|t|t|i|n|g|s|
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 """


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', ''),
        'USER': os.environ.get('MYSQL_USER', ''),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', ''),
        'HOST': 'db',
        'PORT': 3306,
    }
}

print(flag)