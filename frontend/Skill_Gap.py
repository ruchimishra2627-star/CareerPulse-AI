import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

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
    
    # CSS for professional UI
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
        
        .skill-card {
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
        
        .gap-high {
            color: #ff4444;
            font-weight: bold;
        }
        
        .gap-medium {
            color: #ffbb33;
            font-weight: bold;
        }
        
        .gap-low {
            color: #00ff9d;
            font-weight: bold;
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
        
        .career-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 20px;
            margin: 15px 0;
            border-left: 5px solid #00ff9d;
        }
        
        .industry-badge {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 20px;
            padding: 10px 20px;
            display: inline-block;
            color: white;
            font-weight: 600;
            margin: 5px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>📈 Advanced Skill Gap Analysis</h1>", unsafe_allow_html=True)
    
    # Introduction Section - Industry trends ke saath
    with st.expander("ℹ️ What is Skill Gap Analysis? (Click to learn about 2026 trends)"):
        st.markdown("""
        <div class="info-box">
            <h3>🎯 Why Skill Gap Analysis Matters in 2026:</h3>
            <p>According to <b>WorldatWork 2026 report</b> and <b>LinkedIn's most in-demand skills</b>, employers are looking for a blend of technical and human skills [citation:5][citation:7].</p>
            <ul>
                <li><b>🔍 Hard Skills:</b> Technical, measurable abilities (AI, Cloud, Data Analysis, etc.)</li>
                <li><b>🗣️ Soft Skills:</b> Interpersonal strengths that AI cannot replace (Communication, Adaptability, etc.)</li>
                <li><b>📊 85% of job success</b> comes from soft skills, only 15% from technical expertise [citation:9]</li>
                <li><b>⚡ 93% of employers</b> see soft skills as critical for hiring [citation:3]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # ===== INDUSTRY STANDARDS 2026 =====
    # Based on WorldatWork 2026 report and industry research [citation:5][citation:1]
    IDEAL_SKILLS = {
        # Technical Skills (Top Hard Skills 2026) [citation:5]
        'Python': 8,
        'Data Analysis': 8,
        'SQL': 7,
        'Machine Learning': 7,
        'Cloud Computing': 7,
        'Cybersecurity Awareness': 7,
        'AI Tools': 7,
        'Project Management': 7,
        'Software Tools': 8,
        'Data Visualization': 7,
        
        # Soft Skills (Top Soft Skills 2026) [citation:3][citation:5][citation:7]
        'Communication': 9,
        'Problem Solving': 9,
        'Critical Thinking': 8,
        'Adaptability': 8,
        'Teamwork': 8,
        'Time Management': 8,
        'Leadership': 7,
        'Emotional Intelligence': 8,
        'Creativity': 7,
        'Resilience': 7
    }
    
    # Skill categories for organization
    tech_skills = ['Python', 'Data Analysis', 'SQL', 'Machine Learning', 'Cloud Computing', 
                   'Cybersecurity Awareness', 'AI Tools', 'Project Management', 'Software Tools', 'Data Visualization']
    soft_skills = ['Communication', 'Problem Solving', 'Critical Thinking', 'Adaptability', 
                   'Teamwork', 'Time Management', 'Leadership', 'Emotional Intelligence', 'Creativity', 'Resilience']
    
    # Industry-wise importance (for recommendations) [citation:1]
    industry_skills = {
        'Technology & IT': ['Python', 'Machine Learning', 'Cloud Computing', 'Cybersecurity Awareness', 'AI Tools', 'Problem Solving'],
        'Data Science': ['Python', 'Data Analysis', 'SQL', 'Machine Learning', 'Data Visualization', 'Critical Thinking'],
        'Business & Finance': ['Data Analysis', 'Project Management', 'Communication', 'Leadership', 'Time Management'],
        'Engineering': ['Python', 'Project Management', 'Problem Solving', 'Teamwork', 'Adaptability'],
        'Healthcare': ['Communication', 'Emotional Intelligence', 'Resilience', 'Teamwork', 'Problem Solving'],
        'Creative Industries': ['Creativity', 'Software Tools', 'Communication', 'Adaptability', 'Time Management']
    }
    
    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["📝 Enter Skills", "📊 Industry Trends", "🎯 Career Matching"])
    
    with tab1:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown("### 💻 Technical Skills (Rate 1-10)")
        
        # Technical skills in 2 columns
        col1, col2 = st.columns(2)
        
        tech_values = {}
        with col1:
            for skill in tech_skills[:5]:  # First 5 tech skills
                tech_values[skill] = st.slider(skill, 1, 10, 7, key=f"tech_{skill}", 
                                              help=f"Industry standard: {IDEAL_SKILLS[skill]}/10")
        
        with col2:
            for skill in tech_skills[5:]:  # Next 5 tech skills
                tech_values[skill] = st.slider(skill, 1, 10, 6, key=f"tech_{skill}", 
                                              help=f"Industry standard: {IDEAL_SKILLS[skill]}/10")
        
        st.markdown("### 🗣️ Soft Skills (Rate 1-10)")
        st.markdown("_Soft skills are 85% of job success_ [citation:9]")
        
        # Soft skills in 2 columns
        col3, col4 = st.columns(2)
        
        soft_values = {}
        with col3:
            for skill in soft_skills[:5]:  # First 5 soft skills
                soft_values[skill] = st.slider(skill, 1, 10, 7, key=f"soft_{skill}", 
                                              help=f"Industry standard: {IDEAL_SKILLS[skill]}/10")
        
        with col4:
            for skill in soft_skills[5:]:  # Next 5 soft skills
                soft_values[skill] = st.slider(skill, 1, 10, 7, key=f"soft_{skill}", 
                                              help=f"Industry standard: {IDEAL_SKILLS[skill]}/10")
        
        # Combine all skills
        your_skills = {**tech_values, **soft_values}
        
        analyze = st.button("📊 Analyze Complete Skill Gap", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown("### 📈 2026 Industry Skill Trends")
        st.markdown("""
        <p style="color:white;">According to <b>WorldatWork 2026</b> and <b>LinkedIn</b>, these are the most in-demand skills [citation:5]:</p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔧 Top Hard Skills 2026")
            hard_trends = {
                'Software Tools': '85%',
                'Data Analysis': '82%', 
                'Cybersecurity Awareness': '79%',
                'Project Management': '76%',
                'AI Tools': '74%'
            }
            for skill, demand in hard_trends.items():
                st.markdown(f"<div style='background:rgba(255,255,255,0.1); padding:10px; margin:5px; border-radius:10px;'>📊 <b>{skill}</b> - {demand} jobs require this</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 🌟 Top Soft Skills 2026")
            soft_trends = {
                'Communication': '93%',
                'Adaptability': '89%',
                'Problem Solving': '87%',
                'Emotional Intelligence': '85%',
                'Collaboration': '83%'
            }
            for skill, demand in soft_trends.items():
                st.markdown(f"<div style='background:rgba(255,255,255,0.1); padding:10px; margin:5px; border-radius:10px;'>💫 <b>{skill}</b> - {demand} employers value this</div>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Career Paths by Industry")
        st.markdown("""
        <p style="color:white;">Different industries prioritize different skills [citation:1]. Select your target industry to see what matters most:</p>
        """, unsafe_allow_html=True)
        
        selected_industry = st.selectbox("Select Industry", list(industry_skills.keys()))
        
        st.markdown(f"#### Key skills for {selected_industry}:")
        for skill in industry_skills[selected_industry]:
            st.markdown(f"<span class='industry-badge'>{skill}</span>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    if analyze:
        # Calculate gaps
        gaps = {}
        total_gap = 0
        max_possible_gap = sum(IDEAL_SKILLS.values())
        
        for skill, ideal in IDEAL_SKILLS.items():
            your = your_skills.get(skill, 5)  # Default 5 if missing
            gap = max(0, ideal - your)
            gaps[skill] = {
                'your': your,
                'ideal': ideal,
                'gap': gap,
                'status': 'Good' if gap == 0 else 'Needs Improvement',
                'gap_percent': (gap / ideal) * 100 if ideal > 0 else 0
            }
            total_gap += gap
        
        # Overall skill score
        skill_score = 100 - (total_gap / max_possible_gap * 100)
        
        # Results Section
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>🎯 Complete Skill Gap Analysis</h2>", unsafe_allow_html=True)
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{skill_score:.1f}%</div>
                <div class="metric-label">Overall Skill Score</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            strong_skills = sum(1 for s in gaps.values() if s['gap'] == 0)
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{strong_skills}</div>
                <div class="metric-label">Strong Skills</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            weak_skills = sum(1 for s in gaps.values() if s['gap'] > 0)
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{weak_skills}</div>
                <div class="metric-label">Skills to Improve</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            avg_gap = total_gap / len(gaps)
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-value">{avg_gap:.1f}</div>
                <div class="metric-label">Average Gap</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Radar Chart (showing all skills)
        st.markdown("<h3 style='text-align: center;'>📊 Complete Skills Comparison</h3>", unsafe_allow_html=True)
        
        categories = list(IDEAL_SKILLS.keys())
        your_values = [your_skills.get(s, 5) for s in categories]
        ideal_values = [IDEAL_SKILLS[s] for s in categories]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=your_values,
            theta=categories,
            fill='toself',
            name='Your Skills',
            line_color='#00ff9d'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=ideal_values,
            theta=categories,
            fill='toself',
            name='Industry Standard 2026',
            line_color='#ff4444',
            opacity=0.3
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Top 10 Priority Skills to Improve
        st.markdown("<h3 style='text-align: center;'>📋 Your Top 10 Priority Skills</h3>", unsafe_allow_html=True)
        
        # Sort by gap (highest first)
        sorted_gaps = sorted(gaps.items(), key=lambda x: x[1]['gap'], reverse=True)
        priority_skills = sorted_gaps[:10]
        
        # Create bar chart
        priority_df = pd.DataFrame({
            'Skill': [s[0] for s in priority_skills],
            'Gap': [s[1]['gap'] for s in priority_skills],
            'Your Level': [s[1]['your'] for s in priority_skills],
            'Ideal Level': [s[1]['ideal'] for s in priority_skills]
        })
        
        fig = px.bar(priority_df, x='Gap', y='Skill', orientation='h',
                    title='Priority Skills to Improve (Biggest Gaps First)',
                    color='Gap', color_continuous_scale=['#00ff9d', '#ffbb33', '#ff4444'])
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed Table
        st.markdown("<h3 style='text-align: center;'>📊 Detailed Skill Analysis</h3>", unsafe_allow_html=True)
        
        gap_data = []
        for skill, data in gaps.items():
            gap_data.append({
                'Skill': skill,
                'Your Level': data['your'],
                'Ideal Level': data['ideal'],
                'Gap': data['gap'],
                'Status': data['status'],
                'Priority': 'High' if data['gap'] >= 3 else 'Medium' if data['gap'] >= 1 else 'Low'
            })
        
        gap_df = pd.DataFrame(gap_data)
        st.dataframe(gap_df, use_container_width=True)
        
        # Personalized Improvement Plan
        st.markdown("<h3 style='text-align: center;'>💡 Your Personalized Skill Improvement Plan</h3>", unsafe_allow_html=True)
        
        suggestions = []
        
        # Technical skills suggestions
        for skill in tech_skills:
            if your_skills.get(skill, 5) < IDEAL_SKILLS[skill]:
                gap = IDEAL_SKILLS[skill] - your_skills.get(skill, 5)
                if gap >= 3:
                    suggestions.append(f"🔴 **{skill}**: Critical gap! Improve from {your_skills.get(skill, 5)}/10 to {IDEAL_SKILLS[skill]}/10. Take certification courses.")
                elif gap >= 1:
                    suggestions.append(f"🟡 **{skill}**: Moderate gap. Practice and build projects.")
        
        # Soft skills suggestions
        for skill in soft_skills:
            if your_skills.get(skill, 5) < IDEAL_SKILLS[skill]:
                gap = IDEAL_SKILLS[skill] - your_skills.get(skill, 5)
                if gap >= 3:
                    suggestions.append(f"🔴 **{skill}**: Critical soft skill! Join groups, practice daily.")
                elif gap >= 1:
                    suggestions.append(f"🟡 **{skill}**: Can improve. Seek feedback and practice.")
        
        # Display top 10 suggestions
        for i, suggestion in enumerate(suggestions[:10]):
            st.markdown(f'<div class="suggestion-item">{suggestion}</div>', unsafe_allow_html=True)
        
        # Industry-specific recommendations
        st.markdown("<h3 style='text-align: center;'>🎯 Industry-Specific Recommendations</h3>", unsafe_allow_html=True)
        
        for industry, skills in industry_skills.items():
            industry_score = 0
            total = 0
            for skill in skills:
                if skill in your_skills:
                    industry_score += your_skills[skill]
                    total += 1
            
            if total > 0:
                avg = industry_score / total
                match = (avg / 10) * 100
                
                st.markdown(f"""
                <div class="career-card">
                    <h4 style="color:#00ff9d;">{industry}</h4>
                    <p style="color:white;">Match Score: {match:.1f}%</p>
                    <div style="height:10px; background:rgba(255,255,255,0.2); border-radius:5px;">
                        <div style="height:10px; width:{match}%; background:linear-gradient(90deg, #00ff9d, #667eea); border-radius:5px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Save to history
        if 'skill_history' not in st.session_state:
            st.session_state.skill_history = []
        
        st.session_state.skill_history.append({
            'date': datetime.now().strftime("%d %b %Y"),
            'skill_score': skill_score,
            'strong_skills': strong_skills,
            'weak_skills': weak_skills
        })
    
    # Back to Home
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()