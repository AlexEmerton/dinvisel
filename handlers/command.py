import requests
from telegram.ext import CommandHandler

from handlers.helpers.storage import Storage


class Command:
    def __init__(self, storage: Storage):
        self.storage = storage

    def start(self):
        return CommandHandler('start', self._start)

    def get_stats_for_name(self):
        return CommandHandler('stats', self._get_stats_for_name)

    def call_for_rainbow(self):
        return CommandHandler('go', self._call_for_rainbow)

    def get_objects(self):
        return CommandHandler('clips', self._get_hosted_clips)

    def _get_hosted_clips(self, update, context):
        objects = self.storage.get_all_object_keys(file_type="mp4")

        # for _ in objects:
        #     context.bot.send_message(
        #         chat_id=update.effective_chat.id, text=_)

    @ staticmethod
    def _start(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="yo")

    @staticmethod
    def _call_for_rainbow(update, context):
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text="сегодня го?")

        context.bot.pin_chat_message(
            update.effective_chat.id, message['message_id'])

    @ staticmethod
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
