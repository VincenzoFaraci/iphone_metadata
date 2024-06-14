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


Test Dataset

Data Source
The images can be downloaded from [Flickr](https://www.flickr.com/).
You can use the following tool to download the images: [gallery-dl](https://github.com/mikf/gallery-dl).




## Usage
```
usage: main.py [-h] -i IMAGES_PATH [-m {get,set,rem}] [-m_v [MODEL_VALUE]] [-e [EXIF_TEMPLATE]] [-t TOT_IMAGES] [-o OUTPUT_FOLDER]

A script for processing images either individually or in batches. Supports operations to extract, replace, or remove EXIF data from images.
Operations: - 'extract': Extracts EXIF data from images. - 'set': Replaces existing EXIF data in images with new values. - 'remove': Removes all  
EXIF data from images.

options:
  -h, --help            show this help message and exit
  -i IMAGES_PATH, --images_path IMAGES_PATH
                        Specify the path of the folder containing the images or the path of the single image.
  -m {get,set,rem}, --mode {get,set,rem}
                        Specify the mode thet will be used: - Get Exif data (get) - Set Exif data (set) - Remove exif data (rem)
  -m_v [MODEL_VALUE], --model_value [MODEL_VALUE]
                        Specify the smartphone model to analyze. If not specified, the EXIF data returned will not be filtered based on model.
  -e [EXIF_TEMPLATE], --exif_template [EXIF_TEMPLATE]
                        Specify the exif template we want to use to set images exif. If not specified a deafult template will be used.
  -t TOT_IMAGES, --tot_images TOT_IMAGES
                        Specify the total number of images to be analyzed.
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        Specify the folder to save the extracted EXIF data. If not specified, the default 'output' folder will be used.
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

<!-- TODO;- Set EXIF data for all images in a folder using a specific template: `python src\main.py -i data\iphone_images -m set -e templates\exif_template.json` -->

- Set EXIF data for a single image using the default template: `python src\main.py -i data\iphone_images\00001.jpeg -m set`

<!-- - Set EXIF data for all images in a folder using the default template: `python src\main.py -i data\iphone_images -m set` -->

