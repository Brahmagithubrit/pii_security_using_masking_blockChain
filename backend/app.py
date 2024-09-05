from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from docx import Document
from mask_ids import mask_unique_id  # Import the updated masking function

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'jpg', 'png', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract data from the file
        extracted_data = extract_data_from_file(filepath)
        
        # Mask the extracted text
        masked_data = mask_unique_id(extracted_data['text'])
        
        # Return the filename, extracted data, and masked data
        return jsonify({
            "filename": filename,
            "data": extracted_data,
            "masked_data": {"text": masked_data}
        }), 200
    else:
        return jsonify({"error": "File type not allowed"}), 400

def extract_data_from_file(filepath):
    file_extension = filepath.rsplit('.', 1)[1].lower()
    
    if file_extension == 'txt':
        with open(filepath, 'r') as file:
            text = file.read()
    
    elif file_extension == 'pdf':
        text = ""
        pdf_document = fitz.open(filepath)
        for page in pdf_document:
            text += page.get_text()
    
    elif file_extension == 'docx':
        text = ""
        doc = Document(filepath)
        for para in doc.paragraphs:
            text += para.text
    
    elif file_extension in {'jpg', 'png', 'jpeg'}:
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)
    
    else:
        return {"text": "Unsupported file type"}
    
    # Return the entire extracted text
    return {"text": text}

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
