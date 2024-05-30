from functions.extract_exif import get_data
import argparse

#selezionare il modello da analizzare

parser = argparse.ArgumentParser(description="Prima prova di argparse")

parser.add_argument('images_folder', help='La cartella contente le immagini')
#parser.add_argument('output_file', help='Il file dove salvare i risultati')
parser.add_argument("--tot_images", type = int, help="Totale di immagini da voler analizzare")
parser.add_argument("--model_value", type = str, help="Modello da voler analizzare")

args = parser.parse_args()

model_value = args.model_value


def get_images_exif(image_folder=args.images_folder, tot_images = None):
    get_data(image_folder,model_value,tot_images)
    """if tot_images is None:
        get_data(image_folder,model_value)
    else:
        get_data(image_folder,model_value,tot_images)"""
    
if args.tot_images:
    get_images_exif(tot_images=args.tot_images)    
else:
    get_images_exif()
    
print("Il file è nella cartella output")


#RENDERE OPZIONALE LA FILTRAZIONE DEL MODELLO
#ARGPARSE
#RENDERE OPZIONAL IL NUMERO DI IMMAGINI DA VOLER ANALIZZARE E ANCHE IL MODELLO
#GESTIRE QUANDO DIAMO IN INPUT IL PATH DI UN SOLO FILE
#GESTIRE QUANDO VIENE PASSATA LA CARTELLA CON TUTTE LE IMMAGINI
#DOCSTRING DA FARE IN TUTTE LE FUNZIONI
    
    
    
    
    
    
    
    





