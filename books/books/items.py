import scrapy


class BooksItem(scrapy.Item):  # BooksItem inherits form scrap.Item
    url = scrapy.Field()       # .Field() is just a fancy way to say dictionary
    title = scrapy.Field()
    price = scrapy.Field()



