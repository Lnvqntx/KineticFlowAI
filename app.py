import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random

# Page config
st.set_page_config(
    page_title="Kinetic Flow AI - Demo",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); }
    .stButton>button {
        background: linear-gradient(135deg, #00ff9d, #00b8ff);
        color: black; font-weight: bold;
        border: none; border-radius: 25px;
        padding: 12px 30px; font-size: 16px;
    }
    h1, h2, h3 { color: #00ff9d; }
    .metric-card {
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        padding: 20px; border-radius: 15px;
        border: 1px solid rgba(0, 255, 157, 0.2);
        margin: 10px 0;
    }
    .chat-message { padding: 15px; border-radius: 10px; margin: 10px 0; }
    .user-message { background: rgba(0,184,255,0.2); border-left: 4px solid #00b8ff; }
    .bot-message { background: rgba(0,255,157,0.2); border-left: 4px solid #00ff9d; }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Kinetic Flow AI")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🤖 Try AI Agent", "📊 Dashboard Preview", "📅 Book Audit"],
    key="page"
)
st.sidebar.markdown("---")
st.sidebar.info("**Demo Version** — Client Presentation Build")

# Session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'lead_captured' not in st.session_state:
    st.session_state.lead_captured = False

########################################
# HOME PAGE
########################################
if page == "🏠 Home":
    st.markdown("<h1 style='text-align:center; font-size:3.5em;'>⚙️ KINETIC FLOW AI</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#ccc;'>Turning Chaos Into Intelligent Flow</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='text-align:center; font-size:3em;'>24/7</h2>
            <p style='text-align:center; color:#aaa;'>AI Operations</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='text-align:center; font-size:3em; color:#00b8ff;'>4:1</h2>
            <p style='text-align:center; color:#aaa;'>Avg ROI (Internal)</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='text-align:center; font-size:3em; color:#ff00ff;'>80%</h2>
            <p style='text-align:center; color:#aaa;'>Task Reduction</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Try Agent button
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        if st.button("🤖 Try Our AI Agent Demo →", use_container_width=True):
            st.session_state.page = "🤖 Try AI Agent"
            st.experimental_rerun()

########################################
# AI AGENT DEMO
########################################
elif page == "🤖 Try AI Agent":
    st.title("🤖 Frontier AI Agent Demo")
    st.info("Ask about pricing, availability, booking, or services.")

    responses = {
        "pricing": "Our services typically range from $1,500-$3,000...",
        "cost": "Setup ranges from $1,500-$3,000 with $399-$699/mo...",
        "book": "I'd love to get you scheduled — Tuesday 2 PM or Thursday 10 AM?",
        "appointment": "We have openings Tuesday 2 PM, Thursday 10 AM, Friday 3 PM...",
        "availability": "We’re booking audits this week: Tue 2 PM, Thu 10 AM...",
        "insurance": "Our AI agent can handle insurance verification automatically...",
        "how": "Our agent works 24/7 capturing leads and booking appointments...",
        "demo": "You're using a simplified demo — full version integrates with CRM...",
        "roi": "Clients typically see strong ROI from automation...",
        "default": "Great question! Our Frontier Agent can assist with that — want to book an audit?"
    }

    # show history
    for m in st.session_state.chat_history:
        cls = 'user-message' if m['role']=='user' else 'bot-message'
        label = "You" if m['role']=='user' else "Frontier Agent"
        st.markdown(f"<div class='chat-message {cls}'><strong>{label}:</strong> {m['content']}</div>", unsafe_allow_html=True)

    # input form
    with st.form("chat_form"):
        user_input = st.text_input("Type your message:")
        send = st.form_submit_button("Send 📤")

    if send and user_input:
        ul = user_input.lower()
        st.session_state.chat_history.append({"role":"user", "content":user_input})

        matched = None
        for key in ["book","appointment","pricing","availability","insurance","how","demo"]:
            if key in ul:
                matched = key
                break
        response = responses.get(matched, responses["default"])

        # booking capture
        if any(w in ul for w in ["book","schedule","appointment","yes","sure"]):
            if not st.session_state.lead_captured:
                response += "

✅ Lead captured — confirmation will be sent."
                st.session_state.lead_captured = True

        st.session_state.chat_history.append({"role":"bot", "content":response})
        st.experimental_rerun()

    if st.session_state.lead_captured:
        st.success("🎉 Lead captured! This would sync to CRM & calendar in production.")

########################################
# DASHBOARD
########################################
elif page == "📊 Dashboard Preview":
    st.title("📊 Client Dashboard Preview")

    dates = pd.date_range(end=datetime.now(), periods=30)
    leads_data = [random.randint(5,20) for _ in range(30)]
    bookings = [int(l * random.uniform(0.15,0.25)) for l in leads_data]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Leads (30d)", sum(leads_data))
    col2.metric("Bookings", sum(bookings))
    conv = round((sum(bookings)/sum(leads_data))*100,1)
    col3.metric("Conversion", f"{conv}%")
    col4.metric("Avg Response", "8 sec")

    st.markdown("---")

    c1, c2 = st.columns(2)

    # leads chart
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=leads_data, mode="lines+markers", line=dict(color="#00ff9d")))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
        st.subheader("📈 Leads Over Time")
        st.plotly_chart(fig, use_container_width=True)

    # funnel
    with c2:
        funnel = go.Figure(go.Funnel(y=["Leads","Conversations","Qualified","Booked"], x=[sum(leads_data), int(sum(leads_data)*0.8), int(sum(leads_data)*0.4), sum(bookings)], marker=dict(color=["#00ff9d","#00b8ff","#8b5cf6","#ff6b6b"])) )
