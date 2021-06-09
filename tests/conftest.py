# -*- coding: utf-8 -*-
import os

DIRNAME = os.path.dirname(__file__)


def pytest_configure():
    import django
    from django.conf import settings
    settings.configure(
        DEBUG=True,
        TESTING=True,
        PRODUCTION=False,
        DKCSRF_COOKIE_NAME="csrftoken",
        ROOT_URLCONF='cmsplugin_contact.urls',
        APPNAME='cmsplugin_contact',
        SITE_ID=1,
        LANGUAGE_CODE='en',
        LANGUAGES={'en': 'en'},
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                'LOCATION': os.path.join(DIRNAME, 'cache'),
                'TIMEOUT': 60 * 60,
                'OPTIONS': {
                    'MAX_ENTRIES': 5000
                }
            }
        },
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(DIRNAME, 'testing.db'),
                # The following settings are not used with sqlite3:
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sites',
            'cms',
            'cmsplugin_contact',
            'treebeard'
        ),
        AUTH_USER_MODEL='auth.User',
        TEMPLATES=[{
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(DIRNAME, 'templates')],
            "APP_DIRS": True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                ],
            }
        }],
    
    )
    django.setup()
