import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
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
    .main {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
    }
    .stButton>button {
        background: linear-gradient(135deg, #00ff9d, #00b8ff);
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 16px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 40px rgba(0, 255, 157, 0.5);
    }
    h1, h2, h3 {
        color: #00ff9d;
    }
    .metric-card {
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 255, 157, 0.2);
        margin: 10px 0;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .user-message {
        background: rgba(0, 184, 255, 0.2);
        border-left: 4px solid #00b8ff;
    }
    .bot-message {
        background: rgba(0, 255, 157, 0.2);
        border-left: 4px solid #00ff9d;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("⚙️ Kinetic Flow AI")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🤖 Try AI Agent", "📊 Dashboard Preview", "💰 ROI Calculator", "📅 Book Audit"]
)
st.sidebar.markdown("---")
st.sidebar.info("**Demo Version**\nExperience the future of business automation")

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'lead_captured' not in st.session_state:
    st.session_state.lead_captured = False

# HOME PAGE
if page == "🏠 Home":
    st.markdown("<h1 style='text-align: center; font-size: 3.5em;'>⚙️ KINETIC FLOW AI</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #cccccc;'>Turning Chaos Into Intelligent Flow</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='text-align: center; font-size: 3em; color: #00ff9d;'>24/7</h2>
            <p style='text-align: center; color: #aaa;'>AI Operations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='text-align: center; font-size: 3em; color: #00b8ff;'>4:1</h2>
            <p style='text-align: center; color: #aaa;'>ROI Average</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h2 style='text-align: center; font-size: 3em; color: #ff00ff;'>80%</h2>
            <p style='text-align: center; color: #aaa;'>Task Reduction</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    ## 🚀 What We Do
    
    Kinetic Flow AI builds **autonomous AI agents** that work as digital teammates for your business.
    
    ### Our Solution:
    
    ✅ **24/7 Lead Capture** - Never miss another opportunity  
    ✅ **Intelligent Conversations** - Answer questions, handle objections  
    ✅ **Automatic Booking** - Schedule appointments while you sleep  
    ✅ **Smart Follow-ups** - Keep leads warm automatically  
    ✅ **Real Results** - 4:1 ROI in 90 days  
    
    ### The Process:
    
    🔍 **Kinetic Audit** - 2-hour diagnostic to identify bottlenecks  
    ⚡ **Bespoke Implementation** - Custom AI agents built for you  
    🔄 **Managed Flow Retainer** - Continuous optimization & support  
    
    ---
    
    ### 🎯 Perfect For:
    - Dentists, Doctors, Clinics
    - Lawyers & Law Firms
    - Contractors & Home Services
    - Consultants & Agencies
    - Any business losing leads after hours
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🤖 Try Our AI Agent Demo →", use_container_width=True):
            st.switch_page
            st.info("Click '🤖 Try AI Agent' in the sidebar to test it!")

# AI AGENT DEMO PAGE
elif page == "🤖 Try AI Agent":
    st.title("🤖 Frontier AI Agent Demo")
    st.markdown("Experience how our AI agent handles real customer conversations")
    
    st.info("💡 **Demo Mode**: Try asking about pricing, availability, or booking an appointment!")
    
    # Pre-defined responses for demo
    responses = {
        "pricing": "Great question! Our services typically range from $1,500-$3,000 for initial setup, plus $399-$699/month for ongoing management. The exact price depends on your specific needs. Would you like me to check available time slots for a free Kinetic Audit where we can discuss your exact requirements?",
        "cost": "Our pricing is designed to deliver 4:1 ROI. Initial implementation is $1,500-$3,000, with monthly retainers from $399-$699. Most clients see positive ROI within 3 months. Would you like to schedule a call to discuss your specific situation?",
        "book": "Excellent! I'd love to get you scheduled. We offer free 30-minute Kinetic Audits where we analyze your business and show exactly how automation can help. Would Tuesday at 2 PM or Thursday at 10 AM work better for you?",
        "appointment": "Perfect timing! I can schedule you for a free Kinetic Audit. We have availability this week on Tuesday at 2 PM, Thursday at 10 AM, or Friday at 3 PM. Which works best for your schedule?",
        "availability": "We're currently booking Kinetic Audits for this week and next. I have openings on Tuesday 2 PM, Thursday 10 AM, and Friday 3 PM. Would any of these times work for you?",
        "insurance": "For service-based businesses, our AI agents can handle insurance verification questions from your clients. The agent learns your specific insurance policies and can provide instant answers 24/7. Would you like to see how this works for your business?",
        "how": "Our Frontier Agent works 24/7 to capture leads, answer questions, and book appointments automatically. It integrates with your calendar, CRM, and messaging platforms. Leads get instant responses even at 2 AM, and you wake up to booked appointments. Want to see it in action for your business?",
        "demo": "You're experiencing it right now! This is a simplified version of what our full Frontier Agent can do. The production version connects to your actual calendar, CRM, and has deep knowledge of your specific business. Impressive, right? Want to discuss implementing this for your business?",
        "roi": "Our average client sees 4:1 ROI within 90 days. That means for every $1 invested, you get $4 back. This comes from: never missing after-hours leads (30-40% revenue increase), reducing staff time on repetitive tasks (save 15+ hours/week), and increasing conversion rates (20% of chats become bookings). Want me to calculate your specific ROI potential?",
        "default": "That's a great question! Our Frontier AI Agent can help with that and much more. We specialize in 24/7 lead capture, intelligent conversations, and automatic booking. The best way to see how it fits your specific needs is through a free Kinetic Audit. Would you like to schedule one?"
    }
    
    # Chat interface
    st.markdown("---")
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"<div class='chat-message user-message'>👤 <strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message bot-message'>🤖 <strong>Frontier Agent:</strong> {message['content']}</div>", unsafe_allow_html=True)
    
    # User input
    user_input = st.text_input("Type your question here:", key="user_input", placeholder="e.g., What's your pricing? Can I book an appointment?")
    
    col1, col2 = st.columns([1, 5])
    with col1:
        send_button = st.button("Send 📤")
    with col2:
        if st.button("🔄 Clear Chat"):
            st.session_state.chat_history = []
            st.session_state.lead_captured = False
            st.rerun()
    
    if send_button and user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Determine response
        user_lower = user_input.lower()
        response = responses["default"]
        
        for key in responses:
            if key in user_lower:
                response = responses[key]
                break
        
        # Check if this is a booking
        if any(word in user_lower for word in ["book", "schedule", "appointment", "tuesday", "thursday", "friday", "yes", "sure"]):
            if not st.session_state.lead_captured:
                response += "\n\n✅ **Lead Captured!** I've added you to our calendar. You'll receive a confirmation email shortly with meeting details and a calendar invite."
                st.session_state.lead_captured = True
        
        # Add bot response
        st.session_state.chat_history.append({"role": "bot", "content": response})
        st.rerun()
    
    if st.session_state.lead_captured:
        st.success("🎉 **Success!** This lead would now be in your CRM with full conversation history, automatically added to your calendar, and sent confirmation via email/SMS.")
        
        st.markdown("---")
        st.markdown("### 📊 What Just Happened:")
        st.markdown("""
        1. ✅ Lead engaged in real-time conversation
        2. ✅ Questions answered automatically
        3. ✅ Appointment booked without human intervention
        4. ✅ Lead added to CRM with conversation history
        5. ✅ Confirmation sent via email/SMS
        6. ✅ Calendar event created automatically
        
        **All in under 2 minutes. At 2 AM. While you sleep.**
        """)

# DASHBOARD PREVIEW
elif page == "📊 Dashboard Preview":
    st.title("📊 Client Dashboard Preview")
    st.markdown("This is what you'll see when managing your AI agent")
    
    # Generate sample data
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    leads_data = [random.randint(5, 20) for _ in range(30)]
    bookings_data = [int(leads * random.uniform(0.15, 0.25)) for leads in leads_data]
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Leads (30 days)", sum(leads_data), "+12%")
    with col2:
        st.metric("Bookings Made", sum(bookings_data), "+18%")
    with col3:
        conversion = round((sum(bookings_data) / sum(leads_data)) * 100, 1)
        st.metric("Conversion Rate", f"{conversion}%", "+3.2%")
    with col4:
        st.metric("Avg Response Time", "8 seconds", "-45 sec")
    
    # Charts
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Leads Captured Over Time")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates, y=leads_data,
            mode='lines+markers',
            name='Leads',
            line=dict(color='#00ff9d', width=3),
            marker=dict(size=8)
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Conversion Funnel")
        funnel_data = {
            'Stage': ['Leads Captured', 'Conversations', 'Qualified', 'Booked'],
            'Count': [sum(leads_data), int(sum(leads_data)*0.8), int(sum(leads_data)*0.4), sum(bookings_data)]
        }
        fig = go.Figure(go.Funnel(
            y=funnel_data['Stage'],
            x=funnel_data['Count'],
            marker=dict(color=['#00ff9d', '#00b8ff', '#8b5cf6', '#ff6b6b'])
        ))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance metrics
    st.markdown("---")
    st.subheader("⚡ Real-Time Performance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>Response Time</h3>
            <h2 style='color: #00ff9d;'>8 seconds</h2>
            <p>Average time to first response</p>
            <small style='color: #00ff9d;'>↓ 45 seconds from last month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>Active Hours</h3>
            <h2 style='color: #00b8ff;'>24/7</h2>
            <p>Agent availability</p>
            <small style='color: #00b8ff;'>100% uptime this month</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>Satisfaction</h3>
            <h2 style='color: #8b5cf6;'>4.8/5.0</h2>
            <p>Lead satisfaction score</p>
            <small style='color: #8b5cf6;'>Based on 247 interactions</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 **Note**: This is sample data. Your actual dashboard will show real-time metrics from your AI agent.")

# ROI CALCULATOR
elif page == "💰 ROI Calculator":
    st.title("💰 ROI Calculator")
    st.markdown("See your potential return on investment with Kinetic Flow AI")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Your Current Situation")
        
        monthly_leads = st.number_input("Monthly leads received", min_value=10, max_value=1000, value=100, step=10)
        current_conversion = st.slider("Current conversion rate (%)", min_value=5, max_value=50, value=15)
        avg_deal_value = st.number_input("Average deal value ($)", min_value=100, max_value=50000, value=1500, step=100)
        after_hours_leads = st.slider("Leads that come after hours (%)", min_value=10, max_value=60, value=35)
        
    with col2:
        st.subheader("🚀 With Kinetic Flow AI")
        
        # Calculations
        current_monthly_revenue = monthly_leads * (current_conversion/100) * avg_deal_value
        
        # AI improvements
        missed_leads_captured = monthly_leads * (after_hours_leads/100)
        improved_conversion = current_conversion + 5  # AI typically improves by 5%
        total_leads_with_ai = monthly_leads + missed_leads_captured
        new_monthly_revenue = total_leads_with_ai * (improved_conversion/100) * avg_deal_value
        
        additional_revenue = new_monthly_revenue - current_monthly_revenue
        annual_additional = additional_revenue * 12
        
        ai_cost_monthly = 599  # Average retainer
        ai_cost_annual = ai_cost_monthly * 12 + 2000  # Include setup
        
        roi = ((annual_additional - ai_cost_annual) / ai_cost_annual) * 100
        payback_months = ai_cost_annual / additional_revenue if additional_revenue > 0 else 0
        
        st.metric("Leads captured", f"+{int(missed_leads_captured)}/month", "After-hours leads saved")
        st.metric("New conversion rate", f"{improved_conversion}%", f"+{improved_conversion-current_conversion}%")
        st.metric("New monthly revenue", f"${int(new_monthly_revenue):,}", f"+${int(additional_revenue):,}")
    
    st.markdown("---")
    
    # Results
    st.subheader("📈 Your Projected Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>Additional Monthly Revenue</h3>
            <h2 style='color: #00ff9d;'>${int(additional_revenue):,}</h2>
            <p>From captured after-hours leads</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>Annual ROI</h3>
            <h2 style='color: #00b8ff;'>{int(roi)}%</h2>
            <p>Return on investment</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>Payback Period</h3>
            <h2 style='color: #8b5cf6;'>{payback_months:.1f} months</h2>
            <p>Time to break even</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed breakdown
    st.subheader("💡 Detailed Financial Breakdown")
    
    breakdown_data = {
        "Metric": [
            "Current Monthly Revenue",
            "Additional Monthly Revenue",
            "New Monthly Revenue",
            "Annual Additional Revenue",
            "Kinetic Flow AI Cost (Year 1)",
            "Net Profit (Year 1)",
            "ROI %"
        ],
        "Value": [
            f"${int(current_monthly_revenue):,}",
            f"${int(additional_revenue):,}",
            f"${int(new_monthly_revenue):,}",
            f"${int(annual_additional):,}",
            f"${int(ai_cost_annual):,}",
            f"${int(annual_additional - ai_cost_annual):,}",
            f"{int(roi)}%"
        ]
    }
    
    st.table(pd.DataFrame(breakdown_data))
    
    st.success(f"💰 **Bottom Line**: Invest ${int(ai_cost_annual):,} in Year 1, gain ${int(annual_additional):,} in additional revenue. That's ${int(annual_additional - ai_cost_annual):,} in net profit!")
    
    st.markdown("---")
    
    if st.button("📅 Book Free Kinetic Audit to Discuss These Numbers"):
        st.info("Navigate to '📅 Book Audit' in the sidebar to schedule!")

# BOOK AUDIT PAGE
elif page == "📅 Book Audit":
    st.title("📅 Book Your Free Kinetic Audit")
    st.markdown("30-minute session to analyze your business and show exactly how AI can help")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("What You'll Get:")
        st.markdown("""
        ✅ **Process Analysis** - We'll map your current workflows  
        ✅ **Bottleneck Identification** - Find where you're losing time/money  
        ✅ **Custom Roadmap** - Specific AI solutions for your business  
        ✅ **ROI Projections** - Exact numbers for your situation  
        ✅ **Live Demo** - See the AI agent in action  
        ✅ **No Obligation** - Zero pressure, just insights  
        
        ---
        
        ### 📝 Contact Form
        """)
        
        with st.form("contact_form"):
            name = st.text_input("Full Name *")
            email = st.text_input("Email Address *")
            phone = st.text_input("Phone Number")
            company = st.text_input("Company Name")
            industry = st.selectbox("Industry", [
                "Select...",
                "Dental / Medical",
                "Legal Services",
                "Home Services / Contractors",
                "Consulting",
                "Real Estate",
                "Other"
            ])
            message = st.text_area("Tell us about your biggest business challenge")
            
            submitted = st.form_submit_button("📅 Submit & Schedule")
            
            if submitted:
                if name and email:
                    st.success("🎉 **Form Submitted!** We'll contact you within 24 hours to schedule your Kinetic Audit.")
                    st.balloons()
                    st.info("💡 **Next Steps**: Check your email for confirmation and calendar invite options.")
                else:
                    st.error("Please fill in at least your name and email")
    
    with col2:
        st.subheader("📞 Direct Contact")
        st.markdown("""
        **Lochan - CEO**  
        📧 Email: lochan@kineticflow.ai  
        📱 WhatsApp: [Your Number]
        
        **Kaila - AI Architect**  
        📧 Email: kaila@kineticflow.ai
        
        ---
        
        ### 🕐 Availability
        
        **Tuesday**: 2 PM - 6 PM IST  
        **Thursday**: 10 AM - 6 PM IST  
        **Friday**: 3 PM - 7 PM IST  
        
        ---
        
        ### 💬 Prefer to Chat?
        
        DM us on Instagram:  
        [@kineticflow.ai](https://instagram.com/kineticflow.ai)
        
        ---
        
        ### ⚡ Quick Response
        
        Average response time:  
        **< 2 hours** during business hours
        """)
        
        st.markdown("---")
        
        st.markdown("""
        <div class='metric-card' style='background: linear-gradient(135deg, #00ff9d, #00b8ff); color: black;'>
            <h4>🔥 Limited Spots</h4>
            <p><strong>Only 5 audits available this month</strong></p>
            <p>We limit our client intake to ensure quality delivery</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Kinetic Flow AI</strong> | Turning Chaos Into Intelligent Flow</p>
    <p>📧 contact@kineticflow.ai | 🌐 kineticflow.ai | 📱 @kineticflow.ai</p>
    <p><em>Demo Version - Built for prospect presentation</em></p>
</div>
""", unsafe_allow_html=True)
