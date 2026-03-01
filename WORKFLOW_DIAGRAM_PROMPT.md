# FasalSuraksha Workflow Diagram Prompts

## 🎯 For napkin.ai or any diagram tool

---

## 📋 MAIN WORKFLOW PROMPT (Complete User Journey)

```
Create a detailed workflow diagram for FasalSuraksha, an AI-powered plant disease detection system showing the complete user journey:

START: User visits website

AUTHENTICATION FLOW:
1. User lands on Login Page
2. Choose authentication method:
   - Option A: Click "Sign in with Google" → Google OAuth popup → Firebase authenticates → JWT token generated
   - Option B: Enter email/password → Firebase validates → JWT token generated
3. Flask backend verifies token with Firebase Admin SDK
4. Session created and stored
5. Redirect to Home Dashboard

DISEASE DETECTION FLOW:
6. User sees Home Dashboard with upload form
7. User selects/drags plant leaf image
8. Image preview shows
9. User clicks "Analyze Disease"
10. Frontend sends image to Flask backend (/upload route)
11. Backend saves image temporarily
12. Image preprocessed (resize to 160x160, normalize)
13. TensorFlow CNN model analyzes image
14. Model returns prediction (1 of 39 diseases)
15. Backend fetches disease info from plant_disease.json
16. Results displayed: Disease name, cause, treatment recommendations
17. Image and results shown on screen

AI CHATBOT FLOW:
18. User clicks chatbot button (bottom-right)
19. Chatbot window opens with welcome message
20. User types agricultural question
21. Message sent to Flask backend (/chat route)
22. Backend sends query to Google Gemini AI
23. Gemini processes with agricultural context
24. AI generates expert advice
25. Response sent back to user
26. Message appears in chat window
27. User can continue conversation

FEEDBACK FLOW:
28. User clicks "Feedback" button in navbar
29. Modal popup opens
30. User selects emoji rating (1-5)
31. User selects category (Bug/Feature/Improvement/General)
32. User writes feedback message
33. Submit to Flask backend (/feedback route)
34. Backend logs feedback (or saves to Firestore)
35. Success message shown
36. Modal closes

CONTACT FLOW:
37. User clicks "Contact Us" in navbar
38. Redirects to Contact page
39. User fills form: name, email, subject, message
40. Submit to Flask backend (/contact/submit route)
41. Backend processes submission
42. Success confirmation shown

LOGOUT FLOW:
43. User clicks "Logout" button
44. Session destroyed
45. Redirect to Login page

Use clear decision points, color-coded sections (Auth: Orange, Detection: Purple, Chat: Blue, Feedback: Green), and show both success and error paths.
```

---

## 🔄 SIMPLIFIED WORKFLOW PROMPT

```
Create a user workflow diagram for FasalSuraksha plant disease detection app:

1. LOGIN
   - User visits site → Login page
   - Choose: Google Sign-In OR Email/Password
   - Firebase authenticates → Session created
   - Redirect to Dashboard

2. UPLOAD & DETECT
   - User uploads plant image
   - Image sent to backend
   - TensorFlow CNN analyzes (39 diseases)
   - Results displayed: Disease + Treatment

3. AI CHATBOT
   - User opens chatbot
   - Types question
   - Gemini AI responds with advice
   - Conversation continues

4. FEEDBACK
   - User clicks Feedback
   - Rates experience (1-5)
   - Submits feedback
   - Confirmation shown

5. LOGOUT
   - User logs out
   - Session ends
   - Return to login

Show clear flow with arrows, decision points, and color-coded sections.
```

---

## 🎨 TECHNICAL WORKFLOW PROMPT (For Developers)

