# SECURE-PERSONAL-IDENTIFIABLE-INFORMATION


A lightweight tool that takes a PDF as input, extracts its text, and applies masking to sensitive content.

What it does
Extracts text from an input PDF.

Masks sensitive information (e.g., emails, phone numbers, IDs) with placeholders like ****.

Requirements
Python 3.9+


Installation
Clone the repository.

Create and activate a virtual environment.



How masking works
The tool scans extracted text with regex patterns (emails, phone numbers, credit cards, etc.).

Matches are replaced with a mask string (e.g., ****).

You can add or override patterns in patterns.yaml.

Example default patterns:

Email: something@domain.com → ****

Phone: +1-202-555-0123 → ****

Credit card: 4111 1111 1111 1111 → ****



Tips

Scanned PDFs may need OCR first (e.g., Tesseract) before masking will work.

Validate the masked output with a quick manual scan, especially for uncommon IDs.

Limitations
Accuracy depends on PDF text extractability and regex coverage.

Images/scanned pages require OCR to extract text.

Complex layouts may not preserve exact formatting.

Contributing
Open an issue or submit a PR with new patterns or bug fixes.
