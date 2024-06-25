
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-dgpmlwqs%**^59m_%pb+8sa4app7%mi3k@75sl@o04_e^z&yl0'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'library.apps.LibraryConfig',
    'learning.apps.LearningConfig',
    'autoservice.apps.AutoserviceConfig',
    'tinymce',
    'users.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap4',

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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'lt'

TIME_ZONE = 'Europe/Vilnius'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from .tinymce_templates import TINYMCE_TEMPLATES

TINYMCE_DEFAULT_CONFIG = {
    'valid_elements': '*[*]',
    'valid_children': '+body[style]',
    'extended_valid_elements': '*[*]',
    'content_css': 'css/bootstrap.min.css',
    'height': 360,
    'width': 1120,
    'image_advtab': True,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'plugins': '''
        textcolor save link image media preview codesample contextmenu
        table code lists fullscreen insertdatetime nonbreaking
        directionality searchreplace wordcount visualblocks
        visualchars code fullscreen autolink charmap print hr anchor
        pagebreak template
    ''',
    'toolbar1': '''
        fullscreen preview bold italic underline | fontselect | fontsizeselect
        | forecolor backcolor | alignleft alignright aligncenter alignjustify
        | indent outdent | bullist numlist table | link | image media | codesample
    ''',
    'toolbar2': '''
        visualblocks visualchars | charmap hr | pagebreak nonbreaking 
        | code template | Heading 2 Heading 3 Heading 4 Heading 5 Heading 6
    ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    'templates': TINYMCE_TEMPLATES,
}



LOGIN_REDIRECT_URL = 'learning:index'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mano_pastas@gmail.com'
# el. pašto adresas iš kurio siųsite
EMAIL_HOST_PASSWORD = 'VerySecret'
# slaptažodis
