from reservations.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_setting('SECRET_KEY')

BASE_URL = env_setting('BASE_URL', 'https://mf-mesbah.ir/')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_setting('DEBUG', False)

ALLOWED_HOSTS = env_setting("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = env_setting("CSRF_TRUSTED_ORIGINS").split(",")

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env_setting('DB_NAME'),
        'USER': env_setting('DB_USER'),
        'PASSWORD': env_setting('DB_PASSWORD'),
        'HOST': env_setting('DB_HOST'),
        'PORT': env_setting('DB_PORT'),
    }
}

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage

# DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
# STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
# MINIO_STORAGE_ENDPOINT = env_setting('MINIO_STORAGE_ENDPOINT', '')
# MINIO_STORAGE_ACCESS_KEY = env_setting('MINIO_STORAGE_ACCESS_KEY', None)
# MINIO_STORAGE_SECRET_KEY = env_setting('MINIO_SECRET_KEY', None)
# MINIO_STORAGE_USE_HTTPS = True
# MINIO_STORAGE_MEDIA_BUCKET_NAME = 'media'
# MINIO_STORAGE_STATIC_BUCKET_NAME = 'static'
# MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True


# Sentry settings
#
# SENTRY_DSN = env_setting('SENTRY_DSN')
# SENTRY_PORT = env_setting('SENTRY_PORT')
# sentry_sdk.init(
#     dsn="https://{sentry_dsn}@sentry.hamravesh.com/{sentry_port}".format(
#         sentry_dsn=SENTRY_DSN, sentry_port=SENTRY_PORT
#     ),
#     integrations=[DjangoIntegration()],
#
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0,
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )
