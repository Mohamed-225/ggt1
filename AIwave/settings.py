from pathlib import Path
import os # استيراد os للوصول لمتغيرات البيئة
from dotenv import load_dotenv # اختيارية: لتحميل متغيرات البيئة من .env

load_dotenv() # اختيارية: تحميل .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# استخدم متغير بيئة لـ SECRET_KEY بدلاً من وضعه مباشرة هنا
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-wv31dfujthor=$f$p+%zsscb3b!c%l3uf*6_j609%t!%74+bfc') # قيمة افتراضية للتطوير المحلي

# استخدم متغير بيئة لـ DEBUG
# قم بتحويل قيمة المتغير النصية 'False' أو 'True' إلى Boolean
DEBUG = os.environ.get('DEBUG', 'True') == 'True' # افتراضيًا True للتطوير المحلي

ALLOWED_HOSTS = ['kengster.onrender.com', 'localhost', '127.0.0.1']
# على Render، قد تحتاج لإضافة اسم النطاق الخاص بـ Render تلقائيًا
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # أضف تطبيقاتك هنا
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # === أضف Whitenoise هنا ===
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ==========================
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AIwave.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'AIwave.wsgi.application'


# Database settings (يُفضل استخدام dj-database-url مع Render)
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        # إذا لم يتم العثور على DATABASE_URL، استخدم sqlite المحلي
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600 # تحسين أداء الاتصال بقاعدة البيانات
    )
}


# Password validation settings
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/' # أو '/static/'

# المسار الذي سيتم تجميع الملفات الثابتة إليه بواسطة collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# المجلدات الإضافية التي تحتوي على ملفات ثابتة (مثل CSS الناتج عن SASS)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# تحسين أداء Whitenoise (اختياري ولكن موصى به)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'