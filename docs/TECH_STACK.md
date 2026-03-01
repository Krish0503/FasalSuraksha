# FasalSuraksha - Technology Stack

cc
## 🚀 Deployment Stack (Production Ready)

### Web Server
- **Gunicorn** - WSGI HTTP server for production

### Hosting Options
- **Heroku** - Cloud platform (Procfile included)
- **Google Cloud Platform** - Firebase integration
- **AWS** - Scalable cloud hosting
- **Azure** - Microsoft cloud services

### Configuration Files
- **Procfile** - Heroku deployment configuration
- **runtime.txt** - Python version specification
- **.env** - Environment variables (not committed)

---

## 📁 Project Structure

```
FasalSuraksha/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (secret)
├── serviceAccountKey.json         # Firebase credentials (secret)
├── plant_disease.json             # Disease information database
├── models/
│   └── plant_disease_recog_model_pwp.keras  # Trained ML model
├── templates/
│   ├── home.html                  # Main application page
│   ├── login.html                 # Authentication page
│   └── contact.html               # Contact us page
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css      # Bootstrap framework
│   │   └── style.css              # Custom styles
│   ├── js/
│   │   ├── bootstrap.bundle.min.js
│   │   ├── chatbot.js             # Chatbot functionality
│   │   └── upload.js              # Image upload handling
│   └── images/
│       └── logo.svg               # Application logo
└── uploadimages/                  # Temporary image storage
```

---

## 🎯 Key Features Implemented

### 1. Plant Disease Detection
- **Technology**: TensorFlow CNN model
- **Process**: Image upload → Feature extraction → Classification → Results
- **Output**: Disease name, cause, treatment recommendations

### 2. AI Chatbot
- **Technology**: Google Gemini AI
- **Features**: 
  - 24/7 agricultural assistance
  - Disease information
  - Treatment advice
  - Farming best practices

### 3. User Authentication
- **Technology**: Firebase Authentication
- **Methods**: Google OAuth, Email/Password
- **Security**: JWT tokens, session management

### 4. Feedback System
- **Technology**: JavaScript modal, Flask backend
- **Features**: 
  - Emoji-based ratings
  - Category selection
  - User feedback collection

### 5. Contact Form
- **Technology**: HTML forms, Flask routes
- **Features**: 
  - Professional contact page
  - Team information
  - Message submission

---

## 📊 Performance & Scalability

### Current Capabilities
- Real-time disease detection
- Instant AI responses
- Concurrent user support
- Responsive design (mobile-friendly)

### Optimization
- Image preprocessing (160x160 resize)
- Efficient model loading
- Session-based state management
- Asynchronous API calls

---

## 🔧 Configuration Management

### Environment Variables (.env)
```
GEMINI_API_KEY              # Google AI API key
SECRET_KEY                  # Flask session secret
FIREBASE_API_KEY            # Firebase web API key
FIREBASE_AUTH_DOMAIN        # Firebase auth domain
FIREBASE_PROJECT_ID         # Firebase project ID
FIREBASE_STORAGE_BUCKET     # Firebase storage
FIREBASE_MESSAGING_SENDER_ID # Firebase messaging
FIREBASE_APP_ID             # Firebase app ID
FIREBASE_ADMIN_CREDENTIALS  # Path to service account key
```

---

## 👥 Development Team

**Nirvana Coders**
- Sneha
- Akshita
- Rahul
- Raunak
- Krish

---

## 📝 License & Credits

### Third-Party Services
- Google Gemini AI - Conversational AI
- Firebase - Authentication & Database
- TensorFlow - Machine Learning Framework
- Bootstrap - UI Framework

### Open Source Libraries
All dependencies listed in `requirements.txt` are open-source and used under their respective licenses.

---

## 🔮 Future Enhancements (Potential Tech Stack Additions)

- **Redis** - Caching for faster responses
- **Celery** - Background task processing
- **PostgreSQL** - Relational database for analytics
- **Docker** - Containerization
- **Kubernetes** - Orchestration
- **Prometheus** - Monitoring
- **Elasticsearch** - Advanced search
- **WebSockets** - Real-time updates
- **React/Vue.js** - Modern frontend framework
- **GraphQL** - API query language

---

## 📚 Documentation Files

- `README.md` - Project overview
- `FIREBASE_SETUP.md` - Firebase configuration guide
- `EMAIL_AUTH_SETUP.md` - Email authentication setup
- `AUTHENTICATION_CHECKLIST.md` - Auth testing checklist
- `FEEDBACK_CONTACT_SETUP.md` - Feedback system guide
- `TECH_STACK.md` - This file

---

**Built with ❤️ for farmers by Nirvana Coders**
