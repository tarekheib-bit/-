# Python/Flask + Cloudinary

**מעולה!** זה ה-starter project שלך עם Cloudinary ו-Flask.

## 🚀 התחלה מהירה

### 1. Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 2. Install
```bash
pip install -r requirements.txt
```

### 3. Configure
עדכן את ה-.env עם הפרטים שלך

### 4. Run
```bash
python app.py
```

### 5. Test
```bash
curl -X POST http://localhost:5000/api/upload -F "image=@test.jpg"
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
curl -X POST http://localhost:5000/api/upload -F "image=@photo.jpg"

# Transform
curl http://localhost:5000/api/transform/public_id?width=800&height=600

# Delete
curl -X DELETE http://localhost:5000/api/delete/public_id

# List
curl http://localhost:5000/api/images
```
