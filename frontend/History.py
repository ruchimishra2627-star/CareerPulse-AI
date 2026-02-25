import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import random

def show():
    st.set_page_config(
        page_title="CareerPulse AI - History", 
        page_icon="📋",
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
        
        .history-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.25);
            border-color: #00ff9d;
        }
        
        .stat-number {
            font-size: 36px;
            font-weight: bold;
            color: #00ff9d;
        }
        
        .stat-label {
            color: white;
            font-size: 14px;
        }
        
        .history-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            border-left: 5px solid #00ff9d;
            transition: all 0.3s;
        }
        
        .history-item:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.2);
        }
        
        .badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 50px;
            font-size: 12px;
            font-weight: bold;
        }
        
        .badge-high {
            background: rgba(0, 255, 157, 0.3);
            color: #00ff9d;
            border: 1px solid #00ff9d;
        }
        
        .badge-medium {
            background: rgba(255, 187, 51, 0.3);
            color: #ffbb33;
            border: 1px solid #ffbb33;
        }
        
        .badge-low {
            background: rgba(255, 68, 68, 0.3);
            color: #ff4444;
            border: 1px solid #ff4444;
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
        
        .filter-btn {
            background: rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
        }
        
        .filter-btn:hover {
            background: rgba(255, 255, 255, 0.2) !important;
            border-color: #00ff9d !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>📋 Analysis History</h1>", unsafe_allow_html=True)
    
    # Initialize session state for history if not exists
    if 'history_data' not in st.session_state:
        # Create sample history data
        st.session_state.history_data = []
        
        # Generate 20 sample records
        domains = ["Software Developer", "Data Scientist", "Web Developer", "Business Analyst", "Cyber Security"]
        for i in range(20):
            date = datetime.now().replace(day=datetime.now().day - i)
            prob = random.randint(45, 95)
            if prob >= 70:
                risk = "Low Risk"
                badge = "badge-high"
            elif prob >= 40:
                risk = "Medium Risk"
                badge = "badge-medium"
            else:
                risk = "High Risk"
                badge = "badge-low"
            
            st.session_state.history_data.append({
                "date": date.strftime("%d %b %Y"),
                "time": f"{random.randint(9, 18)}:{random.randint(10, 59)}",
                "domain": random.choice(domains),
                "probability": prob,
                "risk": risk,
                "badge": badge,
                "cgpa": round(random.uniform(6.5, 9.5), 1),
                "skills": random.randint(50, 95)
            })
    
    # Filters
    st.markdown('<div class="history-card">', unsafe_allow_html=True)
    st.markdown("### 🔍 Filter History")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        filter_domain = st.selectbox("Domain", ["All", "Software Developer", "Data Scientist", "Web Developer", "Business Analyst", "Cyber Security"])
    
    with col2:
        filter_risk = st.selectbox("Risk Level", ["All", "Low Risk", "Medium Risk", "High Risk"])
    
    with col3:
        filter_date = st.selectbox("Time Period", ["All Time", "Last 7 Days", "Last 30 Days", "Last 90 Days"])
    
    with col4:
        sort_by = st.selectbox("Sort By", ["Newest First", "Oldest First", "Highest Score", "Lowest Score"])
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ===== FIXED STATISTICS SECTION =====
    st.markdown('<div class="history-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Your Progress Overview")
    
    # Check if history_data exists and has data
    if 'history_data' in st.session_state and len(st.session_state.history_data) > 0:
        df = pd.DataFrame(st.session_state.history_data)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            avg_prob = df['probability'].mean() if 'probability' in df.columns else 0
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{avg_prob:.1f}%</div>
                <div class="stat-label">Average Score</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            max_prob = df['probability'].max() if 'probability' in df.columns else 0
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{max_prob:.1f}%</div>
                <div class="stat-label">Highest Score</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            min_prob = df['probability'].min() if 'probability' in df.columns else 0
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{min_prob:.1f}%</div>
                <div class="stat-label">Lowest Score</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            total = len(df)
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-number">{total}</div>
                <div class="stat-label">Total Analyses</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No history data available. Generate some predictions first!")
        df = pd.DataFrame()  # Empty dataframe for later use
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Only show charts and history if data exists
    if 'history_data' in st.session_state and len(st.session_state.history_data) > 0 and not df.empty:
        # Progress Chart
        st.markdown('<div class="history-card">', unsafe_allow_html=True)
        st.markdown("### 📈 Score Trend")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=list(range(len(df))),
            y=df['probability'],
            mode='lines+markers',
            name='Score',
            line=dict(color='#00ff9d', width=3),
            marker=dict(size=8, color='white', line=dict(color='#00ff9d', width=2))
        ))
        
        fig.add_hline(y=70, line_dash="dash", line_color="#00ff9d", annotation_text="Good Score")
        fig.add_hline(y=40, line_dash="dash", line_color="#ffbb33", annotation_text="Medium")
        
        fig.update_layout(
            title="Your Progress Over Time",
            xaxis_title="Analysis Number",
            yaxis_title="Score (%)",
            yaxis_range=[0, 100],
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': 'white'},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Domain Distribution
        st.markdown('<div class="history-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Domain Distribution")
        
        col1, col2 = st.columns(2)
        
        with col1:
            domain_counts = df['domain'].value_counts()
            fig = px.pie(
                values=domain_counts.values,
                names=domain_counts.index,
                title="Analyses by Domain",
                color_discrete_sequence=['#00ff9d', '#ffbb33', '#ff4444', '#667eea', '#764ba2']
            )
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font={'color': 'white'},
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            risk_counts = df['risk'].value_counts()
            fig = px.bar(
                x=risk_counts.index,
                y=risk_counts.values,
                title="Risk Level Distribution",
                color=risk_counts.index,
                color_discrete_map={
                    'Low Risk': '#00ff9d',
                    'Medium Risk': '#ffbb33',
                    'High Risk': '#ff4444'
                }
            )
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font={'color': 'white'},
                height=350,
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # History Table
        st.markdown('<div class="history-card">', unsafe_allow_html=True)
        st.markdown("### 📋 Detailed History")
        
        # Filter data based on selection
        filtered_df = df.copy()
        
        if filter_domain != "All":
            filtered_df = filtered_df[filtered_df['domain'] == filter_domain]
        
        if filter_risk != "All":
            filtered_df = filtered_df[filtered_df['risk'] == filter_risk]
        
        if filter_date == "Last 7 Days":
            filtered_df = filtered_df.head(7)
        elif filter_date == "Last 30 Days":
            filtered_df = filtered_df.head(30)
        elif filter_date == "Last 90 Days":
            filtered_df = filtered_df.head(90)
        
        if sort_by == "Newest First":
            filtered_df = filtered_df
        elif sort_by == "Oldest First":
            filtered_df = filtered_df.iloc[::-1]
        elif sort_by == "Highest Score":
            filtered_df = filtered_df.sort_values('probability', ascending=False)
        elif sort_by == "Lowest Score":
            filtered_df = filtered_df.sort_values('probability', ascending=True)
        
        # Display history items
        for idx, row in filtered_df.iterrows():
            st.markdown(f"""
            <div class="history-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="color: white; font-size: 18px; font-weight: bold;">{row['domain']}</span>
                        <span class="badge {row['badge']}" style="margin-left: 10px;">{row['risk']}</span>
                    </div>
                    <div style="color: #00ff9d; font-size: 24px; font-weight: bold;">{row['probability']}%</div>
                </div>
                <div style="display: flex; gap: 20px; margin-top: 10px; color: rgba(255,255,255,0.7);">
                    <div>📅 {row['date']} at {row['time']}</div>
                    <div>📚 CGPA: {row['cgpa']}</div>
                    <div>📊 Skills: {row['skills']}%</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Export options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Download as CSV", use_container_width=True):
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    label="Click to Download",
                    data=csv,
                    file_name="career_history.csv",
                    mime="text/csv"
                )
        
        with col2:
            if st.button("🔄 Refresh Data", use_container_width=True):
                st.rerun()
        
        with col3:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state.history_data = []
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="history-card">', unsafe_allow_html=True)
        st.info("No history data available. Go to Dashboard and generate some predictions!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Back to Home
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()