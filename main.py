import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS

def extract_exif(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is not None:
            return {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
        else:
            return {}
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return {}

# Percorso relativo alla cartella delle immagini
image_folder = os.path.join(os.path.dirname(__file__), 'images')

# Numero massimo di immagini da processare
max_images = 1

# Inizializza una lista per conservare i dati EXIF
exif_list = []

# Contatore per tracciare il numero di immagini processate
count = 0

# Leggi tutte le immagini nella cartella e estrai i dati EXIF
for filename in os.listdir(image_folder):
    if count >= max_images:
        break
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
        image_path = os.path.join(image_folder, filename)
        exif_data = extract_exif(image_path)
        print(exif_data)
        exif_data['filename'] = filename  # Aggiungi il nome del file ai dati EXIF
        exif_list.append(exif_data)
        count += 1

# Crea un DataFrame di pandas con i dati EXIF
df = pd.DataFrame(exif_list)

# Visualizza le prime righe del DataFrame
print(df.head())

# Salva il DataFrame in un file CSV
output_csv = os.path.join(os.path.dirname(__file__), 'exif_data.csv')
df.to_csv(output_csv, index=False)

print(f"I dati EXIF sono stati salvati in {output_csv}")

# Analisi dei dati EXIF
# Ad esempio, possiamo contare il numero di immagini per ogni modello di fotocamera
if 'Model' in df.columns:
    camera_model_counts = df['Model'].value_counts()
    print(camera_model_counts)
else:
    print("No 'Model' data available in EXIF.")
    
# Trasponi il DataFrame
df_transposed = df.transpose()

# Salva il DataFrame trasposto in un file CSV
output_csv_transposed = os.path.join(os.path.dirname(__file__), 'exif_data_transposed.csv')
df_transposed.to_csv(output_csv_transposed, header=False)

print(f"I dati EXIF sono stati salvati in {output_csv_transposed}")
    
    
    
    
    
    
    
    
    
    





