import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS, GPSTAGS



class Exif_extractor():
    def __clean_value(self,value):
    # Funzione per rimuovere caratteri non validi
        if isinstance(value, str):
            return ''.join(c for c in value if c.isprintable() and c not in ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x0b', '\x0c', '\x0e', '\x0f'))
        return value
    
    def __filter_dict_by_model(self,dict_data, model_value):
    # Trova gli indici in cui il valore di 'Model' è uguale a model_value
        indices_to_keep = [i for i, model in enumerate(dict_data['Model']) if model is not None and model in model_value]
        # Crea un nuovo dizionario con solo i valori corrispondenti agli indici trovati
        filtered_dict = {key: [value[i] for i in indices_to_keep] for key, value in dict_data.items()}
        return filtered_dict
    
    def extract_exif(self,image_path):
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
        
    
    
    def get_data(self,image_folder, tot_images,dict_data:dict,model_value:str):
        print("dentro il get data generale",tot_images)
        count = 0
        images_list = []
        images_list.extend(dict_data.keys())
        images_list.remove("filename")
        for filename in os.listdir(image_folder):
            if count >= tot_images:
                break
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                image_path = os.path.join(image_folder, filename)
                exif_data = self.extract_exif(image_path)
                dict_data['filename'].append(filename)
                """for key in dict_data.keys():  # Usa le chiavi del dizionario esistenti
                    if key != 'filename': #da ottimizzare
                        value = exif_data.get(key, None)
                        clean_val = self.__clean_value(value) if value is not None else None
                        dict_data[key].append(clean_val)"""
                for key in images_list: 
                    value = exif_data.get(key, None)
                    clean_val = self.__clean_value(value) if value is not None else None
                    dict_data[key].append(clean_val)
                count += 1
        filtered_dict_data = self.__filter_dict_by_model(dict_data,model_value)
        return filtered_dict_data
    
    