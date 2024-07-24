import xlsxwriter
import json
import subprocess

# -----------------------------
#           COMPARE
# -----------------------------
def comparison_to_exel(exif1, exif2, output_file):
    """Write EXIF data and differences to an Excel file."""
    def get_unique_tags(exif1, exif2):
        """Return unique tags present in either exif1 or exif2."""
        return set(exif1.keys()).union(set(exif2.keys()))

    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet('EXIF Comparison')
    
    # Add cell formats for different and non-different values
    format_different = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    format_minor_different = workbook.add_format({'bg_color': '#ADD8E6', 'font_color': '#0000FF'})
    format_normal = workbook.add_format()

    # Write headers
    all_tags = sorted(get_unique_tags(exif1, exif2))
    headers = ['Tag', 'Image 1', 'Image 2', 'Different']
    worksheet.write_row(0, 0, headers)

    # Write data
    row = 1
    total_differences = 0
    for tag in all_tags:
        value1 = exif1.get(tag, 'N/A')
        value2 = exif2.get(tag, 'N/A')
        different = value1 != value2 or (value1 is None and value2 is not None) or (value1 is not None and value2 is None)
        worksheet.write(row, 0, tag)

        if "[File]" in tag or "ImageSize" in tag or "Megapixels" in tag or "Width" in tag or "Height" in tag:
            worksheet.write(row, 1, str(value1), format_minor_different if different else format_normal)
            worksheet.write(row, 2, str(value2), format_minor_different if different else format_normal)
            worksheet.write(row, 3, 'Yes' if different else 'No', format_minor_different if different else format_normal)
        else:
            worksheet.write(row, 1, str(value1), format_different if different else format_normal)
            worksheet.write(row, 2, str(value2), format_different if different else format_normal)
            worksheet.write(row, 3, 'Yes' if different else 'No', format_different if different else format_normal)

            # exclude date in te counting
            if different:
                total_differences += 1
        
        row += 1
    
    # Write total differences count
    worksheet.write(row + 1, 0, 'Total Differences')
    worksheet.write(row + 1, 1, total_differences)
    workbook.close()
    print(f"Differences written to {output_file}")


def get_camera_model_from_lens_data(image_path):
    try:
        # Esegui ExifTool per ottenere i metadati in formato JSON
        result = subprocess.run(['exiftool', '-json', image_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Se ExifTool ha restituito un errore
        if result.stderr:
            print(f"Errore di ExifTool: {result.stderr}")
            return None
        
        # Carica i metadati JSON
        metadata = json.loads(result.stdout)[0]
        
        # Estrai i campi rilevanti
        camera_model = metadata.get('Model')
        lens_model = metadata.get('LensModel')
        lens_make = metadata.get('LensMake')
        
        # Combina i dati per fornire un'informazione più completa
        if camera_model:
            if lens_make and lens_model:
                return f"{lens_make} {lens_model} ({camera_model})"
            elif lens_model:
                return f"{lens_model} ({camera_model})"
            else:
                return camera_model
        elif lens_model:
            return lens_model
        else:
            return "Modello della fotocamera non trovato."
    
    except Exception as e:
        print(f"Errore durante l'accesso ai metadati EXIF con ExifTool: {str(e)}")
        return None


