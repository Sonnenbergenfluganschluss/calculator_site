# calculator_site/settings.py
import os

BASE_DIR = 'C:/Users/anast/Desktop/SF/IDE/Django_PostgreSQL/calculator_site'

# Основные настройки URL для статических файлов
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/staticfiles/'  # Для collectstatic
ROOT_URLCONF = 'calculator_site.urls'

# Обязательные middleware (должны быть в таком порядке)
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Обязательные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Для работы со статикой
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
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
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',  # Должен быть ПЕРВЫМ среди auth/messages
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Требуется для admin
    'django.contrib.messages.middleware.MessageMiddleware',  # Требуется для admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',  # Админ-панель
    'django.contrib.auth',  # Аутентификация
    'django.contrib.contenttypes',  # Контент-типы
    'django.contrib.sessions',  # Сессии
    'django.contrib.messages',  # Сообщения
    'django.contrib.staticfiles',  # Статические файлы
    'calculator',  # наше приложение
    # Ваши приложения
]

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite
        'NAME': './db.sqlite3',         # Файл БД создастся автоматически
    }
}


# Для аутентификации
LOGIN_URL = 'login'  # Куда перенаправлять неавторизованных пользователей
LOGIN_REDIRECT_URL = 'home'  # Куда перенаправлять после входа
LOGOUT_REDIRECT_URL = 'home'  # Куда перенаправлять после выхода


SECRET_KEY = 'l1w+_1-vd%h%9a70e+4x^et=$_us%&6f#@6=413&$lr71ty0-o'