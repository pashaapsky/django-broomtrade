import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),) #папка щаблонов
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),) #папка статичных файлов
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload') #папка загружаемых файлов
MEDIA_URL = '/media/'
LOGIN_URL = '/login/'  #имена привязок для страниц входа выхода
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = 'main'
SITE_ID = 1 #идентификатор сайта, из за активации django.contrib.sites
THUMBNAIL_BASEDIR = 'thumbnails' #миниатюры
THUMBNAIL_ALIASES = {
    'goods.Good.images': {
        "base": {"size": (200,100)},
    },
}
MANAGERS = (("admin", "admin@someserver.ru"))
EMAIL_HOST = "someserver.ru"
EMAIL_HOST_USER = "user"
EMAIL_HOST_PASSWORD = '123456789'
DEFAULT_FROM_EMAIL = 'mailer@someserver.ru'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-l3*n-o3(56aj29(r4m%#fzt%pk1^6-n+tt39&qpt7&9l2+*h='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'django.contrib.comments',
    # 'easy_thumbnails',
    # 'taggit',
    # 'precise_bbcode',
    'main',
    'guestbook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'broomtrade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'broomtrade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/site.dat'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


