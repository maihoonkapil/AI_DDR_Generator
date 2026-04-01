import streamlit as st
import os
from extractor import extract_pdf_data
from llm import generate_ddr
from utils import attach_images
from report_generator import generate_pdf

st.title("🧠 AI DDR Generator")

st.write("Upload Inspection and Thermal Reports")

inspection_file = st.file_uploader("Upload Inspection Report", type="pdf")
thermal_file = st.file_uploader("Upload Thermal Report", type="pdf")

if st.button("Generate DDR Report"):

    if inspection_file and thermal_file:

        # Save uploaded files
        with open("inspection.pdf", "wb") as f:
            f.write(inspection_file.read())

        with open("thermal.pdf", "wb") as f:
            f.write(thermal_file.read())

        st.info("📄 Extracting data...")
        inspection_text, inspection_images = extract_pdf_data("inspection.pdf")
        thermal_text, thermal_images = extract_pdf_data("thermal.pdf")

        st.info("🧠 Generating DDR...")
        ddr_data = generate_ddr(inspection_text, thermal_text)

        if not ddr_data:
            st.error("❌ Failed to generate DDR")
        else:
            st.info("🖼 Attaching images...")
            all_images = inspection_images + thermal_images
            ddr_data["Area-wise Observations"] = attach_images(
                ddr_data.get("Area-wise Observations", []),
                all_images
            )

            st.info("📑 Generating PDF...")
            generate_pdf(ddr_data)

            st.success("✅ Report Generated!")

            with open("outputs/DDR_Report.pdf", "rb") as f:
                st.download_button(
                    label="📥 Download DDR Report",
                    data=f,
                    file_name="DDR_Report.pdf",
                    mime="application/pdf"
                )

    else:
        st.warning("⚠️ Please upload both files")