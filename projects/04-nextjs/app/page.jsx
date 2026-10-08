// Next.js + Cloudinary Integration
// כל דבר שאתה צריך כדי להתחיל עם Cloudinary ו-Next.js

'use client'

import { useState } from 'react'
import { CldImage, CldUploadWidget } from 'next-cloudinary'
import styles from './page.module.css'

export default function Home() {
  const [uploadedImage, setUploadedImage] = useState(null)
  const [error, setError] = useState(null)

  const handleUploadSuccess = (result) => {
    setUploadedImage({
      public_id: result.info.public_id,
      secure_url: result.info.secure_url,
      width: result.info.width,
      height: result.info.height,
      bytes: result.info.bytes
    })
    setError(null)
  }

  const handleUploadError = (err) => {
    setError('שגיאה בהעלאה: ' + err.message)
  }

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <h1>🚀 Next.js + Cloudinary</h1>

        {/* Upload Widget */}
        <div className={styles.uploadSection}>
          <h2>העלה תמונה</h2>
          <CldUploadWidget
            uploadPreset="your_upload_preset"
            onSuccess={handleUploadSuccess}
            onError={handleUploadError}
          >
            {({ open }) => (
              <button
                className={styles.uploadBtn}
                onClick={() => open()}
              >
                📤 בחר תמונה
              </button>
            )}
          </CldUploadWidget>

          {error && <p className={styles.error}>❌ {error}</p>}
        </div>

        {/* Display Results */}
        {uploadedImage && (
          <div className={styles.results}>
            <h2>תוצאות</h2>

            <div className={styles.imageGrid}>
              {/* Original Image */}
              <div className={styles.imageCard}>
                <h3>מקורי</h3>
                <CldImage
                  src={uploadedImage.public_id}
                  alt="Original"
                  width={300}
                  height={300}
                />
                <p>גודל: {(uploadedImage.bytes / 1024).toFixed(2)} KB</p>
              </div>

              {/* Optimized Image */}
              <div className={styles.imageCard}>
                <h3>עם אופטימיזציה</h3>
                <CldImage
                  src={uploadedImage.public_id}
                  alt="Optimized"
                  width={300}
                  height={300}
                  crop="fill"
                  gravity="auto"
                  quality="auto"
                  format="auto"
                />
                <p>✨ עם Cloudinary optimization</p>
              </div>
            </div>

            {/* Image Details */}
            <div className={styles.details}>
              <h3>פרטים</h3>
              <table>
                <tbody>
                  <tr>
                    <td><strong>Public ID:</strong></td>
                    <td>{uploadedImage.public_id}</td>
                  </tr>
                  <tr>
                    <td><strong>Width:</strong></td>
                    <td>{uploadedImage.width}px</td>
                  </tr>
                  <tr>
                    <td><strong>Height:</strong></td>
                    <td>{uploadedImage.height}px</td>
                  </tr>
                  <tr>
                    <td><strong>URL:</strong></td>
                    <td><code>{uploadedImage.secure_url}</code></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* API Endpoints Info */}
        <div className={styles.info}>
          <h3>📚 API Endpoints</h3>
          <p>צור את הקבצים הבאים ב-app/api/:</p>
          <ul>
            <li>/api/upload - העלה תמונה</li>
            <li>/api/transform - טרנספורמציה</li>
            <li>/api/delete - מחק תמונה</li>
            <li>/api/images - רשום תמונות</li>
          </ul>
        </div>
      </div>
    </main>
  )
}
