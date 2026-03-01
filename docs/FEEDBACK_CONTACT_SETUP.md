# Contact Us & Feedback Feature

## ✅ What's Been Added:

### 1. Feedback Modal (Home Page)
- Click "Feedback" button in navbar
- Rate experience with emojis (1-5 stars)
- Select category: Bug Report, Feature Request, Improvement, General
- Write detailed feedback
- Instant submission

### 2. Contact Us Page
- Accessible via "Contact Us" button in navbar
- Full contact information display
- Contact form with name, email, subject, message
- Beautiful responsive design
- Success confirmation

## 🎯 Features:

### Feedback System:
- **Rating System**: 5 emoji-based ratings (😞 to 😍)
- **Categories**: Bug, Feature Request, Improvement, General
- **User Context**: Automatically captures user info
- **Modal Interface**: Non-intrusive popup

### Contact Form:
- **Dedicated Page**: Professional contact page
- **Team Information**: Shows Nirvana Coders team
- **Contact Details**: Email, phone, address
- **Message Form**: Full contact form

## 📊 Current Implementation:

Right now, submissions are **logged to console**. You can see them in your Flask terminal:

```
Feedback Submission: {'user_id': '...', 'rating': '5', 'category': 'feature', ...}
Contact Form Submission: {'name': 'John', 'email': '...', 'subject': '...', ...}
```

## 🔥 Optional: Store in Firebase Firestore

To permanently store feedback and contact submissions:

### Step 1: Enable Firestore

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **fasalsuraksha-87e23**
3. Click **Firestore Database** in left sidebar
4. Click **Create database**
5. Choose **Start in production mode**
6. Select a location (closest to your users)
7. Click **Enable**

### Step 2: Update app.py

Replace the feedback and contact routes with Firestore storage:

```python
from firebase_admin import firestore
from datetime import datetime

# Initialize Firestore
db = firestore.client()

@app.route('/feedback', methods=['POST'])
@login_required
def feedback():
    try:
        data = request.get_json()
        user = session.get('user')
        
        # Store in Firestore
        feedback_ref = db.collection('feedback').document()
        feedback_ref.set({
            'user_id': user.get('uid'),
            'user_email': user.get('email'),
            'user_name': user.get('name'),
            'rating': int(data.get('rating')),
            'category': data.get('category'),
            'message': data.get('message'),
            'timestamp': datetime.now(),
            'status': 'new'
        })
        
        return jsonify({
            'success': True,
            'message': 'Feedback submitted successfully'
        })
    except Exception as e:
        print(f"Feedback error: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/contact/submit', methods=['POST'])
@login_required
def contact_submit():
    try:
        data = request.get_json()
        user = session.get('user')
        
        # Store in Firestore
        contact_ref = db.collection('contacts').document()
        contact_ref.set({
            'user_id': user.get('uid'),
            'user_email': user.get('email'),
            'name': data.get('name'),
            'email': data.get('email'),
            'subject': data.get('subject'),
            'message': data.get('message'),
            'timestamp': datetime.now(),
            'status': 'new'
        })
        
        return jsonify({
            'success': True,
            'message': 'Contact form submitted successfully'
        })
    except Exception as e:
        print(f"Contact form error: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
```

### Step 3: View Submissions in Firebase

1. Go to Firebase Console > Firestore Database
2. You'll see two collections:
   - **feedback**: All user feedback
   - **contacts**: All contact form submissions
3. Click on any document to view details
4. You can export data, filter, search, etc.

## 📧 Optional: Email Notifications

To receive email notifications for new submissions, you can:

1. **Use SendGrid/Mailgun**: Send emails via API
2. **Use Firebase Cloud Functions**: Trigger emails on new Firestore documents
3. **Use SMTP**: Send emails directly from Flask

Example with Flask-Mail:

```python
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')

mail = Mail(app)

# In your route:
msg = Message('New Feedback Received',
              sender='noreply@fasalsuraksha.com',
              recipients=['support@fasalsuraksha.com'])
msg.body = f"New feedback from {user.get('name')}: {data.get('message')}"
mail.send(msg)
```

## 🧪 Testing:

1. **Restart your server**:
   ```cmd
   python app.py
   ```

2. **Test Feedback**:
   - Go to home page
   - Click "Feedback" button
   - Select rating, category, write message
   - Submit
   - Check Flask terminal for log

3. **Test Contact Form**:
   - Click "Contact Us" in navbar
   - Fill out the form
   - Submit
   - Check Flask terminal for log

## 📊 Data Structure:

### Feedback Collection:
```json
{
  "user_id": "firebase_uid",
  "user_email": "user@email.com",
  "user_name": "John Doe",
  "rating": 5,
  "category": "feature",
  "message": "Great app! Would love to see...",
  "timestamp": "2024-11-15T10:30:00",
  "status": "new"
}
```

### Contact Collection:
```json
{
  "user_id": "firebase_uid",
  "user_email": "user@email.com",
  "name": "John Doe",
  "email": "john@email.com",
  "subject": "Question about disease detection",
  "message": "How accurate is the AI model?",
  "timestamp": "2024-11-15T10:30:00",
  "status": "new"
}
```

## 🎨 Benefits:

✅ **User Engagement**: Direct communication channel
✅ **Feedback Loop**: Understand user needs
✅ **Bug Reports**: Catch issues early
✅ **Feature Requests**: Build what users want
✅ **Trust Building**: Shows you care about users
✅ **Data Collection**: Valuable insights for improvement

## 🔒 Privacy Note:

- User information is only collected from authenticated users
- Data is stored securely in Firebase
- Consider adding a privacy policy
- Allow users to request data deletion (GDPR compliance)
