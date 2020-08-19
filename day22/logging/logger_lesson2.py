import logging

logger = logging.getLogger(__name__)
# setLevel で変更
logger.setLevel(logging.DEBUG)

#ハンドラの取得
get_handler = logging.FileHandler('logger.log')
logger.addHandler(get_handler)


def do_something():
    logger.info('from logger_lesson2')
    logger.info('from logger_lesson2_debug')
