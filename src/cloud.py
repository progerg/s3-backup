import logging

import boto3
from botocore.exceptions import NoCredentialsError


class CloudS3Uploader:
    def __init__(self, service_name: str, bucket_name: str, access_key: str, secret_key: str, endpoint_url: str):
        """
        Initializes the uploader for Cloud Object Storage.
        :param bucket_name: The name of the bucket in Cloud.
        :param access_key: The access key ID for Yandex Cloud access.
        :param secret_key: The secret access key for Yandex Cloud access.
        :param endpoint_url: The endpoint URL of Yandex Cloud Object Storage.
        """

        self.bucket_name = bucket_name
        session = boto3.session.Session()
        self.s3 = session.client(
            service_name=service_name,
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )

    def upload_file(self, file_path: str, object_name: str = None):
        """
        Uploads a file to Cloud Object Storage.
        :param file_path: The path to the file to be uploaded.
        :param object_name: The name of the object in the bucket. If None, the file name is used.
        """

        if object_name is None:
            object_name = file_path

        try:
            self.s3.upload_file(file_path, self.bucket_name, object_name)
            logging.info(f"File {file_path} has been uploaded to {self.bucket_name}/{object_name}")
        except NoCredentialsError:
            logging.info("Credentials not available")
