# SECURE-PERSONAL-IDENTIFIABLE-INFORMATION


---

A lightweight tool that takes a PDF as input, extracts its text, and masks sensitive content.

---

## Features
- Extracts text from an input PDF.
- Masks sensitive information (emails, phone numbers, IDs, etc.) with placeholders like `****`.
- Easily customizable masking patterns via `patterns.yaml`.

---

## Requirements
- Python **3.9+**

---

## Installation
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd <repo-folder>
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## How Masking Works

* Extracted text is scanned using regex patterns for:

  * Emails
  * Phone numbers
  * Credit cards
  * Other IDs
* Matches are replaced with a mask string (e.g., `****`).
* Patterns can be added or overridden in `patterns.yaml`.

**Example Default Patterns**

| Type        | Input Example          | Masked Output |
| ----------- | ---------------------- | ------------- |
| Email       | `something@domain.com` | `****`        |
| Phone       | `+1-202-555-0123`      | `****`        |
| Credit Card | `4111 1111 1111 1111`  | `****`        |

---

## Tips

* For **scanned PDFs**, run OCR (e.g., with [Tesseract](https://github.com/tesseract-ocr/tesseract)) before masking.
* Always **manually review** masked output for rare/uncommon IDs.

---

## Limitations

* Accuracy depends on:

  * PDF text extractability.

* Images or scanned pages require OCR for text extraction.
* Complex layouts may not preserve exact formatting.

---

## Contributing

* Open an **issue** for bugs or feature requests.
* Submit a **pull request** with:

  * New masking patterns.
  * Bug fixes.
  * Performance improvements.


