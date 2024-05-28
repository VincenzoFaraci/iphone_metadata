import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS
from metadata.iphone_metadata import Iphone,Exif_dataframe
from . import dataframe_f as dataframe




def extract_exif(image_path):
    try:
        image = Image.open(image_path) # usiamo la libreria Image per aprire l'immagine
        exif_data = image._getexif() # creiamo il dizionario con i dati exif dell'immagine
        if exif_data is not None:
            return {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
        else:
            return {}
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return {}



def get_filenames(image_folder, tot_images):
    lista_nomi = []
    count = 0
    for filename in os.listdir(image_folder):
        if count >= tot_images:
            break
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
            lista_nomi.append(filename)
            count += 1
    return lista_nomi



def clean_value(value):
    # Funzione per rimuovere caratteri non validi
    if isinstance(value, str):
        return ''.join(c for c in value if c.isprintable() and c not in ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x0b', '\x0c', '\x0e', '\x0f'))
    return value


def get_data(image_folder, tot_images,model_value: str):
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14"):
        print(f"siamo dentro il caso iphone ed infatti modello è {model_value}")
        iphone_metadata = Iphone(model_value)
        iphone_metadata.get_data(image_folder,tot_images,iphone_metadata.iphone_data)
        df_iphone = Exif_dataframe(iphone_metadata.iphone_data)
        df_iphone.set_dataframe()
    keys = ['filename', 'GPSInfo', 'ResolutionUnit', 'ExifOffset', 'Make', 'Model', 'Software', 'Orientation', 'DateTime', 
            'XResolution', 'YResolution', 'HostComputer', 'ExifVersion', 'ComponentsConfiguration', 'ShutterSpeedValue', 
            'DateTimeOriginal', 'DateTimeDigitized', 'ApertureValue', 'BrightnessValue', 'ExposureBiasValue', 
            'MeteringMode', 'Flash', 'FocalLength', 'ColorSpace', 'ExifImageWidth', 'DigitalZoomRatio', 
            'FocalLengthIn35mmFilm', 'SceneCaptureType', 'OffsetTime', 'OffsetTimeOriginal', 'OffsetTimeDigitized', 
            'SubsecTimeOriginal', 'SubjectLocation', 'SubsecTimeDigitized', 'ExifImageHeight', 'SensingMethod', 
            'ExposureTime', 'FNumber', 'SceneType', 'ExposureProgram', 'ISOSpeedRatings', 'ExposureMode', 
            'FlashPixVersion', 'WhiteBalance', 'LensSpecification', 'LensMake', 'LensModel', 'CompositeImage']

    dict_data = {key: [] for key in keys}

    count = 0
    for filename in os.listdir(image_folder):
        if count >= tot_images:
            break
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
            image_path = os.path.join(image_folder, filename)
            exif_data = extract_exif(image_path)
            dict_data['filename'].append(filename)
            for key in keys[1:]:  # Esclude 'filename' che è già stata aggiunta
                value = exif_data.get(key, None)
                clean_val = clean_value(value) if value is not None else None
                dict_data[key].append(clean_val)
            count += 1     
               
    dataframe.get_dataframe(dict_data)
    dataframe.get_filtered_dataframe(dict_data,model_value)

    #get the most common value for all the keys of the exif dict
    #get_most_common_all_keys(filtered_dict_data,df)
    





#INIZIAMO A FARE REFACTORING