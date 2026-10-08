# Node.js/Express - Cloudinary Setup

**Framework:** Node.js with Express  
**SDK:** cloudinary (v1.30+)  
**Updated:** September 2026

---

## 📦 Installation

```bash
npm init -y
npm install cloudinary express express-fileupload dotenv cors
npm install -D nodemon
```

Update `package.json`:
```json
{
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js"
  }
}
```

---

## ⚙️ Configuration

Create `app.js`:

```javascript
require('dotenv').config();
const express = require('express');
const cloudinary = require('cloudinary').v2;
const fileUpload = require('express-fileupload');
const cors = require('cors');

const app = express();

// Cloudinary config
cloudinary.config({
    cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
    api_key: process.env.CLOUDINARY_API_KEY,
    api_secret: process.env.CLOUDINARY_API_SECRET
});

// Middleware
app.use(express.json());
app.use(fileUpload());
app.use(cors());

console.log('✅ Cloudinary configured:', cloudinary.config().cloud_name);

// Routes
app.post('/api/upload', async (req, res) => {
    try {
        const file = req.files.image;
        const result = await cloudinary.uploader.upload(file.tempFilePath, {
            folder: 'my-app'
        });
        res.json({ success: true, url: result.secure_url });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.get('/api/transform', (req, res) => {
    const url = cloudinary.url('sample-image', {
        transformation: [
            { width: 400, height: 300, crop: 'fill' },
            { quality: 'auto' }
        ]
    });
    res.json({ url });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

---

## 🚀 Usage Examples

### Upload File
```javascript
const result = await cloudinary.uploader.upload('path/to/image.jpg', {
    public_id: 'my-image',
    folder: 'uploads'
});
console.log(result.secure_url);
```

### Transform URL
```javascript
const url = cloudinary.url('my-image', {
    transformation: [
        { width: 800, height: 600, crop: 'fill' },
        { effect: 'sepia' },
        { quality: 'auto', fetch_format: 'auto' }
    ]
});
```

### Delete File
```javascript
const result = await cloudinary.uploader.destroy('public_id');
console.log(result);
```

---

## 🧪 Testing

```bash
# Start server
npm run dev

# Test upload (in another terminal)
curl -X POST http://localhost:3000/api/upload -F "image=@test.jpg"

# Test transform
curl http://localhost:3000/api/transform
```

---

See `CLOUDINARY-SETUP.md` for environment setup.
