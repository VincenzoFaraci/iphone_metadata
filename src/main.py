#What this program can do?
# 1- Get exif data of a single file or a folder of images
# 2- Set exif data of a single image
# 3- Remove exif daat from a single image or from a folder of images   

import argparse
import os

from PIL import Image
from utils.get_exif_data import get_folder_data,get_image_data
from utils.set_exif import set_exif_tags
from utils.delete_exif import remove_exif,remove_multiple_exif
from utils.save_exif import save_exif_dataframe,save_exif_json


root_dir = os.path.dirname(os.path.dirname(__file__))
output_folder = os.path.join(root_dir, 'output')



def convert_png_to_jpg(input_folder, output_folder=None):
    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)
    if os.path.isfile(input_folder):
        if input_folder.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(input_folder, os.path.splitext(filename)[0] + ".jpg")
            
            with Image.open(input_path) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(output_path, "JPEG")
        else:
            pass
    else:
        for filename in os.listdir(input_folder):
            if filename.endswith(".png"):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(input_folder, os.path.splitext(filename)[0] + ".jpg")
                
                with Image.open(input_path) as img:
                    rgb_img = img.convert('RGB')
                    rgb_img.save(output_path, "JPEG")
                    
    #print(f"Converted {input_path} to {output_path}")


def run(args):
    print(args.images_path)
    exif_data = {}
    if os.path.exists(args.images_path):
        
        if (args.mode).lower() == "get":
            print("Get mode")
            if os.path.isdir(args.images_path):
                print(f"folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                exif_data = get_folder_data(args.images_path,args.model_value,args.tot_images)
                if all(len(value) == 0 for value in exif_data.values()):
                    print("The dictionary has not been saved because is empty")
                else:
                    save_exif_dataframe(exif_data,args.output_folder)
                    print(f"The EXIF data has been saved to the file output_excel.xlsx in the {args.output_folder} folder")    
            else:
                print("The specified path is a file.")
                exif_data = get_image_data(args.images_path)
                print(exif_data)
                save_exif_json(exif_data,args.images_path,args.output_folder)
                filename = os.path.splitext(os.path.basename(args.images_path))[0]
                print(f"The EXIF data has been saved to the file {filename}.json in the {args.output_folder} folder")
            
        elif (args.mode).lower() == "set":
            print("Set mode")
            set_exif_tags(args.images_path,args.icc_profile,args.template_image,args.exif_template) 
        
        elif (args.mode).lower() == "rem":
            print("Remove mode")
            if os.path.isdir(args.images_path):
                remove_multiple_exif(args.images_path)
            else:
                remove_exif(args.images_path)
            print("All possible exif removed")    
    else:
        print(f"The specified path: {args.images_path} does not exist.") 
        
if __name__ == "__main__":
    """
    Parses command-line arguments to determine the image path and the smartphone model to analyze.
    Calls the appropriate function based on whether the path is a directory or a file.
    """
    parser = argparse.ArgumentParser(description=  """
        A script for processing images either individually or in batches.
        Supports operations to extract, replace, or remove EXIF data from images.

        Operations:
        - 'extract': Extracts EXIF data from images.
        - 'replace': Replaces existing EXIF data in images with new values.
        - 'remove': Removes all EXIF data from images.
        """)
    parser.add_argument('-i', '--images_path', type=str, help='The folder containing the images or the path to a single image', required=True)
    parser.add_argument('-m', '--mode', type=str, choices=['get', 'set', 'rem'], required=True, help = """Mode select: 
                        - Get Exif data (get) 
                        - Set Exif data (set)
                        - Remove exif data (rem)
                        """)
    parser.add_argument('-m_v','--model_value', nargs='?', default=None, help="The smartphone model to analyze. If not specified, the EXIF data returned will not be filtered based on model.")
    parser.add_argument('-e','--exif_template', nargs='?', default=None, help="The exif template we want to use to set images exif. If not specified a deafult template will be used")
    parser.add_argument('-t','--tot_images', type=int, help="Total number of images to analyze")
    parser.add_argument('-o', '--output_folder', type=str, default=output_folder, help="The folder to save extracted EXIF data. If not specified, the default output folder 'output' will be used.")
    parser.add_argument('-i_p', '--icc_profile', type=str, default=None, help="The image path to use to extract icc_profile")
    parser.add_argument('-t_i', '--template_image', type=str, default=None, help="The path to the image from which to extract EXIF data to copy to other images.")
    
    args = parser.parse_args()
    convert_png_to_jpg(args.images_path)
    run(args)    
    
    





