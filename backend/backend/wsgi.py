"""
backend项目的WSGI配置。

它将WSGI可调用对象暴露为名为``application``的模块级变量。

有关此文件的更多信息，请参阅
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
