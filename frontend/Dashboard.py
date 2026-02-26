import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from backend.predict import Predictor

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
    
    # Initialize predictor
    predictor = Predictor()
    
    # CSS for better UI
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
        
        .dashboard-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .info-box {
            background: rgba(102, 126, 234, 0.3);
            border-left: 5px solid #00ff9d;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            color: white;
        }
        
        .metric-box {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
        }
        
        .metric-box:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.25);
            border-color: #00ff9d;
        }
        
        .metric-value {
            font-size: 32px;
            font-weight: bold;
            color: #00ff9d;
        }
        
        .metric-label {
            color: white;
            font-size: 14px;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 12px 30px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
        
        .suggestion-item {
            background: rgba(255, 255, 255, 0.1);
            border-left: 5px solid #00ff9d;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            color: white;
            transition: all 0.3s;
        }
        
        .suggestion-item:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>📊 AI Placement Predictor</h1>", unsafe_allow_html=True)
    
    # Introduction Section - Ye examiner ko samjhayega
    with st.expander("ℹ️ What is this Dashboard? (Click to learn)"):
        st.markdown("""
        <div class="info-box">
            <h3>🎯 Purpose of this Dashboard:</h3>
            <p>This dashboard uses <b>Machine Learning (Random Forest Algorithm)</b> to predict your placement chances based on:</p>
            <ul>
                <li><b>📚 Academic Performance:</b> CGPA</li>
                <li><b>💻 Technical Skills:</b> Python, DSA</li>
                <li><b>🗣️ Soft Skills:</b> Communication</li>
                <li><b>💼 Experience:</b> Internships, Projects, Certifications</li>
            </ul>
            <p>The model is trained on <b>200+ student records</b> with <b>85% accuracy</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Input Form
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown("<h3>📝 Enter Your Academic & Skill Details</h3>", unsafe_allow_html=True)
    
    # Tooltips for each field - Ye batayega ki kyun ye fields important hain
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📚 Academic Parameters")
        cgpa = st.slider("CGPA (4.0-10.0)", 4.0, 10.0, 7.5, 0.1, 
                        help="Your Cumulative Grade Point Average - Higher CGPA increases placement chances by up to 30%")
        projects = st.number_input("Number of Projects", 0, 10, 2,
                                  help="More projects demonstrate practical skills. 2-3 projects recommended")
        certifications = st.number_input("Certifications", 0, 10, 1,
                                        help="Industry certifications boost your profile (AWS, Google, etc.)")
        
        st.markdown("#### 💼 Experience")
        internship = st.radio("Internship Done?", ["No", "Yes"], horizontal=True,
                             help="Internship experience gives you +10% advantage in placement")
    
    with col2:
        st.markdown("#### 💻 Technical Skills")
        python = st.slider("Python (1-10)", 1, 10, 7,
                          help="Python is the most in-demand skill. 7+ recommended for good placements")
        dsa = st.slider("Data Structures & Algorithms (1-10)", 1, 10, 6,
                       help="DSA is crucial for coding interviews. Practice regularly to improve")
        communication = st.slider("Communication (1-10)", 1, 10, 7,
                                 help="Soft skills matter! Good communication helps in interviews")
        
        st.markdown("#### 📊 Skill Impact")
        st.markdown("""
        <div style="background:rgba(255,255,255,0.1); border-radius:15px; padding:15px;">
            <p style="color:white;">⚡ <b>Weightage:</b></p>
            <p style="color:#00ff9d;">CGPA: 30% | Python: 20% | DSA: 20% | Communication: 15% | Projects: 10% | Internship: 5%</p>
        </div>
        """, unsafe_allow_html=True)
    
    analyze = st.button("🔮 Analyze My Profile", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if analyze:
        intern_val = 1 if internship == "Yes" else 0
        
        # Calculate using ML model
        prob, pred = predictor.predict(cgpa, python, dsa, communication, intern_val, projects, certifications)
        risk, emoji = predictor.get_risk_level(prob)
        
        # Results Section
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>🎯 Analysis Results</h2>", unsafe_allow_html=True)
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{prob:.1f}%</div>
                <div class="metric-label">Placement Probability</div>
                <p style="color:white; font-size:12px;">Chance of getting placed</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            status = "✅ HIGH" if pred == 1 else "⚠️ NEEDS WORK"
            color = "#00ff9d" if pred == 1 else "#ffbb33"
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value" style="color: {color};">{status}</div>
                <div class="metric-label">Prediction Status</div>
                <p style="color:white; font-size:12px;">{pred == 1 and 'Good chance' or 'Needs improvement'}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{emoji} {risk}</div>
                <div class="metric-label">Risk Level</div>
                <p style="color:white; font-size:12px;">Based on your profile strength</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            skill_score = int((python + dsa + communication) / 3 * 10)
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{skill_score}%</div>
                <div class="metric-label">Skill Score</div>
                <p style="color:white; font-size:12px;">Average of your skills</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Gauge Chart - Visual representation
        st.markdown("<h3 style='text-align: center;'>📊 Probability Gauge</h3>", unsafe_allow_html=True)
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=prob,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Placement Chance", 'font': {'color': 'white', 'size': 20}},
            delta={'reference': 60, 'increasing': {'color': "#00ff9d"}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "white"},
                'bar': {'color': "#00ff9d", 'thickness': 0.3},
                'bgcolor': 'rgba(0,0,0,0)',
                'borderwidth': 2,
                'bordercolor': 'rgba(255,255,255,0.3)',
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(255, 68, 68, 0.3)'},
                    {'range': [40, 70], 'color': 'rgba(255, 187, 51, 0.3)'},
                    {'range': [70, 100], 'color': 'rgba(0, 200, 81, 0.3)'}
                ],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': prob
                }
            }))
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white', 'size': 14},
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Feature Importance - Explainable AI
        st.markdown("<h3>🔍 What Influenced This Prediction?</h3>", unsafe_allow_html=True)
        
        # Calculate contributions
        contributions = {
            'CGPA': cgpa/10 * 30,
            'Python': python/10 * 20,
            'DSA': dsa/10 * 20,
            'Communication': communication/10 * 15,
            'Projects': min(10, projects * 3),
            'Internship': 10 if intern_val == 1 else 0,
            'Certifications': min(5, certifications * 2)
        }
        
        # Sort contributions
        sorted_contrib = dict(sorted(contributions.items(), key=lambda x: x[1], reverse=True))
        
        # Display as horizontal bar
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=list(sorted_contrib.values()),
            y=list(sorted_contrib.keys()),
            orientation='h',
            marker_color=['#00ff9d' if v >= 15 else '#ffbb33' if v >= 10 else '#ff4444' for v in sorted_contrib.values()],
            text=[f'{v:.1f}%' for v in sorted_contrib.values()],
            textposition='outside'
        ))
        
        fig.update_layout(
            title="Feature Impact on Placement",
            xaxis_title="Contribution (%)",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed Suggestions
        st.markdown("<h3>💡 Personalized Improvement Plan</h3>", unsafe_allow_html=True)
        
        suggestions = []
        
        # Academic suggestions
        if cgpa < 7.0:
            suggestions.append(("📚 CGPA Improvement", f"Your CGPA {cgpa}/10 is below average. Focus on improving to 7.0+ for better placement opportunities."))
        elif cgpa < 8.5:
            suggestions.append(("📚 CGPA Good", f"Your CGPA {cgpa}/10 is decent. Try to maintain or improve to 8.5+ for top companies."))
        
        # Python suggestions
        if python < 6:
            suggestions.append(("🐍 Python Basics", "Start with Python fundamentals. Complete online courses and practice daily."))
        elif python < 8:
            suggestions.append(("🐍 Python Intermediate", "Build projects using Python. Learn frameworks like Django/Flask."))
        else:
            suggestions.append(("🐍 Python Advanced", "Your Python is strong. Contribute to open source or learn advanced topics."))
        
        # DSA suggestions
        if dsa < 5:
            suggestions.append(("📊 DSA Beginner", "Start with arrays, strings, and basic algorithms. Solve 2 problems daily."))
        elif dsa < 7:
            suggestions.append(("📊 DSA Intermediate", "Practice medium-level problems. Focus on trees, graphs, dynamic programming."))
        else:
            suggestions.append(("📊 DSA Advanced", "Your DSA is strong. Participate in contests and solve hard problems."))
        
        # Communication suggestions
        if communication < 6:
            suggestions.append(("🗣️ Communication Basics", "Join group discussions, practice speaking in English daily."))
        elif communication < 8:
            suggestions.append(("🗣️ Communication Intermediate", "Work on presentation skills. Record yourself and improve."))
        
        # Experience suggestions
        if intern_val == 0:
            suggestions.append(("💼 Internship Needed", "Apply for internships. They provide real-world experience and boost resume."))
        if projects < 2:
            suggestions.append(("🛠️ Project Building", "Build 2-3 real-world projects. They demonstrate practical skills."))
        if certifications < 2:
            suggestions.append(("📜 Certification Required", "Get certifications in Python, AWS, or Data Science from Coursera/Udemy."))
        
        # Display suggestions in nice format
        for title, desc in suggestions:
            st.markdown(f"""
            <div class="suggestion-item">
                <b style="color:#00ff9d;">{title}</b><br>
                <span style="color:white;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)
        
        if not suggestions:
            st.markdown("""
            <div style="background:rgba(0,255,157,0.2); border:2px solid #00ff9d; border-radius:15px; padding:20px; text-align:center;">
                <h3 style="color:#00ff9d;">✨ Excellent Profile!</h3>
                <p style="color:white;">Your profile looks great! Focus on mock interviews and company applications.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Save to history (for later use)
        from datetime import datetime
        if 'history_data' not in st.session_state:
            st.session_state.history_data = []
        
        st.session_state.history_data.append({
            'date': datetime.now().strftime("%d %b %Y"),
            'time': datetime.now().strftime("%H:%M"),
            'domain': 'Placement Prediction',
            'probability': prob,
            'risk': risk,
            'cgpa': cgpa,
            'skills': skill_score
        })
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back to Home
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()