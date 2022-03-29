import requests
from telegram.ext import CommandHandler

from handlers.clients.s3_client import S3Client


class Rainbow(S3Client):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs, aws_secrets)

    def get_stats_for_name(self):
        return CommandHandler('stats', self._get_stats_for_name)

    def call_for_rainbow(self):
        return CommandHandler('go', self._call_for_rainbow)

    @staticmethod
    def _get_stats_for_name(update, context):
        if context.args[0]:
            url = "https://r6.tracker.network/profile/pc/{}/".format(
                context.args[0])
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Нужен аккаунт для поиска, напиши так > /stats никЗдесь")
            raise ValueError("no profile supplied!")

        r = requests.get(url)

        if r.status_code == 200:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Чёрт найден!")

            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=url)
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Аккаунт не найден на Трэкере")

    @staticmethod
    def _call_for_rainbow(update, context):
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text="сегодня го?")

        context.bot.pin_chat_message(
            update.effective_chat.id, message['message_id'])
