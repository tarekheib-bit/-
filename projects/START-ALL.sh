#!/bin/bash
# Start all 4 Cloudinary projects
# כתב לפתיחת כל 4 הפרויקטים בו-זמנית

echo ""
echo "========================================="
echo "🚀 Starting All Cloudinary Projects"
echo "========================================="
echo ""

# Node.js/Express
echo "📦 Starting Node.js/Express..."
(cd 01-nodejs-express && npm install && npm run dev) &
NODE_PID=$!
sleep 3

# Python/Flask
echo "🐍 Starting Python/Flask..."
(cd 02-python-flask && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py) &
FLASK_PID=$!
sleep 3

# React/Vite
echo "⚛️ Starting React/Vite..."
(cd 03-react-vite && npm install && npm run dev) &
REACT_PID=$!
sleep 3

# Next.js
echo "🔷 Starting Next.js..."
(cd 04-nextjs && npm install && npm run dev) &
NEXTJS_PID=$!
sleep 3

echo ""
echo "========================================="
echo "✅ All projects starting!"
echo "========================================="
echo ""
echo "🌐 Open in browser:"
echo "   • Node.js:    http://localhost:3000"
echo "   • Flask:      http://localhost:5000"
echo "   • React:      http://localhost:5173"
echo "   • Next.js:    http://localhost:3001"
echo ""
echo "🔑 Don't forget to configure .env files!"
echo ""
echo "========================================="
echo ""
echo "Press Ctrl+C to stop all projects"
echo ""

# Wait for all background processes
wait $NODE_PID $FLASK_PID $REACT_PID $NEXTJS_PID
