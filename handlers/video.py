import random
from handlers.helpers.consts import Matchers
from telegram.ext import MessageHandler, CommandHandler, Filters


class Video:
    def __init__(self, app_configs):
        self.file_hosting_service = app_configs['file_hosting_service']['url']

    def send_random_quote(self):
        return CommandHandler('wisdom', self._send_random_quote)

    def send_quote_by_key(self):
        return CommandHandler('clip', self._send_quote_by_key)

    def send_video_family(self):
        return CommandHandler('family', self._send_video_family)

    def send_video_fast(self):
        return MessageHandler(
            (Filters.regex(
                Matchers.QUICK) | Filters.regex(Matchers.PROVERNEM)),
            self._send_video_fast)

    def _send_video_fast(self, update, context):
        clip = f'{self.file_hosting_service}/быстро.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    @staticmethod
    def send_video_bro():
        pass

    def _send_video_family(self, update, context):
        clip = f'{self.file_hosting_service}/семья.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    def _send_quote_by_key(self, update, context):
        try:
            # do some check here to verify the requested is in the list of objects in the video bucket
            clip = f'{self.file_hosting_service}/{context.args[0]}.mp4'
            context.bot.send_video(chat_id=update.effective_chat.id,
                                   video=clip)
        except KeyError:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Такого клипа нет 👀")

    @staticmethod
    def _send_random_quote(update, context):
        pass
        # clip = random.choice(list(VideoCuts.cuts.values()))
        #
        # context.bot.send_video(chat_id=update.effective_chat.id,
        #                        video=clip)
