import boto3


def download_file(s3_url: str, tmp_filename: str):
    # Download file
    bucket_name = s3_url.split('/')[2]
    bucket_name = bucket_name.split('.')[0]
    # the object should start with the sub domain or else it will not work
    key = "/".join(s3_url.split("/")[3:])
    s3 = boto3.client(
        's3'
    )
    if not tmp_filename:
        raise Exception("tmp_filename not set")
    s3.download_file(
        bucket_name,
        key,
        tmp_filename
    )


def save_file(bucket_name: str, files: list):
    # save file to s3
    s3 = boto3.client(
        's3'
    )
    for file in files:
        filename = file.split('/')[-1]
        s3.upload_file(
            file,
            bucket_name,
            'processed/thumbnails/1/{}'.format(filename)
        )