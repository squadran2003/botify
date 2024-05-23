from .settings import *
from decouple import config, Csv
import boto3
from botocore.exceptions import ClientError
import json
import os

DEBUG = False

ALLOWED_HOSTS = [".botifyapp.com"]

CSRF_TRUSTED_ORIGINS = [
    'https://botifyapp.com',
]


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Rest of your code...


def get_secret():

    secret_name = "botifyapp-secrets"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secrets = get_secret_value_response['SecretString']
    return json.loads(secrets)


SECRETS = get_secret()

SECRET_KEY = SECRETS['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRETS["DB_NAME"],
        'USER': SECRETS["DB_USER"],
        'PASSWORD': SECRETS["DB_PASSWORD"],
        'HOST': SECRETS["DB_HOST"],
        'PORT': '5432',
    }
}
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = "{}.s3.eu-west-2.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
MEDIA_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, 'media')
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'