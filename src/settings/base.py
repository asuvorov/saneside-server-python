from __future__ import absolute_import

import importlib
import os
import os.path
import random
import sys

from django.utils.translation import ugettext_lazy as _

from decouple import config
from termcolor import colored, cprint


# -----------------------------------------------------------------------------
# --- SETTINGS
DEBUG = config("DEBUG", default=False)

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",))
print colored("[---  INFO   ---] PROJECT_PATH           : %s" % PROJECT_PATH, "cyan")

# We have 4 types of environments: "production", "development", "staging"
# and "testing"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
print colored("[---  INFO   ---] ENVIRONMENT            : %s" % ENVIRONMENT, "cyan")

DJANGO_SETTINGS_MODULE = os.environ.get(
    "DJANGO_SETTINGS_MODULE", "settings.development")
print colored("[---  INFO   ---] DJANGO_SETTINGS_MODULE : %s" % DJANGO_SETTINGS_MODULE, "cyan")

ADMINS = (
    ("Artem Suvorov", "artem.suvorov@gmail.com"),
)
MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE":   "django.db.backends.sqlite3",
        "NAME":     "sqlite.db",
        "USER":     "",
        "PASSWORD": "",
        "HOST":     "",
        "PORT":     "",
    }
}

DOMAIN_NAME = "saneside.com"
ALLOWED_HOSTS = ["*"]
APPEND_SLASH = True

TIME_ZONE = "America/Los_Angeles"

LANGUAGE_CODE = "en-us"
LANGUAGES = (
    ("en",  _("English")),
    ("de",  _("Deutsch")),
    ("es",  _("Spanish")),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "locale"),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMIN_MEDIA_PREFIX = "/static/admin/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "staticserve")
STATICFILES_DIRS = (
    ("", "%s/static" % PROJECT_PATH),
    )
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
)

SECRET_KEY = config("SECRET_KEY", default="")
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool)

TEMPLATES = [
    {
        "BACKEND":  "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_PATH, "templates/"),
            # os.path.join(PROJECT_PATH, "templates/emails/"),
            # os.path.join(PROJECT_PATH, "templates/cyborg/"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug":    DEBUG,
            # "loaders": [
            #     "django.template.loaders.filesystem.Loader",
            #     "django.template.loaders.app_directories.Loader",
            # ],
            "context_processors": [
                "django.template.context_processors.csrf",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


###############################################################################
### DJANGO MIDDLEWARE CLASSES                                               ###
###############################################################################
MIDDLEWARE_CLASSES = (
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "urls"

WSGI_APPLICATION = "wsgi.application"

INSTALLED_APPS = (
    # --- Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",

    # --- 3rd Party Apps
    "ddcore",
    "ddutils",
    "storages",
    "twitter_tag",

    # --- Project Apps
    "accounts",
    "api",
    "app",
    "events",
    "home",
)

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"


###############################################################################
### DJANGO CACHING                                                          ###
###############################################################################
CACHES = {
    "default": {
        "BACKEND":  "django.core.cache.backends.dummy.DummyCache",
    }
}


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
    },
    "loggers": {
        "django": {
            "handlers": [
                "console",
            ],
        },
        "django.request": {
            "handlers": [
                "mail_admins",
            ],
            "level":                "ERROR",
            "propagate":            False,
        },
        "py.warnings": {
            "handlers": [
                "console",
            ],
        },
    },
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)
AUTH_USER_MODEL = "accounts.User"


###############################################################################
### CUSTOM PROJECT SETTINGS                                                 ###
###############################################################################
SELFREFLECTION_SUBMIT_DURATION_PERIOD = 7  # Days
PROFILE_COMPLETENESS_GRACE_PERIOD = 5  # Days

CHALLENGE_NAME_RESERVED_WORDS = [
    "near-you", "new", "dateless", "featured", "categories",
]
ORGANIZATION_NAME_RESERVED_WORDS = [
    "directory", "create",
]


###############################################################################
### DJANGO BOWER                                                            ###
###############################################################################
INSTALLED_APPS += (
    "djangobower",
)
STATICFILES_FINDERS += (
    "djangobower.finders.BowerFinder",
)

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_PATH, "components/")
BOWER_PATH = "/usr/local/bin/bower"
BOWER_INSTALLED_APPS = (
    "bootstrap#3.3.7",
    "fontawesome#5.6.3",
    "ismobilejs#0.5.0",
    "jquery#3.3.1",
    "jquery-popup-overlay",
    "moment#2.24.0",
)


###############################################################################
### DJANGO CKEDITOR                                                         ###
###############################################################################


###############################################################################
### DJANGO COMPRESSOR                                                       ###
###############################################################################
INSTALLED_APPS += (
    "compressor",
)
STATICFILES_FINDERS += (
    "compressor.finders.CompressorFinder",
)

COMPRESS_PRECOMPILERS = (
    ("text/less", "lessc {infile} {outfile}"),
)

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
    # "compressor.filters.cssmin.CSSCompressorFilter",
]
COMPRESS_JS_FILTERS = [
    "compressor.filters.jsmin.JSMinFilter",
    # "compressor.filters.jsmin.SlimItFilter",
]

