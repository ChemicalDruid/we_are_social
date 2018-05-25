from base import *
import dj_database_url

DEBUG = False

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_oTWXN1820at0e3NQzZEsPMAl')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_aC7taKzPyBSL8M5O97p1mjsM')

# PayPal environment variables
PAYPAL_NOTIFY_URL = 'http://codeinst-social-staging.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'sakis.platsas-paypalmerch@gmail.com'

SITE_URL = 'https://codeinst-social-staging.herokuapp.com'
ALLOWED_HOSTS.append('codeinst-social-staging.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
