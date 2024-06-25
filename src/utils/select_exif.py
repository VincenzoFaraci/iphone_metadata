import json
import os

from exiftool import ExifToolHelper

# ATTENZIONE USA OS PATH, LO VEDO DI NUOVO TI TAGLIO LE MANI
default_exif_set_path = "src/models/exif_template.json"
with open(default_exif_set_path, 'r') as file:
    default_exif_set = json.load(file)

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')

def choose_exif_template(exif_template_path:str = None):
    if exif_template_path is None:
        print("Default Exif set has been used since no Exif model was provided.")
        return default_exif_set
    else:
        print("The provided Exif set has been used")
        with open(exif_template_path, 'r') as file:
            data_dict = json.load(file)
    return data_dict

def check_tags(image_path,data_dict):
    image_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys():
                value = data.get(key, None)
                key = key.split(":")[-1]
                image_exif[key] = value  
    print(f"In the file = {image_path}:")
    count = 0    
    for key in data_dict.keys():
        if key in data.keys():
            pass # ????????????
        else:
            print(f"The key {key} was not added because it is incorrect.")
            count += 1
    
    if count == 0:
        print(f"In the file = {image_path} all exif has been setted")
    
    return image_exif

def remove_original(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg_original'):
            os.remove(os.path.join(folder_path, filename))

      
def set_exif_tags(images_folder,exif_template_path:str = None):
    """
    Set EXIF for all the provided image file in the folder.
    
    Args:
        images_folder (str): The path to the image file.
        exif_template_path (str): the path of the provided exif set
    Returns:
        None
    """

    # TODO: DAI LA POSSIBILITà DI RITORNARE L'ERRORE SE IL PATH NON ESISTE
    if os.path.exists(images_folder):
        
        data_dict = choose_exif_template(exif_template_path)

        print(data_dict)
        
        if os.path.isdir(images_folder):
            for filename in os.listdir(images_folder):
                image_path = os.path.join(images_folder, filename)
                with ExifToolHelper() as et:
                    et.set_tags(image_path, data_dict)

                # che cosa fa questo check ???  cosa ritorna ??? 
                check_tags(image_path,data_dict)
                    
                    
                    
        elif os.path.isfile(images_folder):
            image_path = images_folder
            with ExifToolHelper() as et:
                et.set_tags(image_path, data_dict)
            check_tags(image_path,data_dict)    

        if os.path.isfile(images_folder):
            images_folder = os.path.dirname(images_folder)

        # commentino     
        remove_original(images_folder)
    
    # e se non esiste ??? 


         
    
    
    
