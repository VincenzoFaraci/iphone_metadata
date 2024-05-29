#Cosa fa questa classe?


#CLASSE DA CANCELLARE ESSENDO NON UTILIZZATA



import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS, GPSTAGS

#questa classe a cosa serve? Serve a iterare la cartella delle immagini
#Il nostro scopo è quello di passare a exif_extractor il path di una sola immagine
class Images_iterator():
    def __init__(self,image_folder):
        self.filename_list = []
        self.image_folder = image_folder
    #creare una funzione che preso il path della cartella restituisce il path di una immagine
    
    #forse è meglio creare una funzione che restituisce il path in base al nome della foto
# se ad esempio faccio un alista con tutti i filename posso poi restituire il path di ogni singola foto?
    def set_list_filename(self):
        #filename_list = []     
        for filename in os.listdir(self.image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                self.filename_list.append(filename)
    #ma questa funziona è inutile? Sembrerebbe di si
    
    
   #ora posso creare una funzione che restituisce il path
   #Devo capire questo, io voglio poter dare il nome già in input oppure ho comunque una cartella?
    def get_path(image_folder):
        pass
        #image_path = 
    pass


