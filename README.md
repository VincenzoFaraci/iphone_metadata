# Extract Exif

## Description
This project allows extracting EXIF data from provided images in a folder or from a single photo by providing its path.

## Instructions
1. Install the dependencies.
2. Create a data folder and place the images inside it.
3. The images can be downloaded from [Flickr](https://www.flickr.com/).
4. You can use the following tool to download the images: [gallery-dl](https://github.com/mikf/gallery-dl).
5. To execute the script, use argparse.


## Usage
```
usage: main.py [-h] [--tot_images TOT_IMAGES] images_path [model_value]

Extract EXIF data from images and return the results.

positional arguments:
  images_path           The folder containing the images or the path to a single image
  model_value           The model to analyze (required if the path is a folder)

options:
  -h, --help            show this help message and exit
  --tot_images TOT_IMAGES
                        Total number of images to analyze
```

### Usage Example

Save the EXIF data of a single image in a JSON file:
`python src\main.py data\images\flickr_53478347388.jpg`

Save the EXIF data of a specified number of images in a dataframe:
`python src\main.py data\images "iPhone 14 Pro Max" --tot_images 100`

