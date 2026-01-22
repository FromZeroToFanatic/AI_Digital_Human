from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 密钥，生产环境必须保密
SECRET_KEY = 'django-insecure-f5s3ag^doazsd1%v@cdx17bbo_vy)!^k0^=&l%f6xfpseltgv='

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式，生产环境必须设置为False
DEBUG = True

# 允许访问的主机列表，生产环境需要配置具体域名
ALLOWED_HOSTS = []


# 注册的应用列表，分为Django内置应用、第三方应用和本地应用
INSTALLED_APPS = [
    # Django内置应用
    'django.contrib.admin',          # 后台管理系统
    'django.contrib.auth',           # 认证系统
    'django.contrib.contenttypes',   # 内容类型框架
    'django.contrib.sessions',       # 会话框架
    'django.contrib.messages',       # 消息框架
    'django.contrib.staticfiles',    # 静态文件管理

    # 第三方应用
    'rest_framework',                # Django REST Framework，用于构建API
    'corsheaders',                   # 跨域资源共享支持

    # 本地应用
    'web',                           # 主要业务应用
]

# 中间件列表，处理请求和响应的流程
MIDDLEWARE = [
    # 跨域中间件，必须放在最前面
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',  # 安全中间件
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话中间件
    'django.middleware.common.CommonMiddleware',  # 通用中间件
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF保护中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 认证中间件
    'django.contrib.messages.middleware.MessageMiddleware',  # 消息中间件
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 点击劫持保护中间件
]

# 根URL配置
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 模板引擎
        'DIRS': [],  # 模板目录
        'APP_DIRS': True,  # 是否在应用目录中查找模板
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # 请求上下文处理器
                'django.contrib.auth.context_processors.auth',  # 认证上下文处理器
                'django.contrib.messages.context_processors.messages',  # 消息上下文处理器
            ],
        },
    },
]

# WSGI应用配置
WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# 数据库配置，开发阶段使用SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 数据库引擎，使用SQLite
        'NAME': BASE_DIR / 'db.sqlite3',  # 数据库文件路径
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # 密码与用户属性相似度验证
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 密码最小长度验证
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # 常见密码验证
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 纯数字密码验证
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 语言代码，设置为中文

TIME_ZONE = 'Asia/Shanghai'  # 时区，设置为上海时区

USE_I18N = True  # 是否启用国际化

USE_TZ = True  # 是否使用时区

# 静态文件配置
STATIC_URL = 'static/'  # 静态文件URL前缀
# STATIC_ROOT = BASE_DIR / 'static'  # 生产阶段静态文件根目录，收集静态文件时使用

# 静态文件目录配置
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # 静态文件目录
]

# 媒体文件配置
MEDIA_URL = 'http://127.0.0.1:8000/media/'  # 媒体文件URL前缀
MEDIA_ROOT = BASE_DIR / 'media'  # 媒体文件存储根目录

# JWT认证配置
from datetime import timedelta

# DRF配置，设置默认认证类为JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 使用JWT认证作为默认认证方式
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT配置，包括令牌有效期、刷新策略等
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),  # 访问令牌有效期2小时
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # 刷新令牌有效期7天

    'ROTATE_REFRESH_TOKENS': True,  # 刷新令牌时是否同时生成新的刷新令牌
    'BLACKLIST_AFTER_ROTATION': True,  # 刷新令牌后是否将旧令牌加入黑名单

    'AUTH_HEADER_TYPES': ('Bearer',),  # 认证头类型，通常为Bearer
}

# 允许的跨域请求源
CORS_ALLOW_CREDENTIALS = True  # 是否允许携带凭证（cookies）

# 允许的跨域请求源
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # 允许前端开发服务器访问
]