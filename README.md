# Extract Exif

## Description
This project allows extracting EXIF data from provided images in a folder or from a single photo by providing its path.

## Instructions
1. Install the dependencies.
2. Create a data folder and place the images inside it.
3. The images can be downloaded from [Flickr](https://www.flickr.com/).
4. You can use the following tool to download the images: [gallery-dl](https://github.com/mikf/gallery-dl).
5. To execute the script, use argparse.


# Usage Example

Returns the EXIF data of a single image in JSON format:
1. `python src\main.py data\images\flickr_53478347388.jpg`

Returns the EXIF data of a specified number of images in a dataframe:
2. `python src\main.py data\images "iPhone 14 Pro Max" --tot_images 100`
