import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS
from functions.extract_exif import get_data
from models.IphoneExifExtractor import IphoneExifExtractor

#selezionare il modello da analizzare
model_value = 'iPhone 14 Pro Max'


def get_images_exif(image_folder="data\\images", tot_images=40):
    get_data(image_folder, tot_images,model_value)
    
    
get_images_exif()

#ARGPARSE
#GESTIRE QUANDO DIAMO IN INPUT IL PATH DI UN SOLO FILE
#GESTIRE QUANDO VIENE PASSATA LA CARTELLA CON TUTTE LE IMMAGINI
#DOCSTRING DA FARE IN TUTTE LE FUNZIONI
    
    
    
    
    
    
    
    





