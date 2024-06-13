from ..models.modelli_exif_da_usare import dict_da_usare
from exiftool import ExifToolHelper
import json
import os


root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')


def set_exif_tags(image_path,exif_template_path):
    print("exiftemplate_path",exif_template_path)
    """
    Set EXIF data for the provided image file.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        None
    """
    
    if exif_template_path is None:
        print("Default Exif set has been used since no Exif model was provided.")
        data_dict = dict_da_usare
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
            #print(data)
            for key in data.keys():
                value = data.get(key, None)
                key = key.split(":")[-1]
                image_exif[key] = value
    for key in data_dict.keys():
        if key in data.keys():
           pass
        else:
           print(f"La chiave {key} non è stata aggiunta perchè errata")
                   
    output_json = os.path.join(output_folder, 'image_with_new_exif.json')
    with open(output_json, 'w') as f:
        json.dump(image_exif, f, indent=4)