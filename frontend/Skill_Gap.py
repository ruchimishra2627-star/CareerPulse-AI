import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Skill Gap", 
        page_icon="📈",
        layout="wide"
    )
    
    # Check authentication
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.warning("⚠️ Please login first!")
        st.session_state.page = "Login"
        st.rerun()
    
    # CSS
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        h1, h2, h3 {
            color: white !important;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>📈 Skill Gap Analysis</h1>", unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📝 Enter Your Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        python = st.slider("Python", 1, 10, 7)
        dsa = st.slider("DSA", 1, 10, 6)
        sql = st.slider("SQL", 1, 10, 5)
        ml = st.slider("Machine Learning", 1, 10, 4)
    
    with col2:
        communication = st.slider("Communication", 1, 10, 7)
        teamwork = st.slider("Teamwork", 1, 10, 8)
        leadership = st.slider("Leadership", 1, 10, 5)
        problem_solving = st.slider("Problem Solving", 1, 10, 6)
    
    analyze = st.button("📊 Analyze Skill Gap", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if analyze:
        # Ideal skills for different roles
        ideal_skills = {
            "Software Developer": {"Python": 8, "DSA": 9, "SQL": 7, "ML": 5, "Communication": 7, "Teamwork": 8, "Leadership": 6, "Problem Solving": 9},
            "Data Scientist": {"Python": 9, "DSA": 7, "SQL": 8, "ML": 9, "Communication": 8, "Teamwork": 7, "Leadership": 6, "Problem Solving": 8},
            "Web Developer": {"Python": 7, "DSA": 6, "SQL": 7, "ML": 4, "Communication": 7, "Teamwork": 8, "Leadership": 6, "Problem Solving": 7},
            "Business Analyst": {"Python": 6, "DSA": 5, "SQL": 8, "ML": 5, "Communication": 9, "Teamwork": 8, "Leadership": 7, "Problem Solving": 8},
        }
        
        your_skills = {
            "Python": python, "DSA": dsa, "SQL": sql, "ML": ml,
            "Communication": communication, "Teamwork": teamwork, 
            "Leadership": leadership, "Problem Solving": problem_solving
        }
        
        # Calculate gaps for each role
        results = []
        for role, ideals in ideal_skills.items():
            total_gap = 0
            skill_gaps = []
            for skill, ideal in ideals.items():
                your = your_skills[skill]
                gap = ideal - your
                if gap > 0:
                    total_gap += gap
                    skill_gaps.append((skill, your, ideal, gap))
            
            match_percentage = max(0, 100 - (total_gap / sum(ideals.values()) * 100))
            results.append((role, match_percentage, skill_gaps))
        
        # Sort by match percentage
        results.sort(key=lambda x: x[1], reverse=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Your Best Matches")
        
        for role, match, gaps in results[:3]:
            st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 20px;
                margin: 15px 0;
                border-left: 5px solid #00ff9d;
            ">
                <h3 style="color: #00ff9d; margin: 0;">{role}</h3>
                <h2 style="color: white; margin: 10px 0;">Match: {match:.1f}%</h2>
            </div>
            """, unsafe_allow_html=True)
            
            if gaps:
                st.markdown("**Skills to improve:**")
                for skill, your, ideal, gap in gaps[:5]:
                    st.markdown(f"- {skill}: {your}/10 → Need {ideal}/10 (Gap: {gap})")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()