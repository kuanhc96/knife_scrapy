from knife_crawler_spider.items import KnifeImageItem
import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from production.items import ProductionItem, ImageItems

class KnifeSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    name = "knife_spider"
    # allowed_domains = ["seisukeknife.com"]
    # start_urls = ["https://int.seisukeknife.com/"]
    # rules = (
    #     Rule(LinkExtractor(allow="/collections/gyuto-chefs-knife")),
    # )

    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self, response):
        urls = response.css("img ::attr(src)").getall()
        for url in  urls:
            url = response.urljoin(url)
            # url = url.replace("{width}", "440")
            # yield {
            #     "image_url" : url,
            #     "title" : self.counter
            # }
            yield KnifeImageItem(image_url=url, title=self.counter)
            self.counter = self.counter + 1
        
        next_page = response.css("div div div div section div div ul li.next a::attr(href)").extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)


    # def parse(self, response):
    #     urls = response.css("")
        # urls = response.css("div.product-item__wrapper div.product-item__image-wrapper div.height-inherit.has-secondary-image").css("a img::attr(data-src)").extract()
        # image_urls = []
        # for url in  urls:
        #     url = response.urljoin(url)
        #     url = url.replace("{width}", "440")
        #     print(url)
        #     image_urls.append(url)
        
        #     yield {
        #         "image_urls" : image_urls
        #     }
    # response.css("div.product-item__wrapper").css("div.product-item__image-wrapper").css("div.height-inherit.has-secondary-image").css("a.false img").attrib