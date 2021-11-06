import random
from handlers.helpers.consts import Matchers, VideoCuts
from telegram.ext import MessageHandler, CommandHandler, Filters


class Video:

    def send_random_quote(self):
        return CommandHandler('wisdom', self._send_random_quote)

    def send_quote_by_key(self):
        return CommandHandler('wisdom', self._send_quote_by_key)

    def send_video_family(self):
        return CommandHandler('family', self._send_video_family)

    def send_video_fast(self):
        return MessageHandler(
            (Filters.regex(
                Matchers.QUICK) | Filters.regex(Matchers.PROVERNEM)),
            self._send_video_fast)

    @staticmethod
    def _send_video_fast(update, context):
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=VideoCuts.cuts["быстро"])

    @staticmethod
    def send_video_bro():
        pass

    @staticmethod
    def _send_video_family(update, context):
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=VideoCuts.cuts["семья"])

    @staticmethod
    def _send_quote_by_key(update, context):
        try:
            clip = VideoCuts.cuts[context.args[0]]
            context.bot.send_video(chat_id=update.effective_chat.id,
                                   video=clip)
        except KeyError:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Такого клипа нет 👀")

    @staticmethod
    def _send_random_quote(update, context):
        clip = random.choice(list(VideoCuts.cuts.values()))

        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)
