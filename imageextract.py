import os
import fitz
from PIL import Image

def pdf_to_tiff(selected_file, target_directory, zoom=2.0):
    
    pdf_document = fitz.open(selected_file)
    temp_tiff_files = []

    base_name = os.path.splitext(os.path.basename(selected_file))[0]
    tiff_path = os.path.join(target_directory, f"{base_name}.tiff")

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # rendering for more high quality add matrix and zoom. 
        matrix = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=matrix, alpha=False)

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # This steps for using less memory.
        temp_tiff_path = os.path.join(target_directory, f"{base_name}_page_{page_num + 1}.tiff")
        img.save(temp_tiff_path, "TIFF")
        temp_tiff_files.append(temp_tiff_path)

    with Image.open(temp_tiff_files[0]) as img:
        img.save(tiff_path, save_all=True, append_images=[Image.open(f) for f in temp_tiff_files[1:]], compression='tiff_deflate')

    # Geçici TIFF dosyalarını sil
    for temp_file in temp_tiff_files:
        os.remove(temp_file)
