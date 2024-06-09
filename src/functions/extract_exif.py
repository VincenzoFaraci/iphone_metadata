from models.IphoneExifExtractor import IphoneExifExtractor
from models.ExifDataframe import Exif_dataframe
import json
import os
from exiftool import ExifToolHelper 

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
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14"):
        print(f"Provided model {model_value}")
        iphone_metadata = IphoneExifExtractor(model_value)
        iphone_metadata.get_data(image_folder,tot_images)
        df_iphone = Exif_dataframe(iphone_metadata.iphone_data)
        df_iphone.df_to_csv()
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
    image_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys():
                value = data.get(key, None)
                key = key.split(":")[-1]
                image_exif[key] = value
    output_json = os.path.join(output_folder, 'image_exif.json')
    with open(output_json, 'w') as f:
        json.dump(image_exif, f, indent=4)
    return
    
#     

    
