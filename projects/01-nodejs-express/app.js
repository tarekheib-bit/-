// Node.js/Express - Cloudinary Integration
// כל הדברים שאתה צריך כדי להתחיל עם Cloudinary ו-Express

require('dotenv').config();
const express = require('express');
const fileUpload = require('express-fileupload');
const cloudinary = require('cloudinary').v2;
const cors = require('cors');

const app = express();

// ⚙️ Cloudinary Configuration
cloudinary.config({
    cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
    api_key: process.env.CLOUDINARY_API_KEY,
    api_secret: process.env.CLOUDINARY_API_SECRET
});

// Middleware
app.use(express.json());
app.use(fileUpload());
app.use(cors());
app.use(express.static('public'));

console.log('✅ Cloudinary configured:', cloudinary.config().cloud_name);

// ============================================
// ROUTES - מסלולים
// ============================================

// 1️⃣ Upload Image - העלה תמונה
app.post('/api/upload', async (req, res) => {
    try {
        if (!req.files || !req.files.image) {
            return res.status(400).json({ error: 'אין קובץ להעלות' });
        }

        const file = req.files.image;

        // העלה ל-Cloudinary
        const result = await cloudinary.uploader.upload(file.tempFilePath, {
            public_id: req.body.public_id || undefined,
            folder: 'my-app/uploads',
            resource_type: 'auto'
        });

        res.json({
            success: true,
            url: result.secure_url,
            public_id: result.public_id
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 2️⃣ Get Transformed Image - קבל תמונה עם טרנספורמציה
app.get('/api/transform/:public_id', (req, res) => {
    try {
        const { public_id } = req.params;
        const { width = 400, height = 300 } = req.query;

        const url = cloudinary.url(public_id, {
            transformation: [
                {
                    width: parseInt(width),
                    height: parseInt(height),
                    crop: 'fill'
                },
                { quality: 'auto' },
                { fetch_format: 'auto' }
            ]
        });

        res.json({ url });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 3️⃣ Delete Image - מחק תמונה
app.delete('/api/delete/:public_id', async (req, res) => {
    try {
        const { public_id } = req.params;
        const result = await cloudinary.uploader.destroy(public_id);

        res.json({
            success: true,
            message: 'תמונה נמחקה בהצלחה',
            result
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 4️⃣ List Images - רשום תמונות
app.get('/api/images', async (req, res) => {
    try {
        const result = await cloudinary.api.resources({
            type: 'upload',
            prefix: 'my-app/uploads',
            max_results: 10
        });

        res.json({
            images: result.resources,
            total: result.total_count
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 5️⃣ Generate Signature - יצור חתימה להעלאה מחתום
app.post('/api/signature', (req, res) => {
    try {
        const timestamp = Math.round(new Date().getTime() / 1000);

        const signature = cloudinary.utils.api_sign_request({
            timestamp: timestamp,
            folder: 'my-app/signed-uploads'
        }, process.env.CLOUDINARY_API_SECRET);

        res.json({
            signature,
            timestamp,
            cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
            api_key: process.env.CLOUDINARY_API_KEY
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 6️⃣ Home Route
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>Cloudinary + Express</title>
            <style>
                body { font-family: Arial; max-width: 600px; margin: 50px auto; }
                .btn { padding: 10px 20px; background: #4CAF50; color: white; border: none; cursor: pointer; }
                .btn:hover { background: #45a049; }
            </style>
        </head>
        <body>
            <h1>🚀 Cloudinary + Express</h1>
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
    `);
});

// Start Server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
    console.log(`📡 API: http://localhost:${PORT}/api/*`);
});
