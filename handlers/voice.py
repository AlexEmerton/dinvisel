from gtts import gTTS
from telegram.error import BadRequest
from telegram.ext import CommandHandler

from handlers.clients.s3_client import S3Client


class Voice(S3Client):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs, aws_secrets)

    DEFAULT_LANG = 'ru'

    def send_tts(self):
        return CommandHandler('voice', self._send_tts)

    def send_voice_recording(self):
        return CommandHandler('voice_track', self._send_voice_recording)

    def _send_tts(self, update, context):
        tts_text = ' '.join(context.args)

        tts = gTTS(text=tts_text, lang=self.DEFAULT_LANG)
        tts.save('tts.mp3')

        context.bot.send_audio(chat_id=update.effective_chat.id,
                               audio=open('tts.mp3', 'rb'))

    def _send_voice_recording(self, update, context):
        try:
            voice_track = f'{self.bucket_endpoint_name}/{context.args[0]}.ogg'
            context.bot.send_voice(chat_id=update.effective_chat.id,
                                   voice=voice_track)
        except BadRequest:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Такой записи нет 👀")
