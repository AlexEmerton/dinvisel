from telegram.ext import MessageHandler, Filters
from handlers.helpers.consts import Matchers
from handlers.s3_service import S3Service


class Image(S3Service):
    def __init__(self, app_configs):
        super().__init__(app_configs)

    def send_joke(self):
        return MessageHandler(Filters.regex(Matchers.MA), self._send_joke)

    def _send_joke(self, update, context):
        pic = f'{self.bucket_endpoint_name}/vin_laugh.jpg'

        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ma balls")

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=pic)
