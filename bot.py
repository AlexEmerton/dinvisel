from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
from telegram.messageentity import MessageEntity
import logging
import os

TOKEN = '1722312756:AAFi_ipQO6nvqOjf7IREZS7_BgP7GsMneUo'
PORT = int(os.environ.get('PORT', '8443'))
APP_NAME = 'https://dinvisel.herokuapp.com/'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="yo")


def call_for_rainbow(update, context):
    message = context.bot.send_message(
        chat_id=update.effective_chat.id, text="сегодня го?")
    context.bot.pin_chat_message(update.effective_chat.id, message['message_id'])


def image(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo="https://static.wikia.nocookie.net/cyberpunk/images/0/0d/Cyberpunk2077_Wallpapers_Arasaka_1080x1920_EN.png")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # dispatcher.add_handler(MessageHandler(Filters.text, image))

    dispatcher.add_handler(MessageHandler(
        (Filters.entity('mention') & Filters.regex(r'go?')), call_for_rainbow))

    # log all errors
    dispatcher.add_error_handler(error)

    # updater.start_polling()

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url=APP_NAME + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
