import os
from PIL import Image
import pandas as pd
from PIL.ExifTags import TAGS, GPSTAGS
from .ExifExtractor import Exif_extractor


class IphoneExifExtractor(Exif_extractor):
    def __init__(self,model_value:str):
        self.model_value = model_value
        self.keys = ['filename', 'GPSInfo', 'ResolutionUnit', 'ExifOffset', 'Make', 'Model', 'Software', 'Orientation', 'DateTime', 
            'XResolution', 'YResolution', 'HostComputer', 'ExifVersion', 'ComponentsConfiguration', 'ShutterSpeedValue', 
            'DateTimeOriginal', 'DateTimeDigitized', 'ApertureValue', 'BrightnessValue', 'ExposureBiasValue', 
            'MeteringMode', 'Flash', 'FocalLength', 'ColorSpace', 'ExifImageWidth', 'DigitalZoomRatio', 
            'FocalLengthIn35mmFilm', 'SceneCaptureType', 'OffsetTime', 'OffsetTimeOriginal', 'OffsetTimeDigitized', 
            'SubsecTimeOriginal', 'SubjectLocation', 'SubsecTimeDigitized', 'ExifImageHeight', 'SensingMethod', 
            'ExposureTime', 'FNumber', 'SceneType', 'ExposureProgram', 'ISOSpeedRatings', 'ExposureMode', 
            'FlashPixVersion', 'WhiteBalance', 'LensSpecification', 'LensMake', 'LensModel', 'CompositeImage']
        self.iphone_data = {key: [] for key in self.keys}
    
    def get_data(self, image_folder, tot_images):
        self.iphone_data =  super().get_data(image_folder, tot_images, self.iphone_data,self.model_value)
    
    def stampa(self):
        print(self.iphone_data)
    #e fino a qui