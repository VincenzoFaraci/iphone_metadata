from classes.ExifExtractor import ExifExtractor
from classes.IphoneExifExtractor import IphoneExifExtractor

from exiftool import ExifToolHelper 
from models.exif_models import iphone_exif_key



def get_folder_data(image_folder,model_value: str = None, tot_images = None):
    """
    Extracts EXIF data from images in the provided folder.
    
    Args:
        image_folder (str): The path to the folder containing the images.
        model_value (str, optional): The model to analyze.
        tot_images (int, optional): Total number of images to analyze. Defaults to None.
        
    Returns: ??????????????????
        None
    """
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14","iPhone 15"):
        print(f"Provided model = {model_value}")
        iphone_metadata = IphoneExifExtractor(model_value)
        iphone_metadata.set_data(image_folder,tot_images)
        dict_data = iphone_metadata.get_data()
        return dict_data
    elif model_value is None:
        print(f"Provided model = {model_value}") # print unica
        key_dictionary = iphone_exif_key #change to generic_exif_key to be more generic
        dictionary = {key: [] for key in key_dictionary} # usa iphone_exif_key
        extractor = ExifExtractor()
        exif_metadata = extractor.set_data(image_folder,dictionary,model_value,tot_images)
        #### set e non get ???????????
        # non sono consistenti
        return exif_metadata 
    else:
        print("Coming soon")
        # TODO: raise an Exception o return None, meglio eccezione 

def get_image_data(image_path):
    """
    Extracts EXIF data from the provided image file.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns: ??????????????????
        None
    """

    # TODO: VEDI MEGLIO
    image_exif = {}
    prova_interna_exif = {}
    with ExifToolHelper() as et:
        for data in et.get_metadata(image_path):
            for key in data.keys(): # for key, value in data.items():
                value = data.get(key, None)
                prova_interna_exif[key] = value # Non la usi
                #key = key.split(":")[-1] #change the format of exif tags
                image_exif[key] = value
    return image_exif  

    
