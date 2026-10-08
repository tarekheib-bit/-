# React/Vite - Cloudinary Setup

**Framework:** React with Vite  
**SDK:** @cloudinary/react + @cloudinary/url-gen  
**Updated:** September 2026

---

## 📦 Installation

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install @cloudinary/react @cloudinary/url-gen dotenv
npm run dev
```

---

## ⚙️ Configuration

### 1. Create `.env.local`:

```
VITE_CLOUDINARY_CLOUD_NAME=your_cloud_name
```

### 2. Update `main.jsx`:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { CldProvider } from '@cloudinary/react'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <CldProvider cloud={{ 
      cloudName: import.meta.env.VITE_CLOUDINARY_CLOUD_NAME 
    }}>
      <App />
    </CldProvider>
  </React.StrictMode>,
)
```

---

## 🚀 Usage Examples

### Display Image with Transformation

```jsx
import { CldImage } from '@cloudinary/react'

export default function App() {
  return (
    <div>
      <CldImage
        src="sample-image"
        width={400}
        height={300}
        crop="fill"
        quality="auto"
      />
    </div>
  )
}
```

### Build URL Programmatically

```jsx
import { CldImage } from '@cloudinary/react'
import { Cloudinary } from '@cloudinary/url-gen'

const cld = new Cloudinary({
  cloud: { cloudName: import.meta.env.VITE_CLOUDINARY_CLOUD_NAME }
})

export default function App() {
  const url = cld.image('sample').format('auto').quality('auto').toURL()
  
  return <img src={url} alt="optimized" />
}
```

### Upload Widget

```jsx
import { CldUploadWidget } from '@cloudinary/react'

export default function UploadForm() {
  return (
    <CldUploadWidget uploadPreset="my-preset">
      {({ open }) => (
        <button onClick={() => open()}>
          Upload Image
        </button>
      )}
    </CldUploadWidget>
  )
}
```

---

## 🧪 Testing

```bash
npm run dev
# Visit http://localhost:5173
```

---

See `CLOUDINARY-SETUP.md` for environment setup.
