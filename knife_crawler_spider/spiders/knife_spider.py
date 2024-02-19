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
    allowed_domains = ["chubokuknives.com"]

    # List of starting URLs for the spider
    start_urls = [
        "https://www.chuboknives.com/collections/santoku",
    ]

    # Parse method for handling the response
    def parse(self, response):
        # Extract image URLs
        urls = response.css("div div div div div div div div div img::attr(data-src)").getall()

        # Extract the knife type from the response
        knife_type_full = response.css("div div div div div h1::text").extract_first()
        knife_type = knife_type_full.split()[0].lower()

        # Iterate through image URLs and yield KnifeImageItem
        for url in urls:
            url = response.urljoin(url)
            url = url.replace("{width}", "720")
            yield KnifeImageItem(image_url=url, knife_type=knife_type)

        # Extract the URL of the next page
        next_page = None #response.css("div div div div div span.next a::attr(href)").extract_first()

        # Check if there is a next page and send a request to it
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
