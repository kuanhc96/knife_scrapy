from knife_crawler_spider.items import KnifeCrawlerSpiderItem
import datetime
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from production.items import ProductionItem, ImageItems

class KnifeSpider(scrapy.Spider):
    name = "knife_spider"
    allowed_domains = ["seisukeknife.com"]
    start_urls = ["https://int.seisukeknife.com/collections/gyuto-chefs-knife"]
    # rules = (
    #     Rule(LinkExtractor(allow="/collections/gyuto-chefs-knife")),
    # )
    
    def parse(self, response):
        urls = response.css("div.product-item__wrapper div.product-item__image-wrapper div.height-inherit.has-secondary-image").css("a img::attr(data-src)").extract()
        results = []
        for url in  urls:
            url = response.urljoin(url)
            url = url.replace("{width}", "440")
            results.append(url)
        yield {
            "image_urls" : results,
            # "title": 
        }

