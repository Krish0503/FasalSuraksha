# 🌾 FasalSuraksha - AI-Powered Plant Disease Detection

**FasalSuraksha** (Crop Protection) is an intelligent web application that helps farmers identify plant diseases using AI and provides expert treatment recommendations through an AI-powered chatbot.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange)
![Firebase](https://img.shields.io/badge/Firebase-Authentication-yellow)

---

## ✨ Features

- 🔍 **AI Disease Detection** - Upload plant images and get instant disease identification
- 🤖 **AI Chatbot** - 24/7 agricultural assistant powered by Google Gemini AI
- 🔐 **Secure Authentication** - Google Sign-In and Email/Password authentication
- 💬 **Feedback System** - Share your experience and suggestions
- 📧 **Contact Form** - Get in touch with our team
- 📱 **Responsive Design** - Works seamlessly on all devices
- 🌍 **39 Disease Categories** - Supports multiple crops and diseases

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- Firebase account
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fasalsuraksha.git
   cd fasalsuraksha
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Fill in your Firebase and Gemini API credentials
   ```bash
   cp .env.example .env
   ```

4. **Configure Firebase**
   - Download your Firebase service account key
   - Save it as `serviceAccountKey.json` in the project root
   - See `docs/FIREBASE_SETUP.md` for detailed instructions

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Sign in and start detecting plant diseases!

---

## 📁 Project Structure

```
FasalSuraksha/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── Procfile                   # Heroku deployment config
├── runtime.txt                # Python version for deployment
│
├── models/                    # Machine learning models
│   └── plant_disease_recog_model_pwp.keras
│
├── templates/                 # HTML templates
│   ├── home.html             # Main application page
│   ├── login.html            # Authentication page
│   └── contact.html          # Contact us page
│
├── static/                    # Static assets
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript files
│   └── images/               # Images and icons
│
├── uploadimages/             # Temporary image storage
│
├── docs/                     # Documentation
│   ├── FIREBASE_SETUP.md
│   ├── EMAIL_AUTH_SETUP.md
│   ├── TECH_STACK.md
│   └── ...
│
└── plant_disease.json        # Disease information database
```

---

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0** - Web framework
- **TensorFlow 2.15.0** - Deep learning
- **Google Gemini AI** - Conversational AI
- **Firebase Admin SDK** - Authentication & database

### Frontend
- **Bootstrap 5** - UI framework
- **JavaScript (ES6+)** - Client-side logic
- **Firebase SDK** - Client authentication

### Machine Learning
- **CNN Model** - 39 disease classifications
- **Image Processing** - NumPy, Pillow

See `docs/TECH_STACK.md` for complete details.

---

## 🌱 Supported Crops & Diseases

**Crops:** Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

**Diseases:** 39 different plant diseases including:
- Apple Scab, Black Rot, Cedar Apple Rust
- Tomato Early Blight, Late Blight, Leaf Mold
- Potato Early/Late Blight
- Corn Rust, Northern Leaf Blight
- And many more...

---

## 📖 Documentation

Detailed documentation is available in the `docs/` folder:

- **[Firebase Setup Guide](docs/FIREBASE_SETUP.md)** - Configure Firebase authentication
- **[Email Authentication](docs/EMAIL_AUTH_SETUP.md)** - Set up email/password login
- **[Technology Stack](docs/TECH_STACK.md)** - Complete tech stack overview
- **[Feedback System](docs/FEEDBACK_CONTACT_SETUP.md)** - Feedback & contact features
- **[Deployment Guide](docs/DEPLOYMENT_GUIDE.md)** - Deploy to production

---

## 🔐 Security

- Environment variables for sensitive data
- Firebase authentication with JWT tokens
- Session-based state management
- Protected routes with decorators
- `.gitignore` for sensitive files

**Important:** Never commit `.env` or `serviceAccountKey.json` to version control!

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👥 Team

**Nirvana Coders**
- Sneha
- Akshita
- Rahul
- Raunak
- Krish

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Google Gemini AI for conversational AI capabilities
- Firebase for authentication and database services
- TensorFlow team for the machine learning framework
- Bootstrap for the UI framework
- All farmers who inspired this project

---

## 📞 Support

For support, email support@fasalsuraksha.com or use the Contact Us page in the application.

---

**Built with ❤️ for farmers by Nirvana Coders**
