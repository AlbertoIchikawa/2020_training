import time

from selenium import webdriver

from page import Page


class Crawler(object):
    def __init__(self, driver):
        self.driver = driver
        # self.page_store = page_store

    # step1__title,snippet,URLを取得する。
    def crawl_list_page(self, search_url, search_count):
        self.driver.get(search_url)
        result_pages = []
        titles = self.driver.find_elements_by_xpath('//a/h3')
        for count, title in enumerate(titles):
            url = title.find_element_by_xpath('..')
            snippet = title.find_element_by_xpath('../../../div/div/span')
            # ここでのprintをDBにインサートさせる必要がある。。。
            # Pageクラスに取得したtitle,snippet,urlを変数_pageに入れる。
            _page = Page(title.text, snippet.text, '', url.get_attribute('href'))
            result_pages.append(_page)
            if count + 1 == int(search_count):
                break
            time.sleep(1)
        return result_pages

    # ここでfull_textを取得するメソッドを作成する。
    def crawl_page(self, url):
        self.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
        url = 'https://docs.python.org/ja/3/tutorial/'
        self.driver.get(url)
        body = self.driver.find_element_by_tag_name("body")
        print(body.text)
        return body

    # app.pyで呼び出されるメソッド。ここでstep1(クローリング、タイトル・URL・スニペット取得する。)
    def crawl(self, search_url, search_count):
        # step1__title,snippet,URLを取得する。
        crawled_pages = self.crawl_list_page(search_url, search_count)
        # DBに保存する
        # self.page_store.save_list_pages(crawled_pages)  # 引数にはtitleなどの情報が入っている。
        # Pageの詳細を取得(full_textの取得)
        # for _page in crawled_pages:
        #     crawled_page = self.crawl_page(_page)
        # self.page_store.save_page(_page)
        # return crawled_page
        return crawled_pages
