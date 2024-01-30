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
    
    def parse(self, response):
        urls = response.css("div.product-item__wrapper div.product-item__image-wrapper div.height-inherit.has-secondary-image").css("a img::attr(data-src)").extract()
        list_urls = []
        for url in  urls:
            url = response.urljoin(url)
            url = url.replace("{width}", "440")
            list_urls.append(url)
        yield {
            "image_urls" : list_urls,
        }

