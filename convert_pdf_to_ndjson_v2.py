import pdfplumber
import json

# PDF file name
pdf_path = "Sapiens-A-Brief-History-of-Humankind.pdf"
output_json = "sapiens.ndjson"

with pdfplumber.open(pdf_path) as pdf:
    with open(output_json, "w", encoding="utf-8") as f:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            # Write each page as a separate JSON object
            f.write(json.dumps({"page": i + 1, "content": text.strip() if text else ""}) + "\n")

print(f"PDF has been converted to {output_json}")