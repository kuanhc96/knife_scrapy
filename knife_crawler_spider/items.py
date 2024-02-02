import scrapy

class KnifeImageItem(scrapy.Item):
    # define the fields for your item here like:
    image_url = scrapy.Field()
    image = scrapy.Field()
    knife_type = scrapy.Field()
