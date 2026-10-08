/**
 * Clinic Ella Configuration
 * עדכן ערכים זה כדי להתאים לצרכים שלך
 */

const CLINIC_CONFIG = {
  // N8N Webhook Configuration
  n8n: {
    // החלף עם ה-URL של ה-webhook שלך מ-N8N
    webhookUrl: 'https://your-n8n-instance.com/webhook/clinic-ella-leads',
    // כדי לבדוק ללא N8N, החלף עם webhook.site URL
    // webhookUrl: 'https://webhook.site/your-unique-id',
    enabled: true
  },

  // Google Sheet Configuration
  googleSheet: {
    // בדוק את Google Sheets ID (בין /d/ ו-/edit ב-URL)
    spreadsheetId: 'YOUR_GOOGLE_SHEET_ID_HERE',
    sheetName: 'Sheet1'
  },

  // Clinic Information
  clinic: {
    name: 'קליניקה אלה',
    phone: '050-1234567', // עדכן עם מספר בפועל
    whatsappPhone: '972501234567', // בפורמט בינלאומי
    email: 'info@clinicella.co.il',
    timezone: 'Asia/Jerusalem'
  },

  // Form Settings
  form: {
    // זמן המתנה לפני הצגת הודעת תודה (במילישניות)
    successMessageDelay: 500,
    // כיתות CSS לעיצוב הודעה
    successMessageClass: 'success-message-clinic'
  },

  // Services (תואם לרשימה בטופס)
  services: {
    'botox': 'בוטוקס',
    'facial': 'טיפול פנים עמוק',
    'consultation': 'ייעוץ כללי',
    'other': 'אחר'
  },

  // Analytics (Optional - Google Analytics, Mixpanel, etc.)
  analytics: {
    enabled: false,
    googleAnalyticsId: 'UA-XXXXXXXXX-X',
    trackFormSubmission: true
  },

  // Email Notifications (Optional)
  notifications: {
    // השלח דוא"ל כאשר ליד חדש נרשם
    sendEmailOnNewLead: false,
    // כתובת ל-webhook שיכול לשלוח דוא"לים
    // דוגמה: https://api.sendgrid.com/v3/mail/send
    emailWebhookUrl: null
  },

  // Feature Flags
  features: {
    showSuccessMessage: true,
    redirectToWhatsapp: false, // לא מומלץ עם N8N
    showFormErrors: true,
    allowOfflineMode: true // אם N8N לא זמין, תראה הודעה
  },

  // Development/Debug
  debug: {
    enabled: false, // דפוס webhook POSTs ל-Console
    logNetworkRequests: false,
    simulateWebhookDelay: 0 // ms לבדיקה
  }
};

/**
 * Validation Helper
 */
function validateConfig() {
  const errors = [];

  if (CLINIC_CONFIG.n8n.webhookUrl === 'https://your-n8n-instance.com/webhook/clinic-ella-leads') {
    errors.push('⚠️ N8N Webhook URL לא מחובר - עדכן את config.js');
  }

  if (CLINIC_CONFIG.googleSheet.spreadsheetId === 'YOUR_GOOGLE_SHEET_ID_HERE') {
    errors.push('⚠️ Google Sheet ID לא מחובר - עדכן את config.js');
  }

  if (errors.length > 0) {
    console.warn('⚠️ Configuration Issues:');
    errors.forEach(error => console.warn(error));
    return false;
  }

  return true;
}

/**
 * Get Configuration Value
 * שימוש: getConfig('n8n.webhookUrl')
 */
function getConfig(path) {
  return path.split('.').reduce((obj, key) => obj?.[key], CLINIC_CONFIG);
}

// Validate on load
if (typeof window !== 'undefined') {
  window.addEventListener('load', () => {
    if (!validateConfig()) {
      console.log('הודעה: בדוק את config.js כדי להשלים את הגדרות האוטומציה');
    }
  });
}

// Export for use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CLINIC_CONFIG, validateConfig, getConfig };
}
