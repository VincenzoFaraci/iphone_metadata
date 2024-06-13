import os
import pandas as pd

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')


class Exif_dataframe():
    def __init__(self,dict_data:dict):
        self.df = pd.DataFrame(dict_data)
             
    def get_dataframe(self):
        return self.df
    
    
    def df_to_excel(self):
        output_excel = os.path.join(output_folder, 'output_excel.xlsx')
        self.df.to_excel(output_excel, index=False)
        
    def df_to_csv(self):
        output_csv = os.path.join(output_folder, 'output_csv.xlsx')
        self.df.to_csv(output_csv, index=False)
    
    
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
    