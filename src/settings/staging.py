from settings.base import *

# -----------------------------------------------------------------------------
# --- Override Settings here
DEBUG = config("DEBUG", default=False)

DATABASES = {
    "default": {
        "ENGINE":   config("STAGING_DB_ENGINE", default=""),
        "NAME":     config("STAGING_DB_NAME", default=""),
        "USER":     config("STAGING_DB_USER", default=""),
        "PASSWORD": config("STAGING_DB_PASSWORD", default=""),
        "HOST":     config("STAGING_DB_HOST", default=""),
        "PORT":     config("STAGING_DB_PORT", default=""),
        "OPTIONS": {
            # "autocommit": True,
        }
    }
}

SECURE_SSL_REDIRECT = False


###############################################################################
### AWS SETTINGS                                                            ###
###############################################################################
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", default="")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", default="")
AWS_PRELOAD_METADATA = config("AWS_PRELOAD_METADATA", default=True, cast=bool)
AWS_QUERYSTRING_AUTH = config("AWS_QUERYSTRING_AUTH", default=False, cast=bool)
AWS_HEADERS = {
    "Cache-Control":    "max-age=86400",
}

DEFAULT_FILE_STORAGE = "s3utils.MediaS3BotoStorage"
# STATICFILES_STORAGE = "s3utils.StaticS3BotoStorage"

S3_URL = "http://%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
# STATIC_URL = S3_URL + "/static/"
MEDIA_URL = S3_URL + "/media/"


###############################################################################
### DJANGO MIDDLEWARE CLASSES                                               ###
###############################################################################
MIDDLEWARE_CLASSES = (
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)


###############################################################################
### DJANGO CACHING                                                          ###
###############################################################################
CACHES = {
    "default": {
        "BACKEND":  config("CACHE_BACKEND", default=""),
        "LOCATION": config("CACHE_LOCATION", default=""),
        "TIMEOUT":  config("CACHE_TIMEOUT", default=""),
    }
}

CACHE_MIDDLEWARE_ALIAS = config("CACHE_MIDDLEWARE_ALIAS", default="")
CACHE_MIDDLEWARE_SECONDS = config("CACHE_MIDDLEWARE_SECONDS", default="")
CACHE_MIDDLEWARE_KEY_PREFIX = config("CACHE_MIDDLEWARE_KEY_PREFIX", default="")


###############################################################################
### DJANGO LOGGING                                                          ###
###############################################################################
LOGGING = {
    "version":                      1,
    "disable_existing_loggers":     False,
    "filters": {
        "require_debug_false": {
            "()":                   "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()":                   "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "simple": {
            "format":               "[%(asctime)s] %(levelname)s %(message)s",
            "datefmt":              "%Y-%m-%d %H:%M:%S",
        },
        "verbose": {
            "format":               "[%(asctime)s] %(levelname)s "
                                    "[%(name)s.%(funcName)s:%(lineno)d] "
                                    "%(message)s",
            "datefmt":              "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level":                "INFO",
            "filters": [
                "require_debug_true",
            ],
            "class":                "logging.StreamHandler",
            "formatter":            "simple",
        },
        "null": {
            "class":                "logging.NullHandler",
        },
        "mail_admins": {
            "level":                "ERROR",
            "filters": [
                "require_debug_false",
            ],
            "class":                "django.utils.log.AdminEmailHandler",
            "formatter":            "verbose",
        },
        "saneside_logfile": {
            "level":                "DEBUG",
            "filters": [
                "require_debug_false",
                "require_debug_true",
            ],
            "class":                "logging.handlers.RotatingFileHandler",
            "filename":             "saneside.log",
            "maxBytes":             1024 * 1024 * 5,  # 5 MB
            "backupCount":          7,
            "formatter":            "simple",
        },

        # ---------------------------------------------------------------------
        # --- Set up logging to Papertrail (artem.suvorov@gmail.com)
        "papertrail": {
            "level":                "DEBUG",
            "class":                "logging.handlers.SysLogHandler",
            "formatter":            "verbose",
            "address":              (
                "logs4.papertrailapp.com",
                50129
            ),
        },
    },
    "loggers": {
        "saneside": {
            "handlers": [
                "console",
                "saneside_logfile",
                "papertrail",
            ],
        },
        "django": {
            "handlers": [
                "console",
                "saneside_logfile",
                "papertrail",
            ],
        },
        "django.request": {
            "handlers": [
                "mail_admins",
                "saneside_logfile",
                "papertrail",
            ],
            "level":                "ERROR",
            "propagate":            False,
        },
        "py.warnings": {
            "handlers": [
                "console",
                "saneside_logfile",
                "papertrail"
            ],
        },
    },
}
