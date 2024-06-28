import json
import os

from exiftool import ExifToolHelper


def check_tags(image_path,data_dict):
    """
    Return the EXIF model to be used, 
    whether it is the standard one or the user-provided one.
    
    Args:
        exif_template_path (str): The path to the exif template.
        exif_template_path (str): the path of the provided exif set
    Returns:
        dict : dictionary to use as exif template
    """
    image_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys():
                value = data.get(key, None)
                key = key.split(":")[-1]
                image_exif[key] = value  
    count = 0    
    for key in data_dict.keys():
        if key in data.keys():
            continue
        else:
            print(f"The key {key} was not added because it is incorrect.")
            count += 1
    
    if count == 0:
        print(f"In the file = {image_path} all exif has been setted")
    else:
        print(f'n the file = {image_path}, {count} exif has not been setted')
    return image_exif