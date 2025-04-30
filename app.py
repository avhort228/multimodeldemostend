import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI for Personalized Marketing",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Application header
st.title("🤖 AI for Real-Time Personalized Marketing")

# Content
st.header("Problem:")
st.write("""
- 🚀 Marketers manually segment audiences for weeks
- ✅ Only 2–3 hypotheses tested instead of hundreds
- ❌ Customers receive irrelevant offers
- 💸 ML solutions are complex and expensive
- 📉 Result: low conversion, high CAC, wasted budget
""")

st.header("Our Solution:")
st.write("""
- 📈 Real-time personalization
- 🔄 Automated hypothesis testing
- 🔗 Simple REST API
- 👥 No ML team required
""")

st.header("For:")
st.write("""
- 👨‍💼 Marketing teams
- 👩‍💻 CRM specialists
- 👨‍🔧 Developers
""")

st.header("Results:")
st.write("""
- 📊 +30–50% conversion uplift
- 💰 –20% CAC
- 🚀 ROI growth from month one
""")

# Call to action
st.button("Request a demo")