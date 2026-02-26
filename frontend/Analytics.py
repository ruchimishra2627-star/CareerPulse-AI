import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random

def show():
    st.set_page_config(
        page_title="CareerPulse AI - Analytics", 
        page_icon="📊",
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
        
        .analytics-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px;
            margin: 20px 0;
            border: 2px solid rgba(255, 255, 255, 0.2);
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
        
        .insight-box {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            border-left: 5px solid #00ff9d;
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
        
        .trend-up {
            color: #00ff9d;
            font-weight: bold;
        }
        
        .trend-down {
            color: #ff4444;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>📊 Advanced Analytics</h1>", unsafe_allow_html=True)
    
    # Introduction Section
    with st.expander("ℹ️ What is Analytics Page? (Click to learn)"):
        st.markdown("""
        <div style="background:rgba(102,126,234,0.3); border-left:5px solid #00ff9d; border-radius:10px; padding:15px; color:white;">
            <h3>🎯 Purpose of Analytics:</h3>
            <p>This page analyzes your <b>prediction history</b> to show:</p>
            <ul>
                <li>📈 <b>Progress over time</b> - Are you improving?</li>
                <li>📊 <b>Domain preferences</b> - Which career paths you explore</li>
                <li>⚠️ <b>Risk patterns</b> - Your consistency</li>
                <li>💡 <b>Smart insights</b> - What to focus on</li>
            </ul>
            <p>Use this data to understand your strengths and weaknesses!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Generate or get history data
    if 'history_data' not in st.session_state or len(st.session_state.history_data) == 0:
        # Create sample data for analytics
        domains = ["Software Developer", "Data Scientist", "Web Developer", "Business Analyst", "Cyber Security"]
        history_data = []
        
        for i in range(50):  # 50 sample records
            date = datetime.now() - timedelta(days=random.randint(0, 60))
            prob = random.randint(45, 98)
            if prob >= 70:
                risk = "Low Risk"
            elif prob >= 40:
                risk = "Medium Risk"
            else:
                risk = "High Risk"
            
            history_data.append({
                "date": date.strftime("%Y-%m-%d"),
                "domain": random.choice(domains),
                "probability": prob,
                "risk": risk
            })
        
        df = pd.DataFrame(history_data)
    else:
        df = pd.DataFrame(st.session_state.history_data)
        if 'date' not in df.columns:
            df['date'] = datetime.now().strftime("%Y-%m-%d")
    
    # Time period filter
    st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
    st.markdown("### 📅 Select Time Period")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        period = st.selectbox("Period", ["Last 7 Days", "Last 30 Days", "Last 90 Days", "All Time"])
    with col2:
        chart_type = st.selectbox("Chart Type", ["Line", "Bar", "Area"])
    with col3:
        comparison = st.selectbox("Compare", ["None", "Domain", "Risk Level"])
    with col4:
        st.markdown("### 📊")
        refresh = st.button("🔄 Refresh Data")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter data based on period
    if period == "Last 7 Days":
        filtered_df = df.tail(7)
    elif period == "Last 30 Days":
        filtered_df = df.tail(30)
    elif period == "Last 90 Days":
        filtered_df = df.tail(90)
    else:
        filtered_df = df
    
    # Key Metrics
    st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
    st.markdown("### 📈 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_score = filtered_df['probability'].mean()
        prev_avg = df['probability'].mean() if len(df) > len(filtered_df) else avg_score
        trend = avg_score - prev_avg
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{avg_score:.1f}%</div>
            <div class="stat-label">Average Score</div>
            <div style="color: {'#00ff9d' if trend >=0 else '#ff4444'};">
                {trend:+.1f}% vs overall
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        max_score = filtered_df['probability'].max()
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{max_score:.1f}%</div>
            <div class="stat-label">Highest Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        min_score = filtered_df['probability'].min()
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{min_score:.1f}%</div>
            <div class="stat-label">Lowest Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        total = len(filtered_df)
        improvement = filtered_df['probability'].iloc[-1] - filtered_df['probability'].iloc[0] if len(filtered_df) > 1 else 0
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{total}</div>
            <div class="stat-label">Total Analyses</div>
            <div class="{'trend-up' if improvement > 0 else 'trend-down'}">
                {improvement:+.1f}% overall change
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main Chart - FIXED VERSION
    st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Performance Trend")
    
    if chart_type == "Line":
        fig = px.line(
            filtered_df, 
            x=filtered_df.index, 
            y='probability',
            title=f"Score Trend - {period}",
            markers=True
        )
        fig.update_traces(line_color='#00ff9d', marker_color='#00ff9d')
        
    elif chart_type == "Bar":
        fig = px.bar(
            filtered_df, 
            x=filtered_df.index, 
            y='probability',
            title=f"Score Distribution - {period}",
            color_discrete_sequence=['#00ff9d']
        )
        
    else:  # Area
        fig = px.area(
            filtered_df, 
            x=filtered_df.index, 
            y='probability',
            title=f"Score Area - {period}",
            color_discrete_sequence=['#00ff9d']
        )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        xaxis_title="Analysis Number",
        yaxis_title="Score (%)",
        yaxis_range=[0, 100],
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Comparison Charts
    if comparison != "None":
        st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
        st.markdown(f"### 📊 Comparison by {comparison}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if comparison == "Domain":
                avg_by_domain = filtered_df.groupby('domain')['probability'].mean().sort_values()
                fig = px.bar(
                    x=avg_by_domain.values,
                    y=avg_by_domain.index,
                    orientation='h',
                    title="Average Score by Domain",
                    color=avg_by_domain.values,
                    color_continuous_scale=['#ff4444', '#ffbb33', '#00ff9d']
                )
            else:
                avg_by_risk = filtered_df.groupby('risk')['probability'].mean()
                fig = px.pie(
                    values=avg_by_risk.values,
                    names=avg_by_risk.index,
                    title="Score Distribution by Risk Level",
                    color=avg_by_risk.index,
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
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if comparison == "Domain":
                count_by_domain = filtered_df['domain'].value_counts()
                fig = px.pie(
                    values=count_by_domain.values,
                    names=count_by_domain.index,
                    title="Analysis Count by Domain",
                    color_discrete_sequence=['#00ff9d', '#ffbb33', '#ff4444', '#667eea', '#764ba2']
                )
            else:
                risk_counts = filtered_df['risk'].value_counts()
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
                height=400,
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Insights Section
    st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
    st.markdown("### 💡 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if 'domain' in filtered_df.columns:
            best_domain = filtered_df.groupby('domain')['probability'].mean().idxmax()
            best_score = filtered_df.groupby('domain')['probability'].mean().max()
            st.markdown(f"""
            <div class="insight-box">
                <span style="color:#00ff9d; font-size:18px;">🏆 Best Domain</span><br>
                <span style="color: white;">{best_domain}</span><br>
                <span style="color: #00ff9d;">Average Score: {best_score:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)
        
        improvement_rate = (filtered_df['probability'].iloc[-1] - filtered_df['probability'].iloc[0]) / filtered_df['probability'].iloc[0] * 100 if len(filtered_df) > 1 and filtered_df['probability'].iloc[0] > 0 else 0
        st.markdown(f"""
        <div class="insight-box">
            <span style="color:#00ff9d; font-size:18px;">📈 Improvement Rate</span><br>
            <span style="color: white;">{improvement_rate:+.1f}% overall</span><br>
            <span style="color: {'#00ff9d' if improvement_rate > 0 else '#ff4444'};">
                {'📈 Trending Up' if improvement_rate > 0 else '📉 Needs Attention'}
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        consistency = filtered_df['probability'].std()
        st.markdown(f"""
        <div class="insight-box">
            <span style="color:#00ff9d; font-size:18px;">📊 Consistency</span><br>
            <span style="color: white;">Score Std Dev: {consistency:.1f}</span><br>
            <span style="color: {'#00ff9d' if consistency < 15 else '#ffbb33' if consistency < 25 else '#ff4444'};">
                {'✨ Very Consistent' if consistency < 15 else '⚡ Moderately Variable' if consistency < 25 else '⚠️ Highly Variable'}
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        if 'risk' in filtered_df.columns:
            risk_dist = filtered_df['risk'].value_counts()
            primary_risk = risk_dist.index[0] if len(risk_dist) > 0 else "Unknown"
            st.markdown(f"""
            <div class="insight-box">
                <span style="color:#00ff9d; font-size:18px;">⚠️ Primary Risk</span><br>
                <span style="color: white;">{primary_risk}</span><br>
                <span style="color: {'#00ff9d' if primary_risk == 'Low Risk' else '#ffbb33' if primary_risk == 'Medium Risk' else '#ff4444'};">
                    {risk_dist.get('Low Risk', 0)} Low | {risk_dist.get('Medium Risk', 0)} Medium | {risk_dist.get('High Risk', 0)} High
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Recommendations
    st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Smart Recommendations")
    
    recommendations = []
    
    if avg_score < 60:
        recommendations.append("🔴 **Critical**: Your average score is below 60%. Focus on improving fundamental skills.")
    elif avg_score < 75:
        recommendations.append("🟡 **Good**: You're doing well! Focus on consistency to reach the next level.")
    else:
        recommendations.append("🟢 **Excellent**: You're performing great! Consider exploring advanced topics.")
    
    if 'improvement_rate' in locals() and improvement_rate < 0:
        recommendations.append("📉 **Trend Alert**: Your scores are declining. Review your recent strategies.")
    
    if 'consistency' in locals() and consistency > 20:
        recommendations.append("🎯 **Consistency**: Work on maintaining steady performance across all areas.")
    
    if 'domain' in filtered_df.columns:
        weakest_domain = filtered_df.groupby('domain')['probability'].mean().idxmin()
        recommendations.append(f"💪 **Focus Area**: Consider improving in {weakest_domain} domain.")
    
    for rec in recommendations:
        st.markdown(f'<div class="insight-box">{rec}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Back button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()