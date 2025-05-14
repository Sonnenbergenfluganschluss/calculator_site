# calculator_site/settings.py
import os
# Основные настройки URL для статических файлов
STATIC_URL = '/static/'
STATIC_ROOT = 'C:/Users/anast/Desktop/SF/IDE/Django_PostgreSQL/calculator_site/staticfiles/'  # Для collectstatic

# Настройки медиа-файлов (если нужны)
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite
        'NAME': './db.sqlite3',         # Файл БД создастся автоматически
    }
}

ROOT_URLCONF = 'calculator_site.urls'

# Настройка БД (PostgreSQL)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',       # Имя БД (например, из ElephantSQL)
#         'USER': 'mydatabaseuser',   # Пользователь БД
#         'PASSWORD': 'mypassword',   # Пароль
#         'HOST': 'localhost',        # Или адрес от ElephantSQL/Render
#         'PORT': '5432',
#     }
# }

# Для аутентификации
LOGIN_URL = 'login'  # Куда перенаправлять неавторизованных пользователей
LOGIN_REDIRECT_URL = 'home'  # Куда перенаправлять после входа
LOGOUT_REDIRECT_URL = 'home'  # Куда перенаправлять после выхода