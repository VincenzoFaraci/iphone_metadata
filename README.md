# Extract Exif

## Description
The project allows working with the EXIF data of provided images, whether a single image or a folder of images:

It is possible to extract the EXIF data from the provided images.
It is possible to remove the EXIF data from the provided images.
It is possible to set a predefined or provided set of EXIF data to the provided images.

## System Requirements
- [Exiftool](https://exiftool.org/)


## Instructions
1. Install the dependencies trough requirements.txt


Datset di prova

Origine dei dati
3. The images can be downloaded from [Flickr](https://www.flickr.com/).
4. You can use the following tool to download the images: [gallery-dl](https://github.com/mikf/gallery-dl).




## Usage
```
usage: main.py [-h] [--tot_images TOT_IMAGES] images_path mode [model_value] [exif_template]

This program allows you to work with EXIF data in images. Depending on the selected mode, the program can:

- Extract EXIF data from images and return the results.
- Remove EXIF data from images.
- Set EXIF data for images using a predefined or custom template.


positional arguments:
  images_path           The folder containing the images or the path to a single image
  mode                  Mode select: 1. Get Exif data (get) 2. Set Exif data (set) 3. Remove Exif data (rem)
  model_value           The model to analyze. di che cosa???
  exif_template         The exif template we want to use to set images exif

options:
  -h, --help            show this help message and exit
  --tot_images TOT_IMAGES
                        Total number of images to analyze (se è data una directory in input)
```

### Usage Example

- Get and save the EXIF data of a single image in a JSON file: `python src\main.py -i data\images\flickr_53478347388.jpg -m get`

- Get and save the EXIF data of all images in a folder to a dataframe: `python src\main.py -i data\images -m get`

- Get and save the EXIF data of a specified number of images from a specific camera model in a folder to a dataframe: `python src\main.py -i data\images -m get -m_v "iPhone 14 Pro Max" --tot_images 100`

- Get and save the EXIF data of images from a specific model in a folder to a dataframe: `python src\main.py -i data\images -m get -m_v "iPhone 14 Pro Max"`

- Get and save the EXIF data of a specified number of images in a folder to a dataframe: `python src\main.py -i data\images -m get --tot_images 50`

- Remove EXIF data from a single image: `python src\main.py -i data\images\flickr_53478347388.jpg -m rem`

- Remove EXIF data from all images in a folder: `python src\main.py -i data\images -m rem`

- Set EXIF data for a single image using a specific template: `python src\main.py -i data\images\flickr_53478347388.jpg -m set -e templates\exif_template.json`

<!-- TODO;- Set EXIF data for all images in a folder using a specific template: `python src\main.py -i data\images -m set -e templates\exif_template.json` -->

- Set EXIF data for a single image using the default template: `python src\main.py -i data\images\flickr_53478347388.jpg -m set`

<!-- - Set EXIF data for all images in a folder using the default template: `python src\main.py -i data\images -m set` -->

