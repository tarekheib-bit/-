# N8N Setup Guide - Clinic Ella Lead Form Integration

## 📋 שלבים להקמת הזרימה

### שלב 1: יצירת Google Sheet

1. **עבור ל-Google Sheets:**
   - https://sheets.google.com
   - לחץ "צור ספר חדש"
   - שנה שם ל: "Clinic Ella Leads"

2. **צור כותרות לגליון (שורה ראשונה):**
   - A1: `timestamp`
   - B1: `name`
   - C1: `phone`
   - D1: `email`
   - E1: `service`
   - F1: `message`
   - G1: `status`

3. **שתול את הגליון:**
   - עתק את ה-URL של הגליון (יש לך בעורך, כל הדבר עם `/spreadsheets/d/...`)
   - שתול את ה-ID: החלק בין `/d/` ו-`/edit`
   - דוגמה: `1fB8kK2vJ9_xL4mN5pQ6rS7tU8vW9xY0z`

---

### שלב 2: הקמת N8N Workflow

#### 2a. יצירת Webhook Trigger (ידנית)

1. **היכנסו ל-N8N:**
   - https://n8n.cloud/ (או server שלך)
   - צור workflow חדש

2. **הוסף Webhook:**
   - לחץ "+" בשורה הראשונה
   - חפש "Webhook"
   - בחר "Webhook"
   - בחר Method: `POST`
   - לחץ "Save"
   - **עתק את ה-URL של ה-webhook** (צריך להיות משהו כמו `https://your-n8n.com/webhook/abc123`)

3. **עדכן את ה-HTML:**
   - פתח `clinic-ella-landing.html`
   - חפש `const webhookUrl = 'YOUR_N8N_WEBHOOK_URL';`
   - החלף עם ה-webhook URL שלך

---

#### 2b. Automation Flow (5 צמתים)

**בנה את התזרים הזה בN8N:**

```
Webhook (In) 
    ↓
Google Sheets (Append Row)
    ↓
Send Email / Notification (Optional)
    ↓
HTTP Request (Return Success)
```

**צמתים מפורטים:**

##### צומת 1: Webhook
- ✅ כבר יצרת (שלב 2a)
- תוצאה: `body` עם כל הנתונים (name, phone, email, service, message, timestamp)

##### צומת 2: Google Sheets - Append Row
1. לחץ "+" → חפש "Google Sheets"
2. בחר "Append a Row"
3. Authenticate Google Account
4. בחר:
   - **Spreadsheet ID:** הדביקו את ה-ID מ-Google Sheet
   - **Sheet Name:** `Sheet1` (או השם של הגליון)
   
5. **מיפוי שדות (Column Mapping):**
   - ספקו את המידע באופן הבא עבור כל שורה:
   ```
   A (timestamp):  {{ $node.Webhook.json.timestamp }}
   B (name):       {{ $node.Webhook.json.name }}
   C (phone):      {{ $node.Webhook.json.phone }}
   D (email):      {{ $node.Webhook.json.email }}
   E (service):    {{ $node.Webhook.json.service }}
   F (message):    {{ $node.Webhook.json.message }}
   G (status):     "pending"
   ```

##### צומת 3 (Optional): Send Email Notification
1. לחץ "+" → חפש "Gmail" או "Mailgun"
2. בחר "Send Email"
3. הגדרו:
   ```
   To: alaemail@example.com
   Subject: "ליד חדש מהניחתה: {{ $node.Webhook.json.name }}"
   Body: |
     שלום אלה,
     
     ליד חדש נרשם:
     - שם: {{ $node.Webhook.json.name }}
     - טלפון: {{ $node.Webhook.json.phone }}
     - דוא"ל: {{ $node.Webhook.json.email }}
     - שירות: {{ $node.Webhook.json.service }}
     
     תודה!
   ```

##### צומת 4: HTTP Request - Return Success
1. לחץ "+" → חפש "HTTP Request"
2. בחר "HTTP Request"
3. הגדרו:
   - **Method:** `POST`
   - **URL:** (השאר ריק או הגדר endpoint מקומי)
   - **Body Type:** JSON
   - **Body:**
   ```json
   {
     "success": true,
     "message": "ליד נקלט בהצלחה",
     "leadId": "{{ $node['Google Sheets'].json[0].values[0] }}"
   }
   ```

---

### שלב 3: בדיקת הזרימה

#### בדיקה A: בדיקת Webhook
1. בN8N, לחץ על הצומת "Webhook"
2. לחץ "Test" ב-Inspector
3. שלח POST request (שימוש ב-Postman או curl):

```bash
curl -X POST https://your-n8n-webhook-url \
  -H "Content-Type: application/json" \
  -d '{
    "name": "תמר כהן",
    "phone": "050-1234567",
    "email": "tamar@example.com",
    "service": "בוטוקס",
    "message": "בדיקה",
    "timestamp": "2026-09-20T10:00:00Z"
  }'
```

#### בדיקה B: בדיקה במלאות
1. פתח את `clinic-ella-landing.html` בדפדפן
2. מלא את הטופס
3. לחץ "שליחת בקשה"
4. בדוק את Google Sheet האם השורה הוספה

---

### שלב 4: Automation Builder - יצירת Temporary Trigger

(אם אתה רוצה אוטומציה זמנית ידנית)

1. בN8N, לחץ "Automation" (או תפריט דומה)
2. לחץ "Create New Automation"
3. בחר "Manual Trigger"
4. חבר לצומת "Google Sheets - Create Sheet" או update existing
5. שמור עם שם: "Setup Clinic Ella Leads Sheet"
6. הפעל פעם אחת כדי להגדיר

---

## 🔍 Debugging

אם משהו לא עובד:

1. **Webhook לא מקבל נתונים:**
   - בדוק את ה-URL בHTML
   - וודא שהוא בדיוק כמו בN8N
   - בדוק את ה-Browser Console (F12) for errors

2. **Google Sheets לא מתעדכן:**
   - בדוק אימות Google
   - וודא Sheet ID נכון
   - וודא Column mapping מתאים

3. **סטטוס 403 (Forbidden):**
   - ודא שה-Google account יש גישה לSheet
   - בדוק אימות ב-N8N

---

## 📊 תוצאה סופית

כאשר הכל עובד, תוכל לראות:
- ✅ טופס HTML שולח נתונים ל-N8N
- ✅ N8N מקבל webhook
- ✅ נתונים נשמרים ב-Google Sheet
- ✅ הודעת תודה מופיעה ל-לקוח
- ✅ (Optional) אלה קיבלה הודעת דוא"ל על הליד

---

## 🔗 פקודות מהירות

**בדיקת Webhook עם curl:**
```bash
curl -X POST YOUR_WEBHOOK_URL -H "Content-Type: application/json" -d '{"name":"test","phone":"050-1234567"}'
```

**בדיקת Google Sheet:**
- פתח את https://sheets.google.com
- בדוק שורות חדשות מופיעות

**בדיקת N8N Logs:**
- בN8N, לחץ "Executions"
- בדוק משימות אחרונות

---

## 📝 ערכים צפויים בGoogle Sheet

| timestamp | name | phone | email | service | message | status |
|-----------|------|-------|-------|---------|---------|--------|
| 2026-09-20T10:15:00Z | דנה כהן | 050-1234567 | dana@example.com | בוטוקס | אני חדשה | pending |

---

צוות אלה - מוקדש להצלחתך! 💚
