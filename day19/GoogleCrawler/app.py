from crawler import Crawler
import sys
from selenium import webdriver
import time
import requests
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def crawl_page():
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    url = 'https://docs.python.org/ja/3/tutorial/'
    driver.get(url)
    body = driver.find_element_by_tag_name("body")
    print(body.text)
    driver.close()
    driver.quit()

def main():
    # コマンドライン引数で①検索キーワード、②検索数を入力する。
    args = sys.argv
    key_word = args[1]
    search_count = args[2]
    search_url = 'https://www.google.com/search?q=' + key_word
    # seleniumを使ってchromeで検索する。l17=driverの配置を指定。l18=引数に検索キーワードを入れて実行。
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    crawler = Crawler()
    result = crawler.crawl(search_url, search_count)
    # for url in result:
    #     driver.get(url)
    #     crawler2 = Crawler2()
    #     result2 = crawler2.get_full_text(driver)
    print(result)
    driver.close()
    driver.quit()


if __name__ == "__main__":
    crawl_page()
