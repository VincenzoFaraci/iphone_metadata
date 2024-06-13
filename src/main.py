from functions.extract_exif import get_folder_data,get_image_data
from functions.select_exif import set_exif_tags
from functions.delete_exif import remove_exif,remove_multiple_exif
import argparse
import os

  
def main():
    """
    Parses command-line arguments to determine the image path and model to analyze.
    Calls the appropriate function based on whether the path is a directory or a file.
    """
    
    #DA SISTEMARE GLI ARGUMENT IN BASE A QUANDO DOVREMMO USARLI IMPORATANETETETEETETETETET
    parser = argparse.ArgumentParser(description="Extract EXIF data from images and return the results.")
    parser.add_argument('images_path', help='The folder containing the images or the path to a single image')
    parser.add_argument("mode",help="Mode select: 1. Get Exif data (get) 2. Set Exif data (set)")
    parser.add_argument("model_value", nargs='?', default=None, help="The model to analyze")
    parser.add_argument("exif_template", nargs='?', default=None, help="The exif template we want to use to set images exif")
    parser.add_argument("--tot_images", type=int, help="Total number of images to analyze")
    

    args = parser.parse_args()
    
    print(args.exif_template)
    
    if (args.mode).lower() == "get":
        print("Get mode")
        if os.path.isdir(args.images_path):
            """
            Check if the provided path is a directory.
            If it is, check if the model_value is provided. If not, raise an error.
            Call get_folder_data to extract EXIF data from images in the directory.
            """
            if args.model_value is None and args.tot_images is None:
                print(f"A: folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                get_folder_data(args.images_path)
            elif args.tot_images is not None and args.model_value is not None:
                print(f"B: folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                get_folder_data(args.images_path, args.model_value, args.tot_images)
            elif args.tot_images is None and args.model_value is not None:
                print(f"C: folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                get_folder_data(args.images_path, args.model_value)
            elif args.tot_images is not None and args.model_value is None:
                print(f"D: folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
                get_folder_data(args.images_path,args.model_value, args.tot_images)
            else:
                print(f"Error, folder path = {args.images_path}, model = {args.model_value} e tot_images = {args.tot_images}")
            print("The EXIF data has been saved to the file output_excel.xlsx in the output folder")
        elif os.path.isfile(args.images_path):
            print("The specified path is a file.")
            get_image_data(args.images_path)
            print("The EXIF data has been saved to the file image_exif.json in the output folder")
        else:
            print("The specified path does not exist.")
    elif (args.mode).lower() == "set":
        print("Set mode")
        set_exif_tags(args.images_path,args.exif_template)
    elif (args.mode).lower() == "rem":
        print("Remove mode")
        if os.path.isdir(args.images_path):
            remove_multiple_exif(args.images_path)
        elif os.path.isfile(args.images_path):
            remove_exif(args.images_path)
    else:
        print("Error, the selected mode is non-existent")
        
if __name__ == "__main__":
    main()

   
#What this program can do?
# 1- Get exif data of a single file or a folder of images
# 2-Set exif data of a single image
# 3-Remove exif daat from a single image or from a folder of images   
    
    
    
    
    





