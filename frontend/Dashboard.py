import streamlit as st

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Dashboard", 
        page_icon="📊",
        layout="wide"
    )
    
    # Check authentication
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.warning("⚠️ Please login first!")
        st.session_state.page = "Login"
        st.rerun()
    
    # Simple attractive CSS
    st.markdown("""
    <style>
        /* Gradient Background */
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Title */
        h1 {
            color: white !important;
            text-align: center;
            font-size: 48px !important;
            margin-bottom: 30px !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Card Style */
        .dashboard-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Labels */
        .stMarkdown h3 {
            color: white !important;
        }
        
        /* Input Fields */
        .stNumberInput > div > div > input {
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            color: white;
        }
        
        .stSlider > div > div > div > input {
            color: #00ff9d;
        }
        
        .stSelectbox > div > div > select {
            background: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            color: white;
        }
        
        /* Button */
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 50px;
            padding: 12px 30px;
            font-weight: 600;
            border: none;
            width: 100%;
            transition: all 0.3s;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }
        
        /* Success Box */
        .success-box {
            background: rgba(0, 255, 157, 0.2);
            border: 2px solid #00ff9d;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin: 20px 0;
        }
        
        .success-box h2 {
            color: #00ff9d !important;
            font-size: 36px !important;
            margin: 0 !important;
        }
        
        .success-box p {
            color: white;
            font-size: 18px;
        }
        
        /* Medium Score Box */
        .medium-box {
            background: rgba(255, 187, 51, 0.2);
            border: 2px solid #ffbb33;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin: 20px 0;
        }
        
        .medium-box h2 {
            color: #ffbb33 !important;
            font-size: 36px !important;
            margin: 0 !important;
        }
        
        .medium-box p {
            color: white;
            font-size: 18px;
        }
        
        /* Low Score Box */
        .low-box {
            background: rgba(255, 68, 68, 0.2);
            border: 2px solid #ff4444;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            margin: 20px 0;
        }
        
        .low-box h2 {
            color: #ff4444 !important;
            font-size: 36px !important;
            margin: 0 !important;
        }
        
        .low-box p {
            color: white;
            font-size: 18px;
        }
        
        /* Back Button */
        .back-btn {
            text-align: center;
            margin-top: 30px;
        }
        
        .back-btn > button {
            background: transparent;
            color: white;
            border: 2px solid white;
            width: auto;
            padding: 10px 40px;
        }
        
        .back-btn > button:hover {
            background: white;
            color: #333;
        }
        
        /* Suggestion Item */
        .suggestion-item {
            background: rgba(255, 255, 255, 0.1);
            border-left: 5px solid #00ff9d;
            border-radius: 10px;
            padding: 12px;
            margin: 8px 0;
            color: white;
            transition: all 0.3s;
        }
        
        .suggestion-item:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1>📊 Career Dashboard</h1>", unsafe_allow_html=True)
    
    # Main Card
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("<h3>📝 Enter Your Details</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        cgpa = st.number_input("CGPA", 4.0, 10.0, 7.5, step=0.1)
        python = st.slider("Python Skills", 1, 10, 7)
        dsa = st.slider("DSA Skills", 1, 10, 6)
    
    with col2:
        communication = st.slider("Communication", 1, 10, 7)
        projects = st.number_input("Projects", 0, 10, 2)
        internship = st.selectbox("Internship", ["No", "Yes"])
        certifications = st.number_input("Certifications", 0, 10, 1)
    
    analyze = st.button("🔮 Analyze My Profile", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if analyze:
        # Calculate score
        intern_val = 1 if internship == "Yes" else 0
        score = (cgpa/10 * 30) + (python * 5) + (dsa * 4) + (communication * 3) + (intern_val * 10) + (projects * 3) + (certifications * 2)
        prob = min(100, score)
        
        # Show result
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h3>🎯 Your Results</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Placement Probability", f"{prob:.1f}%")
        
        with col2:
            if prob >= 70:
                st.metric("Status", "✅ HIGH")
            elif prob >= 40:
                st.metric("Status", "⚠️ MEDIUM")
            else:
                st.metric("Status", "❌ LOW")
        
        with col3:
            skill_avg = (python + dsa + communication) / 3 * 10
            st.metric("Skill Score", f"{skill_avg:.1f}%")
        
        # Success message - WITHOUT BALLOONS
        if prob >= 70:
            st.markdown("""
            <div class="success-box">
                <h2>🎉 Excellent!</h2>
                <p>Your profile looks great! Keep up the good work.</p>
            </div>
            """, unsafe_allow_html=True)
            # ❌ st.balloons() - REMOVED
        elif prob >= 40:
            st.markdown("""
            <div class="medium-box">
                <h2>📈 Good Progress!</h2>
                <p>You're on the right track. Focus on improving your skills.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="low-box">
                <h2>💪 Keep Working!</h2>
                <p>Don't worry! Focus on the suggestions below.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Suggestions
        st.markdown("<h3>💡 Suggestions</h3>", unsafe_allow_html=True)
        
        suggestions = []
        if python < 7:
            suggestions.append("📘 Improve Python skills - Practice daily, build projects")
        if dsa < 6:
            suggestions.append("📊 Practice DSA regularly on LeetCode")
        if communication < 7:
            suggestions.append("🗣️ Work on communication - Join group discussions")
        if intern_val == 0:
            suggestions.append("💼 Get an internship for practical experience")
        if projects < 2:
            suggestions.append("🛠️ Build more projects - Aim for 3-4 projects")
        if certifications < 2:
            suggestions.append("📜 Add certifications to boost your profile")
        
        for suggestion in suggestions:
            st.markdown(f'<div class="suggestion-item">{suggestion}</div>', unsafe_allow_html=True)
        
        if not suggestions:
            st.markdown("""
            <div class="suggestion-item" style="border-left-color: #00ff9d;">
                ✨ Your profile looks great! Keep up the good work!
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back button
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)