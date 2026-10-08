# 🚀 4 Cloudinary Starter Projects

**כל פרויקט מוכן לתחילה מידית עם Cloudinary!**

---

## 📁 Projects Overview

### 1. **Node.js/Express** (Backend API)
📂 `01-nodejs-express/`

✅ Express server  
✅ Upload API  
✅ Transform API  
✅ Delete API  
✅ List images API  

**Start:**
```bash
cd 01-nodejs-express
npm install
npm run dev
```

**URL:** http://localhost:3000

---

### 2. **Python/Flask** (Backend Web)
📂 `02-python-flask/`

✅ Flask web app  
✅ Upload endpoint  
✅ Transform endpoint  
✅ Delete endpoint  
✅ List images API  

**Start:**
```bash
cd 02-python-flask
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python app.py
```

**URL:** http://localhost:5000

---

### 3. **React/Vite** (Frontend)
📂 `03-react-vite/`

✅ React UI  
✅ Upload functionality  
✅ Image display  
✅ Responsive design  
✅ Automatic optimization  

**Start:**
```bash
cd 03-react-vite
npm install
npm run dev
```

**URL:** http://localhost:5173

---

### 4. **Next.js** (Full-Stack)
📂 `04-nextjs/`

✅ Next.js full-stack  
✅ Server components  
✅ Client components  
✅ Upload widget  
✅ Responsive design  

**Start:**
```bash
cd 04-nextjs
npm install
npm run dev
```

**URL:** http://localhost:3000

---

## 🔑 Configuration for All Projects

### Step 1: Get Credentials
1. Go to: https://console.cloudinary.com/settings/api-keys
2. Copy: Cloud Name, API Key, API Secret

### Step 2: Set Environment Variables
Each project has `.env.example` - copy and edit:

**Node.js/Express:** Create `.env`
```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

**Python/Flask:** Create `.env`
```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

**React/Vite:** Create `.env.local`
```
VITE_CLOUDINARY_CLOUD_NAME=your_cloud_name
VITE_CLOUDINARY_API_KEY=your_api_key
```

**Next.js:** Create `.env.local`
```
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### Step 3: Install Dependencies
Each has `package.json` or `requirements.txt` - just run:
```bash
npm install      # Node.js projects
pip install -r requirements.txt  # Python
```

### Step 4: Run the Project
```bash
npm run dev      # Node.js/React/Next.js
python app.py    # Flask
```

---

## 🎯 Key Features by Project

| Feature | Node.js | Flask | React | Next.js |
|---------|---------|-------|-------|---------|
| Upload API | ✅ | ✅ | ✅ | ✅ |
| Transform API | ✅ | ✅ | ✅ | ✅ |
| Delete API | ✅ | ✅ | - | - |
| List Images | ✅ | ✅ | - | - |
| Web UI | - | ✅ | ✅ | ✅ |
| Full-Stack | - | ✅ | - | ✅ |
| Production Ready | ✅ | ✅ | ✅ | ✅ |

---

## 💡 Common Tasks

### Upload an Image
**Node.js:**
```bash
curl -X POST http://localhost:3000/api/upload -F "image=@photo.jpg"
```

**React:**
Use the file input to upload via widget

**Next.js:**
Use the CldUploadWidget component

### Get Transformed URL
**Node.js:**
```bash
curl http://localhost:3000/api/transform/public_id?width=400&height=300
```

**React/Next.js:**
URLs are automatically optimized with `format="auto"` and `quality="auto"`

### Delete Image
**Node.js:**
```bash
curl -X DELETE http://localhost:3000/api/delete/public_id
```

---

## 📚 Project Structure

Each project includes:
- ✅ Complete code examples
- ✅ Hebrew comments
- ✅ README with instructions
- ✅ .env.example template
- ✅ Ready to run

```
01-nodejs-express/
├── app.js          (Main server)
├── package.json    (Dependencies)
└── README.md       (Instructions)

02-python-flask/
├── app.py          (Main app)
├── requirements.txt (Dependencies)
└── README.md       (Instructions)

03-react-vite/
├── src/App.jsx     (Main component)
├── package.json    (Dependencies)
└── README.md       (Instructions)

04-nextjs/
├── app/page.jsx    (Main page)
├── package.json    (Dependencies)
└── README.md       (Instructions)
```

---

## 🚀 Next Steps After Setup

1. ✅ Run one project
2. ✅ Upload a test image
3. ✅ See it in your Cloudinary dashboard
4. ✅ Modify code to match your needs
5. ✅ Deploy when ready!

---

## 🔐 Security Reminders

- ⚠️ NEVER commit `.env` files
- ⚠️ Keep API_SECRET secret (server-only)
- ⚠️ Use CLOUD_NAME in frontend (public)
- ⚠️ Regenerate keys if exposed
- ⚠️ Use signed URLs for sensitive images

---

## 📞 Support

- **Cloudinary Docs:** https://cloudinary.com/documentation
- **Framework Docs:**
  - Node.js: https://nodejs.org/
  - Flask: https://flask.palletsprojects.com/
  - React: https://react.dev/
  - Next.js: https://nextjs.org/

---

## ✅ Checklist

Before starting:
- [ ] Cloudinary account created
- [ ] API credentials ready
- [ ] Node.js installed (for JS projects)
- [ ] Python installed (for Flask)
- [ ] .env files configured
- [ ] Dependencies installed

---

**Pick a project and start building!** 🎉

Each project is a complete, working example that you can modify and build upon.

---

*4 Cloudinary Starter Projects | September 2026*
