import logging
import random

import telegram

from handlers.helpers.consts import Matchers
from telegram.ext import MessageHandler, CommandHandler, Filters

from handlers.s3_service import S3Service


class Video(S3Service):
    def __init__(self, app_configs):
        super().__init__(app_configs)

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

    def send_video_edgy(self):
        return MessageHandler((Filters.regex(Matchers.EDGY)), self._send_video_edgy)

    def _send_video_fast(self, update, context):
        clip = f'{self.bucket_endpoint_name}/быстро.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)
        # https://dinvisel-media.s3.pl-waw.scw.cloud/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE.mp4

    def _send_video_edgy(self, update, context):
        clip = f'{self.bucket_endpoint_name}/дерзкий.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    @staticmethod
    def send_video_bro():
        pass

    def _send_video_family(self, update, context):
        clip = f'{self.bucket_endpoint_name}/семья.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    def _send_quote_by_key(self, update, context):
        try:
            clip = f'{self.bucket_endpoint_name}/{context.args[0]}.mp4'
            context.bot.send_video(chat_id=update.effective_chat.id,
                                   video=clip)
        except telegram.error.BadRequest:
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
