# Enable Email/Password Authentication

## Step 1: Enable Email/Password in Firebase Console

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **fasalsuraksha-87e23**
3. Click **Authentication** in the left sidebar
4. Click **Sign-in method** tab
5. Find **Email/Password** in the list
6. Click on it
7. Toggle **Enable** to ON
8. Click **Save**

## Step 2: Test the Authentication

1. **Restart your Flask server** (if running):
   ```cmd
   python app.py
   ```

2. **Open your browser**: `http://localhost:5000`

3. **You'll see the login page with:**
   - Email/Password sign-in form (default)
   - Toggle to switch between Sign In and Sign Up
   - Google Sign-In button below

## Features Added:

### Sign Up (New Users)
- Enter full name
- Enter email
- Enter password (minimum 6 characters)
- Click "Create Account"
- Automatically signed in after registration

### Sign In (Existing Users)
- Enter email
- Enter password
- Click "Sign In"

### Toggle Between Forms
- Click "Sign Up" link to create new account
- Click "Sign In" link to return to login

### Google Sign-In
- Still available as an alternative option
- Click "Continue with Google"

## Error Handling:

The system now shows user-friendly error messages for:
- Invalid email format
- Wrong password
- Email already in use (during sign up)
- Weak password (less than 6 characters)
- User not found
- Network errors

## Security Features:

- Passwords are securely hashed by Firebase
- Minimum 6 character password requirement
- Email verification available (can be enabled in Firebase Console)
- Session-based authentication on backend
- Protected routes require login

## Testing Checklist:

- [ ] Enable Email/Password in Firebase Console
- [ ] Restart Flask server
- [ ] Create a new account with email/password
- [ ] Sign out
- [ ] Sign in with the same credentials
- [ ] Try Google Sign-In
- [ ] Verify user profile shows in navbar
- [ ] Test logout functionality

## Optional: Enable Email Verification

To require users to verify their email:

1. In Firebase Console > Authentication > Settings
2. Enable "Email verification"
3. Customize the email template if desired

This will send a verification email to new users before they can access the app.
