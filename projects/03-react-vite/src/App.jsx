// React/Vite - Cloudinary Integration
// כל דבר שאתה צריך כדי להתחיל עם Cloudinary ו-React

import { useState } from 'react'
import { CldImage } from '@cloudinary/react'
import { Cloudinary } from '@cloudinary/url-gen'
import axios from 'axios'
import './App.css'

// Initialize Cloudinary
const cld = new Cloudinary({
  cloud: { cloudName: import.meta.env.VITE_CLOUDINARY_CLOUD_NAME }
})

export default function App() {
  const [image, setImage] = useState(null)
  const [uploading, setUploading] = useState(false)
  const [error, setError] = useState(null)
  const [transformUrl, setTransformUrl] = useState(null)

  // 1️⃣ Handle Upload
  const handleUpload = async (e) => {
    const file = e.target.files[0]
    if (!file) return

    setUploading(true)
    setError(null)

    try {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('upload_preset', 'unsigned_preset') // צריך להגדיר ב-Cloudinary
      formData.append('cloud_name', import.meta.env.VITE_CLOUDINARY_CLOUD_NAME)

      const response = await axios.post(
        `https://api.cloudinary.com/v1_1/${import.meta.env.VITE_CLOUDINARY_CLOUD_NAME}/image/upload`,
        formData
      )

      setImage(response.data)

      // Generate transformed URL
      const url = cld.image(response.data.public_id)
        .resize(400, 300)
        .format('auto')
        .quality('auto')
        .toURL()

      setTransformUrl(url)
    } catch (err) {
      setError('שגיאה בהעלאה: ' + err.message)
    } finally {
      setUploading(false)
    }
  }

  return (
    <div className="container">
      <h1>🚀 Cloudinary + React</h1>

      {/* Upload Section */}
      <div className="upload-section">
        <h2>העלה תמונה</h2>
        <input
          type="file"
          accept="image/*"
          onChange={handleUpload}
          disabled={uploading}
        />
        {uploading && <p>🔄 מעלה...</p>}
        {error && <p className="error">❌ {error}</p>}
      </div>

      {/* Display Images */}
      {image && (
        <div className="results">
          <h2>תוצאות</h2>

          <div className="image-grid">
            {/* Original */}
            <div className="image-card">
              <h3>מקורי</h3>
              <CldImage
                src={image.public_id}
                width={300}
                height={300}
                alt="Original"
              />
              <p>גודל: {(image.bytes / 1024).toFixed(2)} KB</p>
            </div>

            {/* Transformed */}
            <div className="image-card">
              <h3>עם אופטימיזציה</h3>
              <img
                src={transformUrl}
                alt="Transformed"
                style={{ maxWidth: '300px', height: 'auto' }}
              />
              <p>✨ עם Cloudinary optimization</p>
            </div>
          </div>

          {/* Details */}
          <div className="details">
            <h3>פרטים</h3>
            <p><strong>Public ID:</strong> {image.public_id}</p>
            <p><strong>Secure URL:</strong> <code>{image.secure_url}</code></p>
            <p><strong>Format:</strong> {image.format}</p>
            <p><strong>Width:</strong> {image.width}px</p>
            <p><strong>Height:</strong> {image.height}px</p>
          </div>
        </div>
      )}
    </div>
  )
}
