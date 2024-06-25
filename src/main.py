#What this program can do?
# 1- Get exif data of a single file or a folder of images
# 2- Set exif data of a single image
# 3- Remove exif daat from a single image or from a folder of images   



import argparse
import os

from utils.get_exif_data import get_folder_data,get_image_data
from utils.select_exif import set_exif_tags
from utils.delete_exif import remove_exif,remove_multiple_exif
from utils.save_exif import save_exif_dataframe,save_exif_json

exif_data = {}
  
def run(args):
    if os.path.exists(args.images_path):
        if (args.mode).lower() == "get":
            print("Get mode")
            # TODO: aggiusta le chiamate a funzione
            if os.path.isdir(args.images_path):
                if args.model_value is None and args.tot_images is None:
                    # la print una sola volta
                    print(f"folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                    exif_data = get_folder_data(args.images_path)
                    save_exif_dataframe(exif_data)
                elif args.tot_images is not None and args.model_value is not None:
                    print(f"folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                    exif_data = get_folder_data(args.images_path, args.model_value, args.tot_images)
                    save_exif_dataframe(exif_data)
                elif args.tot_images is None and args.model_value is not None:
                    print(f"folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                    exif_data = get_folder_data(args.images_path, args.model_value)
                    save_exif_dataframe(exif_data)
                elif args.tot_images is not None and args.model_value is None:
                    print(f"folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                    exif_data = get_folder_data(args.images_path,args.model_value, args.tot_images)
                    save_exif_dataframe(exif_data)
                else:
                    # TODO: Error di cosa?
                    print(f"Error, folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                
                # ???
                print("The EXIF data has been saved to the file output_excel.xlsx in the output folder")
            else: #os.path.isfile(args.images_path):
                print("The specified path is a file.")
                exif_data = get_image_data(args.images_path)
                save_exif_json(exif_data)
                print("The EXIF data has been saved to the file image_exif.json in the output folder")
            
            # TODO: il controllo di esistenza lo fai già, qua stai controllando se è un file o una dir
            #else:
            #    print("The specified path does not exist.")
        
        elif (args.mode).lower() == "set":
            print("Set mode")
            set_exif_tags(args.images_path,args.exif_template) 
        
        elif (args.mode).lower() == "rem":
            print("Remove mode")
            if os.path.isdir(args.images_path):
                remove_multiple_exif(args.images_path)
            elif os.path.isfile(args.images_path): # elif non serve
                remove_exif(args.images_path)
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
    parser.add_argument('-m', '--mode', type=str, choices=['get', 'set', 'rem'], help = """Mode select: 
                        - Get Exif data (get) 
                        - Set Exif data (set)
                        - Remove exif data (rem)
                        """)
    parser.add_argument('-m_v','--model_value', nargs='?', default=None, help="The smartphone model to analyze. If not specified, the EXIF data returned will not be filtered based on model.")
    parser.add_argument('-e','--exif_template', nargs='?', default=None, help="The exif template we want to use to set images exif. If not specified a deafult template will be used")
    parser.add_argument('-t','--tot_images', type=int, help="Total number of images to analyze")
    parser.add_argument('-o', '--output_folder', type=str, default="output", help="The folder to save extracted EXIF data. If not specified, the default output folder 'output' will be used.")

    args = parser.parse_args()

    run(args)
    
    
    
    
    





