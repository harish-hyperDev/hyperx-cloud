import os
from dotenv import load_dotenv

load_dotenv()

'''
Config VARIABLES for Wasabi Access
'''
WSB_ACCESS_KEY_ID = os.getenv('WSB_ID')
WSB_SECRET_ACCESS_KEY = os.getenv('WSB_SECRET')
WSB_STORAGE_BUCKET_NAME = os.getenv('WSB_BUCKET_NAME')
WSB_S3_CUSTOM_DOMAIN = 'https://s3.ap-southeast-1.wasabisys.com'

#/%s' % WSB_STORAGE_BUCKET_NAME

WSB_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

WSB_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'mysite.storage_backends.StaticStorage'
STATIC_URL = "https://%s/%s/" % (WSB_S3_CUSTOM_DOMAIN, WSB_STATIC_LOCATION)

WSB_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'mysite.storage_backends.PublicMediaStorage'

WSB_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'mysite.storage_backends.PrivateMediaStorage'

'''
Config VARIABLES for MongoDB Atlas Access
'''
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_URI_PASS = os.getenv('MONGO_URI_PASS')
MONGO_URI_UNAME = os.getenv('MONGO_URI_USERNAME')

'''
Config VARIABLES for Auth TOKEN
'''
AUTH_TOKEN = os.getenv('TOKEN_SECRET')