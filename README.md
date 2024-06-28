# Extract Exif

## Description
The project allows working with the EXIF data of provided images, whether a single image or a folder of images:

- Extract the EXIF data from the provided images.

- Remove the EXIF data from the provided images.

- Set a predefined or provided set of EXIF data to the provided images.

## System Requirements
- Python 3.12.3
- [Exiftool](https://exiftool.org/)


## Instructions
1. Install the dependencies trough requirements.txt
2. Install Exiftool and add it to the system PATH (or the virtual environment PATH if one is created)(see how to install ExifTool [here](https://exiftool.org/install.html))


## Test Dataset

### Data Source
The images can be downloaded from [Flickr](https://www.flickr.com/groups/iphone14pro/).
You can use the following tool to download the images: [gallery-dl](https://github.com/mikf/gallery-dl).
AGGIUNGERE ISTRUZIONI UTILIZZO GALLERY-DL


### Results
After utilizing the Pandas library to analyze the dataset, it became possible to effectively study common EXIF tags depending on the camera sensor model. This analysis facilitated the creation of a pre-compiled set of EXIF metadata, which was used to add desired EXIF information to images lacking exif data.




## Usage
```
usage: main.py [-h] -i IMAGES_PATH -m {get,set,rem} [-m_v [MODEL_VALUE]] [-e [EXIF_TEMPLATE]] [-t TOT_IMAGES] [-o OUTPUT_FOLDER]
               [-i_p ICC_PROFILE] [-t_i TEMPLATE_IMAGE]

A script for processing images either individually or in batches. Supports operations to extract, replace, or remove EXIF data from   
images. Operations: - 'extract': Extracts EXIF data from images. - 'replace': Replaces existing EXIF data in images with new values.  
- 'remove': Removes all EXIF data from images.

options:
  -h, --help            show this help message and exit
  -i IMAGES_PATH, --images_path IMAGES_PATH
                        The folder containing the images or the path to a single image
  -m {get,set,rem}, --mode {get,set,rem}
                        Mode select: - Get Exif data (get) - Set Exif data (set) - Remove exif data (rem)
  -m_v [MODEL_VALUE], --model_value [MODEL_VALUE]
                        The smartphone model to analyze. If not specified, the EXIF data returned will not be filtered based on       
                        model.
  -e [EXIF_TEMPLATE], --exif_template [EXIF_TEMPLATE]
                        The exif template we want to use to set images exif. If not specified a deafult template will be used
  -t TOT_IMAGES, --tot_images TOT_IMAGES
                        Total number of images to analyze
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        The folder to save extracted EXIF data. If not specified, the default output folder 'output' will be used.    
  -i_p ICC_PROFILE, --icc_profile ICC_PROFILE
                        The image path to use to extract icc_profile
  -t_i TEMPLATE_IMAGE, --template_image TEMPLATE_IMAGE
                        The path to the image from which to extract EXIF data to copy to other images.
```

### Usage Example


- Get and save the EXIF data of a single image in a JSON file: `python src\main.py -i data\iphone_images\00001.jpeg -m get`

- Get and save the EXIF data of all images in a folder to a dataframe: `python src\main.py -i data\iphone_images -m get`

- Get and save the EXIF data of a specified number of images from a specific camera model in a folder to a dataframe: `python src\main.py -i data\iphone_images -m get -m_v "iPhone 14 Pro Max" --tot_images 100`

- Get and save the EXIF data of images from a specific model in a folder to a dataframe: `python src\main.py -i data\iphone_images -m get -m_v "iPhone 14 Pro Max"`

- Get and save the EXIF data of a specified number of images in a folder to a dataframe: `python src\main.py -i data\iphone_images -m get --tot_images 50`

- Remove EXIF data from a single image: `python src\main.py -i data\iphone_images\00001.jpeg -m rem`

- Remove EXIF data from all images in a folder: `python src\main.py -i data\iphone_images -m rem`

- Set EXIF data for a single image using a specific template provided by the user: `python src\main.py -i data\iphone_images\00001.jpeg -m set -e templates\exif_template.json`

- Set EXIF data for a single image using the default template: `python src\main.py -i data\iphone_images\00001.jpeg -m set`

- Set EXIF data for a single image using the provided image `python src\main.py -i data\iphone_images\00001.jpeg -m set -t_i template_image_path`

- Set EXIF data for a single image using the provided image to set only the icc_profile tags, then choose whether or not to use an arbitrary template or the default one `python src\main.py -i data\iphone_images\00001.jpeg -m set -i_P template_image_path`

- Add `-o output_folder_path` with the path to the folder you want to use to save the output.