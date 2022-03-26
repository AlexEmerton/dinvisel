from telegram.ext import MessageHandler, Filters
from handlers.helpers.consts import Matchers


class Image:
    def __init__(self, app_configs):
        self.s3_service_url = app_configs['file_hosting_service']['url']
        self.s3_bucket_name = app_configs['file_hosting_service']['bucket_name']
        self.s3_bucket_host_name = f"{self.s3_bucket_name}.{self.s3_service_url}"

    def send_joke(self):
        return MessageHandler(Filters.regex(Matchers.MA), self._send_joke)

    def _send_joke(self, update, context):
        pic = f'{self.s3_bucket_host_name}/vin_laugh.jpg'

        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ma balls")

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=pic)
