# Import necessary modules
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

# Custom pipeline class for sorting knife images
class SortKnifeImagesPipeline(ImagesPipeline):
    
    # Method for generating media requests (1st in order of execution)
    def get_media_requests(self, item, info):
        # Extract image URL and knife type from the item
        image_url = item.get('image_url')
        knife_type = item.get('knife_type', 'misc')
        
        # Yield a Request object with metadata containing the knife type
        yield Request(image_url, meta={'knife_type': knife_type})

    # Method for customizing file paths (2nd in order of execution)
    def file_path(self, request, response=None, info=None):
        # Extract knife type from the request metadata
        knife_type = request.meta.get('knife_type', 'misc')
        
        # Call the base class method to get the default file path
        filename = super().file_path(request=request, response=response, info=info)
        
        # Extract the filename from the default path and append the knife type
        filename = filename.split("/")[-1]
        return knife_type + "/" + filename

    # Method called after image download completion (3rd in order of execution)
    def item_completed(self, results, item, info):
        # Extract results for the first image (tuple with success flag and image info)
        results = results[0]
        success = results[0]
        image = results[1]
        
        # If the image download was successful, update the item with the image info
        if success:
            item['image'] = image 
        return item
