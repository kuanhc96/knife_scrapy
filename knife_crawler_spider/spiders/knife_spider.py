# Import necessary modules and the custom item class
from knife_crawler_spider.items import KnifeImageItem
import scrapy

# Define the spider class
class KnifeSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Spider name
    name = "knife_spider"

    # List of allowed domains to scrape
    allowed_domains = ["seisukeknife.com"]

    # List of starting URLs for the spider
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

    # Parse method for handling the response
    def parse(self, response):
        # Extract image URLs
        urls = response.css("div.product-item__wrapper div.product-item__image-wrapper div.height-inherit.has-secondary-image").css("a img::attr(data-src)").getall()

        # Extract the knife type from the response
        knife_type_full = response.css("div div div div div section div div div h2::text").extract_first().split(" ")
        knife_type = knife_type_full[0].lower()

        # Iterate through image URLs and yield KnifeImageItem
        for url in urls:
            url = response.urljoin(url)
            url = url.replace("{width}", "440")
            yield KnifeImageItem(image_url=url, knife_type=knife_type)

        # Extract the URL of the next page
        next_page = response.css("div div.main-content div.index-wrapper div.collection-wrapper section div div main div div.pagination-next a::attr(href)").extract_first()

        # Check if there is a next page and send a request to it
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
