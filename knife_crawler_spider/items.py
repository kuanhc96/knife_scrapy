# Import the Scrapy module
import scrapy

# Define a custom Scrapy Item class for representing knife images
class KnifeImageItem(scrapy.Item):
    # Define fields for the item
    image_url = scrapy.Field()    # URL of the image
    image = scrapy.Field()        # Actual image data (after download)
    knife_type = scrapy.Field()    # Type of the knife associated with the image
