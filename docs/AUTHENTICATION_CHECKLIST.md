# Firebase Authentication Checklist

## ✅ Completed Steps:
- [x] Firebase service account key placed in project root
- [x] `.env` file configured with Firebase credentials
- [x] Dependencies installed (firebase-admin, PyJWT)
- [x] Routes protected with `@login_required` decorator

## 🔧 Required: Enable Google Sign-In in Firebase Console

### Steps to Enable Google Authentication:

1. **Go to Firebase Console**
   - Visit: https://console.firebase.google.com/
   - Select your project: `fasalsuraksha-87e23`

2. **Navigate to Authentication**
   - Click **Authentication** in the left sidebar
   - If this is your first time, click **Get Started**

3. **Enable Google Sign-In**
   - Click the **Sign-in method** tab
   - Find **Google** in the list of providers
   - Click on **Google**
   - Toggle the **Enable** switch to ON
   - Select a **Support email** from the dropdown (your email)
   - Click **Save**

4. **Add Authorized Domains (for development)**
   - Still in Authentication > Sign-in method
   - Scroll down to **Authorized domains**
   - Make sure `localhost` is in the list (it should be by default)
   - For production, add your production domain here

## 🧪 Testing the Authentication

1. **Stop your Flask server** (if running)
   - Press `Ctrl+C` in the terminal

2. **Restart the server**
   ```cmd
   python app.py
   ```

3. **Open your browser**
   - Go to: `http://localhost:5000`
   - You should be redirected to `/login`

4. **Test Google Sign-In**
   - Click "Continue with Google" button
   - Select your Google account
   - Grant permissions
   - You should be redirected to the home page
   - Your profile picture and name should appear in the navbar

5. **Test Logout**
   - Click the "Logout" button in the navbar
   - You should be redirected back to the login page

## 🔒 What's Protected Now:

- `/` (home page) - Requires login
- `/upload/` - Requires login
- `/chat` - Requires login
- `/login` - Public (redirects to home if already logged in)
- `/logout` - Public

## 🐛 Troubleshooting:

### "Firebase credentials not found"
- Check that `serviceAccountKey.json` exists in project root
- Verify `FIREBASE_ADMIN_CREDENTIALS=serviceAccountKey.json` in `.env`

### "Authentication failed" or popup closes immediately
- Make sure Google Sign-In is **enabled** in Firebase Console
- Check that all Firebase config values in `.env` are correct
- Verify `localhost` is in authorized domains

### "Invalid token" error
- Restart your Flask server after making changes
- Clear browser cookies/cache
- Check that Firebase project ID matches in both files

### Still not working?
- Check the browser console for JavaScript errors (F12)
- Check the Flask terminal for Python errors
- Verify your `.env` file has no extra spaces or quotes around values

## 📝 Security Notes:

- Never commit `.env` or `serviceAccountKey.json` to Git
- Both files are already in `.gitignore`
- For production, use environment variables on your hosting platform
- Consider adding rate limiting for authentication endpoints
