import streamlit as st
import time
import hashlib
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from backend.database import Database

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def show():
    st.markdown("""
    <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .stApp {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        .main > div {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .register-card {
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 450px;
            margin: 0 auto;
            animation: slideUp 0.6s ease;
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .logo {
            text-align: center;
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }
        
        .title {
            text-align: center;
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 0.95rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid #f0f0f0;
            padding-bottom: 1.5rem;
        }
        
        /* ✅ FIXED - BLACK TEXT INPUTS */
        .stTextInput > div > div > input {
            border-radius: 12px !important;
            border: 2px solid #e0e0e0 !important;
            padding: 12px 20px !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            background: #ffffff !important;
            color: #000000 !important;  /* 👈 BLACK TEXT */
            margin: 5px 0 !important;
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #666666 !important;  /* 👈 DARK GRAY PLACEHOLDER */
            font-style: italic;
            opacity: 0.8;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1) !important;
            background: #ffffff !important;
            color: #000000 !important;  /* 👈 BLACK TEXT ON FOCUS */
        }
        
        .stCheckbox {
            color: #666 !important;
            margin: 1rem 0 !important;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 12px 20px !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            border: none !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            margin: 1rem 0 !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
        
        .success-message {
            background: rgba(0, 255, 157, 0.1);
            border: 2px solid #00ff9d;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            color: #00ff9d;
            font-weight: 600;
            margin: 10px 0;
        }
        
        .error-message {
            background: rgba(255, 68, 68, 0.1);
            border: 2px solid #ff4444;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            color: #ff4444;
            font-weight: 600;
            margin: 10px 0;
        }
        
        .back-button {
            margin-top: 1rem;
        }
        
        .back-button .stButton > button {
            background: transparent !important;
            color: #667eea !important;
            border: 2px solid #667eea !important;
            margin: 0 !important;
        }
        
        .footer {
            text-align: center;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.85rem;
            margin-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Register card
    st.markdown("""
    <div class="register-card">
        <div class="logo">📝</div>
        <div class="title">Create Account</div>
        <div class="subtitle">Join CareerPulse AI today</div>
    """, unsafe_allow_html=True)

    # Register form
    with st.form("register_form"):
        full_name = st.text_input("", placeholder="Full Name", key="reg_name")
        email = st.text_input("", placeholder="Email Address", key="reg_email")
        password = st.text_input("", type="password", placeholder="Password (min. 6 characters)", key="reg_pass")
        confirm = st.text_input("", type="password", placeholder="Confirm Password", key="reg_confirm")
        
        terms = st.checkbox("I agree to the Terms & Conditions")
        
        register = st.form_submit_button("Create Account", use_container_width=True)
        
        if register:
            if not all([full_name, email, password, confirm]):
                st.markdown("""
                <div class="error-message">
                    ❌ Please fill all fields!
                </div>
                """, unsafe_allow_html=True)
            elif password != confirm:
                st.markdown("""
                <div class="error-message">
                    ❌ Passwords don't match!
                </div>
                """, unsafe_allow_html=True)
            elif len(password) < 6:
                st.markdown("""
                <div class="error-message">
                    ❌ Password must be at least 6 characters!
                </div>
                """, unsafe_allow_html=True)
            elif not terms:
                st.markdown("""
                <div class="error-message">
                    ❌ Please accept Terms & Conditions!
                </div>
                """, unsafe_allow_html=True)
            else:
                with st.spinner("Creating account..."):
                    time.sleep(2)
                
                # Use backend database
                db = Database()
                success, message = db.register_user(full_name, email, password)
                db.close()
                
                if success:
                    st.markdown("""
                    <div class="success-message">
                        ✅ Account created successfully! Redirecting to Login...
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(2)
                    st.session_state.page = "Login"
                    st.rerun()
                else:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ {message}
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Back to login button
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("← Back to Login", use_container_width=True):
            st.session_state.page = "Login"
            st.rerun()

    # Footer
    st.markdown("""
    <div class="footer">
        © 2026 CareerPulse AI. All rights reserved.
    </div>
    """, unsafe_allow_html=True)