import requests
from telegram.ext import CommandHandler


class Command:

    def start(self):
        return CommandHandler('start', self._start)

    def get_stats_for_name(self):
        return CommandHandler('stats', self._get_stats_for_name)

    @ staticmethod
    def _start(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="yo")

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
