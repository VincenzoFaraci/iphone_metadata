import json
import os

from exiftool import ExifToolHelper


default_exif_set_path = "src\\models\\exif_template.json"
with open(default_exif_set_path, 'r') as file:
    default_exif_set = json.load(file)

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')


def set_exif_tags(image_path,exif_template_path:str = None):
    """
    Set EXIF data for the provided image file.
    
    Args:
        image_path (str): The path to the image file.
        exif_template_path (str): the path of the provided exif set
    Returns:
        None
    """
    
    if exif_template_path is None:
        print("Default Exif set has been used since no Exif model was provided.")
        data_dict = default_exif_set
    else:
        print("The provided Exif set has been used")
        with open(exif_template_path, 'r') as file:
            data_dict = json.load(file)
    
    exif_da_settare = data_dict
    with ExifToolHelper() as et:
        et.set_tags(image_path, exif_da_settare)
        
    image_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys():
                value = data.get(key, None)
                key = key.split(":")[-1]
                image_exif[key] = value
    for key in data_dict.keys():
        if key in data.keys():
           pass
        else:
           print(f"The key {key} was not added because it is incorrect.")
                   
    output_json = os.path.join(output_folder, 'image_with_new_exif.json')
    with open(output_json, 'w') as f:
        json.dump(image_exif, f, indent=4)