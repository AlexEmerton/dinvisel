from telegram.ext import MessageHandler, Filters
from handlers.helpers.consts import Assets, Matchers


class Image:

    def send_joke(self):
        return MessageHandler(Filters.regex(Matchers.MA), self._send_joke)

    @staticmethod
    def _send_joke(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ma balls")

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=Assets.LAUGHING_PIC)
