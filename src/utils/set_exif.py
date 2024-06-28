import json
import os

from exiftool import ExifToolHelper,ExifTool

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
default_image_path = os.path.join(root_dir, 'src' , 'models', 'default_image.jpeg')


# CHANGING File:Directory TAG RISE AN ERROR, BUT THE DIRECTORY IS STILL CHANGED


root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
#output_folder = os.path.join(root_dir, 'output')

def icc_set(icc_source_image, icc_dest_image):
    """
    Copy ICC_Profile from one image to another.
    Args:
        icc_source_image (str): The path to the image used to extract the ICC profile..
        icc_dest_image (str): The path to the image we want to overwrite
    Returns:
        None
    
    """
    with ExifTool() as et:
        et.execute(b"-TagsFromFile", icc_source_image ,b"-icc_profile", icc_dest_image)
     

def choose_exif_template(exif_template_path:str = None):
    """
    Return the EXIF model to be used, 
    whether it is the standard one or the user-provided one.
    
    Args:
        exif_template_path (str): The path to the exif template.
        exif_template_path (str): the path of the provided exif set
    Returns:
        dict : dictionary to use as exif template
    """
    if exif_template_path is None:
        print("Default Exif set has been used since no Exif model was provided.")
        default_exif_set_path = os.path.join(root_dir, 'src' , 'models', 'exif_template.json')
        with open(default_exif_set_path, 'r') as file:
            default_exif_set = json.load(file)
        return default_exif_set
    else:
        print("The provided Exif set has been used")
        with open(exif_template_path, 'r') as file:
            data_dict = json.load(file)
    return data_dict



def remove_original(folder_path):
    """
    Remove file ending with jpg_original
    
    Input:
        folder_path: The path to the folder where files jpg_original are stored
    Output:
        None
    """
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg_original','.jpeg_original'):
            os.remove(os.path.join(folder_path, filename))

      
def set_exif_tags(images_folder: str,icc_profile_path: str,image_template_path: str = None,exif_template_path:str = None):
    """
    Set EXIF data for all the image files in the specified folder.

    Args:
        images_folder (str): The path to the folder containing the image files.
        icc_profile_path (str): The path to the image used to extract the ICC profile.
        exif_template_path (str): The path to the provided EXIF data template.

    Returns:
        None
    """
    if os.path.exists(images_folder):
        
        data_dict = choose_exif_template(exif_template_path)

        if os.path.isdir(images_folder):
            tmp_dict = {}
            for filename in os.listdir(images_folder):
                image_path = os.path.join(images_folder, filename)
                print(f"We're working with this file: {image_path}")
                with ExifToolHelper() as et:
                    for key, value in data_dict.items():
                        tmp_dict[key] = value
                        try:
                            et.set_tags(image_path, tmp_dict)
                            print("Added",tmp_dict)
                        except Exception as e:
                            print("Not added",tmp_dict, str(e))
                        tmp_dict = {}
                if icc_profile_path is None:
                    icc_set(default_image_path,image_path)
                else:
                    icc_set(icc_profile_path,image_path)    
            remove_original(images_folder)  
                         
        elif os.path.isfile(images_folder):
            image_path = images_folder
            
            if image_template_path is not None:
                print("We're using the template image to copy his exif")
                with ExifTool() as et:
                    et.execute(b"-tagsfromfile", image_template_path, b"-exif:all", "--subifd:all", image_path)
                icc_set(image_template_path,image_path)
            else:
                tmp_dict = {}
                with ExifToolHelper() as et:
                    for key, value in data_dict.items():
                        tmp_dict[key] = value
                        try:
                            et.set_tags(image_path, tmp_dict)
                            print("Added",tmp_dict)
                        except Exception as e:
                            print("Not added",tmp_dict, str(e))
                        tmp_dict = {}
                        
                if icc_profile_path is None:
                    icc_set(default_image_path,image_path)
                else:
                    icc_set(icc_profile_path,image_path) 
            
    else:
        raise Exception(f"The provided path: {images_folder} does not exist")


         
    
    
    
