class ApplicationConfigs:
    def __init__(self, app_configs):
        self.s3_bucket_name = app_configs['s3_service']['bucket_name']
        self.protocol = app_configs['s3_service']['protocol']
        self.bucket = app_configs['s3_service']['bucket_name']
        self.region_name = app_configs['s3_service']['region_name']
        self.endpoint_name = app_configs['s3_service']['name']

        self.endpoint_url = f'{self.protocol}://{self.endpoint_name}'
        self.bucket_endpoint_name = f'{self.protocol}://{self.s3_bucket_name}.{self.endpoint_name}'
