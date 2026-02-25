import streamlit as st
import re
from collections import Counter
import time

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Resume Scanner", 
        page_icon="📄",
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
        
        .scanner-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .score-box {
            text-align: center;
            padding: 30px;
            border-radius: 20px;
            margin: 20px 0;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        .high-score {
            background: rgba(0, 255, 157, 0.2);
            border: 3px solid #00ff9d;
        }
        
        .medium-score {
            background: rgba(255, 187, 51, 0.2);
            border: 3px solid #ffbb33;
        }
        
        .low-score {
            background: rgba(255, 68, 68, 0.2);
            border: 3px solid #ff4444;
        }
        
        .score-number {
            font-size: 72px;
            font-weight: bold;
            color: white;
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
        
        .missing-skill {
            display: inline-block;
            background: rgba(255, 68, 68, 0.2);
            border-radius: 50px;
            padding: 8px 18px;
            margin: 5px;
            color: #ff8888;
            border: 1px solid #ff4444;
        }
        
        .suggestion-item {
            background: rgba(255, 255, 255, 0.1);
            border-left: 5px solid #00ff9d;
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            color: white;
            transition: all 0.3s;
        }
        
        .suggestion-item:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.2);
        }
        
        .keyword-cloud {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea, #764ba2) !important;
            color: white !important;
            border-radius: 50px !important;
            padding: 12px 30px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: all 0.3s !important;
            width: 100% !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        }
        
        .file-upload {
            background: rgba(255, 255, 255, 0.1);
            border: 2px dashed #00ff9d;
            border-radius: 20px;
            padding: 40px;
            text-align: center;
        }
        
        .ats-tag {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            margin: 5px;
        }
        
        .ats-good {
            background: rgba(0, 255, 157, 0.3);
            color: #00ff9d;
            border: 1px solid #00ff9d;
        }
        
        .ats-bad {
            background: rgba(255, 68, 68, 0.3);
            color: #ff8888;
            border: 1px solid #ff4444;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>📄 AI Resume Scanner</h1>", unsafe_allow_html=True)
    
    # Job role selection
    st.markdown('<div class="scanner-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Select Target Job Role")
    
    job_roles = [
        "Software Developer",
        "Data Scientist", 
        "Web Developer",
        "Business Analyst",
        "Cyber Security Analyst",
        "Cloud Engineer",
        "DevOps Engineer",
        "Product Manager",
        "UI/UX Designer",
        "Machine Learning Engineer"
    ]
    
    col1, col2 = st.columns(2)
    with col1:
        selected_role = st.selectbox("Choose Role", job_roles)
    with col2:
        experience_level = st.selectbox("Experience Level", ["Entry Level (0-2 yrs)", "Mid Level (3-5 yrs)", "Senior Level (5+ yrs)"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Resume input
    st.markdown('<div class="scanner-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Paste Your Resume Text")
    
    # Sample resume template
    with st.expander("📋 View Sample Resume Format"):
        st.markdown("""
        ```
        John Doe
        john.doe@email.com | +91 98765 43210 | github.com/johndoe | linkedin.com/in/johndoe
        
        EDUCATION
        B.Tech in Computer Science, XYZ University (2020-2024)
        CGPA: 8.5/10
        
        SKILLS
        Python, Java, JavaScript, SQL, React, Node.js, MongoDB, AWS, DSA, OOP
        
        EXPERIENCE
        Software Developer Intern, ABC Tech (Jun 2023 - Aug 2023)
        • Developed REST APIs using Python and Flask
        • Worked on database optimization improving query performance by 30%
        
        PROJECTS
        E-commerce Website: Built full-stack app using MERN stack
        ML Model: Developed prediction model with 85% accuracy
        
        CERTIFICATIONS
        AWS Certified Cloud Practitioner
        Google Data Analytics Certificate
        ```
        """)
    
    resume_text = st.text_area("", height=300, placeholder="Copy and paste your resume here...")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        scan_btn = st.button("🔍 Scan Resume", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if scan_btn and resume_text:
        with st.spinner("🔍 Analyzing your resume..."):
            time.sleep(2)
        
        # Convert to lowercase for matching
        text = resume_text.lower()
        
        # Role-specific requirements
        role_requirements = {
            "Software Developer": {
                "skills": ["python", "java", "c++", "sql", "git", "data structures", "algorithms", "oop", "system design", "rest api"],
                "certifications": ["aws", "azure", "oracle", "java"],
                "projects": 3,
                "keywords": ["developed", "built", "implemented", "designed", "created"],
                "tools": ["git", "docker", "jenkins", "jira", "vscode"]
            },
            "Data Scientist": {
                "skills": ["python", "sql", "machine learning", "deep learning", "pandas", "numpy", "tensorflow", "pytorch", "statistics", "r"],
                "certifications": ["tensorflow", "aws ml", "data science", "ibm", "google"],
                "projects": 2,
                "keywords": ["analyzed", "predicted", "model", "accuracy", "visualization"],
                "tools": ["jupyter", "tableau", "power bi", "spark", "hadoop"]
            },
            "Web Developer": {
                "skills": ["html", "css", "javascript", "react", "node.js", "mongodb", "express", "php", "mysql", "typescript"],
                "certifications": ["aws", "meta", "google", "mongodb"],
                "projects": 3,
                "keywords": ["website", "web app", "frontend", "backend", "responsive"],
                "tools": ["vscode", "git", "chrome devtools", "figma", "postman"]
            },
            "Business Analyst": {
                "skills": ["excel", "sql", "tableau", "power bi", "python", "statistics", "communication", "presentation", "requirements", "agile"],
                "certifications": ["cbap", "pmp", "six sigma", "scrum"],
                "projects": 2,
                "keywords": ["requirements", "stakeholder", "analysis", "documentation", "process"],
                "tools": ["jira", "confluence", "visio", "excel", "powerpoint"]
            },
            "Cyber Security Analyst": {
                "skills": ["networking", "linux", "python", "security", "encryption", "firewall", "penetration testing", "risk assessment", "siem", "vulnerability"],
                "certifications": ["ceh", "cissp", "comptia security+", "cism"],
                "projects": 2,
                "keywords": ["security", "threat", "attack", "defense", "compliance"],
                "tools": ["wireshark", "metasploit", "nmap", "burp suite", "kali linux"]
            },
            "Cloud Engineer": {
                "skills": ["aws", "azure", "gcp", "docker", "kubernetes", "linux", "python", "devops", "terraform", "jenkins"],
                "certifications": ["aws", "azure", "gcp", "kubernetes"],
                "projects": 2,
                "keywords": ["cloud", "deployment", "infrastructure", "scaling", "automation"],
                "tools": ["docker", "k8s", "jenkins", "terraform", "ansible"]
            },
            "DevOps Engineer": {
                "skills": ["docker", "kubernetes", "jenkins", "git", "linux", "python", "aws", "terraform", "ansible", "monitoring"],
                "certifications": ["aws devops", "azure devops", "kubernetes", "docker"],
                "projects": 2,
                "keywords": ["ci/cd", "automation", "deployment", "infrastructure", "monitoring"],
                "tools": ["jenkins", "gitlab", "prometheus", "grafana", "elk"]
            },
            "Product Manager": {
                "skills": ["product management", "agile", "scrum", "roadmap", "analytics", "communication", "leadership", "strategy", "marketing", "ux"],
                "certifications": ["pmp", "cspo", "scrum master", "product school"],
                "projects": 2,
                "keywords": ["product", "launch", "roadmap", "stakeholder", "market"],
                "tools": ["jira", "confluence", "figma", "mixpanel", "amplitude"]
            },
            "UI/UX Designer": {
                "skills": ["ui design", "ux design", "figma", "sketch", "adobe xd", "photoshop", "illustrator", "wireframing", "prototyping", "user research"],
                "certifications": ["google ux", "interaction design", "adobe"],
                "projects": 3,
                "keywords": ["design", "user", "interface", "prototype", "wireframe"],
                "tools": ["figma", "sketch", "adobe xd", "invision", "zeplin"]
            },
            "Machine Learning Engineer": {
                "skills": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "nlp", "computer vision", "data science", "sql", "math"],
                "certifications": ["tensorflow", "aws ml", "deep learning", "coursera"],
                "projects": 2,
                "keywords": ["model", "accuracy", "training", "prediction", "neural network"],
                "tools": ["jupyter", "keras", "scikit-learn", "opencv", "hugging face"]
            }
        }
        
        req = role_requirements.get(selected_role, role_requirements["Software Developer"])
        
        # Find skills in resume
        found_skills = []
        missing_skills = []
        
        for skill in req["skills"]:
            if skill in text:
                found_skills.append(skill)
            else:
                missing_skills.append(skill)
        
        # Find certifications
        found_certs = []
        missing_certs = []
        for cert in req["certifications"]:
            if cert in text:
                found_certs.append(cert)
            else:
                missing_certs.append(cert)
        
        # Find keywords
        found_keywords = []
        for keyword in req["keywords"]:
            if keyword in text:
                found_keywords.append(keyword)
        
        # Find tools
        found_tools = []
        for tool in req["tools"]:
            if tool in text:
                found_tools.append(tool)
        
        # Count projects mentioned
        project_count = 0
        for keyword in ["project", "built", "developed", "created", "implemented"]:
            project_count += text.count(keyword)
        
        # Calculate scores
        skill_score = min(40, (len(found_skills) / len(req["skills"])) * 40)
        cert_score = min(15, (len(found_certs) / len(req["certifications"])) * 15) if req["certifications"] else 15
        keyword_score = min(15, (len(found_keywords) / len(req["keywords"])) * 15)
        tool_score = min(10, (len(found_tools) / len(req["tools"])) * 10)
        project_score = min(20, (project_count / req["projects"]) * 20)
        
        total_score = skill_score + cert_score + keyword_score + tool_score + project_score
        
        # ATS checks
        ats_checks = []
        ats_passed = 0
        ats_total = 0
        
        # Email check
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resume_text):
            ats_checks.append(("✅ Email found", "good"))
            ats_passed += 1
        else:
            ats_checks.append(("❌ Email missing", "bad"))
        ats_total += 1
        
        # Phone check
        if re.search(r'\d{10}', resume_text) or re.search(r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}', resume_text):
            ats_checks.append(("✅ Phone number found", "good"))
            ats_passed += 1
        else:
            ats_checks.append(("❌ Phone number missing", "bad"))
        ats_total += 1
        
        # LinkedIn check
        if "linkedin.com" in text:
            ats_checks.append(("✅ LinkedIn profile found", "good"))
            ats_passed += 1
        else:
            ats_checks.append(("❌ LinkedIn profile missing", "bad"))
        ats_total += 1
        
        # GitHub check
        if "github.com" in text:
            ats_checks.append(("✅ GitHub profile found", "good"))
            ats_passed += 1
        else:
            ats_checks.append(("❌ GitHub profile missing", "bad"))
        ats_total += 1
        
        # Education check
        if any(word in text for word in ["b.tech", "b.e", "bachelor", "master", "m.tech", "phd", "degree"]):
            ats_checks.append(("✅ Education section found", "good"))
            ats_passed += 1
        else:
            ats_checks.append(("❌ Education section missing", "bad"))
        ats_total += 1
        
        ats_score = (ats_passed / ats_total) * 100
        
        # Display results
        st.markdown('<div class="scanner-card">', unsafe_allow_html=True)
        st.markdown(f"### 📊 Resume Analysis for {selected_role}")
        
        # Score box
        if total_score >= 70:
            score_class = "high-score"
            score_message = "🌟 Excellent! Your resume is well-optimized!"
        elif total_score >= 40:
            score_class = "medium-score"
            score_message = "📈 Good resume! Some improvements needed."
        else:
            score_class = "low-score"
            score_message = "💪 Needs significant improvement. Let's work on it!"
        
        st.markdown(f"""
        <div class="score-box {score_class}">
            <div class="score-number">{total_score:.1f}%</div>
            <div style="color: white; font-size: 24px; margin: 10px 0;">Overall Match Score</div>
            <div style="color: white; font-size: 16px;">{score_message}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed scores in columns
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Skills", f"{len(found_skills)}/{len(req['skills'])}")
        with col2:
            st.metric("Certifications", f"{len(found_certs)}/{len(req['certifications'])}")
        with col3:
            st.metric("Keywords", f"{len(found_keywords)}/{len(req['keywords'])}")
        with col4:
            st.metric("Tools", f"{len(found_tools)}/{len(req['tools'])}")
        with col5:
            st.metric("Projects", f"{project_count}")
        
        # ATS Score
        st.markdown("### 🤖 ATS Compatibility Score")
        ats_color = "#00ff9d" if ats_score >= 70 else "#ffbb33" if ats_score >= 40 else "#ff4444"
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.1); border-radius: 20px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <span style="color: white;">ATS Score: {ats_score:.1f}%</span>
                <span style="color: {ats_color};">
                    {"✅ Good for ATS" if ats_score >= 70 else "⚠️ Needs ATS Optimization" if ats_score >= 40 else "❌ Poor ATS Score"}
                </span>
            </div>
            <div style="background: rgba(255,255,255,0.2); border-radius: 10px; height: 10px;">
                <div style="background: {ats_color}; width: {ats_score}%; height: 10px; border-radius: 10px;"></div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 20px;">
        """, unsafe_allow_html=True)
        
        for check, status in ats_checks:
            color = "#00ff9d" if status == "good" else "#ff4444"
            st.markdown(f'<div style="color: {color};">{check}</div>', unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Found Skills
        if found_skills:
            st.markdown("### ✅ Skills Found in Resume")
            skills_html = ""
            for skill in sorted(found_skills):
                skills_html += f'<span class="skill-tag">{skill.title()}</span>'
            st.markdown(skills_html, unsafe_allow_html=True)
        
        # Missing Skills
        if missing_skills:
            st.markdown("### ❌ Skills to Add")
            missing_html = ""
            for skill in sorted(missing_skills)[:15]:  # Show top 15
                missing_html += f'<span class="missing-skill">{skill.title()}</span>'
            st.markdown(missing_html, unsafe_allow_html=True)
        
        # Certifications
        if found_certs or missing_certs:
            st.markdown("### 📜 Certifications")
            col1, col2 = st.columns(2)
            with col1:
                if found_certs:
                    st.markdown("**✅ Found:**")
                    for cert in found_certs:
                        st.markdown(f"- {cert.title()}")
            with col2:
                if missing_certs:
                    st.markdown("**📝 Recommended:**")
                    for cert in missing_certs:
                        st.markdown(f"- {cert.title()}")
        
        # Keywords to add
        if missing_skills or missing_certs:
            st.markdown("### 🔑 Keywords to Add")
            st.markdown("Add these keywords to your resume for better ATS scoring:")
            cols = st.columns(3)
            all_missing = missing_skills + missing_certs
            for i, item in enumerate(all_missing[:9]):
                with cols[i % 3]:
                    st.info(item.title())
        
        # Personalized Suggestions
        st.markdown("### 💡 Resume Improvement Suggestions")
        
        suggestions = []
        
        # Skills suggestions
        if len(found_skills) < len(req["skills"]) * 0.3:
            suggestions.append("🎯 **Critical Gap:** You're missing most required skills. Consider taking online courses in: " + ", ".join(missing_skills[:5]))
        elif missing_skills:
            suggestions.append("📚 **Skill Development:** Add these key skills to your resume: " + ", ".join(missing_skills[:5]))
        
        # Certification suggestions
        if missing_certs:
            suggestions.append("📜 **Certifications:** Get certified in " + ", ".join(missing_certs) + " to boost your profile")
        
        # Project suggestions
        if project_count < req["projects"]:
            suggestions.append(f"🛠️ **Projects:** Add {req['projects'] - project_count} more project(s) related to {selected_role}")
        
        # Keyword suggestions
        if len(found_keywords) < len(req["keywords"]) * 0.5:
            suggestions.append("🔑 **Keywords:** Use more action words like: " + ", ".join(req["keywords"]))
        
        # Tool suggestions
        if len(found_tools) < len(req["tools"]) * 0.3:
            suggestions.append("🛠️ **Tools & Technologies:** Mention tools like: " + ", ".join(req["tools"][:5]))
        
        # ATS suggestions
        if ats_score < 70:
            if "Email missing" in str(ats_checks):
                suggestions.append("📧 **Contact Info:** Add your email address")
            if "Phone" in str(ats_checks) and "missing" in str(ats_checks):
                suggestions.append("📱 **Phone Number:** Add your phone number with country code")
            if "LinkedIn" in str(ats_checks) and "missing" in str(ats_checks):
                suggestions.append("🔗 **LinkedIn:** Add your LinkedIn profile URL")
            if "GitHub" in str(ats_checks) and "missing" in str(ats_checks):
                suggestions.append("💻 **GitHub:** Add your GitHub profile URL for technical roles")
            if "Education" in str(ats_checks) and "missing" in str(ats_checks):
                suggestions.append("🎓 **Education:** Add your degree, university, and graduation year")
        
        # Experience suggestions
        years_match = re.search(r'(\d+)\s*\+?\s*years?', text)
        if not years_match and experience_level != "Entry Level (0-2 yrs)":
            suggestions.append("💼 **Experience:** Clearly mention your years of experience (e.g., '5 years experience')")
        
        # Formatting suggestions
        if len(resume_text.split('\n')) < 10:
            suggestions.append("📄 **Format:** Use proper sections (Education, Skills, Experience, Projects)")
        
        if len(resume_text) < 500:
            suggestions.append("📏 **Length:** Your resume seems short. Aim for 1-2 pages with detailed descriptions")
        
        for suggestion in suggestions:
            st.markdown(f'<div class="suggestion-item">{suggestion}</div>', unsafe_allow_html=True)
        
        if not suggestions:
            st.markdown("""
            <div style="background: rgba(0, 255, 157, 0.2); border: 2px solid #00ff9d; border-radius: 15px; padding: 20px; text-align: center;">
                <h3 style="color: #00ff9d;">✨ Perfect! Your resume is well-optimized!</h3>
                <p style="color: white;">You're ready to start applying for {selected_role} positions!</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()