# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class SerializeImagesPipeline(ImagesPipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
    
    def get_media_requests(self, item, info): # order of execution: 1st
        for image_url in item.get('image_urls', []):
            yield Request(image_url)

    def file_path(self, request, response=None, info=None): # order of execution: 2nd
        filename = f"{str( self.counter ).zfill(4)}.jpg"
        self.counter += 1
        return filename

    def item_completed(self, results, item, info): # order of execution: 3rd
        item['images'] = [image for success, image in results if success]
        return item