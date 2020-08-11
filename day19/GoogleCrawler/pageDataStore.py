import mysql.connector

from useDatabase import UseDatabase

CRAWLING_FLAG = 0  # クローリングしてないURL
CRAWLED_FLAG = 1  # クローリングしたURL


# このクラスではDBへのインサートを主に実行させるクラス。
class PagesDataStore(object):
    def __init__(self):
        self.db = UseDatabase()

    def add_link_to_crawl(self, url, flag):
        """Add the given link to `links_to_crawl`."""
        # update url, CRAWLING_FLAG
        pass

    def remove_link_to_crawl(self, url):
        """Remove the given link from `links_to_crawl`."""
        # update url, CRAWLED_FLAG
        pass

    def insert_crawled_page(self, title, url, snipet, full_text):
        """Add crawled_page to `page table`."""
        # "insert into Page(title, snippet, URL_Chek_id_url) values('aeiou', 'aiueokakikukekosasisuseso',
        # 1)"

    # title, snippet, URLをDBに保存させるためのメソッド。
    def save_list_pages(self, crawled_pages):
        for crawled_page in crawled_pages:
            self.insert_crawled_page()  # インサートメソッド
            self.add_link_to_crawl()

    def save_page(self, page):
        pass

    # def crawled_similar(self, url):
    #     """Determine if we've already crawled a page matching the given signature"""
