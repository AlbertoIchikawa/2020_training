class PagesDataStore(object):

    def __init__(self, db);
        self.db = db
        ...

    def add_link_to_crawl(self, title):
        """Add the given link to `links_to_crawl`."""
        ...

    def remove_link_to_crawl(self, title):
        """Remove the given link from `links_to_crawl`."""
        ...

    def reduce_priority_link_to_crawl(self, title):
        """Reduce the priority of a link in `links_to_crawl` to avoid cycles."""
        ...

    def extract_max_priority_page(self):
        """Return the highest priority link in `links_to_crawl`."""
        ...

    def insert_crawled_link(self, title, link):
        """Add the given link to `crawled_links`."""
        ...

    def crawled_similar(self, link):
        """Determine if we've already crawled a page matching the given signature"""
        ...