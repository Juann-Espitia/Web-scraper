import scrapy


class BooksItem(scrapy.Item):  # BooksItem inherits form scrap.Item
    _id = scrapy.Field()       # our pipeline adds this value
    url = scrapy.Field()       # .Field() is just a fancy way to say dictionary
    title = scrapy.Field()
    price = scrapy.Field()



