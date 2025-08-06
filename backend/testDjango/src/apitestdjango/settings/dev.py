
import os
from dotenv import load_dotenv
from pathlib import Path
from .base import *
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in your .env file.")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  os.getenv("DEBUG", "True").lower() in ("true", "1")


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "")
if not ALLOWED_HOSTS:
    raise ValueError("ALLOWED_HOSTS must be set in your .env file.")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS.split(",") if host.strip()]
