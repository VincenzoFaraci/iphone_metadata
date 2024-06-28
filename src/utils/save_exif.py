import os
import json

from classes.ExifDataframe import ExifDataframe

def save_exif_dataframe(dict_data:dict, output_folder_path):
    exif_df = ExifDataframe(dict_data,output_folder_path)
    exif_df.df_to_excel()
    exif_df.df_to_csv() 
    
def save_exif_json(dict_data:dict, output_folder_path):
    output_json = os.path.join(output_folder_path, 'image_exif.json')
    with open(output_json, 'w') as f:
        json.dump(dict_data, f, indent=4)
