from classes.ExifExtractor import ExifExtractor
from classes.IphoneExifExtractor import IphoneExifExtractor

from exiftool import ExifToolHelper 
from models.exif_models import iphone_exif_key



def get_folder_data(image_folder,model_value: str = None, tot_images = None):
    """
    Extracts EXIF data from images in the provided folder.
    
    Args:
        image_folder (str): The path to the folder containing the images.
        model_value (str, optional): The model to analyze.
        tot_images (int, optional): Total number of images to analyze. Defaults to None.
        
    Returns:
        dict: The dictionary with the extracted exif
    """
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14","iPhone 15"):
        iphone_metadata = IphoneExifExtractor(model_value)
        iphone_metadata.set_data(image_folder,tot_images)
        dict_data = iphone_metadata.get_data()
        return dict_data
    elif model_value is None:
        dictionary = {key: [] for key in iphone_exif_key} #change to generic_exif_key to be more generic
        # TODO: create a dynamic dict that keep the unique tags of every processed image
        extractor = ExifExtractor()
        exif_metadata = extractor.set_data(image_folder,dictionary,model_value,tot_images)
        return exif_metadata 
    else:
        raise Exception(f"The provided model - {model_value} - is incorrect")

def get_image_data(image_path):
    """
    Extracts EXIF data from the provided image file.

    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        dict: The dictionary with the extracted exif
    """
    image_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys(): 
                image_exif[key] = data.get(key, None)
    return image_exif  

    
