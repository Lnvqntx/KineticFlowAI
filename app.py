import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import random
import csv
import os

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="Kinetic Flow AI - Demo",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# Custom CSS
# -----------------------
st.markdown(
    """
    <style>
        .main { background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); padding: 20px; }
        .stButton>button {
            background: linear-gradient(135deg, #00ff9d, #00b8ff);
            color: black; font-weight: bold;
            border: none; border-radius: 25px;
            padding: 12px 30px; font-size: 16px;
        }
        .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 10px 40px rgba(0,255,157,0.3); }
        h1, h2, h3 { color: #00ff9d; }
        .metric-card {
            background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
            padding: 20px; border-radius: 15px;
            border: 1px solid rgba(0, 255, 157, 0.12);
            margin: 10px 0;
        }
        .chat-message { padding: 15px; border-radius: 10px; margin: 10px 0; color: #fff; }
        .user-message { background: rgba(0,184,255,0.12); border-left: 4px solid #00b8ff; }
        .bot-message { background: rgba(0,255,157,0.12); border-left: 4px solid #00ff9d; }
        .small-muted { color: #aaa; font-size: 0.9em; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------
# Sidebar navigation
# -----------------------
st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.title("⚙️ Kinetic Flow AI")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🤖 Try AI Agent", "📊 Dashboard Preview", "📅 Book Audit"],
    key="page",
)
st.sidebar.markdown("---")
st.sidebar.info("**Demo Version** — Client presentation")

# -----------------------
# Session state init
# -----------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "lead_captured" not in st.session_state:
    st.session_state.lead_captured = False

# Optional: demo persistence file for leads (keeps leads between app reloads in the same deployment)
LEADS_FILE = "demo_leads.csv"


def save_demo_lead(name: str, email: str, phone: str, message: str):
    """Append lead to a local CSV (demo only). For production use a DB or Airtable/Sheets."""
    header = ["timestamp", "name", "email", "phone", "message"]
    exists = os.path.exists(LEADS_FILE)
    try:
        with open(LEADS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(header)
            writer.writerow([datetime.utcnow().isoformat(), name, email, phone, message])
    except Exception:
        # do not break the demo if file writing fails
        pass


# -----------------------
# HOME PAGE
# -----------------------
if page == "🏠 Home":
    st.markdown("<h1 style='text-align:center; font-size:3.2em;'>⚙️ KINETIC FLOW AI</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:#cccccc;'>Turning Chaos Into Intelligent Flow</h3>", unsafe_allow_html=True)
    st.write("")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class='metric-card'>
                <h2 style='text-align:center; font-size:2.6em;'>24/7</h2>
                <p style='text-align:center; color:#aaa;'>AI Operations</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='metric-card'>
                <h2 style='text-align:center; font-size:2.6em; color:#00b8ff;'>4:1</h2>
                <p style='text-align:center; color:#aaa;'>Avg ROI (internal)</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class='metric-card'>
                <h2 style='text-align:center; font-size:2.6em; color:#ff6b6b;'>80%</h2>
                <p style='text-align:center; color:#aaa;'>Task Reduction</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown(
        """
        ## 🚀 What We Do

        Kinetic Flow AI builds **autonomous AI agents** that work as digital teammates for your business.

        ✅ **24/7 Lead Capture** – Never miss another opportunity  
        ✅ **Intelligent Conversations** – Answer questions & handle objections  
        ✅ **Automatic Booking** – Schedule appointments while you sleep  
        ✅ **Smart Follow-ups** – Keep leads warm automatically

        ---
        """,
        unsafe_allow_html=True,
    )

    # Centered CTA button that switches the page
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("🤖 Try Our AI Agent Demo →", use_container_width=True):
            st.session_state.page = "🤖 Try AI Agent"
            st.experimental_rerun()

# -----------------------
# AI AGENT DEMO PAGE
# -----------------------
elif page == "🤖 Try AI Agent":
    st.title("🤖 Frontier AI Agent Demo")
    st.info("Demo mode — try asking about pricing, booking, or availability.")

    # canned responses
    responses = {
        "pricing": "Our services typically range from $1,500–$3,000 for initial setup, plus $399–$699/month for ongoing management. Exact price depends on scope.",
        "book": "Excellent — we can schedule a free 30-minute Kinetic Audit. Options: Tuesday 2 PM, Thursday 10 AM, Friday 3 PM. Which works?",
        "appointment": "We have openings Tuesday 2 PM, Thursday 10 AM, and Friday 3 PM. Which do you prefer?",
        "availability": "We’re currently booking audits this week and next. I can check availability for you.",
        "insurance": "Our agent can handle insurance verification questions if you provide policy details — it automates the common checks.",
        "how": "The agent integrates with your calendar and CRM and handles lead capture, booking, and confirmations 24/7.",
        "demo": "This is a simplified demo. The production agent syncs to your systems and sends real confirmations.",
        "roi": "Clients typically see strong ROI from automation — we'll discuss your specific numbers in the audit.",
        "default": "Great question! Our Frontier Agent can help. Would you like to book a free Kinetic Audit to discuss your needs?"
    }

    # Display chat history
    for msg in st.session_state.chat_history:
        css_class = "user-message" if msg["role"] == "user" else "bot-message"
        label = "You" if msg["role"] == "user" else "Frontier Agent"
        st.markdown(
            f"<div class='chat-message {css_class}'><strong>{label}:</strong> {msg['content']}</div>",
            unsafe_allow_html=True,
        )

    # Chat input as a form to avoid double-submit issues
    with st.form("chat_form"):
        user_input = st.text_input("Type your question here:", placeholder="e.g., What's your pricing? Can I book an appointment?")
        send = st.form_submit_button("Send 📤")
        clear = st.form_submit_button("Clear Chat")

    if clear:
        st.session_state.chat_history = []
        st.session_state.lead_captured = False
        st.experimental_rerun()

    if send and user_input:
        # add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        lower = user_input.lower()

        # simple prioritized matching
        matched = None
        for key in ["book", "appointment", "pricing", "availability", "insurance", "how", "demo"]:
            if f"{key}" in lower:
                matched = key
                break

        bot_response = responses.get(matched, responses["default"])

        # booking capture demo
        if any(w in lower for w in ["book", "schedule", "appointment", "yes", "sure"]):
            if not st.session_state.lead_captured:
                bot_response += "\n\n✅ Lead captured! We'll send a confirmation email and calendar invite (demo)."
                st.session_state.lead_captured = True

        st.session_state.chat_history.append({"role": "bot", "content": bot_response})
        st.experimental_rerun()

    if st.session_state.lead_captured:
        st.success("🎉 Lead captured! (Demo mode — in production this syncs to your CRM & calendar.)")

# -----------------------
# DASHBOARD PREVIEW
# -----------------------
elif page == "📊 Dashboard Preview":
    st.title("📊 Client Dashboard Preview (Sample Data)")
    # sample data
    dates = pd.date_range(end=datetime.now(), periods=30)
    leads = [random.randint(6, 20) for _ in range(30)]
    bookings = [int(l * random.uniform(0.15, 0.25)) for l in leads]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Leads (30d)", sum(leads))
    c2.metric("Bookings", sum(bookings))
    conv_rate = round((sum(bookings) / sum(leads)) * 100, 1)
    c3.metric("Conversion Rate", f"{conv_rate}%")
    c4.metric("Avg Response Time", "8s")

    st.markdown("---")

    lcol, rcol = st.columns(2)
    with lcol:
        st.subheader("📈 Leads Captured Over Time")
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=dates, y=leads, mode="lines+markers", name="Leads", line=dict(color="#00ff9d", width=3))
        )
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"), height=420)
        st.plotly_chart(fig, use_container_width=True)

    with rcol:
        st.subheader("🎯 Conversion Funnel")
        funnel_counts = [sum(leads), int(sum(leads) * 0.8), int(sum(leads) * 0.4), sum(bookings)]
        funnel = go.Figure(go.Funnel(y=["Leads", "Conversations", "Qualified", "Booked"], x=funnel_counts, marker=dict(color=["#00ff9d", "#00b8ff", "#8b5cf6", "#ff6b6b"])))
        funnel.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"), height=420)
        st.plotly_chart(funnel, use_container_width=True)

    st.markdown("---")
    st.info("Note: sample data only. Production dashboard connects to your agent metrics & CRM.")

# -----------------------
# BOOK AUDIT PAGE
# -----------------------
elif page == "📅 Book Audit":
    st.title("📅 Book Your Free Kinetic Audit")
    st.markdown("30-minute session to analyze your workflows and show how automation helps.")

    left, right = st.columns([2, 1])
    with left:
        st.subheader("What you'll get:")
        st.markdown(
            """
            - Process analysis & bottleneck identification  
            - Custom roadmap to automation & AI agents  
            - Live demo & ROI discussion (private)  
            - No-obligation audit
            """
        )

        with st.form("contact_form"):
            name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
            phone = st.text_input("Phone Number")
            company = st.text_input("Company (optional)")
            industry = st.selectbox("Industry", ["Select...", "Dental / Medical", "Legal", "Home Services", "Consulting", "Real Estate", "Other"])
            message = st.text_area("Briefly describe your biggest challenge")

            submitted = st.form_submit_button("📅 Submit & Schedule")
            if submitted:
                if name and email:
                    # demo: save to CSV (not secure for production)
                    save_demo_lead(name, email, phone, message or "")
                    st.success("🎉 Form submitted! We'll contact you within 24 hours to schedule.")
                    st.balloons()
                else:
                    st.error("Please fill in at least name and email.")

    with right:
        st.subheader("Contact")
        st.markdown(
            """
            **Lochan - CEO**  
            📧 contact@kineticflow.ai  
            📱 Instagram: @kineticflow.ai

            --- 

            **Availability**  
            Tue: 2 PM - 6 PM IST  
            Thu: 10 AM - 6 PM IST  
            Fri: 3 PM - 7 PM IST
            """,
            unsafe_allow_html=True,
        )

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:#888; padding:14px 0;'>
        <strong>Kinetic Flow AI</strong> | Turning Chaos Into Intelligent Flow &nbsp; • &nbsp;
        <span class='small-muted'>Demo presentation only</span>
    </div>
    """,
    unsafe_allow_html=True,
)
