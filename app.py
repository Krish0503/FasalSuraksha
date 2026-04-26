from flask import Flask, render_template,request,redirect,send_from_directory,url_for,jsonify,session,send_file
from datetime import datetime
from fpdf import FPDF
import numpy as np
import json
import uuid
import tensorflow as tf
import google.generativeai as genai
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth, firestore
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
        print("[OK] Firebase Admin initialized from environment variable (Production)")
    else:
        # Fallback to file path (for local development)
        cred_path = os.getenv('FIREBASE_ADMIN_CREDENTIALS', 'serviceAccountKey.json')
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("[OK] Firebase Admin initialized from file (Local)")
        else:
            print("[WARNING] Firebase credentials not found. Authentication will not work.")
except Exception as e:
    print(f"[ERROR] Firebase initialization error: {e}")

# Initialize Firestore
try:
    db = firestore.client()
    print("[OK] Firestore client initialized")
except Exception as e:
    db = None
    print(f"[WARNING] Firestore initialization failed: {e}. Dashboard/history features will be disabled.")

# Configure Gemini AI
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("[WARNING] GEMINI_API_KEY not set in .env file. Chatbot will not work.")
    GEMINI_API_KEY = ""
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

def save_detection(user_uid, prediction, image_path):
    """Save a detection result to Firestore for user history."""
    if not db:
        print("[WARNING] Firestore not available, skipping detection save.")
        return None
    try:
        detection_data = {
            'disease_name': prediction.get('name', 'Unknown'),
            'cause': prediction.get('cause', 'N/A'),
            'cure': prediction.get('cure', 'N/A'),
            'image_path': image_path,
            'timestamp': datetime.utcnow(),
            'is_healthy': 'healthy' in prediction.get('name', '').lower(),
        }
        doc_ref = db.collection('users').document(user_uid).collection('detections').add(detection_data)
        print(f"[OK] Detection saved for user {user_uid}")
        return doc_ref
    except Exception as e:
        print(f"[ERROR] Failed to save detection: {e}")
        return None

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
        
        # Save detection to Firestore history
        save_detection(user.get('uid'), prediction, f'/{temp_name}_{image.filename}')
        
        return render_template('home.html',result=True,imagepath = f'/{temp_name}_{image.filename}', prediction = prediction, user=user)
    
    else:
        return redirect('/')

