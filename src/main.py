from functions.extract_exif import get_folder_data,get_image_data
import argparse
import os
 
def main():
    """
    Parses command-line arguments to determine the image path and model to analyze.
    Calls the appropriate function based on whether the path is a directory or a file.
    """
    
    
    parser = argparse.ArgumentParser(description="Extract EXIF data from images and return the results.")
    parser.add_argument('images_path', help='The folder containing the images or the path to a single image')
    parser.add_argument("model_value", nargs='?', default=None, help="The model to analyze (required if the path is a folder)")
    parser.add_argument("--tot_images", type=int, help="Total number of images to analyze")

    args = parser.parse_args()

    if os.path.isdir(args.images_path):
        """
        Check if the provided path is a directory.
        If it is, check if the model_value is provided. If not, raise an error.
        Call get_folder_data to extract EXIF data from images in the directory.
        """
        if args.model_value is None:
            parser.error("model_value is required when images_path is a folder")
        if args.tot_images:
            get_folder_data(args.images_path, args.model_value, args.tot_images)
        else:
            get_folder_data(args.images_path, args.model_value)
        print("The EXIF data has been saved to the file output_excel.txt in the output folder")
    elif os.path.isfile(args.images_path):
        get_image_data(args.images_path)
        print("The specified path is a file.")
        print("The EXIF data has been saved to the file image_exif.json in the output folder")
    else:
        print("The specified path does not exist.")

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    





