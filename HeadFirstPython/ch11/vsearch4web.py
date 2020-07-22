from flask import Flask, render_template, request, escape
from vsearch import search4letters

from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    """Webリクエストの詳細と結果をロギングする。"""
    # insertがinsertsになっているのでSQLError例外が起こるようにした。
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """inserts into log
         (phrase, letters, ip, browser_string, results)
          values
          (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))

    except ConnectionError as err:
        print('データベースが動作していますか？エラー：', str(err))
    except CredentialsError as err:
        print('ユーザID/パスワード問題。エラー：', str(err))
    except SQLError as err:
        print('クエリは正しいですか？エラー：', str(err))
    except Exception as err:
        print('何か問題がはっせいしました。', str(err))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """ポストされたデータを抽出し、検索を実行し、結果を返す。"""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '検索結果:'
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('*****ロギングが失敗しました:', str(err))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Web版のsearch4lettersにようこそ！')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """ログファイルの内容をHTMLテーブルとして表示する。"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('フレーズ', '検索文字', 'リモートアドレス', 'ユーザエージェント', '結果')
    return render_template('viewlog.html',
                           the_title='ログの閲覧',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)
