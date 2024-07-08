import json
import os
import io


import piexif
from PIL import Image
from exiftool import ExifToolHelper,ExifTool
from test.check_tags import check_tags

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
default_image_path = os.path.join(root_dir, 'src' , 'models', 'default_image.jpeg')


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
        et.execute(b"-TagsFromFile", icc_source_image ,b"-icc_profile", icc_dest_image)
     

def choose_exif_template(exif_template_path:str = None):
    """
    Return the EXIF model to be used, 
    whether it is the standard one or the user-provided one.
    
    Args:
        exif_template_path (str): The path to the exif template.
        exif_template_path (str): the path of the provided exif set
    Returns:
        dict : dictionary to use as exif template
    """
    if exif_template_path is None:
        print("Default Exif set has been used since no Exif model was provided.")
        default_exif_set_path = os.path.join(root_dir, 'src' , 'models', 'exif_template.json')
        with open(default_exif_set_path, 'r') as file:
            default_exif_set = json.load(file)
        return default_exif_set
    else:
        print("The provided Exif set has been used")
        with open(exif_template_path, 'r') as file:
            data_dict = json.load(file)
    return data_dict


def set_date(image_path):
    """
    Set modify_date equal to create_date 
    """
    tmp_dict = {}
    with ExifToolHelper() as et:
        create_date = (et.get_tags(image_path, "File:FileCreateDate"))[0].get("File:FileCreateDate",None)
        access_date = (et.get_tags(image_path, "File:FileAccessDate"))[0].get("File:FileAccessDate",None)
        print(f"create_date: {create_date}, access_date: {access_date}")
        tmp_dict["File:FileModifyDate"] = create_date
        et.set_tags(image_path,tmp_dict)
        print(f"After setting create_date: {create_date}, access_date: {access_date}")
        print("Added",tmp_dict)


def extract_and_save_thumbnail(image_path, thumbnail_size=(128, 128), thumbnail_filename='thumbnail.jpg'):
    """
    Extracts a thumbnail from the given image and saves it to a file.

    Args:
        image_path (str): Path to the image file.
        thumbnail_size (tuple): Size of the thumbnail (width, height). Default is (128, 128).
        thumbnail_filename (str): Name of the file to save the thumbnail. Default is 'thumbnail.jpg'.

    Returns:
        bool: True if thumbnail extraction and saving were successful, False otherwise.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Create thumbnail
        img.thumbnail(thumbnail_size, Image.LANCZOS)

        # Save thumbnail to a file
        thumbnail_path = os.path.join(os.path.dirname(image_path), thumbnail_filename)
        img.save(thumbnail_path, format='JPEG')

        print(f"Thumbnail saved to: {thumbnail_path}")
        img.show()
        # Delete the saved image file
        # os.remove(thumbnail_path)
        # print(f"Deleted: {thumbnail_path}")

        return True

    except Exception as e:
        print(f"Error extracting or saving thumbnail: {str(e)}")
        return False


def thumbnails_set(image_path):
    img_original = Image.open(image_path)
        # Estrai i metadati EXIF dall'immagine originale
    exif_dict = piexif.load(img_original.info['exif'])

    # Rimuovi la miniatura esistente dai metadati EXIF
    if 'thumbnail' in exif_dict:
        del exif_dict['thumbnail']

    # Creare una nuova miniatura
    img_thumbnail = img_original.copy()
    img_thumbnail.thumbnail((128, 128), Image.LANCZOS)

    # Convertire la miniatura in byte
    thumbnail_io = io.BytesIO()
    img_thumbnail.save(thumbnail_io, format='JPEG')
    exif_dict['thumbnail'] = thumbnail_io.getvalue()

    # Converti i metadati EXIF in un formato compatibile
    exif_bytes = piexif.dump(exif_dict)

    # Salva l'immagine modificata mantenendo i metadati originali
    img_original.save(image_path)

    
def set_exif_tags(images_folder: str,icc_profile_path: str,image_template_path: str = None,exif_template_path:str = None):
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
        
        data_dict = choose_exif_template(exif_template_path)

        if os.path.isdir(images_folder):
            for filename in os.listdir(images_folder):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff',".heic")):
                    image_path = os.path.join(images_folder, filename)
                    print(f"We're working with this file: {image_path}")
                    if image_template_path is not None:
                        print("We're using the template image to copy his exif")
                        with ExifTool() as et:
                            et.execute(b"exiftool", b"-TagsFromFile", image_template_path, b"-all:all>all:all", image_path)
                            #et.execute(b"exiftool","-thumbnailimage=",image_path)
                        icc_set(image_template_path,image_path)
                        set_date(image_path)
                        if icc_profile_path is None:
                            icc_set(default_image_path,image_path)
                        else:
                            icc_set(icc_profile_path,image_path)   
                    else:
                        with ExifTool() as et:
                            et.execute(b"exiftool", b"-TagsFromFile", default_image_path, b"-all:all>all:all", image_path)
                            et.execute(b"exiftool","-thumbnailimage=",image_path)
                        icc_set(default_image_path,image_path)
                        set_date(image_path)
                else:
                    print(f"Unrecognized file format: {filename}")
        elif os.path.isfile(images_folder):
            image_path = images_folder
            
            if image_template_path is not None:
                print("We're using the template image to copy his exif")
                with ExifTool() as et:
                    et.execute(b"-tagsfromfile", image_template_path, b"-exif:all", "--subifd:all", "-xmp:all","-jfif:all", "-mpf:all", image_path)
                icc_set(image_template_path,image_path)
                set_date(image_path)
                
                
                with ExifToolHelper() as et:
                    check_tags((et.get_metadata(image_path))[0],(et.get_metadata(image_template_path))[0])
                
                
            else:
                with ExifTool() as et:
                    #et.execute(b"-tagsfromfile", default_image_path, b"-exif:all", "--subifd:all", "-xmp:all", "-jfif:all", "-mpf:all", image_path)
                    et.execute(b"exiftool", b"-TagsFromFile", default_image_path, b"-all:all>all:all", image_path)
                    #et.execute(b"exiftool","-thumbnailimage=",image_path)
                icc_set(default_image_path,image_path)
                set_date(image_path)
                #thumbnails_set(image_path)
                # with ExifTool() as et:
                #     et.execute(b"-b",b"-ThumbnailImage", image_path,"my_thumbnail.jpg")
                #print("Abbiamo fatto?")
                with ExifToolHelper() as et:
                    check_tags((et.get_metadata(image_path))[0],(et.get_metadata(default_image_path))[0])
                
                
            
                    # # Rimuovi la miniatura esistente dai metadati EXIF (opzionale)
            # if 'thumbnail' in exif_dict:
            #     del exif_dict['thumbnail']

            # # Creare una nuova miniatura
            # img_thumbnail = img_result.copy()
            # img_thumbnail.thumbnail((128, 128), Image.ANTIALIAS)

            # # Convertire la miniatura in byte
            # thumbnail_io = io.BytesIO()
            # img_thumbnail.save(thumbnail_io, format='JPEG')
            # exif_dict['thumbnail'] = thumbnail_io.getvalue()
                  
    else:
        raise Exception(f"The provided path: {images_folder} does not exist")


         
    
    

 