```
Create a technical workflow diagram showing FasalSuraksha's backend processing:

USER ACTION → FRONTEND → BACKEND → SERVICES → RESPONSE

AUTHENTICATION WORKFLOW:
User clicks login → Firebase SDK (client) → Firebase Auth API → Token generated → Flask receives token → Firebase Admin SDK verifies → Session created → User authenticated

IMAGE PROCESSING WORKFLOW:
User uploads image → JavaScript FormData → Flask /upload route → Save to uploadimages/ → Load with Pillow → Resize to 160x160 → Convert to numpy array → TensorFlow model.predict() → Get prediction index → Lookup in plant_disease.json → Return disease info → Render results template

CHATBOT WORKFLOW:
User sends message → JavaScript fetch → Flask /chat route → Check for keywords → Build prompt with context → Google Gemini API call → Parse response → Return JSON → Display in chat window

DATA FLOW:
Request → Flask Route → Business Logic → External API/Model → Process Response → Return to Client

Show technical components, API calls, data transformations, and error handling paths.
```

---

## 🌊 DATA FLOW DIAGRAM PROMPT

```
Create a data flow diagram for FasalSuraksha showing how data moves through the system:

LEVEL 0 (Context Diagram):
User ↔ FasalSuraksha System ↔ External Services (Firebase, Gemini AI)

LEVEL 1 (Main Processes):
1. Authentication Process
   - Input: User credentials
   - Process: Firebase authentication
   - Output: Session token

2. Disease Detection Process
   - Input: Plant image
   - Process: ML model analysis
   - Output: Disease prediction + treatment

3. Chatbot Process
   - Input: User question
   - Process: AI processing
   - Output: Agricultural advice

4. Feedback Process
   - Input: User feedback
   - Process: Data storage
   - Output: Confirmation

LEVEL 2 (Detailed):
Show data stores (Sessions, Images, Model, Database), processes (Validate, Analyze, Generate), and data flows between them.

Use standard DFD notation with circles for processes, rectangles for external entities, parallel lines for data stores, and arrows for data flow.
```

---

## 🔀 DECISION FLOW PROMPT

```
Create a decision flowchart for FasalSuraksha user interactions:

START
↓
Is user authenticated?
├─ NO → Show Login Page
│        ↓
│        Login method?
│        ├─ Google → OAuth flow → Success? → YES → Create session
│        └─ Email → Validate → Success? → YES → Create session
│        ↓
│        Authentication failed? → Show error → Return to login
│
└─ YES → Show Dashboard
         ↓
         User action?
         ├─ Upload Image → Valid image? 
         │                 ├─ YES → Process → Show results
         │                 └─ NO → Show error
         │
         ├─ Open Chatbot → Type message → Valid? 
         │                                  ├─ YES → Get AI response
         │                                  └─ NO → Show error
         │
         ├─ Give Feedback → Fill form → Valid?
         │                              ├─ YES → Submit → Success
         │                              └─ NO → Show validation
         │
         └─ Logout → Destroy session → Return to login

Use diamond shapes for decisions, rectangles for processes, and clear YES/NO paths.
```

---

## 🎭 USER JOURNEY MAP PROMPT

```
Create a user journey map for FasalSuraksha showing emotional states and touchpoints:

PERSONA: Farmer with diseased crop

STAGES:
1. AWARENESS
   - Farmer notices diseased plants
   - Searches for solution online
   - Finds FasalSuraksha
   - Emotion: Worried 😟

2. CONSIDERATION
   - Visits website
   - Sees features and benefits
   - Decides to try
   - Emotion: Hopeful 🤔

3. ONBOARDING
   - Creates account (Google/Email)
   - Quick and easy signup
   - Emotion: Satisfied 😊

4. FIRST USE
   - Uploads plant image
   - Waits for analysis (5 seconds)
   - Gets disease identification
   - Emotion: Impressed 😲

5. LEARNING
   - Reads treatment recommendations
   - Asks chatbot for more details
   - Gets expert advice
   - Emotion: Confident 💪

6. ACTION
   - Applies recommended treatment
   - Saves information
   - Shares with other farmers
   - Emotion: Grateful 🙏

7. RETENTION
   - Returns for more scans
   - Uses chatbot regularly
   - Provides feedback
   - Emotion: Loyal 🌟

Show touchpoints (Login, Upload, Results, Chat, Feedback), pain points, and opportunities at each stage.
```

