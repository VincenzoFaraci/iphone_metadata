import os
import json


from classes.ExifDataframe import ExifDataframe

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')



def save_exif_dataframe(dict_data:dict):
    exif_df = ExifDataframe(dict_data)
    exif_df.df_to_excel()
    exif_df.df_to_excel() # 2 volte
    
def save_exif_json(dict_data:dict):
    output_json = os.path.join(output_folder, 'image_exif.json')
    with open(output_json, 'w') as f:
        json.dump(dict_data, f, indent=4)
