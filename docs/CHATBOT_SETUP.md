# FasalSuraksha AI Chatbot Setup Guide

## Features Added
✅ AI-powered chatbot for crop disease queries
✅ Real-time chat interface with beautiful UI
✅ Expert agricultural advice using Google Gemini AI
✅ Floating chatbot button with smooth animations

## Setup Instructions

### 1. Install Required Packages
```bash
python -m pip install flask numpy tensorflow google-generativeai python-dotenv
```

Or use the requirements file:
```bash
python -m pip install -r requirements.txt
```

### 2. Get Your Free Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 3. Configure API Key

Create a `.env` file in your project root:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

Or set it as an environment variable:
```bash
# Windows CMD
set GEMINI_API_KEY=your_actual_api_key_here

# Windows PowerShell
$env:GEMINI_API_KEY="your_actual_api_key_here"

# Linux/Mac
export GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the App
Open your browser and go to: http://localhost:5000

## How to Use the Chatbot

1. Click the purple chat button in the bottom-right corner
2. Type your question about crops, diseases, or treatments
3. Press Enter or click the send button
4. Get instant AI-powered responses!

## Example Questions to Ask

- "What are common tomato diseases?"
- "How to treat potato late blight?"
- "Best organic pesticides for vegetables?"
- "How to prevent fungal infections in crops?"
- "What causes yellowing of leaves?"
- "Treatment for apple scab disease"
- "How to control aphids naturally?"

## Features

- **Smart AI Responses**: Powered by Google Gemini AI
- **Agricultural Expert**: Specialized in crop diseases and treatments
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Real-time Chat**: Instant responses with typing indicators
- **Mobile Friendly**: Works perfectly on all devices

## Troubleshooting

### API Key Issues
- Make sure your `.env` file is in the project root
- Check that the API key is valid and active
- Ensure no extra spaces in the API key

### Module Not Found
```bash
python -m pip install google-generativeai python-dotenv
```

### Chat Not Working
- Check browser console for errors (F12)
- Verify the Flask server is running
- Ensure `/chat` endpoint is accessible

## Tech Stack

- **Backend**: Flask + Google Gemini AI
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Model**: Google Gemini Pro
- **UI Framework**: Bootstrap 5 + Custom CSS

Enjoy your AI-powered crop protection assistant! 🌾🤖
