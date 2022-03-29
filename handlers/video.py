import random

from telegram.error import BadRequest

from handlers.clients.s3_client import S3Client
from handlers.helpers.consts import Matchers
from handlers.helpers.encoder import Encoder
from telegram.ext import MessageHandler, CommandHandler, Filters


class Video(S3Client):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs, aws_secrets)

        self.clip_fast = "быстро.mp4"
        self.clip_edgy = "дерзкий.mp4"
        self.clip_family = "семья.mp4"

    def get_all_clips(self):
        return CommandHandler('clips', self._get_all_clips)

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

    def _get_all_clips(self, update, context):
        objects = self.get_all_object_keys(file_type="mp4")

        context.bot.send_message(
            chat_id=update.effective_chat.id, text=', '.join(objects))

    def _send_video_fast(self, update, context):
        clip_name = Encoder.encode_as_base_64(self.clip_fast)

        clip = f'{self.bucket_endpoint_name}/{clip_name}.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    def _send_video_edgy(self, update, context):
        clip = f'{self.bucket_endpoint_name}/{self.clip_edgy}'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    def _send_video_family(self, update, context):
        clip = f'{self.bucket_endpoint_name}/{self.clip_family}'
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=clip)

    def _send_quote_by_key(self, update, context):
        try:
            clip = f'{self.bucket_endpoint_name}/{context.args[0]}.mp4'
            context.bot.send_video(chat_id=update.effective_chat.id,
                                   video=clip)
        except BadRequest:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Такого клипа нет 👀")

    def _send_random_quote(self, update, context):
        random_clip_name = random.choice(self.get_all_object_keys())
        clip = f'{self.bucket_endpoint_name}/{random_clip_name}'

        context.bot.send_video(chat_id=update.effective_chat.id, video=clip)
