import mysql.connector

# DBの情報をまとめてある。
if __name__ == '__main__':
    connect = mysql.connector.connect(user='Ichikawa',
                                      password='p0ladm1n',
                                      host='127.0.0.1',
                                      database='google_crawler')
    connect.ping(reconnect=True)
    print(connect.is_connected())
    # with UseDatabase(connect)as cursor:
    cursor = connect.cursor()
    # Pageテーブルにtitle,snippetの情報を入れる。
    cursor.execute("""insert into Page(title, snippet, URL_Chek_id_url) values('aeiou', 'aiueokakikukekosasisuseso', 
    1)""")
    # url_chekにURLの情報を入れる。
    cursor.execute("""insert into url_chek(URL) values('aiueokakikukekosasisuseso')""")

