import os
from exiftool import ExifToolHelper


class Exif_extractor():
    # TODO: DESCRIZIONE DELLA CLASSE
    def __clean_value(self,value):
        """
        Cleans the given value by removing invalid characters.
        This function is called for every value in the dictonary in order to avoid problems
        TODO: specifica meglio caso int/str

        Args:
            value (str or int): The value to clean.

        Returns:
            str: The cleaned value.
        """
        # TODO: questa funzione serve ancora???
        if isinstance(value, str):
            return ''.join(c for c in value if c.isprintable() and c not in ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x0b', '\x0c', '\x0e', '\x0f'))
        return value
    
    def __fix_dict(self, dictionary: dict):
        """
        Removes duplicate keys from the dictionary based on their suffixes.

        This method iterates over the keys of the provided dictionary and removes
        keys that have the same suffix (the part after the ':'). If multiple keys
        share the same suffix, only the first key encountered is kept, and the 
        others are removed.

        Args:
            dictionary (dict): The dictionary from which duplicate keys based on 
                            their suffixes will be removed.
        """
        seen_suffixes = set()
        keys_to_remove = []

        for key in dictionary.keys():
            suffix = key.split(':')[-1]
            if suffix in seen_suffixes:
                keys_to_remove.append(key)
            else:
                seen_suffixes.add(suffix)

        for key in keys_to_remove:
            del dictionary[key]

    
    def __set_dict_data(self, image_path:str, dict_data: dict, model_value: str = None):
        """
        Populate a dictionary with EXIF data from an image.

        This method extracts EXIF data from the specified image and appends the values to 
        the provided dictionary. If a model value is specified, it filters the metadata 
        by the given model value before appending.

        Args:
            image_path (str): The path to the image file.
            dict_data (dict): The dictionary to populate with EXIF data.
            model_value (str, optional): The EXIF model value to filter the images. 
                                        If not provided, all EXIF data will be added.
        
        Returns:
            None
        """
        with ExifToolHelper() as et:
            if model_value is not None:
                model_tag = et.get_tags(image_path, "EXIF:Model")
                if model_tag and "EXIF:Model" in model_tag[0]:
                    model_tag = model_tag[0]["EXIF:Model"]
                    if model_tag == model_value:
                        for data in et.get_metadata(image_path):
                            self.__fix_dict(data)
                            for key in dict_data.keys():
                                value = data.get(key, None)
                                if key in dict_data:
                                    clean_val = self.__clean_value(value)
                                    dict_data[key].append(clean_val)   
            else:
                for data in et.get_metadata(image_path):
                    self.__fix_dict(data)
                    for key in dict_data.keys():
                        value = data.get(key, None)
                        if key in dict_data:
                            clean_val = self.__clean_value(value)
                            dict_data[key].append(clean_val)
    
    
    
    def __extract_exif(self, image_folder, dict_data: dict, model_value: str = None, tot_images=None):
        """
        Extract EXIF data from images in the specified folder.

        This method iterates over the images in the specified folder to extract their 
        metadata (EXIF data). It populates a provided dictionary with the extracted data, 
        optionally filtering by a specific model value and limiting the number of images processed.

        Args:
            image_folder (str): The path to the folder containing the images.
            dict_data (dict): The dictionary to populate with EXIF data.
            model_value (str, optional): The EXIF model value to filter the images.
                                        If not provided, all EXIF data will be added.
            tot_images (int, optional): The total number of images to process. If not provided, 
                                        all images in the folder will be processed.

        Returns:
            dict: A dictionary containing the extracted and filtered EXIF metadata from the images.
        """
        print("prova")
        if tot_images is not None:
            count = 0
            for filename in os.listdir(image_folder):
                if count >= tot_images:
                    break
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff',".heic")):
                    image_path = os.path.join(image_folder, filename)
                    self.__set_dict_data(image_path,dict_data,model_value)     
                count += 1      
        else:
            for filename in os.listdir(image_folder):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff',".heic")):
                    image_path = os.path.join(image_folder, filename)
                    print(f"{image_path},{model_value}")
                    self.__set_dict_data(image_path,dict_data,model_value)
        return dict_data
    
    # def __fix_data(self,dict_data: str):
    #     """
    #     Fix the lists of dict_data
        
    #     Args:
    #         dict_data (dict): The dictionary containing the EXIF data.
        
    #     """
    #     max_length = max(len(v) for v in dict_data.values()) 
    #     for key in dict_data:
    #         while len(dict_data[key]) < max_length:
    #             dict_data[key].append(None)
    
    
    def set_data(self, image_folder, dict_data: dict, model_value: str = None, tot_images=None):
        """
        Extracts EXIF data from images in the provided folder.

        Args:
            image_folder (str): The path to the folder containing the images.
            dict_data (dict): The dictionary to populate with the extracted EXIF data.
            model_value (str): The model value to filter by.
            tot_images (int, optional): Total number of images to analyze. Defaults to None.

        Returns:
            dict: The filtered dictionary data.
        """
        
        return self.__extract_exif(image_folder,dict_data,model_value,tot_images)
    
    