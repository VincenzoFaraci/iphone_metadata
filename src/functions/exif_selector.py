#in this file we should create functions that we use to select a set of exif for a exif-less image

#we should start veryfing that an image without exif can be overwritten with a provided set of exif

from PIL import Image
from PIL.ExifTags import TAGS
from .modelli_exif_da_usare import dict_da_usare

def aggiungi_exif(image_path):
    try:
        #print("Dict da usare",dict_da_usare)
        image = Image.open(image_path)
        exif_data = image._getexif()
        print("Exif prima",exif_data)
        if exif_data is None:
            exif_data = {}
        
        # Aggiungi o sovrascrivi i tag EXIF con quelli forniti nel dizionario dict_da_usare
        for key, value in dict_da_usare.items():
            print("key,value",key,value)
            # Converti il nome del tag in un ID valido di EXIF
            tag_id = TAGS.get(key)
            print("tag id",tag_id)
            if tag_id is not None:
                print("qui dentro")
                exif_data[key] = value
        print("prima del salvataggio")
        print("Exif dopo",exif_data)
        # Salva i nuovi dati EXIF nell'immagine
        image.save(image_path, exif=image.info['exif'])
        print("Exif dopo",exif_data)
        return "Dati EXIF aggiunti con successo."

    except Exception as e:
        print(f"Errore durante l'aggiunta dei dati EXIF a {image_path}: {e}")
        return "Errore durante l'aggiunta dei dati EXIF."
