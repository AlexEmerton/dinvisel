import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)


class Error:
    def log_exception(update, context, x):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)
