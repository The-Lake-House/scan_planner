import boto3
import urllib.parse

s3 = boto3.client('s3')


class NoSuchKey(Exception):
    pass


def parse_s3a(uri):
    location = urllib.parse.urlparse(uri)
    bucket = location.netloc
    prefix = location.path.removeprefix('/')
    return bucket, prefix


def s3_list_objects(bucket, prefix, delimiter='/'):
    response = s3.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix,
        Delimiter=delimiter,
    )
    return response.get('Contents', [])


def s3_list_subdirs(bucket, prefix, delimiter='/'):
    response = s3.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix,
        Delimiter=delimiter,
    )
    return response.get('CommonPrefixes', [])


def s3_get(bucket, key, binary=False):
    try:
        response = s3.get_object(
            Bucket=bucket,
            Key=key,
        )
        if binary:
            return response['Body']
        else:
            return response['Body'].read()
    except s3.exceptions.NoSuchKey:
        raise NoSuchKey()
