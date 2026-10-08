# 🏥 Clinic Ella - Lead Form Integration Setup

דוד שלם לחיבור טופס הלידים של קליניקה אלה עם N8N ו-Google Sheets.

## 📋 תוכן הקבצים

```
clinic-ella-landing.html          ← הניחתה (עם webhook)
N8N_SETUP_GUIDE.md               ← הנחיות מפורטות ל-N8N
clinic-ella-n8n-workflow.json    ← Workflow JSON לייבוא
test_clinic_form_e2e.py          ← סקריפט בדיקה
upload_to_cloudinary.py          ← העלאת תמונות
update_landing_with_urls.py      ← עדכון URLs בHTML
```

---

## 🚀 Quick Start (15 דקות)

### 1️⃣ יצירת Google Sheet

```
1. עבור ל https://sheets.google.com
2. צור ספר חדש: "Clinic Ella Leads"
3. בשורה ראשונה, הוסף כותרות:
   A1: timestamp
   B1: name
   C1: phone
   D1: email
   E1: service
   F1: message
   G1: status
4. שמור את ה-Sheet ID (החלק בין /d/ ו-/edit)
```

---

### 2️⃣ התקנת N8N וחיבור Webhook

#### אפשרות A: N8N Cloud (הכי פשוט)
```
1. היכנסו ל https://n8n.cloud
2. צרו חשבון חדש (חינם)
3. צרו Workflow חדש
4. ייבאו את clinic-ella-n8n-workflow.json:
   - Click "Import"
   - בחרו את הקובץ
   - בחרו "Replace"
5. חברו Google account (לחץ "Authenticate")
6. הגדרו:
   - Google Sheet ID → הדביקו את ה-ID מ-Google Sheets
   - Webhook URL → תקבלו אחרי שתפעילו
```

#### אפשרות B: N8N Self-Hosted
```
# התקנה עם Docker
docker run -d \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# גישה
http://localhost:5678
```

---

### 3️⃣ עדכון HTML עם Webhook URL

```javascript
// בקובץ clinic-ella-landing.html, חפש:
const webhookUrl = 'YOUR_N8N_WEBHOOK_URL';

// החלף עם ה-URL של ה-webhook שקיבלת מ-N8N
// דוגמה:
const webhookUrl = 'https://n8n.your-domain.com/webhook/clinic-ella-leads';
```

---

### 4️⃣ בדיקה

```bash
# 1. ודא שהשרת פועל
python -m http.server 8000

# 2. בדוק את ה-form
open http://localhost:8000/clinic-ella-landing.html

# 3. מלא את הטופס ושלח

# 4. בדוק את Google Sheet - אם הנתונים הופיעו, הצלחת! ✅
```

---

## 🔧 Configuration Details

### Google Sheets Authentication

ב-N8N:
1. בצומת "Google Sheets", לחץ "Authenticate"
2. בחר את ה-Google Account שלך
3. אשר גישה
4. בחר את ה-Spreadsheet
5. בחר את ה-Sheet

### N8N Webhook Configuration

```
Method:     POST
Path:       clinic-ella-leads (אתה קובע)
URL Format: https://[your-n8n-domain]/webhook/clinic-ella-leads
```

### HTML Form Payload

כאשר המשתמש שולח את הטופס, N8N מקבל:

```json
{
  "name": "דנה כהן",
  "phone": "050-1234567",
  "email": "dana@example.com",
  "service": "בוטוקס",
  "message": "אני חדשה לטיפולים",
  "timestamp": "2026-09-20T10:15:30.000Z",
  "source": "clinic-ella-landing"
}
```

---

## 🧪 בדיקה End-to-End

### שימוש ב-WEBAPP TESTING

```bash
# בדיקה אוטומטית של הטופס
python test_clinic_form_e2e.py
```

יצרה:
- `clinic-form-before.png` - טופס ריק
- `clinic-form-filled.png` - טופס עם נתונים
- `clinic-form-result.png` - ההודעה אחרי הגשה

### בדיקה ידנית עם curl

```bash
# שלח webhook test
curl -X POST https://your-n8n-webhook-url \
  -H "Content-Type: application/json" \
  -d '{
    "name": "בדיקה",
    "phone": "050-0000000",
    "email": "test@example.com",
    "service": "בוטוקס",
    "message": "בדיקה",
    "timestamp": "2026-09-20T10:00:00Z"
  }'
```

---

## 📊 Expected Flow

```
User fills form
    ↓
Clicks "שליחת בקשה"
    ↓
HTML validates form
    ↓
Sends POST to N8N Webhook
    ↓
N8N receives data
    ↓
Appends row to Google Sheet
    ↓
Sets status = "pending"
    ↓
Returns success response
    ↓
HTML shows success message
    ↓
Lead appears in Google Sheet ✅
```

---

## 🐛 Troubleshooting

### בעיה: Webhook לא משדר נתונים

```
✓ בדוק שה-URL בHTML תואם ל-N8N
✓ וודא שהוא https (לא http)
✓ בדוק ב-N8N Logs אם יש errors
✓ בדוק Browser Console (F12) for errors
```

### בעיה: Google Sheet לא מתעדכן

```
✓ בדוק אימות Google
✓ ודא Sheet ID נכון
✓ בדוק permissions ב-Google Sheet
✓ בדוק ב-N8N את ה-Column Mapping
```

### בעיה: בטופס מופיעה שגיאה

```
✓ פתח Browser Console (F12)
✓ בדוק את ההודעה
✓ בדוק Network tab (request/response)
✓ בדוק שכל השדות מלאים
```

---

## 🔐 Security Notes

1. **Webhook URL:**
   - לא תשתול בקבצי סודיים
   - השתמש ב-HTTPS בלבד
   - שקול להוסיף אימות (bearer token)

2. **Google Sheets:**
   - בדוק permissions
   - אל תשתול sensitive API keys בHTML
   - השתמש ב-Service Account ל-production

3. **N8N:**
   - הפעל עם SSL/TLS
   - סגור את HTTP port
   - הגדר strong credentials

---

## 📝 Next Steps

- [ ] יצירת Google Sheet
- [ ] התקנת N8N
- [ ] ייבוא Workflow
- [ ] חיבור Google Account
- [ ] עדכון HTML עם Webhook URL
- [ ] בדיקה דרך הטופס
- [ ] בדיקה ש-Google Sheet התעדכנה
- [ ] הפעלה ב-Production

---

## 📞 Support

אם יש בעיות:
1. בדוק את N8N_SETUP_GUIDE.md לפרטים מלאים
2. בדוק את Logs ב-N8N
3. בדוק את Browser Console
4. נסה את curl test כדי לבדוק webhook

---

**אל תשכח:** אחרי שהכל עובד, שנה את ה-Webhook URL מה-test ל-production! 🚀
