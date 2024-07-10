import os

from exiftool import ExifTool


def remove_exif(image_path):
    """
    Remove EXIF data for the provided image file.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        None
    """ 
    with ExifTool() as e:
        e.execute(b'-all=', image_path.encode())


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
