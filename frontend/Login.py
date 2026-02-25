import streamlit as st
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from backend.database import Database

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
            min-height: 100vh;
        }
        
        .main > div {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .login-card {
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            width: 100%;
            max-width: 420px;
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
        
        .stTextInput > div > div > input {
            border-radius: 12px !important;
            border: 2px solid #e0e0e0 !important;
            padding: 15px 20px !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            background: #f8f9fa !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1) !important;
            background: white !important;
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #999 !important;
            font-style: italic;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 12px !important;
            padding: 15px 20px !important;
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
            padding: 12px;
            text-align: center;
            color: #00ff9d;
            font-weight: 600;
            margin: 10px 0;
        }
        
        .error-message {
            background: rgba(255, 68, 68, 0.1);
            border: 2px solid #ff4444;
            border-radius: 10px;
            padding: 12px;
            text-align: center;
            color: #ff4444;
            font-weight: 600;
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Login card
    st.markdown("""
    <div class="login-card">
        <div class="logo">✨</div>
        <div class="title">CareerPulse AI</div>
        <div class="subtitle">Your Future, Predicted by AI</div>
    """, unsafe_allow_html=True)

    # Login form
    with st.form("login_form"):
        email = st.text_input("", placeholder="Enter your email address")
        password = st.text_input("", type="password", placeholder="Enter your password")
        
        col1, col2 = st.columns(2)
        with col1:
            remember = st.checkbox("Remember me", value=True)
        
        sign_in = st.form_submit_button("Sign In", use_container_width=True)
        
        if sign_in:
            if email and password:
                # Database se check karo
                db = Database()
                success, result = db.login_user(email, password)
                db.close()
                
                if success:
                    st.markdown("""
                    <div class="success-message">
                        ✅ Login successful! Redirecting to Home...
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(1)
                    st.session_state['authenticated'] = True
                    st.session_state['user'] = email
                    st.session_state['user_name'] = result['name']
                    st.session_state['page'] = "Home"
                    st.rerun()
                else:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ {result}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="error-message">
                    ❌ Please fill all fields!
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📝 Create Account", use_container_width=True):
            st.session_state.page = "Register"
            st.rerun()
    
    with col2:
        if st.button("❓ Need Help?", use_container_width=True):
            st.info("📧 Contact: support@careerpulse.ai")
    
    with col3:
        if st.button("🔒 Forgot?", use_container_width=True):
            st.info("📧 Password reset link sent to your email!")

    # Footer
    st.markdown("""
    <div style="text-align: center; color: rgba(255, 255, 255, 0.8); font-size: 0.85rem; margin-top: 2rem;">
        © 2026 CareerPulse AI. All rights reserved.
    </div>
    """, unsafe_allow_html=True)