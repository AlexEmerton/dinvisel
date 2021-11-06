from handlers.helpers.consts import Assets


class Image:

    @staticmethod
    def send_joke(update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="ma balls")

        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=Assets.LAUGHING_PIC)
