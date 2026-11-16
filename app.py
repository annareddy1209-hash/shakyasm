import streamlit as st

# Configure the Streamlit page to look sleek and mobile-friendly
st.set_page_config(
    page_title="Your Brand Name | Sports & Gaming Platform",
    page_icon="⚡",
    layout="centered"
)

# Custom Styling to match your dark/gold theme
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0e14;
        color: #f3f4f6;
    }
    .gold-gradient {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        padding: 12px 24px;
        border-radius: 12px;
        color: black;
        text-align: center;
        font-weight: bold;
        text-decoration: none;
        display: block;
    }
    .gold-text {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    .card {
        background-color: #131824;
        border: 1px solid #1f2937;
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header / Hero Section
st.markdown("<p style='text-align:center; color:#fbbf24; font-size:14px; font-weight:600;'>🔥 24/7 INSTANT SUPPORT & FAST ACCESS</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>India's Trusted Online <span class='gold-text'>Sports & Gaming</span> Experience</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Experience seamless navigation, instant account setup, and round-the-clock customer assistance on a fast mobile platform.</p>", unsafe_allow_html=True)

st.write("")

# WhatsApp CTA Button
st.markdown("""
    <a href="https://wa.me/1234567890" target="_blank" class="gold-gradient">
        💬 Create Instant ID on WhatsApp
    </a>
""", unsafe_allow_html=True)

st.write("---")

# Categories Section
st.markdown("### 🏆 Popular Categories")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class="card">
            <h4>🏏 Cricket Action</h4>
            <p style='color: #9ca3af; font-size: 13px;'>Live match updates, tournaments, and leagues.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <h4>🃏 Live Card Rooms</h4>
            <p style='color: #9ca3af; font-size: 13px;'>Interactive real-time tables with smooth streaming.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h4>⚽ Football Leagues</h4>
            <p style='color: #9ca3af; font-size: 13px;'>Coverage across top European clubs and cups.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <h4>⚡ Instant Games</h4>
            <p style='color: #9ca3af; font-size: 13px;'>Quick-play arcade games built for mobile.</p>
        </div>
    """, unsafe_allow_html=True)

# How It Works
st.markdown("### 🚀 Get Started in 3 Simple Steps")
st.markdown("""
<div class="card">
    <p><b>1. Click WhatsApp:</b> Tap the button above to start a direct chat.</p>
    <p><b>2. Receive Credentials:</b> Our support team will issue your secure login details.</p>
    <p><b>3. Log In & Explore:</b> Sign in from any mobile browser and enjoy 24/7 support.</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #6b7280; font-size: 12px; margin-top: 40px;'>18+ Only. Please play responsibly. © 2026 YourBrand.</p>", unsafe_allow_html=True)
