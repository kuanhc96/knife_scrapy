from knife_crawler_spider.items import KnifeCrawlerSpiderItem
import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from production.items import ProductionItem, ImageItems

class KnifeSpider(scrapy.Spider):
    name = "knife_spider"
    # allowed_domains = ["seisukeknife.com"]
    # start_urls = ["https://int.seisukeknife.com/"]
    # rules = (
    #     Rule(LinkExtractor(allow="/collections/gyuto-chefs-knife")),
    # )

    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self, response):
        urls = response.css("img ::attr(src)").getall()
        results = []
        for url in  urls:
            url = response.urljoin(url)
            # url = url.replace("{width}", "440")
            results.append(url)
        yield {
            "image_urls" : results
        }


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