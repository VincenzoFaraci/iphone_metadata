from .ExifExtractor import ExifExtractor
from models.exif_models import iphone_exif_key


class IphoneExifExtractor(ExifExtractor):
    """
    This class inherits from ExifExtractor.
    
    The purpose of this class is to use ExifExtractor when the sensor model provided is that of an iPhone.
    
    The class contains a dictionary with the main keys present in the EXIF data of a photo taken by an iPhone, 
    which is populated using the methods inherited from ExifExtractor.
    
    Attributes:
        model_value (str): The model value of the iPhone.
        keys (list): A list of the main EXIF keys for iPhone photos.
        iphone_data (dict): A dictionary where each key from `keys` is associated with an empty list, to be populated with EXIF data.
    
    Methods:
        __init__(model_value: str): Initializes the IphoneExifExtractor with the specified model value and sets up the iphone_data dictionary.
        print_iphone_dict(): Prints the current state of the iphone_data dictionary.
        set_data(image_folder: str, tot_images: int = None): Populates the iphone_data dictionary with EXIF data from images in the specified folder.
        get_data(): Returns the populated iphone_data dictionary.
    """
    def __init__(self,model_value:str):
        self.model_value = model_value
        self.keys = iphone_exif_key
        self.iphone_data = {key: [] for key in self.keys}
        
    def print_iphone_dict(self):
        print(self.iphone_data)
    
    def set_data(self, image_folder, tot_images = None):
        self.iphone_data =  super().set_data(image_folder, self.iphone_data, self.model_value, tot_images)
        
    def get_data(self):
        return self.iphone_data