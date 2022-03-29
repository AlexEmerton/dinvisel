from telegram.error import BadRequest
from telegram.ext import CommandHandler

from handlers.clients.s3_client import S3Client


class Audio(S3Client):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs, aws_secrets)

    def get_all_tracks(self):
        return CommandHandler('tracks', self._get_all_tracks)

    def get_track_by_key(self):
        return CommandHandler('track', self._get_track_by_key)

    def _get_all_tracks(self, update, context):
        tracks = self.get_all_object_keys(file_type='mp3')

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=', '.join(tracks)
        )

    def _get_track_by_key(self, update, context):
        try:
            track = f'{self.bucket_endpoint_name}/{context.args[0]}.mp3'
            context.bot.send_audio(chat_id=update.effective_chat.id,
                                   title=context.args[0],
                                   video=track)
        except BadRequest:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Такого трэка нет 👀")
