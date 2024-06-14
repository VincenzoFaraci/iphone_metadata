from .ExifExtractor import ExifExtractor
from models.exif_models import iphone_exif_key



class IphoneExifExtractor(ExifExtractor):
    def __init__(self,model_value:str):
        self.model_value = model_value
        self.keys = iphone_exif_key
        self.iphone_data = {key: [] for key in self.keys}
        
    def stampa(self):
        print(self.iphone_data)
    
    def set_data(self, image_folder, tot_images = None):
        self.iphone_data =  super().set_data(image_folder, self.iphone_data, self.model_value, tot_images)
        
    def get_data(self):
        return self.iphone_data