import boto3


class Storage:
    def __init__(self, app_configs, aws_secrets):
        self.bucket = app_configs['file_hosting_service']['bucket_name']
        self.region_name = app_configs['file_hosting_service']['region_name']
        self.endpoint_url = app_configs['file_hosting_service']['url']
        self.aws_access_key_id = aws_secrets.aws_access_key_id
        self.aws_secret_access_key = aws_secrets.aws_access_key

    def get_resource(self):
        return boto3.resource(
            's3',
            region_name=self.region_name,
            use_ssl=True,
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )

    def get_all_objects(self):
        import logging
        log = logging.getLogger(__name__)
        s3 = self.get_resource()

        bucket = s3.Bucket(self.bucket)

        for my_bucket_object in bucket.objects.all():
            log.info(my_bucket_object.key)
