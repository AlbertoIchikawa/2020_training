import logging

# ログレベルを DEBUG に変更
logging.basicConfig(filename='logger.log', level=logging.DEBUG)

# 従来の出力
logging.info('error{}'.format('outputting error'))
logging.info('warning %s %s' % ('was', 'outputted'))
# logging のみの書き方
logging.info('info %s %s', 'test', 'test')
