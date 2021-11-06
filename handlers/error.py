import logging


class Error:

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    logger = logging.getLogger(__name__)

    def log_exception(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning(
            'Update "%s" caused error "%s"', update, context.error)
