import json
from models.ExifDataframe import Exif_dataframe


def save_exif_dataframe(dict_data:dict):
    exif_df = Exif_dataframe(dict_data)
    exif_df.df_to_excel()
    exif_df.df_to_excel()
