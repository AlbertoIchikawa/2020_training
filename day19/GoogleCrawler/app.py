# from crawler import Crawler
import sys
import time
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def main():
    # コマンドライン引数で①検索キーワード、②検索数を入力する。
    args = sys.argv
    key_word = args[1]
    search_count = args[2]

    # seleniumを使ってchromeで検索する。l17=driverの配置を指定。l18=引数に検索キーワードを入れて実行。
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.google.com/search?q=' + key_word)
    # 検索件数ようにあらかじめ変数countを0にする。
    count = 0

    # step1__title,snippet,URLを取得する。(DBに保存するまで)
    urls = []
    # 変数title_h3はtitleの取得
    for title_h3 in driver.find_elements_by_xpath('//a/h3'):
        # URlの取得
        url_a = title_h3.find_element_by_xpath('..')
        # snippetの取得
        snippet = title_h3.find_element_by_xpath('../../../div/div/span')
        print(title_h3.text)
        print(url_a.get_attribute('href'))
        print(snippet.text)
        # urlsリストにurl情報を入れる。
        urls.append(url_a.get_attribute('href'))
        count += 1
        if count == int(search_count):
            break
        time.sleep(1)
    driver.close()
    driver.quit()

    # step2__取得したURL情報をもとに次はfull_textの情報を取得する。
    for url in urls:
        full_text = get_text_from_url(url)

    # 最終的にresultで情報を表示させる。
    # crawler_ = Crawler()
    # results = crawler_.crawl(url)
    # print(results)


if __name__ == "__main__":
    main()
