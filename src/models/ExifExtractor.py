import os
from PIL import Image,TiffImagePlugin
from PIL.ExifTags import TAGS, GPSTAGS



class Exif_extractor():
    def __clean_value(self,value):
        """
        Cleans the given value by removing invalid characters.

        Args:
            value: The value to clean.

        Returns:
            str: The cleaned value.
        """
        if isinstance(value, str):
            return ''.join(c for c in value if c.isprintable() and c not in ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x0b', '\x0c', '\x0e', '\x0f'))
        return value
    
    def __filter_dict_by_model(self,dict_data, model_value):
        """
        Filters the dictionary data by model value.

        Args:
            dict_data (dict): The dictionary containing the EXIF data.
            model_value (str): The model value to filter by.

        Returns:
            dict: The filtered dictionary data.
        """
        indices_to_keep = [i for i, model in enumerate(dict_data['Model']) if model is not None and model == model_value] #CHANGE == TO in 
        filtered_dict = {key: [value[i] for i in indices_to_keep] for key, value in dict_data.items()}
        return filtered_dict
    
    def extract_exif(self,image_path):
        """
        Extracts EXIF data from the provided image file.

        Args:
            image_path (str): The path to the image file.

        Returns:
            dict: A dictionary containing the extracted EXIF data.
        """
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
        
    def get_image_data(self, image_path, dict_data:dict):
        """
        Updates the provided dictionary data with EXIF data from the image file.

        Args:
            image_path (str): The path to the image file.
            dict_data (dict): The dictionary containing the EXIF data to update.

        Returns:
            dict: The updated dictionary data.
        """
        exif_data = self.extract_exif(image_path)
        for key in dict_data.keys(): 
            value = exif_data.get(key, None)
            clean_val = self.__clean_value(value) if value is not None else None
            dict_data[key] = clean_val   
        return dict_data
    

    def get_data(self,image_folder, dict_data:dict,model_value:str, tot_images = None):
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
        images_list = []
        images_list.extend(dict_data.keys())
        images_list.remove("filename")
        if tot_images is not None:
            count = 0
            for filename in os.listdir(image_folder):
                if count >= tot_images:
                    break
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                    image_path = os.path.join(image_folder, filename)
                    exif_data = self.extract_exif(image_path)
                    dict_data['filename'].append(filename)
                    for key in images_list: 
                        value = exif_data.get(key, None)
                        clean_val = self.__clean_value(value) if value is not None else None
                        dict_data[key].append(clean_val)
                    count += 1
        else:
            for filename in os.listdir(image_folder):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                    image_path = os.path.join(image_folder, filename)
                    exif_data = self.extract_exif(image_path)
                    dict_data['filename'].append(filename)
                    for key in images_list: 
                        value = exif_data.get(key, None)
                        clean_val = self.__clean_value(value) if value is not None else None
                        dict_data[key].append(clean_val)
        filtered_dict_data = self.__filter_dict_by_model(dict_data,model_value)
        return filtered_dict_data
    
    