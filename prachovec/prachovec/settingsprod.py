from .settingsbase import *



SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

DEBUG = False

ALLOWED_HOSTS = ['www.itutorialy.cz', 'itutorialy.cz']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_prachovec',
        'USER': 'user_prachovec',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}



LOGGING = {                                                                                                                 
            'version': 1,
                'disable_existing_loggers': False,
                    'handlers': {
                                'logfile': {
                                                'class': 'logging.FileHandler',
                                                            'filename': '../../logs/django_server.log',
                                                                    },
                                    },
                        'loggers': {
                                    'django': {
                                                    'handlers': ['logfile'],
                                                            },
                                        },
                        }
