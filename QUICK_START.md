# 🚀 Quick Start Guide - FasalSuraksha

## 📋 Prerequisites Checklist

- [ ] Python 3.12 installed
- [ ] Firebase account created
- [ ] Google Gemini API key obtained
- [ ] Git installed (optional)

---

## ⚡ 5-Minute Setup

### 1. Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### 2. Configure Environment (2 min)

**Copy the example file:**
```bash
copy .env.example .env
```

**Edit `.env` and add your credentials:**
```env
GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_random_secret_key

FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your_sender_id
FIREBASE_APP_ID=your_app_id

FIREBASE_ADMIN_CREDENTIALS=serviceAccountKey.json
```

### 3. Add Firebase Service Account (1 min)

1. Download from Firebase Console > Project Settings > Service Accounts
2. Save as `serviceAccountKey.json` in project root

### 4. Enable Firebase Authentication (1 min)

1. Go to Firebase Console > Authentication
2. Enable **Google** sign-in method
3. Enable **Email/Password** sign-in method
4. Add `localhost` and `127.0.0.1` to authorized domains

### 5. Run the App! (30 sec)
```bash
python app.py
```

**Open browser:** http://localhost:5000

---

## 🎯 First Time Usage

1. **Sign Up** - Create account with Google or Email
2. **Upload Image** - Take/upload a plant leaf photo
3. **Get Results** - View disease detection and treatment
4. **Ask AI** - Use chatbot for agricultural advice
5. **Give Feedback** - Share your experience

---

## 📚 Need More Help?

- **Firebase Setup:** `docs/FIREBASE_SETUP.md`
- **Email Auth:** `docs/EMAIL_AUTH_SETUP.md`
- **Tech Stack:** `docs/TECH_STACK.md`
- **Full README:** `README.md`

---

## 🐛 Common Issues

### "Firebase credentials not found"
- Ensure `serviceAccountKey.json` is in project root
- Check path in `.env` file

### "Authentication failed"
- Enable Google/Email sign-in in Firebase Console
- Add `localhost` to authorized domains

### "Module not found"
- Run: `pip install -r requirements.txt`

---

## 🎉 You're Ready!

Your FasalSuraksha app is now running at **http://localhost:5000**

Happy farming! 🌾
