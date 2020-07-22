from flask import Flask, render_template, request, escape
from vsearch import search4letters

from ch05.DBcm import UseDatabase

app = Flask(__name__)

import mysql.connector


def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    with UseDatabase(dbconfig) as cursor:

    _SQL = """insert into log (phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    conn.commit()
    conn.close()
    cursor.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '検索結果:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Web版のsearch4lettersにようこそ！')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('フォームデータ', 'リモートアドレス', 'ユーザエージェント', '結果')
    return render_template('viewlog.html',
                           the_title='ログの閲覧',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run()
