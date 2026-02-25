import streamlit as st
from datetime import datetime
import random

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
    
    # Initialize profile data in session state if not exists
    if 'profile_data' not in st.session_state:
        st.session_state.profile_data = {
            'name': 'Demo User',
            'email': 'demo@careerpulse.ai',
            'phone': '+91 98765 43210',
            'education': 'B.Tech Computer Science',
            'college': 'Indian Institute of Technology',
            'grad_year': '2024',
            'location': 'Mumbai, India',
            'bio': 'Passionate developer looking to make a difference in the tech world.',
            'skills': ['Python', 'Machine Learning', 'Data Analysis', 'SQL', 'JavaScript', 'React', 'DSA'],
            'soft_skills': ['Communication', 'Teamwork', 'Leadership', 'Problem Solving', 'Time Management']
        }
    
    # CSS
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
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
            border: 4px solid #00ff9d;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .avatar-text {
            font-size: 60px;
            color: white;
            font-weight: bold;
        }
        
        .info-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            border-left: 5px solid #00ff9d;
            transition: all 0.3s;
        }
        
        .info-item:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.2);
        }
        
        .info-label {
            color: #00ff9d;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .info-value {
            color: white;
            font-size: 18px;
        }
        
        .stat-box {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
        }
        
        .stat-box:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.25);
            border-color: #00ff9d;
        }
        
        .stat-number {
            font-size: 32px;
            font-weight: bold;
            color: #00ff9d;
        }
        
        .stat-label {
            color: white;
            font-size: 14px;
        }
        
        .edit-btn {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 10px 30px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s !important;
        }
        
        .edit-btn:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
        
        .skill-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            padding: 8px 18px;
            margin: 5px;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            font-size: 14px;
            transition: all 0.3s;
        }
        
        .skill-tag:hover {
            background: #00ff9d;
            color: #333;
            transform: scale(1.05);
        }
        
        .badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 50px;
            font-size: 12px;
            font-weight: bold;
            margin: 5px;
        }
        
        .badge-gold {
            background: rgba(255, 215, 0, 0.2);
            color: #ffd700;
            border: 1px solid #ffd700;
        }
        
        .badge-silver {
            background: rgba(192, 192, 192, 0.2);
            color: #c0c0c0;
            border: 1px solid #c0c0c0;
        }
        
        .badge-bronze {
            background: rgba(205, 127, 50, 0.2);
            color: #cd7f32;
            border: 1px solid #cd7f32;
        }
        
        .success-message {
            background: rgba(0, 255, 157, 0.2);
            border: 2px solid #00ff9d;
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            color: #00ff9d;
            margin: 10px 0;
        }
        
        .warning-message {
            background: rgba(255, 187, 51, 0.2);
            border: 2px solid #ffbb33;
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            color: #ffbb33;
            margin: 10px 0;
        }
        
        .stTextInput > div > div > input {
            background: rgba(255, 255, 255, 0.15) !important;
            border: 2px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 15px !important;
            color: white !important;
            padding: 12px !important;
        }
        
        .stTextArea > div > textarea {
            background: rgba(255, 255, 255, 0.15) !important;
            border: 2px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 15px !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>👤 My Profile</h1>", unsafe_allow_html=True)
    
    # Initialize edit mode
    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False
    if 'password_mode' not in st.session_state:
        st.session_state.password_mode = False
    
    # Get user info from session
    user_email = st.session_state.get('user', 'demo@careerpulse.ai')
    user_name = st.session_state.profile_data['name']
    
    # Profile Header
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="profile-card" style="text-align: center;">
        """, unsafe_allow_html=True)
        
        # Avatar with first letter
        first_letter = user_name[0] if user_name else "U"
        st.markdown(f"""
        <div class="avatar">
            <div class="avatar-text">{first_letter}</div>
        </div>
        <h2 style="color: white; margin: 10px 0;">{user_name}</h2>
        <p style="color: rgba(255,255,255,0.7);">{st.session_state.profile_data['email']}</p>
        <p style="color: #00ff9d;">✨ Member since {datetime.now().strftime('%B %Y')}</p>
        """, unsafe_allow_html=True)
        
        # Edit/View toggle buttons
        col_a, col_b, col_c = st.columns(3)
        with col_b:
            if not st.session_state.edit_mode and not st.session_state.password_mode:
                if st.button("✏️ Edit Profile", use_container_width=True):
                    st.session_state.edit_mode = True
                    st.rerun()
            elif st.session_state.edit_mode:
                if st.button("❌ Cancel Edit", use_container_width=True):
                    st.session_state.edit_mode = False
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistics Section
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Your Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Get history data if available
    history_count = len(st.session_state.get('history_data', [])) if 'history_data' in st.session_state else 0
    
    if history_count > 0:
        avg_score = sum(item['probability'] for item in st.session_state.history_data) / history_count
        best_score = max(item['probability'] for item in st.session_state.history_data)
        total_domains = len(set(item['domain'] for item in st.session_state.history_data))
    else:
        avg_score = 0
        best_score = 0
        total_domains = 0
    
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
    
    with col4:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total_domains}</div>
            <div class="stat-label">Domains Explored</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # EDIT MODE - Show editable form
    if st.session_state.edit_mode:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### ✏️ Edit Personal Information")
        
        with st.form("edit_profile_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                new_name = st.text_input("Full Name", value=st.session_state.profile_data['name'])
                new_phone = st.text_input("Phone Number", value=st.session_state.profile_data['phone'])
                new_education = st.text_input("Education", value=st.session_state.profile_data['education'])
                new_location = st.text_input("Location", value=st.session_state.profile_data['location'])
            
            with col2:
                new_email = st.text_input("Email", value=st.session_state.profile_data['email'], disabled=True)
                new_college = st.text_input("College", value=st.session_state.profile_data['college'])
                new_grad_year = st.text_input("Graduation Year", value=st.session_state.profile_data['grad_year'])
                new_bio = st.text_area("Bio", value=st.session_state.profile_data['bio'], height=100)
            
            col_a, col_b, col_c = st.columns(3)
            with col_b:
                save_btn = st.form_submit_button("💾 Save Changes", use_container_width=True)
            
            if save_btn:
                st.session_state.profile_data['name'] = new_name
                st.session_state.profile_data['phone'] = new_phone
                st.session_state.profile_data['education'] = new_education
                st.session_state.profile_data['location'] = new_location
                st.session_state.profile_data['college'] = new_college
                st.session_state.profile_data['grad_year'] = new_grad_year
                st.session_state.profile_data['bio'] = new_bio
                st.session_state.edit_mode = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # PASSWORD CHANGE MODE
    elif st.session_state.password_mode:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Change Password")
        
        with st.form("change_password_form"):
            current_pw = st.text_input("Current Password", type="password")
            new_pw = st.text_input("New Password", type="password")
            confirm_pw = st.text_input("Confirm New Password", type="password")
            
            col_a, col_b, col_c = st.columns(3)
            with col_b:
                change_btn = st.form_submit_button("🔄 Update Password", use_container_width=True)
            with col_a:
                cancel_btn = st.form_submit_button("❌ Cancel", use_container_width=True)
            
            if change_btn:
                if not current_pw or not new_pw or not confirm_pw:
                    st.error("❌ Please fill all fields!")
                elif new_pw != confirm_pw:
                    st.error("❌ New passwords don't match!")
                elif len(new_pw) < 6:
                    st.error("❌ Password must be at least 6 characters!")
                else:
                    st.markdown('<div class="success-message">✅ Password changed successfully!</div>', unsafe_allow_html=True)
                    st.session_state.password_mode = False
                    st.rerun()
            
            if cancel_btn:
                st.session_state.password_mode = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # VIEW MODE - Show normal profile
    else:
        # Personal Information
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Personal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="info-item">
                <div class="info-label">📧 Email Address</div>
                <div class="info-value">{st.session_state.profile_data['email']}</div>
            </div>
            <div class="info-item">
                <div class="info-label">📱 Phone</div>
                <div class="info-value">{st.session_state.profile_data['phone']}</div>
            </div>
            <div class="info-item">
                <div class="info-label">🎓 Education</div>
                <div class="info-value">{st.session_state.profile_data['education']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="info-item">
                <div class="info-label">🏫 College</div>
                <div class="info-value">{st.session_state.profile_data['college']}</div>
            </div>
            <div class="info-item">
                <div class="info-label">📅 Graduation Year</div>
                <div class="info-value">{st.session_state.profile_data['grad_year']}</div>
            </div>
            <div class="info-item">
                <div class="info-label">📍 Location</div>
                <div class="info-value">{st.session_state.profile_data['location']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Bio
        st.markdown(f"""
        <div class="info-item">
            <div class="info-label">📝 Bio</div>
            <div class="info-value">{st.session_state.profile_data['bio']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Skills & Achievements
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 💪 Skills & Achievements")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔧 Technical Skills")
            skills_html = ""
            for skill in st.session_state.profile_data['skills']:
                skills_html += f'<span class="skill-tag">{skill}</span>'
            st.markdown(skills_html, unsafe_allow_html=True)
            
            st.markdown("#### 🗣️ Soft Skills")
            soft_html = ""
            for skill in st.session_state.profile_data['soft_skills']:
                soft_html += f'<span class="skill-tag">{skill}</span>'
            st.markdown(soft_html, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🏆 Achievements")
            st.markdown("""
            <div class="badge badge-gold">🏅 Gold Medalist - Hackathon 2024</div>
            <div class="badge badge-silver">🥈 Runner Up - Coding Competition</div>
            <div class="badge badge-bronze">📜 Certified Python Developer</div>
            <div class="badge badge-gold">⭐ Top 10% - LeetCode</div>
            <div class="badge badge-silver">📊 Data Science Certification</div>
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
            if st.button("📧 Notification Settings", use_container_width=True):
                st.markdown('<div class="warning-message">📧 Notification preferences coming soon!</div>', unsafe_allow_html=True)
        
        with col3:
            if st.button("🗑️ Delete Account", use_container_width=True):
                st.markdown("""
                <div style="background: rgba(255,68,68,0.2); border:2px solid #ff4444; border-radius:15px; padding:20px; text-align:center;">
                    <h3 style="color:#ff4444;">⚠️ Warning!</h3>
                    <p style="color:white;">This action cannot be undone. All your data will be permanently deleted.</p>
                    <p style="color:#ff8888;">Please contact support to delete your account.</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recent Activity
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        st.markdown("### 📋 Recent Activity")
        
        if 'history_data' in st.session_state and len(st.session_state.history_data) > 0:
            recent = st.session_state.history_data[:5]
            for item in recent:
                st.markdown(f"""
                <div class="info-item">
                    <div style="display: flex; justify-content: space-between;">
                        <span style="color: white;">📊 {item['domain']}</span>
                        <span style="color: #00ff9d;">{item['probability']}%</span>
                    </div>
                    <div style="color: rgba(255,255,255,0.5); font-size: 12px;">{item['date']} at {item['time']}</div>
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