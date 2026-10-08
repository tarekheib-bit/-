@echo off
REM Start all 4 Cloudinary projects
REM כתב לפתיחת כל 4 הפרויקטים בו-זמנית

echo.
echo =========================================
echo 🚀 Starting All Cloudinary Projects
echo =========================================
echo.

REM Open Node.js/Express in new terminal
echo 📦 Starting Node.js/Express...
start "Node.js/Express - http://localhost:3000" cmd /k "cd 01-nodejs-express && npm install && npm run dev"
timeout /t 3 /nobreak

REM Open Python/Flask in new terminal
echo 🐍 Starting Python/Flask...
start "Python/Flask - http://localhost:5000" cmd /k "cd 02-python-flask && pip install -r requirements.txt && python app.py"
timeout /t 3 /nobreak

REM Open React/Vite in new terminal
echo ⚛️ Starting React/Vite...
start "React/Vite - http://localhost:5173" cmd /k "cd 03-react-vite && npm install && npm run dev"
timeout /t 3 /nobreak

REM Open Next.js in new terminal
echo 🔷 Starting Next.js...
start "Next.js - http://localhost:3000" cmd /k "cd 04-nextjs && npm install && npm run dev"
timeout /t 3 /nobreak

echo.
echo =========================================
echo ✅ All projects starting!
echo =========================================
echo.
echo 🌐 Open in browser:
echo   • Node.js:    http://localhost:3000
echo   • Flask:      http://localhost:5000
echo   • React:      http://localhost:5173
echo   • Next.js:    http://localhost:3001
echo.
echo 🔑 Don't forget to configure .env files!
echo.
echo =========================================
pause
