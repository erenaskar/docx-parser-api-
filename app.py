from flask import Flask, request, jsonify
from docx import Document
import io

app = Flask(__name__)

@app.route('/parse-docx', methods=['POST'])
def parse_docx():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if not file.filename.endswith('.docx'):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        doc = Document(io.BytesIO(file.read()))
        full_text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
        return jsonify({'text': full_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
