from telegram.ext import Updater

from handlers.audio import Audio
from handlers.rainbow import Rainbow
from handlers.voice import Voice
from helpers.configs import ConfigParser

from handlers.chat import Chat
from handlers.command import Command
from loggers.error import Error
from handlers.image import Image
from handlers.video import Video
from secrets.aws_secrets import AwsSecrets

APP_CONFIGS = ConfigParser.get_app_configs()
TOKEN = ConfigParser.get_token()
PORT = ConfigParser.get_port()

AWS_SECRET_KEY_ID = ConfigParser.get_aws_access_key_id()
AWS_SECRET_KEY = ConfigParser.get_aws_secret_access_key()

AWS_SECRETS = AwsSecrets(AWS_SECRET_KEY_ID, AWS_SECRET_KEY)

APP_NAME = APP_CONFIGS['application']['hosted_address']


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # log all errors
    error = Error()
    dispatcher.add_error_handler(error.log_exception)

    # handlers
    video = Video(APP_CONFIGS, AWS_SECRETS)
    image = Image(APP_CONFIGS, AWS_SECRETS)
    audio = Audio(APP_CONFIGS, AWS_SECRETS)
    voice = Voice(APP_CONFIGS, AWS_SECRETS)
    rainbow = Rainbow(APP_CONFIGS, AWS_SECRETS)
    commands = Command(APP_CONFIGS, AWS_SECRETS)

    chat = Chat()

    # handle /slash commands
    dispatcher.add_handler(commands.start())

    # handle image sending commands
    dispatcher.add_handler(image.send_joke())

    # handle rainbow6 commands
    dispatcher.add_handler(rainbow.call_for_rainbow())
    dispatcher.add_handler(rainbow.get_stats_for_name())

    # handle chat commands
    dispatcher.add_handler(chat.against())

    # handle video sending commands
    dispatcher.add_handler(video.get_all_clips())
    dispatcher.add_handler(video.send_video_fast())
    dispatcher.add_handler(video.send_video_edgy())
    dispatcher.add_handler(video.send_random_quote())
    dispatcher.add_handler(video.send_video_family())
    dispatcher.add_handler(video.send_quote_by_key())

    # handle audio sending commands
    dispatcher.add_handler(audio.get_all_tracks())
    dispatcher.add_handler(audio.get_track_by_key())

    # handle voice sending commands
    dispatcher.add_handler(voice.send_tts())
    dispatcher.add_handler(voice.send_voice_recording())
    dispatcher.add_handler(voice.get_voice_recordings())

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url=APP_NAME + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
