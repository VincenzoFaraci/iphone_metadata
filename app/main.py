import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS
from functions.extract_exif import get_data

#selezionare il modello da analizzare
model_value = 'iPhone 14 Pro Max'


def get_images_exif(image_path="data\images", tot_images=1000):
    print("prova")
    get_data(image_path, tot_images,model_value)

get_images_exif()

    
    
    
    
    
    
    
    
    
    





