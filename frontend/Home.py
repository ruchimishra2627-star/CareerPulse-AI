import streamlit as st

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Home", 
        page_icon="🏠",
        layout="wide"
    )
    
    # ANIMATED GRADIENT BACKGROUND
    st.markdown("""
    <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .stApp {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        /* Welcome Card */
        .welcome-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 40px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
            animation: float 6s infinite;
        }
        
        h1 {
            color: white !important;
            text-align: center;
            font-size: 56px !important;
            margin-bottom: 10px !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .welcome-text {
            text-align: center;
            color: white;
            font-size: 20px;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        
        .user-email {
            text-align: center;
            color: #ffd700;
            font-size: 18px;
            padding: 10px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            display: inline-block;
            margin: 0 auto 30px;
            animation: pulse 3s infinite;
        }
        
        /* Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 40px 0;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.25);
            border-color: #ffd700;
        }
        
        .stat-icon {
            font-size: 40px;
            margin-bottom: 10px;
        }
        
        .stat-number {
            color: white;
            font-size: 32px;
            font-weight: bold;
        }
        
        .stat-label {
            color: rgba(255, 255, 255, 0.8);
            font-size: 14px;
        }
        
        /* Features Grid */
        .section-title {
            color: white;
            font-size: 36px;
            text-align: center;
            margin: 50px 0 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin: 30px 0;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 25px;
            padding: 30px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
            cursor: pointer;
        }
        
        .feature-card:hover {
            transform: translateY(-15px) scale(1.05);
            background: rgba(255, 255, 255, 0.2);
            border-color: #ffd700;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }
        
        .feature-icon {
            font-size: 50px;
            margin-bottom: 20px;
        }
        
        .feature-title {
            color: white;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .feature-desc {
            color: rgba(255, 255, 255, 0.8);
            font-size: 14px;
            line-height: 1.6;
        }
        
        /* Quick Actions */
        .actions-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin: 40px 0;
        }
        
        .action-btn {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50px;
            padding: 15px;
            color: white;
            font-size: 16px;
            font-weight: 600;
            text-align: center;
            transition: all 0.3s;
            cursor: pointer;
        }
        
        .action-btn:hover {
            background: #ffd700;
            color: #333;
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: rgba(255, 255, 255, 0.6);
            margin-top: 60px;
            padding: 20px;
            font-size: 14px;
        }
        
        /* Style for buttons */
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s !important;
            width: 100% !important;
            margin: 5px 0 !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Welcome Section
    user_email = st.session_state.get('user', 'demo@careerpulse.ai')
    
    st.markdown("""
    <div class="welcome-card">
        <h1>🎯 CareerPulse AI</h1>
        <div class="welcome-text">Your AI-Powered Career Assistant</div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div class="user-email">✨ {user_email} ✨</div>', unsafe_allow_html=True)
    
    # Stats Grid
    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-icon">📊</div>
            <div class="stat-number">85%</div>
            <div class="stat-label">Placement Rate</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🎯</div>
            <div class="stat-number">92%</div>
            <div class="stat-label">Skill Score</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">📈</div>
            <div class="stat-number">78%</div>
            <div class="stat-label">Growth</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <div class="stat-number">500+</div>
            <div class="stat-label">Students</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close welcome-card
    
    # Features Section
    st.markdown('<div class="section-title">🚀 Explore Features</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Placement Prediction</div>
            <div class="feature-desc">AI-powered analysis of your placement chances with 85% accuracy</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Analyze Now", key="pred", use_container_width=True):
            st.session_state.page = "Dashboard"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Skill Gap Analysis</div>
            <div class="feature-desc">Identify areas for improvement with detailed skill comparison</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📈 Check Skills", key="skill", use_container_width=True):
            st.session_state.page = "SkillGap"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Career Paths</div>
            <div class="feature-desc">Discover the best career options tailored to your strengths</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎯 Explore Paths", key="career", use_container_width=True):
            st.session_state.page = "CareerPath"
            st.rerun()
    
    # Quick Actions
    st.markdown('<div class="section-title">⚡ Quick Actions</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📊 Dashboard", use_container_width=True):
            st.session_state.page = "Dashboard"
            st.rerun()
    
    with col2:
        if st.button("📄 Resume Scanner", use_container_width=True):
            st.session_state.page = "Resume"
            st.rerun()
    
    with col3:
        if st.button("📋 History", use_container_width=True):
            st.session_state.page = "History"
            st.rerun()
    
    with col4:
        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = "Profile"
            st.rerun()
    
    # Second row of Quick Actions
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📈 Skill Gap", use_container_width=True):
            st.session_state.page = "SkillGap"
            st.rerun()
    
    with col2:
        if st.button("🎯 Career Path", use_container_width=True):
            st.session_state.page = "CareerPath"
            st.rerun()
    
    with col3:
        if st.button("📊 Analytics", use_container_width=True):
            st.session_state.page = "Analytics"  # 👈 YEH CHANGE KIYA - Coming Soon HATAYA
            st.rerun()
    
    with col4:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.page = "Login"
            st.rerun()
    
    # Third row of Quick Actions - About button
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        if st.button("ℹ️ About Project", use_container_width=True):
            st.session_state.page = "About"
            st.rerun()
    
    # Footer
    st.markdown("""
    <div class="footer">
        Made with ❤️ for your career journey<br>
        © 2026 CareerPulse AI. All rights reserved.
    </div>
    """, unsafe_allow_html=True)