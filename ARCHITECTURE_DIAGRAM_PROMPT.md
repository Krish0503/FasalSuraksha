# FasalSuraksha System Architecture Diagram Prompt

## 📋 Copy this prompt to napkin.ai:

---

## Prompt for napkin.ai:

```
Create a comprehensive system architecture diagram for FasalSuraksha, an AI-powered plant disease detection web application with the following components:

**Frontend Layer (Client Side):**
- Web Browser (User Interface)
  - Login Page (Google OAuth & Email/Password)
  - Home Dashboard
  - Image Upload Interface
  - Disease Results Display
  - AI Chatbot Widget
  - Feedback Modal
  - Contact Form

**Application Layer (Flask Backend):**
- Flask Web Server (Python 3.12)
  - Authentication Routes (/login, /auth/verify, /logout)
  - Upload Route (/upload)
  - Chat Route (/chat)
  - Feedback Route (/feedback)
  - Contact Route (/contact)
  - Session Management
  - Protected Routes with @login_required decorator

**AI/ML Layer:**
- TensorFlow CNN Model
  - Input: 160x160 plant leaf images
  - Output: 39 disease classifications
  - Model file: plant_disease_recog_model_pwp.keras
- Google Gemini AI (gemini-2.5-flash)
  - Agricultural chatbot
  - Natural language processing
  - Context-aware responses

**Authentication & Database Layer:**
- Firebase Authentication
  - Google Sign-In (OAuth 2.0)
  - Email/Password authentication
  - JWT token verification
- Firebase Admin SDK
  - User management
  - Session validation
- Firebase Firestore (Optional)
  - Feedback storage
  - Contact form submissions
  - User analytics

**External APIs:**
- Google Gemini AI API
  - Chatbot responses
  - Agricultural advice
- Firebase Authentication API
  - User sign-in/sign-up
  - Token management

**Data Flow:**
1. User uploads plant image → Flask processes → TensorFlow model analyzes → Returns disease prediction with treatment
2. User sends chat message → Flask receives → Gemini AI processes → Returns agricultural advice
3. User signs in → Firebase authenticates → Flask verifies token → Creates session → Grants access

**Storage:**
- Temporary Image Storage (uploadimages/)
- ML Model Storage (models/)
- Static Assets (CSS, JS, Images)
- Session Storage (Flask sessions)

**Security Components:**
- Environment Variables (.env)
- Firebase Service Account Key
- Session-based authentication
- Protected routes
- HTTPS (in production)

**Deployment Infrastructure:**
- Development: localhost:5000
- Production: Render.com
  - Gunicorn WSGI server
  - Auto-deploy from GitHub
  - Environment variables
  - Cloud storage

Use modern, clean design with:
- Color coding for different layers (Frontend: Blue, Backend: Green, AI/ML: Purple, Auth: Orange, External: Yellow)
- Clear arrows showing data flow
- Icons for each component
- Grouped sections for related components
- Professional tech stack appearance
```

---

## 🎨 Alternative Simplified Prompt:

```
Create a system architecture diagram for FasalSuraksha plant disease detection app:

**User Layer:**
- Web Browser → Login/Dashboard/Upload/Chat

**Frontend:**
- HTML/CSS/JavaScript
- Bootstrap UI
- Firebase SDK (client)

**Backend (Flask):**
- Authentication routes
- Image upload handler
- Chat API
- Session management

**AI/ML:**
- TensorFlow CNN (39 disease classes)
- Google Gemini AI (chatbot)

**Services:**
- Firebase Auth (Google + Email/Password)
- Firebase Firestore (data storage)
- Gemini AI API

**Data Flow:**
1. User → Upload Image → TensorFlow → Disease Result
2. User → Chat → Gemini AI → Agricultural Advice
3. User → Login → Firebase → Session → Access

Use clean, modern design with color-coded layers and clear arrows.
```

---

## 🎯 Key Components to Highlight:

### Frontend Components:
- Login Interface
- Image Upload Form
- Disease Results Display
- AI Chatbot Widget
- Feedback System
- Contact Form

### Backend Components:
- Flask Application Server
- Route Handlers
- Session Manager
- Authentication Middleware

### AI/ML Components:
- TensorFlow Model (CNN)
- Image Preprocessing
- Disease Classification
- Google Gemini AI
- NLP Processing

### External Services:
- Firebase Authentication
- Firebase Firestore
- Google Gemini API

### Data Stores:
- User Sessions
- Uploaded Images (temp)
- ML Model Files
- Static Assets

---

## 📊 Suggested Diagram Layout:

```
┌─────────────────────────────────────────────────┐
│           USER (Web Browser)                     │
│  Login | Upload | Chat | Feedback | Contact     │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│         FRONTEND LAYER                           │
│  HTML/CSS/JS | Bootstrap | Firebase SDK         │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│         FLASK BACKEND                            │
│  Routes | Auth | Session | API Handlers         │
└─────┬───────────┬───────────┬───────────────────┘
      │           │           │
      ▼           ▼           ▼
┌─────────┐ ┌─────────┐ ┌─────────────┐
│Firebase │ │TensorFlow│ │Gemini AI    │
│  Auth   │ │   CNN   │ │  Chatbot    │
└─────────┘ └─────────┘ └─────────────┘
      │           │           │
      ▼           ▼           ▼
┌─────────────────────────────────────┐
│         DATA LAYER                   │
│  Sessions | Images | Model | DB     │
└─────────────────────────────────────┘
```

---

## 🎨 Color Scheme Suggestion:

- **Frontend**: Light Blue (#667eea)
- **Backend**: Green (#38ef7d)
- **AI/ML**: Purple (#764ba2)
- **Authentication**: Orange (#f093fb)
- **External APIs**: Yellow (#fad961)
- **Data Storage**: Gray (#718096)

---

## 📝 Additional Details to Include:

**Technologies Used:**
- Python 3.12
- Flask 3.0.0
- TensorFlow 2.15.0
- Firebase Admin SDK
- Google Gemini AI
- Bootstrap 5
- JavaScript ES6+

**Key Features:**
- Real-time disease detection
- AI-powered chatbot
- Multi-auth support
- Feedback system
- Responsive design
- Session management

**Security:**
- JWT tokens
- Environment variables
- Protected routes
- HTTPS encryption
- Firebase security rules

---

## 🚀 How to Use:

1. Go to **napkin.ai**
2. Paste the **main prompt** above
3. Click "Generate"
4. Adjust layout and colors as needed
5. Export as PNG/SVG

---

**This will create a professional system architecture diagram for your FasalSuraksha project!** 🌾✨
