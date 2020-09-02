""" Production Settings """
import os
import dj_database_url
from .base import *


############
# SECURITY #
############

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')

ALLOWED_HOSTS = ['*']