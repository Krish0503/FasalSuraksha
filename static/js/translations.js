// Multi-language translation system
const translations = {
  en: {
    // Navbar
    "nav.tagline": "AI-Powered Crop Protection",
    "nav.home": "Home",
    "nav.dashboard": "Dashboard",
    "nav.contact": "Contact Us",
    "nav.feedback": "Feedback",
    "nav.logout": "Logout",
    // Hero
    "hero.title1": "Protect Your Crops",
    "hero.title2": "with AI Intelligence",
    "hero.subtitle": "Instant disease detection • Expert recommendations • Save your harvest",
    // Upload
    "upload.title": "Upload Plant Image",
    "upload.desc": "Click to select or drag & drop your image",
    "upload.select": "Select Image",
    "upload.analyze": "Analyze Disease",
    // Results
    "result.complete": "Analysis Complete",
    "result.newScan": "New Scan",
    "result.download": "Download Report",
    "result.aiAnalyzed": "AI Analyzed",
    "result.diagnosis": "Diagnosis",
    "result.cause": "Cause",
    "result.treatment": "Treatment",
    // Chatbot
    "chat.title": "FasalSuraksha AI",
    "chat.subtitle": "Ask me about crop diseases",
    "chat.greeting": "Hello! I'm your FasalSuraksha AI assistant. Ask me anything about crop diseases, treatments, pest control, or farming practices!",
    "chat.placeholder": "Ask about crop diseases...",
    // Feedback Modal
    "feedback.title": "Share Your Feedback",
    "feedback.rateQ": "How would you rate your experience?",
    "feedback.category": "Category",
    "feedback.selectCat": "Select category...",
    "feedback.bug": "Bug Report",
    "feedback.feature": "Feature Request",
    "feedback.improvement": "Improvement Suggestion",
    "feedback.general": "General Feedback",
    "feedback.yourFeedback": "Your Feedback",
    "feedback.placeholder": "Tell us what you think...",
    "feedback.submit": "Submit Feedback",
    "feedback.thanks": "✓ Thank you for your feedback!",
    // Login
    "login.welcome": "Welcome to FasalSuraksha",
    "login.subtitle": "AI-Powered Crop Protection System",
    "login.email": "Email",
    "login.password": "Password",
    "login.signIn": "Sign In",
    "login.noAccount": "Don't have an account?",
    "login.signUp": "Sign Up",
    "login.fullName": "Full Name",
    "login.createAccount": "Create Account",
    "login.hasAccount": "Already have an account?",
    "login.or": "OR",
    "login.google": "Continue with Google",
    "login.why": "Why FasalSuraksha?",
    "login.feature1": "Instant AI-powered disease detection",
    "login.feature2": "Expert treatment recommendations",
    "login.feature3": "24/7 AI agricultural assistant",
    "login.signingIn": "Signing you in...",
    // Contact
    "contact.back": "Back to Home",
    "contact.title": "Get in Touch",
    "contact.subtitle": "We're here to help farmers protect their crops. Reach out to us anytime!",
    "contact.info": "Contact Information",
    "contact.emailLabel": "Email",
    "contact.phoneLabel": "Phone",
    "contact.addressLabel": "Address",
    "contact.teamLabel": "Team",
    "contact.sendMsg": "Send us a Message",
    "contact.yourName": "Your Name",
    "contact.emailAddr": "Email Address",
    "contact.subject": "Subject",
    "contact.message": "Message",
    "contact.send": "Send Message",
    "contact.success": "✓ Message sent successfully! We'll get back to you soon.",
    // Dashboard
    "dash.totalScans": "Total Scans",
    "dash.diseasesFound": "Diseases Found",
    "dash.healthyPlants": "Healthy Plants",
    "dash.healthRate": "Health Rate",
    "dash.diseaseDistribution": "Disease Distribution",
    "dash.mostCommon": "Most Common Detection",
    "dash.basedOn": "Based on your scan history",
    "dash.newScan": "New Scan",
    "dash.detectionHistory": "Detection History",
    "dash.searchPlaceholder": "Search diseases...",
    "dash.filterAll": "All",
    "dash.filterDiseased": "Diseased",
    "dash.filterHealthy": "Healthy",
    "dash.clearAll": "Clear All",
    "dash.cause": "Cause",
    "dash.noHistory": "No Scans Yet",
    "dash.noHistoryDesc": "Upload a plant image to start detecting diseases and building your history.",
    "dash.startScan": "Start Your First Scan",
    // Language
    "lang.label": "Language"
  },
  hi: {
    // Navbar
    "nav.tagline": "AI-संचालित फसल सुरक्षा",
    "nav.home": "होम",
    "nav.dashboard": "डैशबोर्ड",
    "nav.contact": "संपर्क करें",
    "nav.feedback": "प्रतिक्रिया",
    "nav.logout": "लॉग आउट",
    // Hero
    "hero.title1": "अपनी फसलों की रक्षा करें",
    "hero.title2": "AI बुद्धिमत्ता के साथ",
    "hero.subtitle": "तुरंत रोग पहचान • विशेषज्ञ सुझाव • अपनी फसल बचाएं",
    // Upload
    "upload.title": "पौधे की छवि अपलोड करें",
    "upload.desc": "चुनने के लिए क्लिक करें या खींचकर छोड़ें",
    "upload.select": "छवि चुनें",
    "upload.analyze": "रोग विश्लेषण करें",
    // Results
    "result.complete": "विश्लेषण पूर्ण",
    "result.newScan": "नया स्कैन",
    "result.download": "रिपोर्ट डाउनलोड करें",
    "result.aiAnalyzed": "AI विश्लेषित",
    "result.diagnosis": "निदान",
    "result.cause": "कारण",
    "result.treatment": "उपचार",
    // Chatbot
    "chat.title": "फसलसुरक्षा AI",
    "chat.subtitle": "फसल रोगों के बारे में पूछें",
    "chat.greeting": "नमस्ते! मैं आपका फसलसुरक्षा AI सहायक हूं। फसल रोग, उपचार, कीट नियंत्रण, या खेती के बारे में कुछ भी पूछें!",
    "chat.placeholder": "फसल रोगों के बारे में पूछें...",
    // Feedback Modal
    "feedback.title": "अपनी प्रतिक्रिया साझा करें",
    "feedback.rateQ": "आप अपने अनुभव को कैसे रेट करेंगे?",
    "feedback.category": "श्रेणी",
    "feedback.selectCat": "श्रेणी चुनें...",
    "feedback.bug": "बग रिपोर्ट",
    "feedback.feature": "फीचर अनुरोध",
    "feedback.improvement": "सुधार सुझाव",
    "feedback.general": "सामान्य प्रतिक्रिया",
    "feedback.yourFeedback": "आपकी प्रतिक्रिया",
    "feedback.placeholder": "हमें बताएं आप क्या सोचते हैं...",
    "feedback.submit": "प्रतिक्रिया भेजें",
    "feedback.thanks": "✓ आपकी प्रतिक्रिया के लिए धन्यवाद!",
    // Login
    "login.welcome": "फसलसुरक्षा में आपका स्वागत है",
    "login.subtitle": "AI-संचालित फसल सुरक्षा प्रणाली",
    "login.email": "ईमेल",
    "login.password": "पासवर्ड",
    "login.signIn": "साइन इन करें",
    "login.noAccount": "खाता नहीं है?",
    "login.signUp": "साइन अप करें",
    "login.fullName": "पूरा नाम",
    "login.createAccount": "खाता बनाएं",
    "login.hasAccount": "पहले से खाता है?",
    "login.or": "या",
    "login.google": "Google से जारी रखें",
    "login.why": "फसलसुरक्षा क्यों?",
    "login.feature1": "तुरंत AI-संचालित रोग पहचान",
    "login.feature2": "विशेषज्ञ उपचार सुझाव",
    "login.feature3": "24/7 AI कृषि सहायक",
    "login.signingIn": "आपको साइन इन कर रहे हैं...",
    // Contact
    "contact.back": "होम पर वापस जाएं",
    "contact.title": "संपर्क करें",
    "contact.subtitle": "हम किसानों की फसल सुरक्षा में मदद के लिए यहां हैं। कभी भी संपर्क करें!",
    "contact.info": "संपर्क जानकारी",
    "contact.emailLabel": "ईमेल",
    "contact.phoneLabel": "फोन",
    "contact.addressLabel": "पता",
    "contact.teamLabel": "टीम",
    "contact.sendMsg": "हमें संदेश भेजें",
    "contact.yourName": "आपका नाम",
    "contact.emailAddr": "ईमेल पता",
    "contact.subject": "विषय",
    "contact.message": "संदेश",
    "contact.send": "संदेश भेजें",
    "contact.success": "✓ संदेश सफलतापूर्वक भेजा गया! हम जल्द ही आपसे संपर्क करेंगे।",
    // Dashboard
    "dash.totalScans": "कुल स्कैन",
    "dash.diseasesFound": "रोग पाए गए",
    "dash.healthyPlants": "स्वस्थ पौधे",
    "dash.healthRate": "स्वास्थ्य दर",
    "dash.diseaseDistribution": "रोग वितरण",
    "dash.mostCommon": "सबसे आम पहचान",
    "dash.basedOn": "आपके स्कैन इतिहास के आधार पर",
    "dash.newScan": "नया स्कैन",
    "dash.detectionHistory": "पहचान इतिहास",
    "dash.searchPlaceholder": "रोग खोजें...",
    "dash.filterAll": "सभी",
    "dash.filterDiseased": "रोगग्रस्त",
    "dash.filterHealthy": "स्वस्थ",
    "dash.clearAll": "सब हटाएं",
    "dash.cause": "कारण",
    "dash.noHistory": "अभी तक कोई स्कैन नहीं",
    "dash.noHistoryDesc": "रोग का पता लगाने और अपना इतिहास बनाने के लिए एक पौधे की छवि अपलोड करें।",
    "dash.startScan": "अपना पहला स्कैन शुरू करें",
    // Language
    "lang.label": "भाषा"
  }
};

