#What this program can do?
# 1- Get exif data of a single file or a folder of images
# 2- Set exif data of a single image
# 3- Remove exif daat from a single image or from a folder of images   

import argparse
import os
import shutil

from utils.get_exif_data import get_folder_data,get_image_data
from utils.set_exif import set_exif_tags
from utils.delete_exif import remove_exif,remove_multiple_exif
from utils.save_exif import save_exif_dataframe,save_exif_json


root_dir = os.path.dirname(os.path.dirname(__file__))
output_folder = os.path.join(root_dir, 'output')


def file_backup(images_path,tot_images = None):
    if os.path.exists(images_path):
        if os.path.isdir(images_path):
            if tot_images is not None:
                count = 0
                backup_dir = os.path.join(images_path, 'backup')
                os.makedirs(backup_dir, exist_ok=True)
                for filename in os.listdir(images_path):
                    if count >= tot_images:
                        break
                    source_file = os.path.join(images_path, filename)
                    if os.path.isfile(source_file):
                        backup_path = os.path.join(backup_dir, filename)
                        try:
                            shutil.copy2(source_file, backup_path)
                        except Exception as e:
                            print(f"Failed to copy {source_file} to {backup_path}: {e}")
                    count += 1
            else:
                backup_dir = os.path.join(images_path, 'backup')
                os.makedirs(backup_dir, exist_ok=True)
                for filename in os.listdir(images_path):
                    source_file = os.path.join(images_path, filename)
                    if os.path.isfile(source_file):
                        backup_path = os.path.join(backup_dir, filename)
                        try:
                            shutil.copy2(source_file, backup_path)
                        except Exception as e:
                            print(f"Failed to copy {source_file} to {backup_path}: {e}")
            #print(f"Images copied to {backup_path}")
        else:
            image_dir = os.path.dirname(images_path)
            backup_dir = os.path.join(image_dir, 'backup')
            os.makedirs(backup_dir, exist_ok=True)
            image_name = os.path.basename(images_path)
            backup_path = os.path.join(backup_dir, image_name)
            shutil.copy2(images_path, backup_path)
            print(f"Image copied to {backup_path}")
    else:
        raise Exception(f"The provided path - {images_path} - deos not exist")


def run(args):
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
                save_exif_json(exif_data,args.output_folder)
                print(f"The EXIF data has been saved to the file image_exif.json in the {args.output_folder} folder")
            
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
    file_backup(args.images_path,args.tot_images)
    run(args)    
    
    





