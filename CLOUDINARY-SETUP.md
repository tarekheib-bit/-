# 🚀 Cloudinary Setup Guide - Complete Instructions

**Last Updated:** September 20, 2026  
**Status:** Ready for Implementation

---

## 📋 Table of Contents

1. [Before You Start](#before-you-start)
2. [Step 1: Create Cloudinary Account](#step-1-create-cloudinary-account)
3. [Step 2: Get Your Credentials](#step-2-get-your-credentials)
4. [Step 3: Set Up Environment Variables](#step-3-set-up-environment-variables)
5. [Step 4: Choose Your Framework](#step-4-choose-your-framework)
6. [Step 5: Install SDK](#step-5-install-sdk)
7. [Step 6: Configure Your App](#step-6-configure-your-app)
8. [Step 7: Test Integration](#step-7-test-integration)

---

## ✅ Before You Start

You have:
- ✅ MCP servers configured (`.mcp.json`)
- ✅ Cloudinary skills installed (`.claude/skills/cloudinary-*`)
- ✅ `.env.example` template ready
- ✅ Multi-framework support

You need:
- ⏳ A Cloudinary account (free or paid)
- ⏳ 5 minutes to set it up

---

## Step 1: Create Cloudinary Account

### Option A: Free Account (Recommended for Getting Started)

1. Go to: https://cloudinary.com/users/register_free
2. Sign up with your email
3. Confirm email
4. You now have a free Cloudinary account!

**Free tier includes:**
- 25 GB storage
- 25 GB bandwidth/month
- Unlimited transformations
- All core features

### Option B: Claimable Cloud (No Signup Required)

If you want to try without signing up:

```bash
cd "C:\Users\USER\OneDrive\שולחן העבודה\AI DEV FOCUS AI"
npx @cloudinary/cloud
```

This creates a temporary cloud you can claim later with your email.

---

## Step 2: Get Your Credentials

1. Log in to Cloudinary Console: https://console.cloudinary.com
2. Go to **Settings → API Keys**
3. You'll see:
   - **Cloud Name** - Your unique identifier
   - **API Key** - Public key for API calls
   - **API Secret** - Private key (keep secure!)

**IMPORTANT:** 
- ⚠️ Never share your API Secret
- ⚠️ Keep it only in `.env` file
- ⚠️ Add `.env` to `.gitignore`

---

## Step 3: Set Up Environment Variables

### 3A: Create Your `.env` File

```bash
# Navigate to project folder
cd "C:\Users\USER\OneDrive\שולחן העבודה\AI DEV FOCUS AI"

# Copy the template
copy .env.example .env
```

### 3B: Edit `.env` With Your Credentials

Open `.env` and fill in:

```
# Cloudinary Credentials (from API Keys page)
CLOUDINARY_CLOUD_NAME=your_cloud_name_here
CLOUDINARY_API_KEY=your_api_key_here
CLOUDINARY_API_SECRET=your_api_secret_here

# Optional: Framework-specific (uncomment as needed)
# VITE_CLOUDINARY_CLOUD_NAME=your_cloud_name  # React/Vite
# NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME=your_cloud  # Next.js
```

### 3C: Verify `.env` is in `.gitignore`

Check that `.gitignore` contains:
```
.env
.env.local
.env.*.local
```

If not, add it!

---

## Step 4: Choose Your Framework

Pick the one you'll use:

| Framework | File | Install Command |
|-----------|------|-----------------|
| **Node.js/Express** | `configs/nodejs-setup.md` | `npm install cloudinary express-fileupload dotenv` |
| **Python/Flask** | `configs/python-flask-setup.md` | `pip install cloudinary python-dotenv flask` |
| **Python/Django** | `configs/python-django-setup.md` | `pip install cloudinary python-dotenv django` |
| **React** | `configs/react-setup.md` | `npm install @cloudinary/react @cloudinary/url-gen` |
| **Vue** | `configs/vue-setup.md` | `npm install @cloudinary/vue cloudinary` |
| **Next.js** | `cloudinary-next skill` | `npm install next-cloudinary cloudinary` |
| **Multiple** | See each config | Install multiple SDKs |

---

## Step 5: Install SDK

### For Node.js/Express:
```bash
npm install cloudinary dotenv express-fileupload
npm install -D nodemon  # For development
```

### For Python:
```bash
pip install cloudinary python-dotenv
pip install flask  # If using Flask
# OR
pip install django  # If using Django
```

### For React/Vue/Angular:
```bash
npm install @cloudinary/react @cloudinary/url-gen
# OR
npm install @cloudinary/vue cloudinary
```

---

## Step 6: Configure Your App

### Node.js Example:

```javascript
// app.js
require('dotenv').config();
const cloudinary = require('cloudinary').v2;

cloudinary.config({
    cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
    api_key: process.env.CLOUDINARY_API_KEY,
    api_secret: process.env.CLOUDINARY_API_SECRET
});

console.log('✅ Cloudinary configured:', cloudinary.config().cloud_name);
```

### Python Example:

```python
# app.py
import os
from dotenv import load_dotenv
import cloudinary

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

print('✅ Cloudinary configured:', cloudinary.config()['cloud_name'])
```

### React Example:

```javascript
// main.jsx
import { CldProvider } from '@cloudinary/react';

export default function App() {
    return (
        <CldProvider cloud={{ 
            cloudName: import.meta.env.VITE_CLOUDINARY_CLOUD_NAME 
        }}>
            {/* Your app */}
        </CldProvider>
    );
}
```

---

## Step 7: Test Integration

### Test 1: Verify Configuration

```bash
# Node.js
node -e "require('dotenv').config(); const c = require('cloudinary').v2; console.log('Cloud Name:', c.config().cloud_name)"

# Python
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Cloud Name:', os.getenv('CLOUDINARY_CLOUD_NAME'))"
```

### Test 2: Upload a Test Image

**Node.js:**
```javascript
cloudinary.uploader.upload('test.jpg', {
    public_id: 'test-upload',
    folder: 'test'
}, (err, result) => {
    if (err) console.error(err);
    else console.log('✅ Upload successful:', result.secure_url);
});
```

**Python:**
```python
result = cloudinary.uploader.upload('test.jpg', 
    public_id='test-upload',
    folder='test'
)
print('✅ Upload successful:', result['secure_url'])
```

### Test 3: Generate a Transformed URL

**Node.js:**
```javascript
const url = cloudinary.url('test-upload', {
    transformation: [
        { width: 400, height: 300, crop: 'fill' },
        { quality: 'auto' }
    ]
});
console.log('Transformed URL:', url);
```

**Python:**
```python
from cloudinary.utils import cloudinary_url

url, _ = cloudinary_url('test-upload', 
    transformation=[
        {'width': 400, 'height': 300, 'crop': 'fill'},
        {'quality': 'auto'}
    ]
)
print('Transformed URL:', url)
```

---

## 🎯 Common Issues & Solutions

### Issue: "Cannot find module 'cloudinary'"
**Solution:** Install SDK: `npm install cloudinary` or `pip install cloudinary`

### Issue: "CLOUDINARY_CLOUD_NAME is undefined"
**Solution:** Make sure `.env` is created and filled with real values, not placeholders

### Issue: "MCP server won't connect"
**Solution:** Restart Claude Code after updating `.env` with real credentials

### Issue: "API calls return 401 Unauthorized"
**Solution:** Check your API Key and API Secret are correct (not swapped)

---

## 📚 Framework-Specific Guides

After setup, read the framework config:

- **Node.js/Express**: `configs/nodejs-setup.md`
- **Python/Flask**: `configs/python-flask-setup.md`
- **Python/Django**: `configs/python-django-setup.md`
- **React**: `configs/react-setup.md`
- **Vue**: `configs/vue-setup.md`
- **Next.js**: Use `cloudinary-next` skill in Claude Code

---

## ✅ Verification Checklist

After setup, verify:

- [ ] `.env` file created in project root
- [ ] `.env` filled with real Cloudinary credentials
- [ ] `.env` is in `.gitignore`
- [ ] SDK installed (`npm install` or `pip install`)
- [ ] Configuration code added to app
- [ ] Test upload successful
- [ ] Transformed URL generated
- [ ] MCP servers can connect

---

## 🚀 Next Steps

1. ✅ Complete this guide
2. ✅ Read your framework-specific guide
3. ✅ Add upload functionality to your app
4. ✅ Integrate image transformations
5. ✅ Deploy with Cloudinary!

---

## 📞 Resources

- **Cloudinary Console**: https://console.cloudinary.com
- **API Documentation**: https://cloudinary.com/documentation/cloudinary_api
- **SDK Guides**: https://cloudinary.com/documentation/libraries
- **Transformation Reference**: https://cloudinary.com/documentation/transformation_reference

---

**You're all set! 🎉 Start with your framework-specific guide.**

---

*Complete Cloudinary setup guide | Version 1.0*
