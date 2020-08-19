import logging

# フォーマットを定義
# levelnameにINFO、asctimeに今日の日付と時刻、messageに下記の文字列が表示される。
formatter = '%(levelname)s : %(asctime)s : %(message)s'

# ログレベルを DEBUG に変更
logging.basicConfig(level=logging.DEBUG, format=formatter)

logging.info('%s %s', 'test', 'test')
