from pathlib import Path
from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6=6qqqefe8z@8_id2iw1t%8pb_@6q7q_ypd5+je11tn7jvgwhr"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'dhruv-portfolio-chatbot.onrender.com',  # Backend
    'dhruv-portfolio-f5ux.onrender.com',     # Frontend
    'localhost',
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    "rest_framework",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware should be first!
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # Keep CSRF middleware for other views
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Portfolio_chatboat.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Portfolio_chatboat.wsgi.application"

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------
# ✅ CORS Configuration
# ------------------------

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Local development frontend
    "http://127.0.0.1:8000",  # Local development frontend
    "http://127.0.0.1:8001",  # Local dev on alternate port
    "https://dhruv-portfolio-f5ux.onrender.com",  # Frontend hosted on Render
    "https://dhruv-portfolio-chatbot.onrender.com",  # Backend hosted on Render (optional, remove if not needed)
]

CORS_ALLOW_CREDENTIALS = True

# Add headers for CORS requests
CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
]

# Expose headers to frontend
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']

# ------------------------
# ✅ CSRF Configuration
# ------------------------

# Trusted origins for CSRF (used when sending cookies for cross-origin requests)
CSRF_TRUSTED_ORIGINS = [
    "https://dhruv-portfolio-f5ux.onrender.com",  # Frontend hosted on Render
]

# CSRF settings (optional if you use `@csrf_exempt` on your API)
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'

# ------------------------
# ✅ Django Security Configuration
# ------------------------

# To protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# To use secure cookies (recommended in production)
SECURE_SSL_REDIRECT = True

# Default settings for secure cookies
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# ------------------------
# ✅ Other Settings
# ------------------------

# Limitations on upload size for requests (e.g. for large files)
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5 MB

# Optional, but good for debugging purposes in development
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
