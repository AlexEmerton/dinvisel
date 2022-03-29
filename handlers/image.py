from telegram.ext import MessageHandler, Filters

from handlers.clients.s3_client import S3Client
from handlers.helpers.consts import Matchers


class Image(S3Client):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs, aws_secrets)

    def send_joke(self):
        return MessageHandler(Filters.regex(Matchers.MA), self._send_joke)

    def _send_joke(self, update, context):
        pic = f'{self.bucket_endpoint_name}/vin_laugh.jpg'

        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ma balls")

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=pic)