COMPRESS_ENABLED = True


###############################################################################
### DJANGO CYBORG                                                           ###
###############################################################################


###############################################################################
### DJANGO EASY TIMEZONES                                                   ###
###############################################################################


###############################################################################
### DJANGO GEOIP                                                            ###
###############################################################################
GEOIP_PATH = os.path.join(PROJECT_PATH, "geoip/")


###############################################################################
### DJANGO HAYSTACK                                                         ###
###############################################################################


###############################################################################
### DJANGO IMAGEKIT                                                         ###
###############################################################################
INSTALLED_APPS += (
    "imagekit",
)

IMAGEKIT_CACHEFILE_DIR = "CACHE/images"
IMAGEKIT_DEFAULT_CACHEFILE_BACKEND = "imagekit.cachefiles.backends.Simple"
IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = "imagekit.cachefiles.strategies.JustInTime"
IMAGEKIT_CACHEFILE_NAMER = "imagekit.cachefiles.namers.hash"
IMAGEKIT_SPEC_CACHEFILE_NAMER = "imagekit.cachefiles.namers.source_name_as_path"


###############################################################################
### DJANGO MPTT                                                             ###
###############################################################################


###############################################################################
### DJANGO MPTT ADMIN                                                       ###
###############################################################################


###############################################################################
### DJANGO PAGINATOR                                                        ###
###############################################################################
MAX_MEMBERS_PER_PAGE = 50
MAX_MEMBERS_PER_QUERY = 500

MAX_POSTS_PER_PAGE = 20
MAX_POSTS_PER_QUERY = 100

MAX_CHALLENGES_PER_PAGE = 25
MAX_CHALLENGES_PER_QUERY = 250

MAX_ORGANIZATIONS_PER_PAGE = 25
MAX_ORGANIZATIONS_PER_QUERY = 250


###############################################################################
### DJANGO PASSWORDS                                                        ###
###############################################################################
PASSWORD_MIN_LENGTH = 6         # Defaults to 6
PASSWORD_MAX_LENGTH = 30        # Defaults to None
PASSWORD_DICTIONARY = None
PASSWORD_MATCH_THRESHOLD = 0.9  # Defaults to 0.9, should be 0.0 - 1.0, where 1.0 means exactly the same.
PASSWORD_COMMON_SEQUENCES = []  # Should be a List of Strings. See `passwords/validators.py` for default
PASSWORD_COMPLEXITY = {         # You can omit any or all of these for no Limit for that particular Set
    "UPPER":    1,              # Uppercase
    "LOWER":    1,              # Lowercase
    "LETTERS":  1,              # Either uppercase or lowercase Letters
    "DIGITS":   1,              # Digits
    "SPECIAL":  1,              # Not alphanumeric, Space or punctuation Character
    "WORDS":    0               # Words (alphanumeric Sequences, separated by a Whitespace or punctuation character)
}


###############################################################################
### DJANGO PHONE NUMBER FIELD                                               ###
###############################################################################


###############################################################################
### DJANGO REST FRAMEWORK                                                   ###
###############################################################################


###############################################################################
### DJANGO REST FRAMEWORK SWAGGER                                           ###
###############################################################################


###############################################################################
### DJANGO ROSETTA                                                          ###
###############################################################################


###############################################################################
### DJANGO SEO                                                              ###
###############################################################################


###############################################################################
### DJANGO SIMPLE CAPTCHA                                                   ###
###############################################################################
INSTALLED_APPS += (
    "captcha",
)

CAPTCHA_FONT_SIZE = 22
CAPTCHA_BACKGROUND_COLOR = "#ffffff"
CAPTCHA_FOREGROUND_COLOR = "#001100"
CAPTCHA_PUNCTUATION = '''_"',.;:-'''
CAPTCHA_TIMEOUT = 5  # Minutes
CAPTCHA_LENGTH = 4  # Chars
CAPTCHA_IMAGE_BEFORE_FIELD = True
CAPTCHA_DICTIONARY_MIN_LENGTH = 0
CAPTCHA_DICTIONARY_MAX_LENGTH = 99
CAPTCHA_TEST_MODE = False


###############################################################################
### PYTHON/DJANGO SOCIAL AUTH                                               ###
###############################################################################

# -----------------------------------------------------------------------------
# --- FACEBOOK
SOCIAL_AUTH_FACEBOOK_KEY = config("SOCIAL_AUTH_FACEBOOK_KEY", default="")
SOCIAL_AUTH_FACEBOOK_SECRET = config("SOCIAL_AUTH_FACEBOOK_SECRET", default="")
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", ]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "fields":   "id,name,email",
}

# -----------------------------------------------------------------------------
# --- TWITTER
TWITTER_OAUTH_TOKEN = config("TWITTER_OAUTH_TOKEN", default="")
TWITTER_OAUTH_SECRET = config("TWITTER_OAUTH_SECRET", default="")
TWITTER_CONSUMER_KEY = config("TWITTER_CONSUMER_KEY", default="")
TWITTER_CONSUMER_SECRET = config("TWITTER_CONSUMER_SECRET", default="")