---

## 🔄 SYSTEM INTERACTION DIAGRAM PROMPT

```
Create a sequence diagram showing interactions between FasalSuraksha components:

ACTORS: User, Browser, Flask Backend, TensorFlow Model, Firebase, Gemini AI

SCENARIO 1: Disease Detection
User → Browser: Upload image
Browser → Flask: POST /upload (image file)
Flask → Flask: Save image temporarily
Flask → TensorFlow: Load and preprocess image
TensorFlow → TensorFlow: Run CNN prediction
TensorFlow → Flask: Return prediction (disease index)
Flask → Flask: Lookup disease info in JSON
Flask → Browser: Render results page
Browser → User: Display disease + treatment

SCENARIO 2: Authentication
User → Browser: Click "Sign in with Google"
Browser → Firebase: Initiate OAuth
Firebase → Firebase: Authenticate user
Firebase → Browser: Return ID token
Browser → Flask: POST /auth/verify (token)
Flask → Firebase Admin: Verify token
Firebase Admin → Flask: Token valid + user info
Flask → Flask: Create session
Flask → Browser: Redirect to dashboard
Browser → User: Show dashboard

SCENARIO 3: Chatbot
User → Browser: Type message
Browser → Flask: POST /chat (message)
Flask → Gemini AI: Send query with context
Gemini AI → Gemini AI: Process with NLP
Gemini AI → Flask: Return response
Flask → Browser: JSON response
Browser → User: Display message

Use standard sequence diagram notation with lifelines, activation boxes, and message arrows.
```

---

## 🎨 VISUAL STYLE SUGGESTIONS

**Colors:**
- Authentication: 🟠 Orange (#f093fb)
- Disease Detection: 🟣 Purple (#764ba2)
- AI Chatbot: 🔵 Blue (#667eea)
- Feedback: 🟢 Green (#38ef7d)
- Error States: 🔴 Red (#ff6b6b)
- Success States: ✅ Green (#51cf66)

**Icons:**
- 🔐 Lock for authentication
- 🌿 Leaf for disease detection
- 🤖 Robot for chatbot
- 💬 Speech bubble for feedback
- ⚠️ Warning for errors
- ✅ Checkmark for success

**Layout:**
- Top to bottom flow
- Left to right for alternatives
- Clear decision diamonds
- Grouped related processes
- Color-coded sections

---

## 📱 MOBILE WORKFLOW PROMPT

```
Create a mobile-specific workflow for FasalSuraksha:

MOBILE USER JOURNEY:
1. User opens app on phone
2. Responsive login page adapts to screen
3. Touch-friendly buttons
4. Camera integration for image capture
5. Tap to upload or take photo
6. Full-screen results view
7. Swipe-friendly chatbot
8. Bottom navigation
9. Touch gestures for feedback

Show mobile-specific interactions: tap, swipe, pinch, camera access, and responsive layouts.
```

---

## 🎯 QUICK REFERENCE

**For napkin.ai:**
1. Copy the **MAIN WORKFLOW PROMPT** (most comprehensive)
2. Paste into napkin.ai
3. Click "Generate"
4. Adjust layout and colors
5. Export as PNG/SVG

**For draw.io or Lucidchart:**
- Use the **TECHNICAL WORKFLOW** or **DECISION FLOW** prompts
- Manually create based on the structure

**For presentations:**
- Use **SIMPLIFIED WORKFLOW** for non-technical audiences
- Use **USER JOURNEY MAP** for stakeholder presentations

---

## 📊 DIAGRAM TYPES AVAILABLE

1. **Main Workflow** - Complete user journey (recommended)
2. **Simplified Workflow** - High-level overview
3. **Technical Workflow** - Developer-focused
4. **Data Flow Diagram** - Data movement
5. **Decision Flow** - Logic and decisions
6. **User Journey Map** - Emotional journey
7. **System Interaction** - Component communication
8. **Mobile Workflow** - Mobile-specific

---

**Choose the prompt that best fits your needs and create professional workflow diagrams! 🎨✨**
