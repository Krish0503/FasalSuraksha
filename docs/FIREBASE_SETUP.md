# Firebase Google Authentication Setup Guide

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project" or select existing project
3. Enter project name (e.g., "FasalSuraksha")
4. Follow the setup wizard

## Step 2: Enable Google Authentication

1. In Firebase Console, go to **Authentication** > **Sign-in method**
2. Click on **Google** provider
3. Toggle **Enable**
4. Add your support email
5. Click **Save**

## Step 3: Register Web App

1. In Firebase Console, go to **Project Settings** (gear icon)
2. Scroll to "Your apps" section
3. Click the **Web** icon (`</>`)
4. Register app with a nickname (e.g., "FasalSuraksha Web")
5. Copy the Firebase configuration object

## Step 4: Get Firebase Admin SDK Credentials

1. In Firebase Console, go to **Project Settings** > **Service Accounts**
2. Click **Generate new private key**
3. Download the JSON file
4. Save it as `serviceAccountKey.json` in your project root
5. **IMPORTANT**: Add `serviceAccountKey.json` to `.gitignore`

## Step 5: Configure Environment Variables

Create a `.env` file in your project root with:

```env
# Gemini AI
GEMINI_API_KEY=your_gemini_api_key_here

# Flask Secret Key (generate a random string)
SECRET_KEY=your_random_secret_key_here

# Firebase Web Config (from Step 3)
FIREBASE_API_KEY=AIza...
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=123456789
FIREBASE_APP_ID=1:123456789:web:abc123

# Firebase Admin SDK
FIREBASE_ADMIN_CREDENTIALS=serviceAccountKey.json
```

## Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 7: Update .gitignore

Add these lines to `.gitignore`:

```
.env
serviceAccountKey.json
*.json
```

## Step 8: Run the Application

```bash
python app.py
```

Visit `http://localhost:5000/login` to test Google authentication!

## Security Notes

- Never commit `.env` or `serviceAccountKey.json` to version control
- Keep your Firebase API keys secure
- Use environment variables for all sensitive data
- Enable Firebase security rules for production

## Troubleshooting

### "Firebase credentials not found"
- Ensure `serviceAccountKey.json` exists in project root
- Check `FIREBASE_ADMIN_CREDENTIALS` path in `.env`

### "Authentication failed"
- Verify Firebase config values in `.env`
- Check that Google sign-in is enabled in Firebase Console
- Ensure authorized domains include `localhost` for development

### "Module not found"
- Run `pip install -r requirements.txt`
- Ensure you're using the correct Python environment

## Testing

1. Navigate to `/login`
2. Click "Continue with Google"
3. Select your Google account
4. You should be redirected to the home page with your profile visible
5. Click "Logout" to sign out

## Production Deployment

For production:
1. Add your production domain to Firebase authorized domains
2. Update CORS settings if needed
3. Use secure session configuration
4. Enable HTTPS
5. Set proper Firebase security rules
