# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class SerializeImagesPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info): # order of execution: 1st
        # for image_url in item.get('image_urls', []):
        image_url = item.get('image_url')
        title = item.get('title', 'XXXXX')
        yield Request(image_url, meta={'title': title})

    def file_path(self, request, response=None, info=None): # order of execution: 2nd
        title = request.meta.get('title', 'XXXXX')
        filename = f"{str( title ).zfill(4)}.jpg"
        return filename

    def item_completed(self, results, item, info): # order of execution: 3rd
        results = results[0]
        success = results[0]
        image = results[1]
        if success:
            item['image'] = image 
        return item