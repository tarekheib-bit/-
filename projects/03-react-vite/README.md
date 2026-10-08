# React/Vite + Cloudinary

**מעולה!** זה ה-starter project שלך עם Cloudinary ו-React.

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
http://localhost:5173
```

## 🔑 Setup Cloudinary

1. הכנס ל-Cloudinary Console
2. יצור unsigned upload preset
3. הוסף לשם שלך

## 💡 Features

- ✅ Upload images
- ✅ Display original & transformed
- ✅ Automatic optimization
- ✅ Responsive design

## 📚 דוגמאות בקוד

```jsx
// Display image
<CldImage src="public_id" width={300} height={300} />

// Transform URL
const url = cld.image('public_id')
  .resize(400, 300)
  .quality('auto')
  .toURL()
```
