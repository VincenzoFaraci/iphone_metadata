import os
import json

from classes.ExifDataframe import ExifDataframe

def save_exif_dataframe(dict_data:dict, output_folder_path):
    exif_df = ExifDataframe(dict_data,output_folder_path)
    exif_df.df_to_csv() 
    exif_df.df_to_excel()
    
def save_exif_json(dict_data:dict, image_path:str, output_folder_path):
    filename = os.path.basename(image_path)
    filename_without_ext = os.path.splitext(filename)[0]
    print(filename)
    output_json = os.path.join(output_folder_path, f'{filename_without_ext}.json')
    
    with open(output_json, 'w') as f:
        json.dump(dict_data, f, indent=4)
