import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS, GPSTAGS
#from metadata import iphone_metadata as im
from metadata.iphone_metadata import Iphone,Exif_dataframe


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

def filter_dict_by_model(dict_data, model_value):
    # Trova gli indici in cui il valore di 'Model' è uguale a model_value
    indices_to_keep = [i for i, model in enumerate(dict_data['Model']) if model == model_value]

    # Crea un nuovo dizionario con solo i valori corrispondenti agli indici trovati
    filtered_dict = {key: [value[i] for i in indices_to_keep] for key, value in dict_data.items()}

    return filtered_dict

def get_data(image_folder, tot_images,model_value: str):
    if model_value in ("iPhone 14 Pro","iPhone 14 Pro Max","iPhone 14"):
        print(f"siamo dentro il caso iphone ed infatti modello è {model_value}")
        iphone_metadata = Iphone(model_value)
        #iphone_metadata.stampa()
        iphone_metadata.get_data(image_folder,tot_images,iphone_metadata.iphone_data)
        #iphone_metadata.stampa()
        df_iphone = Exif_dataframe(iphone_metadata.iphone_data)
        df_iphone.set_dataframe()
        print("SE VABBè")
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

    # Aggiungi valori None per le chiavi mancanti
    max_length = max(len(v) for v in dict_data.values())
    for key in dict_data:
        while len(dict_data[key]) < max_length:
            dict_data[key].append(None)

    model_value = 'iPhone 14 Pro Max'
    filtered_dict_data = filter_dict_by_model(dict_data, model_value)
    
    df = pd.DataFrame(dict_data)
    #df = pd.DataFrame(filtered_dict_data)
    
    output_csv = os.path.join(os.path.dirname(__file__), 'exif_data.csv')
    df.to_csv(output_csv, index=False)
    df.to_excel('output_excel.xlsx', index=False)

    #get the most common value for all the keys of the exif dict
    #get_most_common_all_keys(filtered_dict_data,df)
    

# Esempio di utilizzo
def get_most_common(key_name:str,df: pd.DataFrame):
    if key_name in df.columns:
        counts = df[key_name].value_counts()
        most_common= counts.idxmax()
        most_common_count = counts.max()
        print(f"{key_name},Valore:{most_common}, Totale:{most_common_count}")
    else:
        print(f"No {key_name} data available in EXIF.")
    
def get_most_common_all_keys(dict:dict,df: pd.DataFrame):
    for key in dict:
        if key not in ('filename', 'GPSInfo'):
            get_most_common(key,df)



#INIZIAMO A FARE REFACTORING