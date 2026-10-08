# Python/Flask - Cloudinary Integration
# כל דבר שאתה צריך כדי להתחיל עם Cloudinary ו-Flask

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# ⚙️ Cloudinary Configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

print('✅ Cloudinary configured:', cloudinary.config()['cloud_name'])

# ============================================
# ROUTES - מסלולים
# ============================================

# 1️⃣ Upload Image - העלה תמונה
@app.route('/api/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'אין קובץ להעלות'}), 400

        file = request.files['image']

        # העלה ל-Cloudinary
        result = cloudinary.uploader.upload(
            file,
            folder='my-app/uploads',
            resource_type='auto'
        )

        return jsonify({
            'success': True,
            'url': result['secure_url'],
            'public_id': result['public_id']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2️⃣ Get Transformed Image - קבל תמונה עם טרנספורמציה
@app.route('/api/transform/<public_id>', methods=['GET'])
def transform_image(public_id):
    try:
        width = request.args.get('width', 400, type=int)
        height = request.args.get('height', 300, type=int)

        url = cloudinary.utils.cloudinary_url(
            public_id,
            transformation=[
                {'width': width, 'height': height, 'crop': 'fill'},
                {'quality': 'auto'},
                {'fetch_format': 'auto'}
            ]
        )[0]

        return jsonify({'url': url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3️⃣ Delete Image - מחק תמונה
@app.route('/api/delete/<public_id>', methods=['DELETE'])
def delete_image(public_id):
    try:
        result = cloudinary.uploader.destroy(public_id)

        return jsonify({
            'success': True,
            'message': 'תמונה נמחקה בהצלחה',
            'result': result
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 4️⃣ List Images - רשום תמונות
@app.route('/api/images', methods=['GET'])
def list_images():
    try:
        result = cloudinary.api.resources(
            type='upload',
            prefix='my-app/uploads',
            max_results=10
        )

        return jsonify({
            'images': result.get('resources', []),
            'total': result.get('total_count', 0)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 5️⃣ Generate Signature - יצור חתימה להעלאה מחתום
@app.route('/api/signature', methods=['POST'])
def generate_signature():
    try:
        import time
        timestamp = int(time.time())

        signature = cloudinary.utils.api_sign_request({
            'timestamp': timestamp,
            'folder': 'my-app/signed-uploads'
        }, os.getenv('CLOUDINARY_API_SECRET'))

        return jsonify({
            'signature': signature,
            'timestamp': timestamp,
            'cloud_name': os.getenv('CLOUDINARY_CLOUD_NAME'),
            'api_key': os.getenv('CLOUDINARY_API_KEY')
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 6️⃣ Home Route
@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>Cloudinary + Flask</title>
            <style>
                body { font-family: Arial; max-width: 600px; margin: 50px auto; }
                .btn { padding: 10px 20px; background: #4CAF50; color: white; border: none; cursor: pointer; }
                .btn:hover { background: #45a049; }
            </style>
        </head>
        <body>
            <h1>🚀 Cloudinary + Flask</h1>
            <p>API endpoints ready:</p>
            <ul>
                <li>POST /api/upload - העלה תמונה</li>
                <li>GET /api/transform/:id - טרנספורמציה</li>
                <li>DELETE /api/delete/:id - מחק</li>
                <li>GET /api/images - רשום</li>
                <li>POST /api/signature - חתימה</li>
            </ul>
            <button class="btn" onclick="alert('בדוק את ה-API endpoints בpostman או curl')">
                בדוק API
            </button>
        </body>
        </html>
    '''

if __name__ == '__main__':
    print('🚀 Flask server running on http://localhost:5000')
    print('📡 API: http://localhost:5000/api/*')
    app.run(debug=True)
