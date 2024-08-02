# DJANGO

# DATABASES
from .core import DATABASES  # noqa
DATABASES['default']['PASSWORD'] = '1029384756.Ass'

# DEBUG
from .core import TEMPLATES  # noqa
DEBUG = True
INTERNAL_IPS = ('127.0.0.1', 'localhost')
TEMPLATES[0]['OPTIONS'].update({'debug': DEBUG})
ALLOWED_HOSTS = ['*']

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# THIRD-PARTY
