import exiftool

# Specifica il percorso completo di exiftool.exe
import os
from exiftool import ExifToolHelper


file = "data\\iphone_images\\01.jpg"
print(type(file),file)
lista_chiavi = []
with ExifToolHelper() as et:
    for d in et.get_metadata(file):
        for k, v in d.items():
            #print(type(k),k)
            tmp = k.split(":")
            k = tmp[-1]
            lista_chiavi.append(k)
            #print(tmp,k)
            #print(type(d))
            #print(f"{k} = {v}")
#print(lista_chiavi)

