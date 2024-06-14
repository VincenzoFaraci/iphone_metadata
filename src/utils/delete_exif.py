import json
import os

from exiftool import ExifToolHelper,ExifTool


root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')


def remove_exif(image_path):
    """
    Remove EXIF data for the provided image file.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        None
    """ 
    with ExifTool() as e:
        e.execute(f'-all=', image_path.encode())

    image_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys():
                value = data.get(key, None)
                key = key.split(":")[-1]
                image_exif[key] = value
                
    output_json = os.path.join(output_folder, 'image_without_exif.json')
    with open(output_json, 'w') as f:
        json.dump(image_exif, f, indent=4)


def remove_multiple_exif(image_folder):
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
            image_path = os.path.join(image_folder, filename)
            with ExifTool() as e:
                e.execute(f'-all=', image_path.encode())