// Get saved language or default to English
let currentLanguage = localStorage.getItem('fasalLang') || 'en';

// Apply translations to all elements with data-i18n attribute
function applyTranslations(lang) {
  currentLanguage = lang;
  localStorage.setItem('fasalLang', lang);

  const elements = document.querySelectorAll('[data-i18n]');
  elements.forEach(el => {
    const key = el.getAttribute('data-i18n');
    const text = translations[lang] && translations[lang][key];
    if (text) {
      el.textContent = text;
    }
  });

  // Handle placeholder translations
  const placeholders = document.querySelectorAll('[data-i18n-placeholder]');
  placeholders.forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    const text = translations[lang] && translations[lang][key];
    if (text) {
      el.setAttribute('placeholder', text);
    }
  });

  // Update language selector display
  const langBtn = document.getElementById('currentLangText');
  if (langBtn) {
    langBtn.textContent = lang === 'hi' ? 'हिंदी' : 'English';
  }

  // Update html lang attribute
  document.documentElement.lang = lang;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  applyTranslations(currentLanguage);

  // Language button click handlers
  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = btn.getAttribute('data-lang');
      applyTranslations(lang);
      // Close dropdown
      const dropdown = document.getElementById('langDropdown');
      if (dropdown) dropdown.classList.remove('show');
    });
  });

  // Toggle dropdown
  const langToggle = document.getElementById('langToggle');
  const langDropdown = document.getElementById('langDropdown');
  if (langToggle && langDropdown) {
    langToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      langDropdown.classList.toggle('show');
    });
    document.addEventListener('click', () => {
      langDropdown.classList.remove('show');
    });
  }
});

// Expose for chatbot.js
function getCurrentLanguage() {
  return currentLanguage;
}