SOCIAL_AUTH_TWITTER_KEY = TWITTER_CONSUMER_KEY
SOCIAL_AUTH_TWITTER_SECRET = TWITTER_CONSUMER_SECRET

# -----------------------------------------------------------------------------
# --- LINKEDIN
LINKEDIN_OAUTH_TOKEN = config("LINKEDIN_OAUTH_TOKEN", default="")
LINKEDIN_OAUTH_SECRET = config("LINKEDIN_OAUTH_SECRET", default="")
LINKEDIN_CONSUMER_KEY = config("LINKEDIN_CONSUMER_KEY", default="")
LINKEDIN_CONSUMER_SECRET = config("LINKEDIN_CONSUMER_SECRET", default="")
LINKEDIN_SCOPE = ["r_basicprofile", "r_emailaddress", ]
LINKEDIN_EXTRA_FIELD_SELECTORS = ["email-address", ]

# --- OAuth1 Settings
SOCIAL_AUTH_LINKEDIN_KEY = LINKEDIN_CONSUMER_KEY
SOCIAL_AUTH_LINKEDIN_SECRET = LINKEDIN_CONSUMER_SECRET
SOCIAL_AUTH_LINKEDIN_SCOPE = LINKEDIN_SCOPE
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = LINKEDIN_EXTRA_FIELD_SELECTORS

# --- OAuth2 Settings
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = LINKEDIN_CONSUMER_KEY
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = LINKEDIN_CONSUMER_SECRET
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = LINKEDIN_SCOPE
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = LINKEDIN_EXTRA_FIELD_SELECTORS

# -----------------------------------------------------------------------------
# --- GOOGLE-PLUS
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", default="")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", default="")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = []


###############################################################################
### DJANGO TAGGIT                                                           ###
###############################################################################


###############################################################################
### DJANGO WHITE NOISE                                                      ###
###############################################################################
WHITENOISE_MAX_AGE = 31536000


###############################################################################
### MAILING                                                                 ###
###############################################################################


###############################################################################
### PROJECT PAGES TRIGGERS                                                  ###
###############################################################################


###############################################################################
### SANESIDE SOCIAL LINKS                                                   ###
###############################################################################


###############################################################################
### UPLOADING ATTACHMENTS                                                   ###
###############################################################################
UPLOADER_SETTINGS = {
    "default": {
        "FILE_TYPES": [
            "gif", "jpg", "jpeg", "png",
            "doc", "docx", "txt", "rtf",
        ],
        "CONTENT_TYPES": [
            "image/gif",
            "image/jpeg",
            "image/pjpeg",
            "image/png",
            "application/pdf",
            "application/msword",
            "text/plain",
            "text/rtf",
        ],
        "MAX_FILE_SIZE":    10485760,
        "MAX_FILE_NUMBER":  5,
        "AUTO_UPLOAD":      True,
    },
    "documents": {
        "FILE_TYPES": [
            "doc", "docx", "txt", "rtf",
        ],
        "CONTENT_TYPES": [
            "application/pdf",
            "application/msword",
            "text/plain",
            "text/rtf",
            ],
        "MAX_FILE_SIZE":    10485760,
        "MAX_FILE_NUMBER":  5,
        "AUTO_UPLOAD":      True,
    },
    "images": {
        "FILE_TYPES": [
            "gif", "jpg", "jpeg", "png",
        ],
        "CONTENT_TYPES": [
            "image/gif",
            "image/jpeg",
            "image/pjpeg",
            "image/png",
            ],
        "MAX_FILE_SIZE":    10485760,
        "MAX_FILE_NUMBER":  5,
        "AUTO_UPLOAD":      True,
    },
    "video": {
        "FILE_TYPES": [
            "flv", "mpg", "mpeg", "mp4",
            "avi", "mkv", "ogg",
            "wmv", "mov", "webm",
        ],
        "CONTENT_TYPES": [
            "video/mpeg",
            "video/mp4",
            "video/ogg",
            "video/quicktime",
            "video/webm",
            "video/x-ms-wmv",
            "video/x-flv",
            ],
        "MAX_FILE_SIZE":    10485760,
        "MAX_FILE_NUMBER":  5,
        "AUTO_UPLOAD":      True,
    },
    "audio": {
        "FILE_TYPES": [
            "mp3", "mp4", "ogg", "wma", "wax", "wav", "webm",
        ],
        "CONTENT_TYPES": [
            "audio/basic",
            "audio/L24",
            "audio/mp4",
            "audio/mpeg",
            "audio/ogg",
            "audio/vorbis",
            "audio/x-ms-wma",
            "audio/x-ms-wax",
            "audio/vnd.rn-realaudio",
            "audio/vnd.wave",
            "audio/webm",
            ],
        "MAX_FILE_SIZE":    10485760,
        "MAX_FILE_NUMBER":  5,
        "AUTO_UPLOAD":  True,
    }
}
