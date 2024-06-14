import os
import pandas as pd

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
output_folder = os.path.join(root_dir, 'output')


class ExifDataframe:
    """
    A class to handle operations on pandas DataFrame containing EXIF data.

    This class initializes with a dictionary of EXIF data and converts it into 
    a pandas DataFrame. It provides methods to manipulate and export the DataFrame 
    to Excel or CSV formats, as well as to retrieve the most common values for 
    specified keys within the DataFrame.

    """

    def __init__(self, dict_data: dict):
        """
        Initializes the Exif_dataframe object with a dictionary of EXIF data.
        
        Args:
            dict_data (dict): The dictionary containing EXIF data.
        """
        self.df = pd.DataFrame(dict_data)
             
    def get_dataframe(self):
        """
        Returns the underlying pandas DataFrame containing EXIF data.
        
        Returns:
            pd.DataFrame: The DataFrame containing EXIF data.
        """
        return self.df
    
    def df_to_excel(self):
        """
        Saves the DataFrame to an Excel file in the 'output' folder.
        """
        output_excel = os.path.join(output_folder, 'output_excel.xlsx')
        self.df.to_excel(output_excel, index=False)
        
    def df_to_csv(self):
        """
        Saves the DataFrame to a CSV file in the 'output' folder.
        """
        output_csv = os.path.join(output_folder, 'output_csv.csv')
        self.df.to_csv(output_csv, index=False)
    
    def get_most_common(self, key_name: str, df: pd.DataFrame):
        """
        Retrieves the most common value and its count for a specified key within the DataFrame.
        
        Args:
            key_name (str): The name of the key for which to find the most common value.
            df (pd.DataFrame): The DataFrame containing EXIF data.
        """
        if key_name in df.columns:
            counts = df[key_name].value_counts()
            most_common = counts.idxmax()
            most_common_count = counts.max()
            print(f"{key_name}, Value: {most_common}, Total: {most_common_count}")
        else:
            print(f"No {key_name} data available in EXIF.")
    
    def get_most_common_all_keys(self, dict_data: dict, df: pd.DataFrame):
        """
        Iterates over keys in the provided dictionary and retrieves the most common 
        value and its count for each key in the DataFrame, excluding 'filename' and 'GPSInfo'.
        
        Args:
            dict_data (dict): The dictionary containing keys for which to find the most common values.
            df (pd.DataFrame): The DataFrame containing EXIF data.
        """
        for key in dict_data:
            if key not in ('filename', 'GPSInfo'):
                self.get_most_common(key, df) 
    