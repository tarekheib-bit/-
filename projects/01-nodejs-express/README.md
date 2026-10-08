# Node.js/Express + Cloudinary

**מעולה!** זה ה-starter project שלך עם Cloudinary ו-Express.

## 🚀 התחלה מהירה

### 1. Install
```bash
npm install
```

### 2. Configure
עדכן את ה-.env עם הפרטים שלך

### 3. Run
```bash
npm run dev
```

### 4. Test
```bash
curl -X POST http://localhost:3000/api/upload -F "image=@test.jpg"
```

## 📚 API Endpoints

| Method | Endpoint | תיאור |
|--------|----------|-------|
| POST | `/api/upload` | העלה תמונה |
| GET | `/api/transform/:id` | טרנספורמציה |
| DELETE | `/api/delete/:id` | מחק |
| GET | `/api/images` | רשום |
| POST | `/api/signature` | חתימה |

## 💡 דוגמאות

```bash
# Upload
curl -X POST http://localhost:3000/api/upload -F "image=@photo.jpg"

# Transform
curl http://localhost:3000/api/transform/public_id?width=800&height=600

# Delete
curl -X DELETE http://localhost:3000/api/delete/public_id

# List
curl http://localhost:3000/api/images
```
