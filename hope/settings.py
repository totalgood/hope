"""
Django settings for hope project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from .constants import DB_PATH, PROJECT_ROOT, MODULE_ROOT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = PROJECT_ROOT
APP_NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
STATICFILES_DIRS = ()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ljr#li4@^_3zch&+&f4m+o9tfc4yp61#t36=6v@z5nw52s*gi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


SITE_ROOT = os.path.dirname(BASE_DIR)
SITE_NAME = os.path.basename(BASE_DIR)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    'pipeline',
    'rest_framework',

    'chatterbot.ext.django_chatterbot',
    'chatterbot_app',
    # 'predict',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hope.urls'

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

WSGI_APPLICATION = 'hope.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_PATH,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'static')),
    os.path.normpath(os.path.join(BASE_DIR, APP_NAME, 'static')),
    os.path.normpath(os.path.join(BASE_DIR, 'chatterbot_app', 'static')),
    )

# Django Pipeline (and browserify)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# browserify-specific
PIPELINE_COMPILERS = (
    'pipeline_browserify.compiler.BrowserifyCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'

if DEBUG:
    PIPELINE_BROWSERIFY_ARGUMENTS = '-t babelify'

PIPELINE_CSS = {
    'hope_css': {
        'source_filenames': (
            'css/style.css',
        ),
        'output_filename': 'css/hope_css.css',
    },
}

PIPELINE_JS = {
    'hope_js': {
        'source_filenames': (
            'js/bower_components/jquery/dist/jquery.min.js',
            'js/bower_components/react/JSXTransformer.js',
            'js/bower_components/react/react-with-addons.js',
            'js/app.browserify.js',
        ),
        'output_filename': 'js/hope_js.js',
    }
}

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'hopestyle': {
            'source_filenames': (
              'css/bootstrap.css',
              # 'css/colors/*.css',
              # 'css/layers.css'
            ),
            'output_filename': 'css/compressed_hopestyle.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'hope': {
            'source_filenames': (
              'js/jquery.js',
              'js/bootstrap.js',
              # 'js/d3.js',
              # 'js/collections/*.js',
              # 'js/application.js',
            ),
            'output_filename': 'js/compresed_hope.js',
        }
    }
}
