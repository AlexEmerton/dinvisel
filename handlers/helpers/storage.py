import boto3
from botocore.client import Config

from handlers.s3_service import S3Service


class Storage(S3Service):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs)

        self.aws_access_key_id = aws_secrets.aws_access_key_id
        self.aws_secret_access_key = aws_secrets.aws_access_key

        self.config = Config(
            read_timeout=900,
            connect_timeout=900,
            retries={
                'max_attempts': 2,
                'mode': 'standard'
            }
        )

        self.s3 = self.get_resource()

    def get_resource(self):
        return boto3.client(
            's3',
            region_name=self.region_name,
            use_ssl=True,
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            config=self.config
        )

    def get_all_object_keys(self, file_type=None):
        """
        get keys of all s3 objects from bucket
        :param file_type: optional, only filter by files ending with a specific file_type
        :return:
        """
        import logging
        logger = logging.getLogger(__name__)

        objects = []
        fetched_objects = self.s3.list_objects_v2(
            Bucket=self.bucket
        )

        logger.info("OBJECT TYPE::::::")

        for _ in fetched_objects['Contents'][0]:
            logger.info(_)
            logger.info(type(_))
            if file_type:
                if _['Key'].endswith("mp4"):
                    objects.append(_)
            else:
                objects.append(_)

        return objects
