from telegram.ext import CommandHandler

from handlers.clients.s3_client import S3Client


class Command(S3Client):
    def __init__(self, app_configs, aws_secrets):
        super().__init__(app_configs, aws_secrets)

    def start(self):
        return CommandHandler('start', self._start)

    @staticmethod
    def _start(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="yo")
