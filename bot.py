from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import Matchers
from helpers.configs import ConfigParser

from handlers.chat import Chat
from handlers.command import Command
from handlers.error import Error
from handlers.image import Image
from handlers.video import Video

TOKEN = ConfigParser.get_token()
PORT = ConfigParser.get_port()
APP_NAME = ConfigParser.get_app_name()


def main():
    commands = Command()
    chat = Chat()
    error = Error()
    image = Image()
    video = Video()

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(commands.start())
    dispatcher.add_handler(commands.get_stats_for_name())

    # dispatcher.add_handler(MessageHandler(Filters.regex(joke_regex), ma_balls))
    #
    # dispatcher.add_handler(MessageHandler(
    #     (Filters.entity('mention') & Filters.regex(Matchers.GO)),
    #     call_for_rainbow))
    #
    # dispatcher.add_handler(MessageHandler(
    #     Filters.regex(Matchers.GO), send_video_fast))

    # log all errors
    dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url=APP_NAME + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
