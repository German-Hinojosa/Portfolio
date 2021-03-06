"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9v3a!y5$6uzxrzk$q$wmwy8^!j2!mdjq!y51iy00&%g&zsy0t-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jobs.apps.JobsConfig', #added, basically telling django theres a new app
                            #in the project it should know about
                            #Go to the jobs app folder, go to the apps.py class,
                            #and added the class that was autogenerated for us called
                            #JobsConfig
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #CHANGED DB TO POSTGRESQL
        'NAME': 'portfoliodb',  #the name of your database for the project
        'USER': 'postgres',    #your username, in this case we chose postgres
        'PASSWORD': 'Thiscool1',    #your postgres user password
        'HOST': '127.0.0.1', #or 'localhost'
        'PORT': '5432', #found if you go to your postgres app and click
                        #"server settings..."
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


#tell our django project where it should be saving our media files
#and so we need to add two new variables here down at the bottom
MEDIA_ROOT = os.path.join(BASE_DIR, 'db.sqlite3')
#when someone wants to save some image or file, it should be happening here
#and so basically, we want to go to where our project's base directory is
#and then have a media folder on top of that
#under DATABASES, you'll find NAME and to the right of it, it says the path of where
#we we should save our databse (default being db.sqlite3)
#add variable MEDIA_ROOT, and set with code copied from Name under DATABASES
#from this class. And change 'db.sqlite3' to 'media' (NO backslash after media)
#SO BASICALLY, it should go into a new folder called media aound the same
#space where db.sqlite3 is


MEDIA_URL = '/media/'
#this says when someones trying to access an image, where they can go do that
#SO ESSENTIALLY WHATS HAPPENING HERE IS, when we go back to our models.py (jobs),
#we're saying "we want to save images connected with the Job to the images/ directory"
#so if someone creates a new Job and theres an image connected to it, whats gonna happen
#is that its gonna go to our
#media folder (the one around the default db.sqlite3) and its gonna create an
#images folder, and save that image there.
#Now if we wanted to access that image, we go to the name our website SLASH (/) media
#SLASH (/) images SLASH (/) nameoffile (<-whatever the name of the file ends up being)
