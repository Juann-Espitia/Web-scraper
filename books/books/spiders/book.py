import scrapy
from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            item = BooksItem()
            item["url"] = book.css("h3 > a::attr(href)").get()
            item["title"] = book.css("h3 > a::attr(title)").get()
            item["price"] = book.css(".price_color::text").get()
            yield item   # yield allows us to store many values that we get into a generator to later use
        
        next_page = response.css("li.next > a::attr(href)").get()        # this grabs the elements in li.next and the a child, but this isn't a URL but rather the path
        if next_page:
            next_page_url = response.urljoin(next_page)                  # so, here we have to join that path with our original URL
            self.logger.info(f"Navigating to next page with URL {next_page_url}")
            yield scrapy.Request(url=next_page_url, callback=self.parse) # then we can finally yield to scrapy.Request with our new URL and using the same parse method
