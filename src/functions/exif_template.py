
#Prima di tutto dobbiamo chiederci, quali sono i dati exif che vogliamo cambiare in una immagine e quali vogliamo restino intatti?
# Una cosa comoda dei tag di exiftool è quello di raggruppare i dati in base alla categoria,
#Ci sono diverse categorie come ad esempio:



#Cosa sono le cose da tenere in considerazione per creare dei template?
#Potremmo diversificare sicuramente il modello e la versione del software

#Quale formato dovremmo scegliere? Ogni formato ha una tabella exif diversa(ovviamente cambiano solo alcuni dati), ad esempio tra heic e jpeg quale scegliere?


import json

import_json_path = "src\models\exif_template.json"

# Open the JSON file and load its content
with open(import_json_path, 'r') as file:
    data_dict = json.load(file)

# Print the dictionary to verify its content
print(data_dict)

def choose_exif():
    pass