class Chat:

    @staticmethod
    def call_for_rainbow(update, context):
        message = context.bot.send_message(
            chat_id=update.effective_chat.id, text="сегодня го?")

        context.bot.pin_chat_message(
            update.effective_chat.id, message['message_id'])
