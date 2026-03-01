from flask import Flask, render_template,request,redirect,send_from_directory,url_for,jsonify,session
import numpy as np
import json
import uuid
import tensorflow as tf
import google.generativeai as genai
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth
from functools import wraps

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))

# Initialize Firebase Admin SDK
try:
    # Try to load from JSON string (for production deployment)
    firebase_creds_json = os.getenv('FIREBASE_CREDENTIALS_JSON')
    if firebase_creds_json:
        import json
        cred_dict = json.loads(firebase_creds_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        print("✅ Firebase Admin initialized from environment variable (Production)")
    else:
        # Fallback to file path (for local development)
        cred_path = os.getenv('FIREBASE_ADMIN_CREDENTIALS', 'serviceAccountKey.json')
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("✅ Firebase Admin initialized from file (Local)")
        else:
            print("⚠️ Warning: Firebase credentials not found. Authentication will not work.")
except Exception as e:
    print(f"❌ Firebase initialization error: {e}")

# Configure Gemini AI
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyAaNcmZqswxCczTXtggd1nsMl15880i2Q4')
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-2.5-flash')

model = tf.keras.models.load_model("models/plant_disease_recog_model_pwp.keras")
label = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Background_without_leaves',
 'Blueberry___healthy',
 'Cherry___Powdery_mildew',
 'Cherry___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight',
 'Corn___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

with open("plant_disease.json",'r') as file:
    plant_disease = json.load(file)

# print(plant_disease[4])

@app.route('/uploadimages/<path:filename>')
def uploaded_images(filename):
    return send_from_directory('./uploadimages', filename)

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/',methods = ['GET'])
@login_required
def home():
    user = session.get('user')
    return render_template('home.html', user=user)

@app.route('/login')
def login():
    # If user is already logged in, redirect to home
    if 'user' in session:
        return redirect(url_for('home'))
    
    return render_template('login.html', 
                         firebase_config={
                             'apiKey': os.getenv('FIREBASE_API_KEY'),
                             'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
                             'projectId': os.getenv('FIREBASE_PROJECT_ID'),
                             'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
                             'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
                             'appId': os.getenv('FIREBASE_APP_ID')
                         })

@app.route('/auth/verify', methods=['POST'])
def verify_token():
    try:
        data = request.get_json()
        id_token = data.get('idToken')
        
        # Verify the Firebase ID token
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        
        # Store user info in session
        session['user'] = {
            'uid': uid,
            'email': decoded_token.get('email'),
            'name': decoded_token.get('name'),
            'picture': decoded_token.get('picture')
        }
        
        return jsonify({
            'success': True,
            'message': 'Authentication successful',
            'user': session['user']
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 401

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/contact')
@login_required
def contact():
    user = session.get('user')
    return render_template('contact.html', user=user)

@app.route('/contact/submit', methods=['POST'])
@login_required
def contact_submit():
    try:
        data = request.get_json()
        user = session.get('user')
        
        # Store contact submission (you can save to Firestore or send email)
        contact_data = {
            'user_id': user.get('uid'),
            'user_email': user.get('email'),
            'name': data.get('name'),
            'email': data.get('email'),
            'subject': data.get('subject'),
            'message': data.get('message'),
            'timestamp': str(uuid.uuid4())  # You can use datetime here
        }
        
        # Log to console (in production, save to database or send email)
        print(f"Contact Form Submission: {contact_data}")
        
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

@app.route('/feedback', methods=['POST'])
@login_required
def feedback():
    try:
        data = request.get_json()
        user = session.get('user')
        
        # Store feedback (you can save to Firestore)
        feedback_data = {
            'user_id': user.get('uid'),
            'user_email': user.get('email'),
            'user_name': user.get('name'),
            'rating': data.get('rating'),
            'category': data.get('category'),
            'message': data.get('message'),
            'timestamp': str(uuid.uuid4())  # You can use datetime here
        }
        
        # Log to console (in production, save to database)
        print(f"Feedback Submission: {feedback_data}")
        
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

def extract_features(image):
    image = tf.keras.utils.load_img(image,target_size=(160,160))
    feature = tf.keras.utils.img_to_array(image)
    feature = np.array([feature])
    return feature

def model_predict(image):
    img = extract_features(image)
    prediction = model.predict(img)
    # print(prediction)
    prediction_label = plant_disease[prediction.argmax()]
    return prediction_label

@app.route('/upload/',methods = ['POST','GET'])
@login_required
def uploadimage():
    if request.method == "POST":
        image = request.files['img']
        temp_name = f"uploadimages/temp_{uuid.uuid4().hex}"
        image.save(f'{temp_name}_{image.filename}')
        print(f'{temp_name}_{image.filename}')
        prediction = model_predict(f'./{temp_name}_{image.filename}')
        user = session.get('user')
        return render_template('home.html',result=True,imagepath = f'/{temp_name}_{image.filename}', prediction = prediction, user=user)
    
    else:
        return redirect('/')

@app.route('/chat', methods=['POST'])
@login_required
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({
                'success': False,
                'response': 'Please enter a message.'
            })
        
        # Check for creator/about questions
        creator_keywords = ['who created', 'who made', 'who built', 'who developed', 'your creator', 'your developer', 'who are you', 'about you', 'about this', 'created by', 'made by', 'your team']
        if any(keyword in user_message.lower() for keyword in creator_keywords):
            return jsonify({
                'success': True,
                'response': 'I am FasalSuraksha AI Assistant! 🌾 Created by Nirvana Coders under the guidance of Sneha, Akshita, Rahul, Raunak, and Krish. We are here to help farmers protect their crops with AI-powered disease detection and expert agricultural advice. How can I assist you today?'
            })
        
        # Create a context-aware prompt for agricultural queries
        system_prompt = """You are an expert agricultural AI assistant for FasalSuraksha (Crop Protection), created by Nirvana Coders team (Sneha, Akshita, Rahul, Raunak, and Krish).
        Provide helpful, accurate, and practical advice to farmers in a friendly and easy-to-understand manner.
        Keep responses concise (2-4 sentences) but informative.
        Focus on: plant diseases, symptoms, treatments, prevention, organic farming, pest control, crop management, and agricultural best practices.
        If asked about non-agricultural topics, politely redirect to agricultural topics.
        IMPORTANT: If asked about who created you, always mention "Created by Nirvana Coders under the guidance of Sneha, Akshita, Rahul, Raunak, and Krish"."""
        
        full_prompt = f"{system_prompt}\n\nFarmer's Question: {user_message}\n\nYour helpful answer:"
        
        # Generate response using Gemini with safety settings
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 500,
        }
        
        # Safety settings to prevent blocking
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        
        response = gemini_model.generate_content(
            full_prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        # Debug: Print response object
        print(f"Gemini Response Object: {response}")
        
        # Check if response has text
        bot_response = None
        
        # Try to get text from response
        try:
            if response and hasattr(response, 'text'):
                bot_response = response.text
                print(f"Response text: {bot_response}")
        except Exception as text_error:
            print(f"Error accessing response.text: {text_error}")
            # Try alternative ways to get response
            if hasattr(response, 'candidates') and response.candidates:
                try:
                    bot_response = response.candidates[0].content.parts[0].text
                    print(f"Got response from candidates: {bot_response}")
                except Exception as candidate_error:
                    print(f"Error accessing candidates: {candidate_error}")
        
        # If still no response, provide fallback
        if not bot_response:
            print(f"No response text found. Response object: {response}")
            print(f"Response prompt_feedback: {getattr(response, 'prompt_feedback', 'N/A')}")
            bot_response = "I apologize, but I couldn't generate a proper response. This might be due to content safety filters. Could you please rephrase your question?"
        
        return jsonify({
            'success': True,
            'response': bot_response
        })
    
    except Exception as e:
        print(f"Chat Error: {str(e)}")  # Log error to console
        print(f"Error type: {type(e).__name__}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return jsonify({
            'success': False,
            'response': f'I apologize for the inconvenience. There was a technical issue: {str(e)}. Please try asking your question again.'
        })
        
    
if __name__ == "__main__":
    app.run(debug=True)