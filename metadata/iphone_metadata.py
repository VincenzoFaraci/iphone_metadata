#DEFINIAMO LA CLASSE IPHONE METADATA
#OPPURE DEFINIAMO TUTTE LE CLASSI?
import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS, GPSTAGS

class Exif_metadata():
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
        
    def clean_value(self,value):
    # Funzione per rimuovere caratteri non validi
        if isinstance(value, str):
            return ''.join(c for c in value if c.isprintable() and c not in ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x0b', '\x0c', '\x0e', '\x0f'))
        return value
    
    def filter_dict_by_model(self,dict_data, model_value):
    # Trova gli indici in cui il valore di 'Model' è uguale a model_value
        #print(dict_data)
        indices_to_keep = [i for i, model in enumerate(dict_data['Model']) if model is not None and model in model_value]
        print("Banana",indices_to_keep)
        # Crea un nuovo dizionario con solo i valori corrispondenti agli indici trovati
        filtered_dict = {key: [value[i] for i in indices_to_keep] for key, value in dict_data.items()}
        #print(filtered_dict) qua ci siamo
        return filtered_dict
    
    def get_data(self,image_folder, tot_images,dict_data:dict,model_value:str):
        count = 0
        for filename in os.listdir(image_folder):
            if count >= tot_images:
                break
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                image_path = os.path.join(image_folder, filename)
                exif_data = self.extract_exif(image_path)
                dict_data['filename'].append(filename)
                for key in dict_data.keys():  # Usa le chiavi del dizionario esistenti
                    if key != 'filename':
                        value = exif_data.get(key, None)
                        clean_val = self.clean_value(value) if value is not None else None
                        dict_data[key].append(clean_val)
                count += 1
        filtered_dict_data = self.filter_dict_by_model(dict_data,model_value)
        #print(filtered_dict_data) qua ci siamo
        return filtered_dict_data

class Exif_dataframe():
    #creiamo la classe del dataframe, ma è utile? Direi di si perchè così gestiamo solo una classe
    #Ricorda, tutto quello che deve essere ripetuto è meglio astrarlo e farlo diventare classe in mod da gestirlo una volta sola
    def __init__(self,dict_data:dict):
        self.df = pd.DataFrame(dict_data)
    
    def get_dataframe(self,dict_data:dict):
        return self.df
    
    def set_dataframe(self):
        self.df.to_excel('output_excel_refactoring.xlsx', index=False)
    
    def get_most_common(self,key_name:str,df: pd.DataFrame):
        if key_name in df.columns:
            counts = df[key_name].value_counts()
            most_common= counts.idxmax()
            most_common_count = counts.max()
            print(f"{key_name},Valore:{most_common}, Totale:{most_common_count}")
        else:
            print(f"No {key_name} data available in EXIF.")
    
    def get_most_common_all_keys(self,dict:dict,df: pd.DataFrame):
        for key in dict:
            if key not in ('filename', 'GPSInfo'):
                self.get_most_common(key,df)  
    
    """def df_to_excel(self):
        self.df.to_excel('output_excel.xlsx', index=False)"""


class Iphone(Exif_metadata):
    def __init__(self,model_value:str):
        self.model_value = model_value
        self.keys = ['filename', 'GPSInfo', 'ResolutionUnit', 'ExifOffset', 'Make', 'Model', 'Software', 'Orientation', 'DateTime', 
            'XResolution', 'YResolution', 'HostComputer', 'ExifVersion', 'ComponentsConfiguration', 'ShutterSpeedValue', 
            'DateTimeOriginal', 'DateTimeDigitized', 'ApertureValue', 'BrightnessValue', 'ExposureBiasValue', 
            'MeteringMode', 'Flash', 'FocalLength', 'ColorSpace', 'ExifImageWidth', 'DigitalZoomRatio', 
            'FocalLengthIn35mmFilm', 'SceneCaptureType', 'OffsetTime', 'OffsetTimeOriginal', 'OffsetTimeDigitized', 
            'SubsecTimeOriginal', 'SubjectLocation', 'SubsecTimeDigitized', 'ExifImageHeight', 'SensingMethod', 
            'ExposureTime', 'FNumber', 'SceneType', 'ExposureProgram', 'ISOSpeedRatings', 'ExposureMode', 
            'FlashPixVersion', 'WhiteBalance', 'LensSpecification', 'LensMake', 'LensModel', 'CompositeImage']
        self.iphone_data = {key: [] for key in self.keys}
    
    def get_data(self, image_folder, tot_images, dict_data: dict):
        #print(super().get_data(image_folder, tot_images, self.iphone_data,self.model_value)) #se la chiamo di nuovo mi stampa tutte le cose nuovamente
        """print("vedi qui")
        self.stampa()"""
        self.iphone_data =  super().get_data(image_folder, tot_images, self.iphone_data,self.model_value)
        #self.stampa()
    
    def stampa(self):
        print(self.iphone_data)
    #e fino a qui
    

class Stampa():
    
    pass