import streamlit as st

# Установка страницы
st.set_page_config(page_title="AI for Personalized Marketing", layout="centered")

# Стили
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
        margin: 0;
        padding: 0;
        line-height: 1.6;
        color: #000; /* Черный шрифт */
    }
    .main {
        max-width: 800px;
        margin: 40px auto;
        padding: 40px;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    h1 {
        font-size: 2.5em;
        color: #000; /* Черный шрифт */
    }
    h2 {
        font-size: 1.8em;
        color: #000; /* Черный шрифт */
    }
    ul {
        list-style-type: none;
        padding: 0;
        text-align: left;
        margin: 0 auto;
        max-width: 600px;
    }
    li {
        margin-bottom: 15px;
        padding-left: 25px;
        position: relative;
    }
    li:before {
        content: "–";
        position: absolute;
        left: 0;
        color: #007BFF;
    }
    button {
        padding: 12px 25px;
        font-size: 1.1em;
        color: #fff;
        background-color: #007BFF;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        margin-top: 30px;
        transition: background-color 0.3s, transform 0.3s;
    }
    button:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Контент
st.markdown("""
<div class="main">
    <h1>🤖 AI for real-time personalized marketing</h1>
    <h2>Problem:</h2>
    <ul>
        <li>🚀 Marketers manually segment audiences for weeks</li>
        <li>✅ Only 2–3 hypotheses tested instead of hundreds</li>
        <li>❌ Customers receive irrelevant offers</li>
        <li>💸 ML solutions are complex and expensive</li>
        <li>📉 Result: low conversion, high CAC, wasted budget</li>
    </ul>
    <h2>Our solution:</h2>
    <ul>
        <li>📈 Real-time personalization</li>
        <li>🔄 Automated hypothesis testing</li>
        <li>🔗 Simple REST API</li>
        <li>👥 No ML team required</li>
    </ul>
    <h2>For:</h2>
    <ul>
        <li>👨‍💼 Marketing teams</li>
        <li>👩‍💻 CRM specialists</li>
        <li>👨‍🔧 Developers</li>
    </ul>
    <h2>Results:</h2>
    <ul>
        <li>📊 +30–50% conversion uplift</li>
        <li>💰 –20% CAC</li>
        <li>🚀 ROI growth from month one</li>
    </ul>
    <button>Request a demo</button>
</div>
""", unsafe_allow_html=True)