from telegram.ext import MessageHandler, Filters
from handlers.helpers.consts import Matchers


class Chat:

    def against(self):
        return MessageHandler((Filters.regex(Matchers.SCRIPTED)), self._against)

    @staticmethod
    def _against(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="против Азика")
