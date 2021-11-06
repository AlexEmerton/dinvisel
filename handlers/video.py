from ..helpers.consts import Assets


class Video:

    @staticmethod
    def send_video_fast(update, context):
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
