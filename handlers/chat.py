from telegram.ext import MessageHandler, Filters
from handlers.helpers.consts import Matchers


class Chat:

    def call_for_rainbow(self):
        return MessageHandler(
            (Filters.entity('mention') & Filters.regex(Matchers.GO)),
            self._call_for_rainbow)

    @staticmethod
    def _call_for_rainbow(update, context):
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text="сегодня го?")

        context.bot.pin_chat_message(
            update.effective_chat.id, message['message_id'])
