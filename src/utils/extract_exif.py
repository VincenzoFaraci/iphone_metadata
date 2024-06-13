from models.ExifExtractor import Exif_extractor
from models.IphoneExifExtractor import IphoneExifExtractor

import json
import os
from exiftool import ExifToolHelper 
from models.ExifModels import iphone_exif_key

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')

def get_folder_data(image_folder,model_value: str = None, tot_images = None):
    """
    Extracts EXIF data from images in the provided folder.
    
    Args:
        image_folder (str): The path to the folder containing the images.
        model_value (str, optional): The model to analyze.
        tot_images (int, optional): Total number of images to analyze. Defaults to None.
        
    Returns:
        None
    """
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14","iPhone 15"):
        print(f"Provided model {model_value}")
        iphone_metadata = IphoneExifExtractor(model_value)
        iphone_metadata.set_data(image_folder,tot_images)
        dict_data = iphone_metadata.get_data()
        return dict_data
        # df_iphone = Exif_dataframe(iphone_metadata.iphone_data)
        # df_iphone.df_to_csv()
        # df_iphone.df_to_excel()
    elif model_value is None:
        print("without model")
        key_dictionary = iphone_exif_key
        dictionary = {key: [] for key in key_dictionary}
        extractor = Exif_extractor()
        exif_metadata = extractor.get_data(image_folder,dictionary,model_value,tot_images)
        ed = Exif_dataframe(exif_metadata)
        ed.df_to_excel()
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
    prova_interna_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys():
                value = data.get(key, None)
                prova_interna_exif[key] = value
                #key = key.split(":")[-1] #change the format of exif tags
                image_exif[key] = value
    print(image_exif)
    output_json = os.path.join(output_folder, 'image_exif.json')
    with open(output_json, 'w') as f:
        json.dump(image_exif, f, indent=4)
    return
    
#     

    
