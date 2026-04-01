from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(data, output_file="outputs/DDR_Report.pdf"):
    os.makedirs("outputs", exist_ok=True)

    doc = SimpleDocTemplate(output_file)
    styles = getSampleStyleSheet()
    elements = []

    def add_section(title, content):
        elements.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(content or "Not Available", styles["Normal"]))
        elements.append(Spacer(1, 20))

    # Sections
    add_section("1. Property Issue Summary", data.get("Property Issue Summary"))

    elements.append(Paragraph("<b>2. Area-wise Observations</b>", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    for obs in data.get("Area-wise Observations", []):
        elements.append(Paragraph(f"<b>Area:</b> {obs.get('area', 'Unknown')}", styles["Normal"]))
        elements.append(Paragraph(f"<b>Observation:</b> {obs.get('observation', '')}", styles["Normal"]))
        elements.append(Paragraph(f"<b>Issue:</b> {obs.get('issue', '')}", styles["Normal"]))
        elements.append(Spacer(1, 10))

        img_path = obs.get("image")
        if img_path and img_path != "Image Not Available" and os.path.exists(img_path):
            try:
                elements.append(Image(img_path, width=300, height=200))
            except:
                elements.append(Paragraph("Image Not Available", styles["Normal"]))
        else:
            elements.append(Paragraph("Image Not Available", styles["Normal"]))

        elements.append(Spacer(1, 20))

    add_section("3. Probable Root Cause", data.get("Probable Root Cause"))
    add_section("4. Severity Assessment", data.get("Severity Assessment"))
    add_section("5. Recommended Actions", data.get("Recommended Actions"))
    add_section("6. Additional Notes", data.get("Additional Notes"))
    add_section("7. Missing Information", data.get("Missing Information"))

    doc.build(elements)