# Next.js + Cloudinary

**מעולה!** זה ה-starter project שלך עם Cloudinary ו-Next.js.

## 🚀 התחלה מהירה

### 1. Install
```bash
npm install
```

### 2. Configure
```bash
cp .env.example .env.local
# ערוך את ה-.env.local עם הפרטים שלך
```

### 3. Run
```bash
npm run dev
```

### 4. Open
```
http://localhost:3000
```

## 🔑 Setup

1. הכנס ל-Cloudinary Console
2. יצור unsigned upload preset
3. עדכן את ה-.env.local

## 💡 Features

- ✅ Upload widget
- ✅ Display images
- ✅ Automatic optimization
- ✅ Responsive design
- ✅ Server & Client components

## 📚 Next Steps

1. יצור API routes ב-app/api/
2. הוסף delete functionality
3. יצור image gallery

```bash
# Create API routes
mkdir -p app/api/upload
mkdir -p app/api/delete
mkdir -p app/api/images
```

## 🎯 Example API Routes

```javascript
// app/api/upload/route.js
import cloudinary from 'cloudinary'

export async function POST(req) {
  const data = await req.json()
  // Handle upload
}
```
