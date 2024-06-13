# Extract Exif

## Description
This project allows extracting EXIF data from provided images in a folder or from a single photo by providing its path.

Aggiorna perchè fa anche altre cose.

## System Requirements
1. Exiftool 
Metti qui il link ad exiftool 
5. Install Exiftool [Exiftool](https://exiftool.org/)
6. Insert exiftool into the system path

## Instructions
1. Install the dependencies. Come?? Requirements.txt??


Datset di prova

Origine dei dati
3. The images can be downloaded from [Flickr](https://www.flickr.com/).
4. You can use the following tool to download the images: [gallery-dl](https://github.com/mikf/gallery-dl).




## Usage
```
usage: main.py [-h] [--tot_images TOT_IMAGES] images_path mode [model_value] [exif_template]

Extract EXIF data from images and return the results. Aggiorna la descrizione

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

Inserisci un esempio per modalità e descrivi meglio l'output.

Save the EXIF data of a single image in a JSON file:
`python src\main.py data\images\flickr_53478347388.jpg`

Save the EXIF data of a specified number of images in a dataframe:
`python src\main.py data\images "iPhone 14 Pro Max" --tot_images 100`
