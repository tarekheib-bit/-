# Python/Flask - Cloudinary Setup

**Framework:** Flask  
**SDK:** cloudinary (v1.30+)  
**Updated:** September 2026

---

## 📦 Installation

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install cloudinary flask python-dotenv flask-cors
```

---

## ⚙️ Configuration

Create `app.py`:

```python
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import cloudinary
import cloudinary.uploader

load_dotenv()

app = Flask(__name__)
CORS(app)

# Cloudinary config
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

print('✅ Cloudinary configured:', cloudinary.config()['cloud_name'])

@app.route('/api/upload', methods=['POST'])
def upload():
    try:
        file = request.files['image']
        result = cloudinary.uploader.upload(file, folder='my-app')
        return jsonify({
            'success': True,
            'url': result['secure_url']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/transform', methods=['GET'])
def transform():
    url = cloudinary.utils.cloudinary_url('sample-image', 
        transformation=[
            {'width': 400, 'height': 300, 'crop': 'fill'},
            {'quality': 'auto'}
        ]
    )[0]
    return jsonify({'url': url})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🚀 Usage Examples

### Upload File
```python
result = cloudinary.uploader.upload('path/to/image.jpg',
    public_id='my-image',
    folder='uploads'
)
print(result['secure_url'])
```

### Transform URL
```python
from cloudinary.utils import cloudinary_url

url, options = cloudinary_url('my-image',
    transformation=[
        {'width': 800, 'height': 600, 'crop': 'fill'},
        {'effect': 'sepia'},
        {'quality': 'auto', 'fetch_format': 'auto'}
    ]
)
```

### Delete File
```python
result = cloudinary.uploader.destroy('public_id')
print(result)
```

---

## 🧪 Testing

```bash
# Activate venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Start Flask
python app.py

# In another terminal, test upload
curl -X POST http://localhost:5000/api/upload -F "image=@test.jpg"

# Test transform
curl http://localhost:5000/api/transform
```

---

See `CLOUDINARY-SETUP.md` for environment setup.
