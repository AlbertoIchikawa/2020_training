from selenium import webdriver
import requests


class Crawler(object):

    def __init__(self, data_store, reverse_index_queue, doc_index_queue):
        self.data_store = data_store
        self.reverse_index_queue = reverse_index_queue
        self.doc_index_queue = doc_index_queue

    def create_link(self, page):
        """Create link based on url and contents."""

    def crawl_page(self, page):
        for link in page.link:
            self.data_store.add_link_to_crawl(link)
        page.full_text = self.create_full_text(page)
        # self.data_store.remove_link_to_crawl(page.url)
        # self.data_store.insert_crawled_link(page.url, page.signature)

    def crawl(self):
        pages = []
        for title_h3 in driver.find_elements_by_xpath('//a/h3'):
            url_a = title_h3.find_element_by_xpath('..')
            snippet = title_h3.find_element_by_xpath('../../../div/div/span')
            print(title_h3.text)
            print(url_a.get_attribute('href'))
            print(snippet.text)
            page = Page(title, link, ...)
            pages.append(page)
            save_to_db(url, ti)
            count += 1
            if count == int(search_count):
                break
            time.sleep(1)
        driver.close()
        driver.quit()

        # step2
        for page in pages:
            crawl_page(page)
            save_to_db(full_text)
            update_flag
        return [page1, page2]
        pass