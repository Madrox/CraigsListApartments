


# Configure how email gets sent by the crawler

# Body of emails the crawler sends
EMAIL_BODY = """{0}
Cost: {2}
Bedrooms: {3}

{4}
"""
EMAIL_FROM_USER = 'nobody@domain.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_USE_TLS = False

# The database to store all the listings you find.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                     # Or path to database file if using sqlite3.
        'USER': '',                     # Not used with sqlite3.
        'PASSWORD': '',                 # Not used with sqlite3.
        'HOST': '',                     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                     # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y$a0^awld=b!1^z1&zb7ql!=k@t8wj*(y)9xcmnornv7ql!q6i2=k@tzte'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'





# Don't really need to worry about anything below


DEBUG = True
TEMPLATE_DEBUG = DEBUG
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)
ROOT_URLCONF = 'urls'
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'common',
    'crawler'
)

