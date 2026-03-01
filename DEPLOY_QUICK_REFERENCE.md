# 🚀 Quick Deploy Reference Card

## ✅ YES - Ready to Deploy!

---

## 📝 Quick Steps

### 1️⃣ Push to GitHub (2 min)
```bash
git init
git add .
git commit -m "Deploy FasalSuraksha"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/FasalSuraksha.git
git push -u origin main
```

### 2️⃣ Deploy on Render (10 min)
1. https://render.com → Sign up with GitHub
2. New Web Service → Select `FasalSuraksha` repo
3. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
   - Instance: Free
4. Add environment variables (see below)
5. Create Web Service

### 3️⃣ Update Firebase (2 min)
1. Firebase Console → Authentication → Settings
2. Add domain: `your-app.onrender.com`

---

## 🔑 Environment Variables to Add

Copy from your `.env` file:

```
GEMINI_API_KEY=AIzaSyAaNcmZqswxCczTXtggd1nsMl15880i2Q4
SECRET_KEY=your_random_secret_key
FIREBASE_API_KEY=AIzaSyCsHRLMCzkJqH3eFhubL19siqguVHO6MzI
FIREBASE_AUTH_DOMAIN=fasalsuraksha-87e23.firebaseapp.com
FIREBASE_PROJECT_ID=fasalsuraksha-87e23
FIREBASE_STORAGE_BUCKET=fasalsuraksha-87e23.firebasestorage.app
FIREBASE_MESSAGING_SENDER_ID=823826876688
FIREBASE_APP_ID=1:823826876688:web:680523112baf7b2ad33d95
```

**PLUS:** Copy entire `serviceAccountKey.json` content as:
```
FIREBASE_CREDENTIALS_JSON={"type":"service_account",...entire JSON...}
```

---

## ⏱️ Timeline

- Push to GitHub: 2 min
- Render setup: 5 min
- Build & deploy: 5-10 min
- Firebase update: 2 min
- **Total: ~15-20 minutes**

---

## 🎯 Your App Will Be Live At:

`https://fasalsuraksha.onrender.com`

(or your chosen name)

---

## 📚 Full Guides Available:

- `DEPLOY_NOW.md` - Detailed step-by-step
- `READY_TO_DEPLOY.md` - Complete checklist
- `docs/DEPLOYMENT_GUIDE.md` - Alternative platforms

---

**You're ready! Follow DEPLOY_NOW.md for detailed instructions! 🌾**
