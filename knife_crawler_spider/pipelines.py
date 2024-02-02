# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class SortKnifeImagesPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info): # order of execution: 1st
        # for image_url in item.get('image_urls', []):
        image_url = item.get('image_url')
        knife_type = item.get('knife_type', 'misc')
        yield Request(image_url, meta={'knife_type': knife_type})

    def file_path(self, request, response=None, info=None): # order of execution: 2nd
        knife_type = request.meta.get('knife_type', 'misc')
        filename = super().file_path(request=request, response=response, info=info)
        filename = filename.split("/")[-1]
        return knife_type + "/" + filename

    def item_completed(self, results, item, info): # order of execution: 3rd
        results = results[0]
        success = results[0]
        image = results[1]
        if success:
            item['image'] = image 
        return item