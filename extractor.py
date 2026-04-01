import fitz  # PyMuPDF
import os

def extract_pdf_data(file_path, output_dir="outputs/images"):
    os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(file_path)
    full_text = ""
    image_paths = []

    for page_num, page in enumerate(doc):
        full_text += page.get_text()

        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            ext = base_image["ext"]

            img_name = f"{output_dir}/img_{page_num}_{img_index}.{ext}"

            with open(img_name, "wb") as f:
                f.write(image_bytes)

            image_paths.append(img_name)

    return full_text, image_paths