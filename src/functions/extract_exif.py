from models.ExifExtractor import Exif_extractor
from models.IphoneExifExtractor import IphoneExifExtractor
from models.ExifDataframe import Exif_dataframe
from PIL.ExifTags import TAGS
import json
import os
from PIL import Image,TiffImagePlugin
from exiftool import ExifTool 

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')

def get_folder_data(image_folder,model_value: str, tot_images = None):
    """
    Extracts EXIF data from images in the provided folder.
    
    Args:
        image_folder (str): The path to the folder containing the images.
        model_value (str): The model to analyze.
        tot_images (int, optional): Total number of images to analyze. Defaults to None.
        
    Returns:
        None
    """
    print("prova")
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14"):
        print(f"Provided model {model_value}")
        iphone_metadata = IphoneExifExtractor(model_value)
        iphone_metadata.get_data(image_folder,tot_images)
        df_iphone = Exif_dataframe(iphone_metadata.iphone_data)
        df_iphone.df_to_excel()
    return 

def get_image_data(image_path):
    """
    Extracts EXIF data from the provided image file.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        None
    """
    # keys_list = ExifModels.generic_exif_key
    # image_exif = {key: None for key in keys_list} 
    image_exif = {}
    image_exif_extractor = Exif_extractor()
    image_exif = image_exif_extractor.get_image_data(image_path, image_exif)
    image_exif["filename"] = os.path.basename(image_path)
    normalized_exif = {key: cast(value) for key, value in image_exif.items()}

    output_json = os.path.join(output_folder, 'image_exif.json')
    with open(output_json, 'w') as f:
        json.dump(normalized_exif, f, indent=4)
    
def cast(v):
    """
    Casts the given value to the appropriate type.

    Args:
        v: The value to cast.

    Returns:
        The casted value.
    """
    if isinstance(v, TiffImagePlugin.IFDRational):
        if v.denominator != 0:
            return float(v.numerator) / float(v.denominator)
        else:
            return None  
    elif isinstance(v, tuple):
        return tuple(cast(t) for t in v)
    elif isinstance(v, bytes):
        return v.decode(errors="replace")
    elif isinstance(v, dict):
        for kk, vv in v.items():
            v[kk] = cast(vv)
        return v
    else: 
        return v

    
