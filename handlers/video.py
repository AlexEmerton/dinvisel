from handlers.helpers.consts import Assets, Matchers
from telegram.ext import MessageHandler, Filters


class Video:

    def send_video_fast(self):
        return MessageHandler(
            Filters.regex(Matchers.QUICK) | Filters.regex(Matchers.PROVERNEM),
            self._send_video_fast)

    @staticmethod
    def _send_video_fast(update, context):
        context.bot.send_video(chat_id=update.effective_chat.id,
                               video=Assets.QUICK_VIDEO_ID)

    @staticmethod
    def send_video_bro():
        pass

    @staticmethod
    def send_video_head():
        pass

    @staticmethod
    def send_quote(update, context):
        pass
