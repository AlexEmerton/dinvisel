from telegram.ext import Updater
from handlers.helpers.configs import ConfigParser

from handlers.chat import Chat
from handlers.command import Command
from handlers.error import Error
from handlers.image import Image
from handlers.video import Video

TOKEN = ConfigParser.get_token()
PORT = ConfigParser.get_port()
APP_NAME = ConfigParser.get_app_name()
APP_CONFIGS = ConfigParser.get_app_configs()


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    commands, chat, error, image = Command(), Chat(), Error(), Image()
    video = Video(APP_CONFIGS)

    # handle /slash commands
    dispatcher.add_handler(commands.start())
    dispatcher.add_handler(commands.get_stats_for_name())

    # handle image sending commands
    dispatcher.add_handler(image.send_joke())

    # handle chat commands
    dispatcher.add_handler(chat.call_for_rainbow())
    dispatcher.add_handler(chat.against())

    # handle video sending commands
    dispatcher.add_handler(video.send_video_fast())
    dispatcher.add_handler(video.send_random_quote())
    dispatcher.add_handler(video.send_video_family())
    dispatcher.add_handler(video.send_quote_by_key())

    # log all errors
    dispatcher.add_error_handler(error.log_exception)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url=APP_NAME + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
