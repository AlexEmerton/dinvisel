from gtts import gTTS
import os
from telegram.ext import CommandHandler


class Voice:
    DEFAULT_LANG = 'ru'

    def send_tts(self):
        return CommandHandler('voice', self._send_tts)

    def _send_tts(self, update, context):
        tts_text = context.args[0]

        tts = gTTS(text=tts_text, lang=self.DEFAULT_LANG)
        # tts.save('tts.mp3')

        context.bot.send_voice(chat_id=update.effective_chat.id,
                               voice=tts.stream())