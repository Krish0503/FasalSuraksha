# FasalSuraksha Deployment Guide 🚀

## Quick Deploy Options

### Option 1: Render (Recommended - FREE)

1. **Create Account**: Go to https://render.com and sign up
2. **Connect GitHub**: 
   - Push your code to GitHub
   - Connect your GitHub account to Render
3. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Select your repository
   - Configure:
     - **Name**: fasalsuraksha
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
4. **Add Environment Variable**:
   - Go to "Environment" tab
   - Add: `GEMINI_API_KEY` = `AIzaSyAaNcmZqswxCczTXtggd1nsMl15880i2Q4`
5. **Deploy**: Click "Create Web Service"

✅ Your app will be live at: `https://fasalsuraksha.onrender.com`

---

### Option 2: Railway

1. **Create Account**: https://railway.app
2. **New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
3. **Configure**:
   - Railway auto-detects Python
   - Add environment variable: `GEMINI_API_KEY`
4. **Deploy**: Automatic!

✅ Live at: `https://fasalsuraksha.up.railway.app`

---

### Option 3: PythonAnywhere

1. **Create Account**: https://www.pythonanywhere.com
2. **Upload Files**:
   - Go to "Files" tab
   - Upload all your project files
3. **Create Web App**:
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose Flask
   - Set path to your app.py
4. **Install Dependencies**:
   - Open Bash console
   - Run: `pip install -r requirements.txt`
5. **Set Environment Variable**:
   - In Web tab, add to WSGI file:
   ```python
   os.environ['GEMINI_API_KEY'] = 'AIzaSyAaNcmZqswxCczTXtggd1nsMl15880i2Q4'
   ```
6. **Reload**: Click "Reload" button

✅ Live at: `https://yourusername.pythonanywhere.com`

---

### Option 4: Google Cloud Run

1. **Install Google Cloud SDK**
2. **Create Dockerfile**:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn --bind :$PORT app:app
```
3. **Deploy**:
```bash
gcloud run deploy fasalsuraksha --source . --region us-central1 --allow-unauthenticated
```

---

## 📋 Pre-Deployment Checklist

- ✅ All files committed to Git
- ✅ requirements.txt updated
- ✅ .gitignore configured
- ✅ Environment variables set
- ✅ Test locally first: `python app.py`
- ✅ Create uploadimages folder on server

## 🔧 Important Notes

### For Production:
1. **Change Debug Mode** in app.py:
```python
if __name__ == "__main__":
    app.run(debug=False)  # Change to False
```

2. **Create uploadimages folder** on server:
```bash
mkdir uploadimages
```

3. **Set Environment Variables** on platform:
   - `GEMINI_API_KEY` = Your API key
   - `FLASK_ENV` = production

### File Size Limits:
- Most platforms limit file uploads to 10-50MB
- Your model file is large, ensure platform supports it
- Consider using cloud storage for model file

## 🎯 Recommended: Render

**Why Render?**
- ✅ Free tier (750 hours/month)
- ✅ Auto-deploy from GitHub
- ✅ Easy environment variables
- ✅ Good for ML apps
- ✅ Supports large files

## 🆘 Troubleshooting

### Issue: Model file too large
**Solution**: Use Git LFS or cloud storage
```bash
git lfs install
git lfs track "*.keras"
```

### Issue: Out of memory
**Solution**: Upgrade to paid tier or optimize model

### Issue: Slow cold starts
**Solution**: Use Railway or upgrade Render plan

## 📞 Support

If you face issues:
1. Check platform logs
2. Verify environment variables
3. Test locally first
4. Check file permissions

---

**Your FasalSuraksha app is ready to deploy! 🌾✨**

Choose Render for easiest free deployment!
