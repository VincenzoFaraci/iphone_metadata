from PIL.ExifTags import TAGS, GPSTAGS
from .ExifExtractor import Exif_extractor
from .ExifModels import iphone_exif_key



class IphoneExifExtractor(Exif_extractor):
    def __init__(self,model_value:str):
        self.model_value = model_value
        self.keys = iphone_exif_key
        self.iphone_data = {key: [] for key in self.keys}
    
    def get_data(self, image_folder, tot_images = None):
        self.iphone_data =  super().get_data(image_folder, self.iphone_data,self.model_value, tot_images)
    
    def stampa(self):
        print(self.iphone_data)
    #e fino a qui