import os
from PIL import Image
import pandas as pd
#from metadata import iphone_metadata as im

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
smc_folder = os.path.join(root_dir, 'smc')


def get_dataframe(dict_data:dict):
    df = pd.DataFrame(dict_data)
    output_excel = os.path.join(smc_folder, 'output_excel.xlsx')
    df.to_excel(output_excel, index=False)
    

def get_filtered_dataframe(dict_data:dict, model_value:str):
    df_filtered = pd.DataFrame(dict_data)
    filtered_dict_data = filter_dict_by_model(dict_data, model_value)
    df_filtered = pd.DataFrame(filtered_dict_data)
    
    
    output_excel_filtered = os.path.join(smc_folder, 'output_excel_filtered.xlsx')
    df_filtered.to_excel(output_excel_filtered, index = False)
    
    
# Esempio di utilizzo
def get_most_common(key_name:str,df: pd.DataFrame):
    if key_name in df.columns:
        counts = df[key_name].value_counts()
        most_common= counts.idxmax()
        most_common_count = counts.max()
        print(f"{key_name},Valore:{most_common}, Totale:{most_common_count}")
    else:
        print(f"No {key_name} data available in EXIF.")

  
def get_most_common_all_keys(dict:dict,df: pd.DataFrame):
    for key in dict:
        if key not in ('filename', 'GPSInfo'):
            get_most_common(key,df)
            
            
def filter_dict_by_model(dict_data, model_value):
    # Trova gli indici in cui il valore di 'Model' è uguale a model_value
    indices_to_keep = [i for i, model in enumerate(dict_data['Model']) if model == model_value]
    print(indices_to_keep)

    # Crea un nuovo dizionario con solo i valori corrispondenti agli indici trovati
    filtered_dict = {key: [value[i] for i in indices_to_keep] for key, value in dict_data.items()}

    return filtered_dict