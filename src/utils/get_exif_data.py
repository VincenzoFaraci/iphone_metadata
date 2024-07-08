from classes.ExifExtractor import ExifExtractor
from classes.IphoneExifExtractor import IphoneExifExtractor

from exiftool import ExifToolHelper,ExifTool 
from models.exif_models import iphone_exif_key

import re


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
        dictionary = {key: [] for key in iphone_exif_key}
        # TODO: create a dynamic dict that keep the unique tags of every processed image
        extractor = ExifExtractor()
        exif_metadata = extractor.set_data(image_folder,dictionary,model_value,tot_images)
        return exif_metadata 
    else:
        raise Exception(f"The provided model - {model_value} - is incorrect")
    
    
    
def parse_exif_output(output):
    exif_dict = {}
    pattern = re.compile(r"\s*\[(?P<group>[^\]]+)\]\s+(?P<tag>[^:]+)\s*:\s*(?P<value>.+)")
    for line in output.split('\n'):
        match = pattern.match(line)
        if match:
            group = match.group('group').strip()
            tag = match.group('tag').strip().replace(" ", "") 
            value = match.group('value').strip()
            exif_dict[f"{group}:{tag}"] = value
    return exif_dict




def get_image_data(image_path):
    """
    Extracts EXIF data from the provided image file.

    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        dict: The dictionary with the extracted exif
    """
    with ExifTool() as et:
        dict = et.execute(b"exiftool",image_path)
        parsed_dict = parse_exif_output(dict)
        return parsed_dict
    
    # with ExifToolHelper() as et:
    #     return et.get_metadata(image_path)[0]
    
