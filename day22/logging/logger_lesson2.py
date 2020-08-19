import logging

logger = logging.getLogger(__name__)
# setLevel で変更
logger.setLevel(logging.DEBUG)


def do_something():
    logger.info('from logger_lesson2')
    logger.debug('from logger_lesson2_debug')
