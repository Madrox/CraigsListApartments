

# The database to store all the listings you find.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',    # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                         # Or path to database file if using sqlite3.
        'USER': '',                         # Not used with sqlite3.
        'PASSWORD': '',                     # Not used with sqlite3.
        'HOST': '',                         # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                         # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'





# You shouldn't have to worry about anything else

# Make this unique, and don't share it with anybody.
SECRET_KEY = '----- =D ------- nv7ql!=ky$a0^aj*(y)9xcmnor2ejkldfs09u('

DEBUG = True
TEMPLATE_DEBUG = DEBUG
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)
ROOT_URLCONF = 'craigslist_apartments.urls'
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'common',
    'crawler'
)

