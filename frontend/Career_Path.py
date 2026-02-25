import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Career Path", 
        page_icon="🎯",
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
        
        .career-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .path-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 25px;
            margin: 15px 0;
            border-left: 5px solid #00ff9d;
            transition: all 0.3s;
        }
        
        .path-card:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.25);
        }
        
        .match-badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 50px;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .high-match {
            background: rgba(0, 255, 157, 0.3);
            border: 2px solid #00ff9d;
            color: #00ff9d;
        }
        
        .medium-match {
            background: rgba(255, 187, 51, 0.3);
            border: 2px solid #ffbb33;
            color: #ffbb33;
        }
        
        .low-match {
            background: rgba(255, 68, 68, 0.3);
            border: 2px solid #ff4444;
            color: #ff4444;
        }
        
        .skill-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            padding: 5px 15px;
            margin: 5px;
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        .roadmap-step {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            border-left: 5px solid #ffd700;
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
    
    st.markdown("<h1 style='text-align: center;'>🎯 Career Path Recommendations</h1>", unsafe_allow_html=True)
    
    # Input Section
    st.markdown('<div class="career-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Tell Us About Yourself")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💻 Technical Skills")
        python = st.slider("Python", 1, 10, 7)
        java = st.slider("Java", 1, 10, 5)
        javascript = st.slider("JavaScript", 1, 10, 6)
        sql = st.slider("SQL", 1, 10, 6)
        dsa = st.slider("DSA/Problem Solving", 1, 10, 6)
        
    with col2:
        st.markdown("#### 🗣️ Soft Skills & Interests")
        communication = st.slider("Communication", 1, 10, 7)
        leadership = st.slider("Leadership", 1, 10, 5)
        teamwork = st.slider("Teamwork", 1, 10, 8)
        creativity = st.slider("Creativity", 1, 10, 6)
        analytical = st.slider("Analytical Thinking", 1, 10, 7)
        
    st.markdown("#### 📚 Academics")
    col1, col2, col3 = st.columns(3)
    with col1:
        cgpa = st.slider("CGPA", 4.0, 10.0, 7.5, 0.1)
    with col2:
        projects = st.number_input("Projects Done", 0, 10, 2)
    with col3:
        internships = st.number_input("Internships", 0, 5, 0)
    
    analyze = st.button("🎯 Find My Career Path", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if analyze:
        # Career paths data
        career_paths = {
            "Data Scientist": {
                "skills": {"Python": 9, "SQL": 8, "Analytical Thinking": 9, "DSA": 7},
                "cgpa": 7.5,
                "projects": 2,
                "internships": 1,
                "salary": "₹12-25 LPA",
                "demand": "🔥 High",
                "description": "Analyze complex data to help companies make better decisions",
                "companies": ["Google", "Amazon", "Microsoft", "Flipkart"],
                "certifications": ["AWS ML", "Google Data Analytics", "IBM Data Science"],
                "roadmap": [
                    "Month 1-2: Learn Python, SQL, Statistics",
                    "Month 3-4: Master Machine Learning algorithms",
                    "Month 5-6: Build 2-3 ML projects",
                    "Month 7-8: Learn Deep Learning",
                    "Month 9-10: Get certified",
                    "Month 11-12: Apply for internships"
                ]
            },
            "Software Developer": {
                "skills": {"Python": 8, "Java": 8, "DSA": 9, "JavaScript": 7},
                "cgpa": 7.0,
                "projects": 3,
                "internships": 1,
                "salary": "₹8-20 LPA",
                "demand": "🔥🔥 Very High",
                "description": "Build and maintain software applications",
                "companies": ["Microsoft", "Amazon", "Google", "Infosys", "TCS"],
                "certifications": ["AWS Developer", "Azure Developer", "Oracle Java"],
                "roadmap": [
                    "Month 1-2: Master DSA (LeetCode 200+ problems)",
                    "Month 3-4: Learn System Design",
                    "Month 5-6: Build 3 full-stack projects",
                    "Month 7-8: Learn DevOps basics",
                    "Month 9-10: Contribute to open source",
                    "Month 11-12: Prepare for interviews"
                ]
            },
            "Web Developer": {
                "skills": {"JavaScript": 9, "Python": 7, "Creativity": 8, "Teamwork": 7},
                "cgpa": 6.5,
                "projects": 3,
                "internships": 0,
                "salary": "₹6-15 LPA",
                "demand": "🔥🔥 High",
                "description": "Create amazing websites and web applications",
                "companies": ["Startups", "E-commerce", "Tech Companies"],
                "certifications": ["Meta Frontend", "AWS Developer", "MongoDB"],
                "roadmap": [
                    "Month 1-2: HTML, CSS, JavaScript",
                    "Month 3-4: React/Angular framework",
                    "Month 5-6: Backend (Node.js/Python)",
                    "Month 7-8: Build 3 full-stack projects",
                    "Month 9-10: Learn DevOps/Cloud",
                    "Month 11-12: Build portfolio"
                ]
            },
            "Business Analyst": {
                "skills": {"SQL": 8, "Communication": 9, "Analytical Thinking": 8, "Leadership": 7},
                "cgpa": 7.0,
                "projects": 2,
                "internships": 1,
                "salary": "₹7-15 LPA",
                "demand": "🔥 High",
                "description": "Bridge gap between business and technology",
                "companies": ["Deloitte", "PwC", "KPMG", "Amazon", "Flipkart"],
                "certifications": ["CBAP", "PMP", "Six Sigma"],
                "roadmap": [
                    "Month 1-2: Learn SQL, Excel advanced",
                    "Month 3-4: Tableau/Power BI",
                    "Month 5-6: Python for analytics",
                    "Month 7-8: Business communication",
                    "Month 9-10: Get CBAP certified",
                    "Month 11-12: Case study practice"
                ]
            },
            "Cyber Security Analyst": {
                "skills": {"Python": 7, "Analytical Thinking": 8, "DSA": 6, "Creativity": 7},
                "cgpa": 7.0,
                "projects": 2,
                "internships": 1,
                "salary": "₹8-18 LPA",
                "demand": "🔥🔥 High",
                "description": "Protect organizations from cyber threats",
                "companies": ["TCS", "Wipro", "HCL", "Cisco", "Palo Alto"],
                "certifications": ["CEH", "CISSP", "CompTIA Security+"],
                "roadmap": [
                    "Month 1-2: Networking basics",
                    "Month 3-4: Linux security",
                    "Month 5-6: Python security",
                    "Month 7-8: CEH certification",
                    "Month 9-10: Build security projects",
                    "Month 11-12: Bug bounty hunting"
                ]
            }
        }
        
        # Calculate match scores
        results = []
        for career, details in career_paths.items():
            score = 0
            max_score = 0
            
            # Skill match (50 points)
            skill_weight = 50 / len(details["skills"])
            for skill, required in details["skills"].items():
                max_score += skill_weight
                if skill == "Python" and python >= required:
                    score += skill_weight * (python/required)
                elif skill == "Java" and java >= required:
                    score += skill_weight * (java/required)
                elif skill == "JavaScript" and javascript >= required:
                    score += skill_weight * (javascript/required)
                elif skill == "SQL" and sql >= required:
                    score += skill_weight * (sql/required)
                elif skill == "DSA" and dsa >= required:
                    score += skill_weight * (dsa/required)
                elif skill == "Communication" and communication >= required:
                    score += skill_weight * (communication/required)
                elif skill == "Leadership" and leadership >= required:
                    score += skill_weight * (leadership/required)
                elif skill == "Teamwork" and teamwork >= required:
                    score += skill_weight * (teamwork/required)
                elif skill == "Creativity" and creativity >= required:
                    score += skill_weight * (creativity/required)
                elif skill == "Analytical Thinking" and analytical >= required:
                    score += skill_weight * (analytical/required)
            
            # CGPA (20 points)
            max_score += 20
            if cgpa >= details["cgpa"]:
                score += 20
            else:
                score += 20 * (cgpa / details["cgpa"])
            
            # Projects (15 points)
            max_score += 15
            if projects >= details["projects"]:
                score += 15
            else:
                score += 15 * (projects / details["projects"])
            
            # Internships (15 points)
            max_score += 15
            if internships >= details["internships"]:
                score += 15
            else:
                score += 15 * (internships / details["internships"]) if details["internships"] > 0 else 15
            
            match_percentage = (score / max_score) * 100
            results.append((career, match_percentage, details))
        
        # Sort by match percentage
        results.sort(key=lambda x: x[1], reverse=True)
        
        # Display results
        st.markdown('<div class="career-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Your Top Career Matches")
        
        for i, (career, match, details) in enumerate(results[:3]):
            # Determine match class
            if match >= 70:
                match_class = "high-match"
            elif match >= 40:
                match_class = "medium-match"
            else:
                match_class = "low-match"
            
            st.markdown(f"""
            <div class="path-card">
                <h2 style="color: #00ff9d; margin: 0;">{i+1}. {career}</h2>
                <div class="match-badge {match_class}">Match Score: {match:.1f}%</div>
                <p style="color: white;">{details['description']}</p>
                <p style="color: white;">💰 Salary Range: {details['salary']}</p>
                <p style="color: white;">📈 Market Demand: {details['demand']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Skills required
            st.markdown("**🔑 Key Skills Required:**")
            skills_html = ""
            for skill, level in details["skills"].items():
                skills_html += f'<span class="skill-tag">{skill} ({level}/10)</span>'
            st.markdown(skills_html, unsafe_allow_html=True)
            
            # Top companies
            st.markdown("**🏢 Top Companies:**")
            companies_html = ""
            for company in details["companies"]:
                companies_html += f'<span class="skill-tag">{company}</span>'
            st.markdown(companies_html, unsafe_allow_html=True)
            
            # Certifications
            with st.expander(f"📜 Recommended Certifications for {career}"):
                for cert in details["certifications"]:
                    st.markdown(f"- {cert}")
            
            # Roadmap
            with st.expander(f"🗺️ Learning Roadmap for {career}"):
                for step in details["roadmap"]:
                    st.markdown(f"<div class='roadmap-step'>{step}</div>", unsafe_allow_html=True)
            
            st.markdown("---")
        
        # Career comparison chart
        st.markdown("### 📊 Career Match Comparison")
        
        fig = go.Figure(data=[
            go.Bar(
                x=[r[0] for r in results[:5]],
                y=[r[1] for r in results[:5]],
                marker_color=['#00ff9d' if r[1] >= 70 else '#ffbb33' if r[1] >= 40 else '#ff4444' for r in results[:5]],
                text=[f'{r[1]:.1f}%' for r in results[:5]],
                textposition='outside',
            )
        ])
        
        fig.update_layout(
            title="Career Match Scores",
            xaxis_title="Career Path",
            yaxis_title="Match Percentage",
            yaxis_range=[0, 100],
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()