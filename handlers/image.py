from telegram.ext import MessageHandler, Filters
from handlers.helpers.consts import Matchers


class Image:
    def __init__(self, app_configs):
        self.file_hosting_service = app_configs['file_hosting_service']['url']

    def send_joke(self):
        return MessageHandler(Filters.regex(Matchers.MA), self._send_joke)

    def _send_joke(self, update, context):
        pic = f'{self.file_hosting_service}/vin_laugh.jpg'

        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ma balls")

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=pic)
