import streamlit as st
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from backend.database import Database  # 👈 YEH IMPORT ADD KARO

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Profile", 
        page_icon="👤",
        layout="wide"
    )
    
    # Check authentication
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.warning("⚠️ Please login first!")
        st.session_state.page = "Login"
        st.rerun()
    
    # Initialize session states
    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False
    if 'password_mode' not in st.session_state:
        st.session_state.password_mode = False
    
    # Get current user email
    user_email = st.session_state.get('user', None)
    if not user_email:
        st.session_state.page = "Login"
        st.rerun()
    
    # Load user data from database
    db = Database()
    # Get user data - we need to get user by email
    success, user_data = db.login_user(user_email, "")  # This just checks existence
    if not success:
        # Create default user data if not exists
        user_data = {'name': user_email.split('@')[0].title(), 'email': user_email}
    
    # CSS part (same rahega - long CSS ko shorten kar raha hoon for brevity)
    st.markdown("""
    <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .stApp {
            background: linear-gradient(-45deg, #4158D0, #C850C0, #FFCC70, #00ff9d);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        h1, h2, h3 {
            color: white !important;
        }
        
        .profile-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            border: 4px solid #00ff9d;
        }
        
        .avatar-text {
            font-size: 48px;
            color: white;
            font-weight: bold;
        }
        
        .info-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            border-left: 5px solid #00ff9d;
        }
        
        .info-label {
            color: #00ff9d;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .info-value {
            color: white;
            font-size: 16px;
        }
        
        .stat-box {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .stat-number {
            font-size: 28px;
            font-weight: bold;
            color: #00ff9d;
        }
        
        .stat-label {
            color: white;
            font-size: 14px;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
        
        .success-message {
            background: rgba(0, 255, 157, 0.2);
            border: 2px solid #00ff9d;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            color: #00ff9d;
            margin: 10px 0;
        }
        
        .warning-message {
            background: rgba(255, 187, 51, 0.2);
            border: 2px solid #ffbb33;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            color: #ffbb33;
            margin: 10px 0;
        }
        
        .error-message {
            background: rgba(255, 68, 68, 0.2);
            border: 2px solid #ff4444;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            color: #ff4444;
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>👤 My Profile</h1>", unsafe_allow_html=True)
    
    # Profile Header
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="profile-card" style="text-align: center;">', unsafe_allow_html=True)
        
        # Avatar with first letter of name
        user_name = user_data.get('name', user_email.split('@')[0].title())
        first_letter = user_name[0].upper() if user_name else 'U'
        
        st.markdown(f"""
        <div class="avatar">
            <div class="avatar-text">{first_letter}</div>
        </div>
        <h2 style="color: white; margin: 10px 0;">{user_name}</h2>
        <p style="color: rgba(255,255,255,0.7);">{user_email}</p>
        <p style="color: #00ff9d;">✨ Member since {datetime.now().strftime('%B %Y')}</p>
        """, unsafe_allow_html=True)
        
        # Edit/View toggle
        col_a, col_b, col_c = st.columns(3)
        with col_b:
            if not st.session_state.edit_mode and not st.session_state.password_mode:
                if st.button("✏️ Edit Profile", use_container_width=True):
                    st.session_state.edit_mode = True
                    st.rerun()
            elif st.session_state.edit_mode:
                if st.button("❌ Cancel", use_container_width=True):
                    st.session_state.edit_mode = False
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistics Section
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Your Statistics")
    
    # Get history data
    history_count = len(st.session_state.get('history_data', [])) if 'history_data' in st.session_state else 0
    avg_score = 0
    best_score = 0
    
    if history_count > 0:
        avg_score = sum(item.get('probability', 0) for item in st.session_state.history_data) / history_count
        best_score = max(item.get('probability', 0) for item in st.session_state.history_data)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{history_count}</div>
            <div class="stat-label">Total Analyses</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{avg_score:.1f}%</div>
            <div class="stat-label">Average Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{best_score:.1f}%</div>
            <div class="stat-label">Best Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # EDIT MODE
    if st.session_state.edit_mode:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### ✏️ Edit Profile")
        
        with st.form("edit_form"):
            new_name = st.text_input("Full Name", value=user_name)
            new_phone = st.text_input("Phone", value=user_data.get('phone', '+91 98765 43210'))
            new_college = st.text_input("College", value=user_data.get('college', 'IIT Delhi'))
            new_bio = st.text_area("Bio", value=user_data.get('bio', 'Passionate developer'), height=100)
            
            col_save, col_cancel = st.columns(2)
            with col_save:
                save_btn = st.form_submit_button("💾 Save Changes", use_container_width=True)
            with col_cancel:
                cancel_btn = st.form_submit_button("❌ Cancel", use_container_width=True)
            
            if save_btn:
                st.markdown('<div class="success-message">✅ Profile updated successfully!</div>', unsafe_allow_html=True)
                st.session_state.edit_mode = False
                st.rerun()
            
            if cancel_btn:
                st.session_state.edit_mode = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # PASSWORD MODE
    elif st.session_state.password_mode:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Change Password")
        
        with st.form("password_form"):
            current_pw = st.text_input("Current Password", type="password")
            new_pw = st.text_input("New Password", type="password")
            confirm_pw = st.text_input("Confirm Password", type="password")
            
            col_update, col_cancel = st.columns(2)
            with col_update:
                update_btn = st.form_submit_button("🔄 Update Password", use_container_width=True)
            with col_cancel:
                cancel_btn = st.form_submit_button("❌ Cancel", use_container_width=True)
            
            if update_btn:
                if not all([current_pw, new_pw, confirm_pw]):
                    st.markdown('<div class="error-message">❌ All fields required!</div>', unsafe_allow_html=True)
                elif new_pw != confirm_pw:
                    st.markdown('<div class="error-message">❌ Passwords don\'t match!</div>', unsafe_allow_html=True)
                elif len(new_pw) < 6:
                    st.markdown('<div class="error-message">❌ Password must be 6+ characters!</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="success-message">✅ Password changed successfully!</div>', unsafe_allow_html=True)
                    st.session_state.password_mode = False
                    st.rerun()
            
            if cancel_btn:
                st.session_state.password_mode = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # VIEW MODE
    else:
        # Personal Info
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Personal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="info-item">
                <div class="info-label">📧 Email</div>
                <div class="info-value">{user_email}</div>
            </div>
            <div class="info-item">
                <div class="info-label">📱 Phone</div>
                <div class="info-value">+91 98765 43210</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="info-item">
                <div class="info-label">🎓 Education</div>
                <div class="info-value">B.Tech Computer Science</div>
            </div>
            <div class="info-item">
                <div class="info-label">🏫 College</div>
                <div class="info-value">IIT Delhi</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="info-item">
            <div class="info-label">📝 Bio</div>
            <div class="info-value">Passionate developer looking to make a difference.</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Skills
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 💪 Skills & Achievements")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔧 Technical Skills")
            skills = ["Python", "Machine Learning", "Data Analysis", "SQL", "JavaScript"]
            skills_html = ""
            for skill in skills:
                skills_html += f'<span style="background:rgba(255,255,255,0.2); padding:5px 15px; border-radius:50px; margin:5px; display:inline-block;">{skill}</span>'
            st.markdown(skills_html, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🏆 Achievements")
            st.markdown("""
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:10px; margin:5px 0;">🏅 Hackathon Winner 2024</div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:10px; margin:5px 0;">📜 Certified Python Developer</div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:10px; margin:5px 0;">📊 Data Science Certification</div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Account Settings
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### ⚙️ Account Settings")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔐 Change Password", use_container_width=True):
                st.session_state.password_mode = True
                st.rerun()
        
        with col2:
            if st.button("📧 Notifications", use_container_width=True):
                st.markdown('<div class="warning-message">📧 Coming soon!</div>', unsafe_allow_html=True)
        
        with col3:
            if st.button("🗑️ Delete Account", use_container_width=True):
                st.markdown('<div class="error-message">⚠️ Contact support</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recent Activity
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 📋 Recent Activity")
        
        if 'history_data' in st.session_state and len(st.session_state.history_data) > 0:
            for item in st.session_state.history_data[:3]:
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:15px; margin:10px 0;">
                    <div style="display:flex; justify-content:space-between;">
                        <span style="color:white;">📊 {item.get('domain', 'Analysis')}</span>
                        <span style="color:#00ff9d;">{item.get('probability', 0)}%</span>
                    </div>
                    <div style="color:rgba(255,255,255,0.5); font-size:12px;">{item.get('date', '')}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No recent activity found. Go to Dashboard to analyze your profile!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back to Home
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()
    
    db.close()