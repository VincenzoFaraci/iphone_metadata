from exiftool import ExifTool
import os

from PIL import Image
from exiftool import ExifToolHelper, ExifTool
from test.check_tags import check_tags

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
default_image_path = os.path.join(
    root_dir, 'src', 'models', 'default_image.jpeg')


def create_thumbnail(input_image_path, thumbnail_size=(128, 128)):
    """
    Create a thumbnail of the specified image and save it to the output path.

    Args:
    input_image_path (str): Path to the original image.
    output_thumbnail_path (str): Path to save the thumbnail.
    thumbnail_size (tuple): Dimensions of the thumbnail (width, height).
    """
    file_name, file_extension = os.path.splitext(
        os.path.basename(input_image_path))
    thumbnail_path = os.path.join(os.path.dirname(
        input_image_path), file_name + '_thumbnail.jpg')
    try:
        image = Image.open(input_image_path)
        image.thumbnail(thumbnail_size)
        image.save(thumbnail_path)

        print(f"Thumbnail creata con successo: {thumbnail_path}")
        return thumbnail_path
    except IOError:
        print(f"Impossibile aprire l'immagine: {input_image_path}")
    finally:
        image.close()

def del_thumbnail(thumbnail_path):
    os.remove(thumbnail_path)

def restore_orientation_tag(image_path):
    """
    Restore the original EXIF orientation tag of the image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        None
    """
    tmp = 0
    # with ExifToolHelper() as eth:
    #     tmp = eth.get_tags(image_path,"EXIF:Orientation")[0]["EXIF:Orientation"]
    with ExifTool() as et:
        et.execute(b"exiftool", b"-EXIF:Orientation=", image_path)


def icc_set(icc_source_image, icc_dest_image):
    """
    Copy ICC_Profile from one image to another.
    Args:
        icc_source_image (str): The path to the image used to extract the ICC profile..
        icc_dest_image (str): The path to the image we want to overwrite
    Returns:
        None

    """
    with ExifTool() as et:
        et.execute(b"-TagsFromFile", icc_source_image,
                   b"-icc_profile", icc_dest_image)

#TODO: implement this
# def choose_exif_template(exif_template_path: str = None):
#     """
#     Return the EXIF model to be used,
#     whether it is the standard one or the user-provided one.

#     Args:
#         exif_template_path (str): The path to the exif template.
#         exif_template_path (str): the path of the provided exif set
#     Returns:
#         dict : dictionary to use as exif template
#     """
#     if exif_template_path is None:
#         print("Default Exif set has been used since no Exif model was provided.")
#         default_exif_set_path = os.path.join(
#             root_dir, 'src', 'models', 'exif_template.json')
#         with open(default_exif_set_path, 'r') as file:
#             default_exif_set = json.load(file)
#         return default_exif_set
#     else:
#         print("The provided Exif set has been used")
#         with open(exif_template_path, 'r') as file:
#             data_dict = json.load(file)
#     return data_dict


def set_date(image_path):
    """
    Set modify_date equal to create_date
    """
    with ExifTool() as et:
        et.execute(b"exiftool", b"-filemodifydate<datetimeoriginal",b"-filecreatedate<datetimeoriginal", image_path)


def set_all_tags(image_path,icc_profile_path,thumbnail_path,image_template_path):
    if image_template_path is not None:
        with ExifTool() as et:
            et.execute(b"exiftool", b"-TagsFromFile", image_template_path,
                        b"-all:all>all:all", b"--ThumbnailImage",
                        b"-filemodifydate<datetimeoriginal",b"-filecreatedate<datetimeoriginal", image_path)
            et.execute(
                b"exiftool", (f"-ThumbnailImage<={thumbnail_path}").encode(), image_path)
        icc_set(image_template_path, image_path)
    else:
        with ExifTool() as et:
            et.execute(b"exiftool", b"-TagsFromFile",
                        default_image_path, b"-all:all>all:all",
                        b"-filemodifydate<datetimeoriginal",b"-filecreatedate<datetimeoriginal", image_path)
            et.execute(
                b"exiftool", (f"-ThumbnailImage<={thumbnail_path}").encode(), image_path)
        icc_set(default_image_path, image_path)
        
    #set_date(image_path)
    if icc_profile_path is not None:
        icc_set(icc_profile_path, image_path)
    restore_orientation_tag(image_path)



def set_exif_tags(images_folder: str, icc_profile_path: str, image_template_path: str = None, exif_template_path: str = None):
    """
    Set EXIF data for all the image files in the specified folder.

    Args:
        images_folder (str): The path to the folder containing the image files.
        icc_profile_path (str): The path to the image used to extract the ICC profile.
        exif_template_path (str): The path to the provided EXIF data template.

    Returns:
        None
    """
    if os.path.exists(images_folder):
        # data_dict = choose_exif_template(exif_template_path) TODO: permettere il passaggio di un dizionario?
        if os.path.isdir(images_folder):
            for filename in os.listdir(images_folder):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', ".heic")):
                    image_path = os.path.join(images_folder, filename)
                    thumbnail_path = create_thumbnail(image_path)
                    print(f"We're working with this file: {image_path}")
                    set_all_tags(image_path,icc_profile_path,thumbnail_path,image_template_path)
                    os.remove(thumbnail_path)
                else:
                    print(f"Unrecognized file format: {filename}")

        elif os.path.isfile(images_folder):
            image_path = images_folder
            thumbnail_path = create_thumbnail(image_path)
            set_all_tags(image_path,icc_profile_path,thumbnail_path,image_template_path)
            os.remove(thumbnail_path)
            with ExifToolHelper() as et:
                check_tags((et.get_metadata(image_path))[
                            0], (et.get_metadata(default_image_path))[0])
    else:
        raise Exception(f"The provided path: {images_folder} does not exist")

#10 luglio 11:07