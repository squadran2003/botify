import boto3
from botocore.exceptions import ClientError
import json
import os
import sys


def get_secrets():

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
    secret_dict = json.loads(secrets)
    return secret_dict["DJANGO_SETTINGS_MODULE"]


if __name__ == "__main__":
    print(sys.argv)
    if sys.argv[1] == "production":
        print("Getting settings from AWS Secrets Manager")
        print(get_secrets())
        os.environ["DJANGO_SETTINGS_MODULE"] = "botify.production_settings"
    else:
        print("Using local settings")
        os.environ["DJANGO_SETTINGS_MODULE"] = "botify.settings"