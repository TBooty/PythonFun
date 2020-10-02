import os
import boto3
from botocore.exceptions import NoCredentialsError



def create_aws_session():
    return boto3.session.Session(aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))

def make_s3_bucket():
    session = create_aws_session()
    s3_bucket = session.resource('s3')
    return s3_bucket.create_bucket(Bucket="catbucket.python", ACL='public-read')


def upload_to_aws_(local_file, bucket, s3_file):
    session = create_aws_session()
    s3_resource= session.resource('s3')
    bucket = s3_resource.Bucket('catbucket.python')

    try:
        print(local_file)
        bucket.upload_file(Filename=local_file, Key=s3_file)
        print("Upload success")
        return True
    except NoCredentialsError:
        print("Creds error")
        return False


make_s3_bucket()
uploaded = upload_to_aws_('cat.jpg', 'catbucket.python', 'BlackCat.jpg')