@app.route('/generate_report', methods=['POST'])
@login_required
def generate_report():
    try:
        data = request.get_json()
        diagnosis = data.get('diagnosis', 'N/A')
        cause = data.get('cause', 'N/A')
        treatment = data.get('treatment', 'N/A')
        image_path = data.get('imagePath', '')
        lang = data.get('lang', 'en')
        user = session.get('user', {})

        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        
        # Add Fonts
        font_dir = os.path.join(app.root_path, 'static', 'fonts')
        en_font = os.path.join(font_dir, 'NotoSans-Regular.ttf')
        hi_font = os.path.join(font_dir, 'NotoSansDevanagari-Regular.ttf')
        
        if os.path.exists(en_font):
            pdf.add_font('NotoSans', '', en_font)
            default_font = 'NotoSans'
        else:
            default_font = 'Arial' # Fallback
            
        if os.path.exists(hi_font):
            pdf.add_font('NotoHindi', '', hi_font)
            hindi_font = 'NotoHindi'
        else:
            hindi_font = default_font # Fallback
            
        # Use Hindi font if language is Hindi
        current_font = hindi_font if lang == 'hi' else default_font
        pdf.set_font(current_font, size=12)

        # Header / Branding
        pdf.set_fill_color(30, 60, 114) # Navbar color
        pdf.rect(0, 0, 210, 45, 'F')
        
        pdf.set_text_color(255, 255, 255)
        pdf.set_font(current_font, size=24)
        pdf.cell(0, 15, 'FasalSuraksha', ln=True, align='C')
        pdf.set_font(current_font, size=10)
        pdf.cell(0, 6, 'AI-Powered Crop Protection System | www.fasalsuraksha.com', ln=True, align='C')
        pdf.cell(0, 6, 'Helpline: +91 1800-XXX-XXXX | Email: support@fasalsuraksha.com', ln=True, align='C')
        
        pdf.ln(20)
        pdf.set_text_color(0, 0, 0)
        
        # User Details & Date (Prescription Header)
        from datetime import datetime
        now = datetime.now().strftime("%d-%m-%Y")
        
        pdf.set_draw_color(102, 126, 234)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        pdf.set_font(current_font, size=11)
        pdf.cell(100, 6, f"Farmer Name: {user.get('name', 'N/A')}", ln=False)
        pdf.cell(90, 6, f"Date: {now}", ln=True, align='R')
        pdf.cell(100, 6, f"Email: {user.get('email', 'N/A')}", ln=True)
        
        pdf.ln(5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(15)

        # Rx Symbol or Title
        pdf.set_font(current_font, size=20)
        pdf.set_text_color(30, 60, 114)
        title_text = "Plant Health Rx" if lang == 'en' else "पौधे का स्वास्थ्य पर्चा"
        pdf.cell(0, 10, title_text, ln=True)
        pdf.ln(8)
        
        pdf.set_text_color(0, 0, 0)

        # Add Image if exists (top right of result section)
        if image_path:
            import urllib.parse
            # Unquote the path in case JS sends '%20' for spaces
            decoded_path = urllib.parse.unquote(image_path)
            full_image_path = os.path.join(app.root_path, decoded_path.lstrip('/'))
            if os.path.exists(full_image_path):
                # Calculate image dimensions to fit
                pdf.image(full_image_path, x=150, y=pdf.get_y(), w=45)
            else:
                print(f"Image not found at: {full_image_path}")

        # Diagnosis
        pdf.set_font(current_font, size=14)
        diag_label = "Diagnosis: " if lang == 'en' else "निदान: "
        pdf.set_font(current_font, '') 
        pdf.cell(130, 10, f"{diag_label} {diagnosis}", ln=True)
        
        # Cause
        pdf.ln(5)
        cause_label = "Cause: " if lang == 'en' else "कारण: "
        pdf.set_font(current_font, size=11)
        pdf.multi_cell(130, 6, f"{cause_label} {cause}")
        
        pdf.ln(15)
        if image_path and pdf.get_y() < 140: pdf.set_y(140) # Ensure we are below image

        # Treatment
        pdf.set_draw_color(102, 126, 234)
        pdf.set_fill_color(245, 247, 255)
        pdf.set_font(current_font, size=12)
        treat_label = "Recommended Treatment & Advice" if lang == 'en' else "अनुशंसित उपचार और सलाह"
        pdf.cell(0, 10, treat_label, border=0, ln=True, fill=True)
        pdf.set_font(current_font, size=10)
        pdf.multi_cell(0, 6, treatment, border=0)

        pdf.ln(30)
        pdf.set_font(current_font, size=8)
        pdf.set_text_color(100, 100, 100)
        footer_text = "This is an AI-generated prescription for reference. Please consult a professional agricultural expert before applying chemicals."
        if lang == 'hi':
            footer_text = "यह संदर्भ के लिए एक AI-जनरेटेड पर्चा है। रसायनों का उपयोग करने से पहले कृपया एक पेशेवर कृषि विशेषज्ञ से परामर्श लें।"
        pdf.multi_cell(0, 5, footer_text, align='C')

        # Save to temporary file
        temp_pdf = f"static/reports/report_{uuid.uuid4().hex}.pdf"
        os.makedirs("static/reports", exist_ok=True)
        pdf.output(temp_pdf)
        
        return send_file(temp_pdf, as_attachment=True)

    except Exception as e:
        print(f"PDF Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/chat', methods=['POST'])
@login_required
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        user_language = data.get('language', 'en')
        
        if not user_message:
            return jsonify({
                'success': False,
                'response': 'Please enter a message.' if user_language == 'en' else 'कृपया एक संदेश दर्ज करें।'
            })
        
        # Check for creator/about questions
        creator_keywords = ['who created', 'who made', 'who built', 'who developed', 'your creator', 'your developer', 'who are you', 'about you', 'about this', 'created by', 'made by', 'your team', 'kisne banaya', 'kiske dwara']
        if any(keyword in user_message.lower() for keyword in creator_keywords):
            if user_language == 'hi':
                response_text = 'मैं फसलसुरक्षा AI सहायक हूं! 🌾 निर्वाण कोडर्स द्वारा स्नेहा, अक्षिता, राहुल, रौनक और कृष के मार्गदर्शन में बनाया गया। हम AI-संचालित रोग पहचान से किसानों की फसल सुरक्षा में मदद करते हैं। मैं आज आपकी कैसे मदद कर सकता हूं?'
            else:
                response_text = 'I am FasalSuraksha AI Assistant! 🌾 Created by Nirvana Coders under the guidance of Sneha, Akshita, Rahul, Raunak, and Krish. We are here to help farmers protect their crops with AI-powered disease detection and expert agricultural advice. How can I assist you today?'
            return jsonify({
                'success': True,
                'response': response_text
            })
        
        # Language instruction for Gemini
        lang_instruction = ""
        if user_language == 'hi':
            lang_instruction = "IMPORTANT: You MUST respond in Hindi (Devanagari script). Do not respond in English."
        
        # Create a context-aware prompt for agricultural queries
        system_prompt = f"""You are an expert agricultural AI assistant for FasalSuraksha (Crop Protection), created by Nirvana Coders team (Sneha, Akshita, Rahul, Raunak, and Krish).
        Provide helpful, accurate, and practical advice to farmers in a friendly and easy-to-understand manner.
        Keep responses concise (2-4 sentences) but informative.
        Focus on: plant diseases, symptoms, treatments, prevention, organic farming, pest control, crop management, and agricultural best practices.
        If asked about non-agricultural topics, politely redirect to agricultural topics.
        IMPORTANT: If asked about who created you, always mention "Created by Nirvana Coders under the guidance of Sneha, Akshita, Rahul, Raunak, and Krish".
        {lang_instruction}"""
        
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
        

@app.route('/dashboard')
@login_required
def dashboard():
    user = session.get('user')
    stats = {
        'total_scans': 0,
        'diseases_found': 0,
        'healthy_count': 0,
        'success_rate': 0,
        'most_common': 'N/A'
    }
    detections = []
    disease_distribution = {}
    
    if db:
        try:
            docs = db.collection('users').document(user['uid']).collection('detections').order_by('timestamp', direction=firestore.Query.DESCENDING).stream()
            
            for doc in docs:
                data = doc.to_dict()
                data['id'] = doc.id
                # Convert Firestore timestamp to string
                if data.get('timestamp'):
                    ts = data['timestamp']
                    if hasattr(ts, 'strftime'):
                        data['timestamp_str'] = ts.strftime('%d %b %Y, %I:%M %p')
                        data['timestamp_iso'] = ts.isoformat()
                    else:
                        data['timestamp_str'] = str(ts)
                        data['timestamp_iso'] = str(ts)
                else:
                    data['timestamp_str'] = 'Unknown'
                    data['timestamp_iso'] = ''
                detections.append(data)
                
                # Build disease distribution
                disease_name = data.get('disease_name', 'Unknown')
                # Clean up name for display
                clean_name = disease_name.replace('___', ' - ').replace('_', ' ')
                disease_distribution[clean_name] = disease_distribution.get(clean_name, 0) + 1
            
            stats['total_scans'] = len(detections)
            stats['healthy_count'] = sum(1 for d in detections if d.get('is_healthy', False))
            stats['diseases_found'] = stats['total_scans'] - stats['healthy_count']
            stats['success_rate'] = round((stats['healthy_count'] / stats['total_scans'] * 100) if stats['total_scans'] > 0 else 0)
            
            if disease_distribution:
                stats['most_common'] = max(disease_distribution, key=disease_distribution.get)
                
        except Exception as e:
            print(f"[ERROR] Failed to fetch dashboard data: {e}")
            import traceback
            print(traceback.format_exc())
    
    return render_template('dashboard.html', 
                         user=user, 
                         stats=stats, 
                         detections=detections,
                         disease_distribution=disease_distribution)


@app.route('/api/history')
@login_required
def api_history():
    user = session.get('user')
    detections = []
    
    if db:
        try:
            docs = db.collection('users').document(user['uid']).collection('detections').order_by('timestamp', direction=firestore.Query.DESCENDING).stream()
            
            for doc in docs:
                data = doc.to_dict()
                data['id'] = doc.id
                if data.get('timestamp'):
                    ts = data['timestamp']
                    if hasattr(ts, 'strftime'):
                        data['timestamp_str'] = ts.strftime('%d %b %Y, %I:%M %p')
                    else:
                        data['timestamp_str'] = str(ts)
                    # Firestore timestamps aren't JSON serializable
                    data['timestamp'] = str(data['timestamp'])
                detections.append(data)
        except Exception as e:
            print(f"[ERROR] Failed to fetch history: {e}")
    
    return jsonify({'success': True, 'detections': detections})


@app.route('/api/history/<detection_id>/delete', methods=['POST'])
@login_required
def delete_detection(detection_id):
    user = session.get('user')
    
    if not db:
        return jsonify({'success': False, 'message': 'Database not available'}), 500
    
    try:
        db.collection('users').document(user['uid']).collection('detections').document(detection_id).delete()
        return jsonify({'success': True, 'message': 'Detection deleted successfully'})
    except Exception as e:
        print(f"[ERROR] Failed to delete detection: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/history/clear', methods=['POST'])
@login_required
def clear_history():
    user = session.get('user')
    
    if not db:
        return jsonify({'success': False, 'message': 'Database not available'}), 500
    
    try:
        docs = db.collection('users').document(user['uid']).collection('detections').stream()
        for doc in docs:
            doc.reference.delete()
        return jsonify({'success': True, 'message': 'All history cleared'})
    except Exception as e:
        print(f"[ERROR] Failed to clear history: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500

    
if __name__ == "__main__":
    app.run(debug=True)