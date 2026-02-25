import streamlit as st
from datetime import datetime

def show():
    st.set_page_config(
        page_title="CareerPulse AI - About", 
        page_icon="ℹ️",
        layout="wide"
    )
    
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
        
        .about-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 40px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .team-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
        }
        
        .team-card:hover {
            transform: translateY(-10px);
            border-color: #00ff9d;
        }
        
        .feature-list {
            list-style: none;
            padding: 0;
        }
        
        .feature-list li {
            padding: 10px 0;
            color: white;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .feature-list li:before {
            content: "✅ ";
            color: #00ff9d;
        }
        
        .tech-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            padding: 8px 20px;
            margin: 5px;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            font-size: 14px;
            transition: all 0.3s;
        }
        
        .tech-tag:hover {
            background: #00ff9d;
            color: #333;
            transform: scale(1.05);
        }
        
        .version-badge {
            display: inline-block;
            background: #00ff9d;
            color: #333;
            padding: 5px 15px;
            border-radius: 50px;
            font-weight: bold;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 10px 30px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>ℹ️ About CareerPulse AI</h1>", unsafe_allow_html=True)
    
    # Main About Section
    st.markdown('<div class="about-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <h2 style="color: #00ff9d;">🎯 Our Mission</h2>
        <p style="color: white; font-size: 18px; line-height: 1.8;">
            CareerPulse AI is designed to help students and professionals make data-driven career decisions. 
            Using advanced machine learning algorithms, we analyze your academic profile, skills, and experience 
            to provide personalized career recommendations and placement predictions.
        </p>
        <h2 style="color: #00ff9d; margin-top: 30px;">✨ Key Features</h2>
        <ul class="feature-list">
            <li>AI-powered placement prediction with 85% accuracy</li>
            <li>Comprehensive skill gap analysis</li>
            <li>Personalized career path recommendations</li>
            <li>Intelligent resume scanning</li>
            <li>Progress tracking and history</li>
            <li>User profile management</li>
        </ul>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h2 style="color: #00ff9d;">🛠️ Technology Stack</h2>
        <div style="margin: 20px 0;">
            <span class="tech-tag">Python</span>
            <span class="tech-tag">Streamlit</span>
            <span class="tech-tag">Pandas</span>
            <span class="tech-tag">Scikit-learn</span>
            <span class="tech-tag">Plotly</span>
            <span class="tech-tag">MySQL</span>
            <span class="tech-tag">Random Forest</span>
            <span class="tech-tag">Machine Learning</span>
            <span class="tech-tag">HTML/CSS</span>
            <span class="tech-tag">Data Analytics</span>
        </div>
        
        <h2 style="color: #00ff9d; margin-top: 30px;">📊 Project Statistics</h2>
        <div style="background: rgba(255,255,255,0.1); border-radius: 20px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: white;">Pages Created</span>
                <span style="color: #00ff9d; font-weight: bold;">10+</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: white;">ML Models</span>
                <span style="color: #00ff9d; font-weight: bold;">3</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: white;">Lines of Code</span>
                <span style="color: #00ff9d; font-weight: bold;">5000+</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: white;">Development Time</span>
                <span style="color: #00ff9d; font-weight: bold;">10 Days</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Version Info
    st.markdown('<div class="about-card">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <h2 style="color: #00ff9d;">📌 Version</h2>
            <div class="version-badge">v1.0.0</div>
            <p style="color: white; margin-top: 10px;">Release Date: March 2026</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <h2 style="color: #00ff9d;">👨‍💻 Developer</h2>
            <p style="color: white; font-size: 18px;">BSc Computer Science</p>
            <p style="color: #00ff9d;">Final Year Project</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <h2 style="color: #00ff9d;">📞 Contact</h2>
            <p style="color: white;">Email: support@careerpulse.ai</p>
            <p style="color: white;">GitHub: /careerpulse-ai</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Future Scope
    st.markdown('<div class="about-card">', unsafe_allow_html=True)
    st.markdown("""
    <h2 style="color: #00ff9d; text-align: center;">🚀 Future Scope</h2>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px;">
        <div style="background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px;">
            <h3 style="color: white;">🤖 Advanced AI</h3>
            <p style="color: rgba(255,255,255,0.7);">Deep learning models for more accurate predictions</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px;">
            <h3 style="color: white;">📱 Mobile App</h3>
            <p style="color: rgba(255,255,255,0.7);">iOS and Android apps for on-the-go access</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px;">
            <h3 style="color: white;">🌐 Job Integration</h3>
            <p style="color: rgba(255,255,255,0.7);">Real-time job posting integration</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px;">
            <h3 style="color: white;">📊 Company Analytics</h3>
            <p style="color: rgba(255,255,255,0.7);">Hiring trends and company insights</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Thank You Note
    st.markdown("""
    <div style="text-align: center; padding: 40px; background: rgba(255,255,255,0.05); border-radius: 50px; margin: 30px 0;">
        <h1 style="color: white; font-size: 48px;">🙏 Thank You</h1>
        <p style="color: #00ff9d; font-size: 20px;">for exploring CareerPulse AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Back to Home
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()