import os

from exiftool import ExifTool


def remove_original(folder_path):
    """
    Remove file ending with jpg_original
    
    Input:
        folder_path: The path to the folder where files jpg_original are stored
    Output:
        None
    """
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg_original'):
            os.remove(os.path.join(folder_path, filename))

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
 
    image_dir_path = os.path.dirname(image_path)    
    remove_original(image_dir_path)


def remove_multiple_exif(image_folder_path):
    """
    Remove EXIF data for all the provided image file in the folder.
    
    Args:
        image_folder_path (str): The path to the image file.
        
    Returns:
        None
    """
    for filename in os.listdir(image_folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
            image_path = os.path.join(image_folder_path, filename)
            with ExifTool() as e:
                e.execute(f'-all=', image_path.encode())
    remove_original(image_folder_path)
