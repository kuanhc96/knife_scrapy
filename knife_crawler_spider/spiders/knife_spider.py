from knife_crawler_spider.items import KnifeImageItem
import scrapy

class KnifeSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = "knife_spider"
    allowed_domains = ["seisukeknife.com"]
    start_urls = [
        "https://int.seisukeknife.com/collections/gyuto-chefs-knife",
        "https://int.seisukeknife.com/collections/santoku-all-purpose-knives",
        "https://int.seisukeknife.com/collections/bunka-knife",
        "https://int.seisukeknife.com/collections/nakiri-vegetable",
        "https://int.seisukeknife.com/collections/petty-utility",
        "https://int.seisukeknife.com/collections/paring-peeling-knives",
        "https://int.seisukeknife.com/collections/sujihiki-slicer-knives",
        "https://int.seisukeknife.com/collections/honesuki-boning-knife-1",
        "https://int.seisukeknife.com/collections/yanagiba-fuguhiki-slicer",
        "https://int.seisukeknife.com/collections/deba-butchery",
        "https://int.seisukeknife.com/collections/usuba-mukimono"

    ]
    
    def parse(self, response):
        urls = response.css("div.product-item__wrapper div.product-item__image-wrapper div.height-inherit.has-secondary-image").css("a img::attr(data-src)").getall()
        knife_type_full = response.css("div div div div div section div div div h2::text").extract_first().split(" ")
        knife_type = knife_type_full[0].lower()
        for url in  urls:
            url = response.urljoin(url)
            url = url.replace("{width}", "440")
            yield KnifeImageItem(image_url=url, knife_type=knife_type)
        
        next_page = response.css("div div.main-content div.index-wrapper div.collection-wrapper section div div main div div.pagination-next a::attr(href)").extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

