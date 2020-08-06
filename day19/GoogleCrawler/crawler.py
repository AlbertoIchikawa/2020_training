import time
from page import Page


class Crawler(object):
    def __init__(self, driver, page_store):
        self.driver = driver
        self.page_store = page_store

    # step1__title,snippet,URLを取得する。
    def crawl_list_page(self, search_url, search_count):
        self.driver.get(search_url)
        result_pages = []
        # 検索件数ようにあらかじめ変数countを0にする。
        # 変数title_h3はtitleの取得
        titles = self.driver.find_elements_by_xpath('//a/h3')
        for count, title_h3 in enumerate(titles):
            # URlの取得
            url_a = title_h3.find_element_by_xpath('..')
            # snippetの取得
            snippet = title_h3.find_element_by_xpath('../../../div/div/span')
            # ここでのprintをDBにインサートさせる必要がある。。。
            _page = Page(title_h3.text, snippet.text, '', url_a.get_attribute('href'))
            result_pages.append(_page)
            if count+1 == int(search_count):
                break

            time.sleep(1)
        return result_pages

    def crawl_page(self):
        pass

    def crawl(self, search_url, search_count):
        # step1__title,snippet,URLを取得する。
        crawled_pages = self.crawl_list_page(search_url, search_count)
        # DBに保存するまで
        self.page_store.save_list_pages(crawled_pages)
        # # Pageの詳細を取得
        # for _page in crawled_pages:
        #     self.crawl_page(_page)
        #     self.page_store.save_page(_page)


