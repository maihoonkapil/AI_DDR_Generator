from extractor import extract_pdf_data
from llm import generate_ddr
from utils import attach_images
from report_generator import generate_pdf

def run_pipeline():

    inspection_path = "Sample Report.pdf"
    thermal_path = "Thermal Images.pdf"

    print("📄 Extracting PDFs...")
    inspection_text, inspection_images = extract_pdf_data(inspection_path)
    thermal_text, thermal_images = extract_pdf_data(thermal_path)

    print("🧠 Generating DDR via LLM...")
    ddr_data = generate_ddr(inspection_text, thermal_text)

    if not ddr_data:
        print("❌ Failed to generate DDR")
        return

    print("🖼 Attaching images...")
    all_images = inspection_images + thermal_images
    ddr_data["Area-wise Observations"] = attach_images(
        ddr_data["Area-wise Observations"],
        all_images
    )

    print("📑 Generating PDF...")
    generate_pdf(ddr_data)

    print("✅ DDR Report Generated Successfully!")

if __name__ == "__main__":
    run_pipeline()