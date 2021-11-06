import random
from handlers.helpers.consts import Matchers, VideoCuts
from telegram.ext import MessageHandler, CommandHandler, Filters


class Video:

    def send_random_quote(self):
        return CommandHandler('wisdom', self._send_random_quote)

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
    def send_video_head():
        pass

    @staticmethod
    def send_quote(update, context):
        pass

    @staticmethod
    def _send_random_quote(update, context):
        clip = random.choice(list(VideoCuts.cuts.values()))

        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)
