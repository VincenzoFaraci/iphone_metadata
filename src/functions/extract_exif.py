import os
from models.IphoneExifExtractor import IphoneExifExtractor
from models.ExifDataframe import Exif_dataframe

def get_data(image_folder, tot_images,model_value: str):
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14"):
        print(f"siamo dentro il caso iphone ed infatti modello è {model_value}")
        iphone_metadata = IphoneExifExtractor(model_value)
        iphone_metadata.get_data(image_folder,tot_images)
        df_iphone = Exif_dataframe(iphone_metadata.iphone_data)
        df_iphone.df_to_excel()
    return 