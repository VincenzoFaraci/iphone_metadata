import json
import os

from exiftool import ExifToolHelper




def check_tags(image_exif_dict:dict, template_data_dict:dict):
    """
    Check if the image_exif_dict has all the templte_data_dict keys and value
    
    Args:
        exif_template_path (str): The path to the exif template.
        exif_template_path (str): the path of the provided exif set
    Returns:
        dict : dictionary to use as exif template
    """
    for key in template_data_dict.keys():
        if key in image_exif_dict.keys():
            if image_exif_dict[key] == template_data_dict[key]:
                #print(f"Tag present and the value has been set: {key} , setted:{image_exif_dict[key]}, template:{template_data_dict[key]}")
                continue
            else:
                print(f"Tag present BUT the value has NOT been set: {key} , setted:{image_exif_dict[key]}, template:{template_data_dict[key]}")
        else:
            print(f"Tag not present: {key}") # potrebbe dare errore da testare
    