import os
from exiftool import ExifToolHelper


class ExifExtractor():
    """
    A class to extract EXIF metadata from images.

    This class provides methods to extract EXIF data from images located in a specified 
    folder or a single image file. It uses the ExifTool library for metadata extraction.
    
    """
    
    
    def __clean_value(self,value):
        """
        Cleans the given value by removing invalid characters.
        This function is called for every value in the dictonary in order to avoid problems

        # problems IN COSA??????

        Args:
            value (str or int): The value to clean.

        Returns:
            str: The cleaned value.
        """
        if isinstance(value, str):
            return ''.join(c for c in value if c.isprintable() and c not in ('\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x0b', '\x0c', '\x0e', '\x0f'))
        return value
    
    
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
                            for key in dict_data.keys(): 
                                value = data.get(key, None)
                                clean_val = self.__clean_value(value)
                                dict_data[key].append(clean_val)
            else:
                print(et.get_metadata(image_path))
                for data in et.get_metadata(image_path):
                    for key in dict_data.keys():
                        value = data.get(key, "None") #None means that key is not in data
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
        if tot_images is not None:
            count = 0
            for filename in os.listdir(image_folder):
                file_path = os.path.join(image_folder, filename)
                if not os.path.isfile(file_path):
                    count -= 1
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
                    self.__set_dict_data(image_path,dict_data,model_value)
        return dict_data
    
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
    
    
