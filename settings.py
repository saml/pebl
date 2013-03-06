
import os

DEBUG = True

CDN_URL = 'http://localhost:8080'
CSS_URL = CDN_URL
JS_URL = CDN_URL
IMG_URL = CDN_URL

CONTENT_DIR = os.path.abspath('./content')
TEMPLATE_DIRS = [os.path.abspath('./templates')]

HOST = '0.0.0.0'
PORT = 8080


try:
    from settings_local import *
except ImportError:
    pass

