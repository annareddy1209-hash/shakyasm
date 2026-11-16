import streamlit as st
import random
import time
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="REDDY ANNA | Live Sports & Exchange",
    page_icon="🏏",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = "Guest"
if "balance" not in st.session_state:
    st.session_state.balance = 10000.00
if "active_section" not in st.session_state:
    st.session_state.active_section = "Home"
if "selected_bet" not in st.session_state:
    st.session_state.selected_bet = None
if "bets_history" not in st.session_state:
    st.session_state.bets_history = []
if "show_auth" not in st.session_state:
    st.session_state.show_auth = None

# Custom CSS Matching Layout & Typography
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
    background-color: #f3f4f6 !important;
}
.stApp { background-color: #f3f4f6 !important; }

#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 5rem !important;
    padding-left: 0.75rem !important;
    padding-right: 0.75rem !important;
    max-width: 480px !important;
}

/* Top Black Header Bar */
.top-navbar {
    background-color: #050505;
    padding: 12px 14px;
    margin: 0 -0.75rem 16px -0.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.brand-logo {
    display: flex;
    flex-direction: column;
    align-items: center;
    line-height: 1;
}
.brand-main {
    font-size: 24px;
    font-weight: 400;
    letter-spacing: 2px;
    color: #e5c158;
}
.brand-sub-overlay {
    font-size: 7px;
    font-weight: 700;
    color: #ffffff;
    background: #050505;
    padding: 0 2px;
    letter-spacing: 0.5px;
    margin-top: -14px;
    margin-bottom: 6px;
}
.brand-since {
    font-size: 6px;
    color: #a3a3a3;
    letter-spacing: 1.5px;
}

/* Live Match Feed Cards */
.match-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 3px 8px rgba(0,0,0,0.05);
}
.live-badge {
    color: #16a34a;
    font-weight: 700;
    font-size: 11px;
    background: #dcfce7;
    padding: 2px 8px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 6px;
}
.match-teams {
    font-size: 15px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 2px;
}
.match-league {
    font-size: 12px;
    color: #6b7280;
    margin-bottom: 12px;
}

/* Floating Green WhatsApp Pill */
.whatsapp-float {
    position: fixed;
    bottom: 18px;
    right: 16px;
    background-color: #25d366;
    color: #ffffff !important;
    padding: 12px 22px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 14px;
    text-decoration: none;
    box-shadow: 0 6px 18px rgba(37, 211, 102, 0.45);
    z-index: 9999;
    display: flex;
    align-items: center;
    gap: 8px;
}

div.stButton > button {
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR NAVIGATION DRAWER -----------------
with st.sidebar:
    st.markdown("### 📋 Navigation Menu")
    if st.button("🏠 Home / Lobby", use_container_width=True):
        st.session_state.active_section = "Home"
        st.rerun()
    
    with st.expander("🏏 Reddy Anna Sports"):
        if st.button("Cricket Exchange", use_container_width=True):
            st.session_state.active_section = "Cricket"
            st.rerun()
        if st.button("Football Exchange", use_container_width=True):
            st.session_state.active_section = "Football"
            st.rerun()
        if st.button("Tennis Exchange", use_container_width=True):
            st.session_state.active_section = "Tennis"
            st.rerun()

    with st.expander("🔑 ID Providers"):
        st.markdown("- VIP Master Hub\n- Instant Support Desk\n- 24/7 Automated Agent")

    if st.button("🆔 Reddy Anna ID Info", use_container_width=True):
        st.info("Reddy Anna ID is India's most trusted online sports and exchange platform active since 2010.")

    if st.button("ℹ️ About Us", use_container_width=True):
        st.success("Trusted gaming provider offering secure access, instant chat onboarding, and 24/7 customer service.")

    st.divider()
    if st.session_state.logged_in:
        st.write(f"User: **{st.session_state.username}**")
        st.write(f"Wallet: **₹{st.session_state.balance:,.2f}**")
        if st.button("Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

# ----------------- TOP NAVBAR -----------------
st.markdown("""
<div class="top-navbar">
    <div style="color:white; font-size:22px; font-weight:bold;">☰</div>
    <div class="brand-logo">
        <div class="brand-main">REDDY</div>
        <div class="brand-sub-overlay">ANNA</div>
        <div class="brand-since">— SINCE 2010 —</div>
    </div>
    <div style="font-size:11px; color:#facc15; font-weight:600;">VIP</div>
</div>
""", unsafe_allow_html=True)

# Auth Header Buttons
if not st.session_state.logged_in:
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Login", type="primary", use_container_width=True):
            st.session_state.show_auth = "Login"
    with c2:
        if st.button("Register", type="primary", use_container_width=True):
            st.session_state.show_auth = "Register"
else:
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown(f"<div style='background:#111827; color:#facc15; padding:6px; border-radius:8px; text-align:center; font-size:12px; font-weight:bold;'>💰 ₹{st.session_state.balance:,.2f}</div>", unsafe_allow_html=True)
    with c2:
        if st.button("📜 My Bets History", use_container_width=True):
            st.session_state.active_section = "History"
            st.rerun()

# Auth Modal
if st.session_state.show_auth and not st.session_state.logged_in:
    with st.container(border=True):
        st.subheader(f"{st.session_state.show_auth}")
        u = st.text_input("Username", placeholder="Enter your ID")
        p = st.text_input("Password", type="password")
        ca, cb = st.columns(2)
        with ca:
            if st.button("Submit", type="primary", use_container_width=True):
                if u:
                    st.session_state.logged_in = True
                    st.session_state.username = u
                    st.session_state.show_auth = None
                    st.rerun()
        with cb:
            if st.button("Close", use_container_width=True):
                st.session_state.show_auth = None
                st.rerun()

# ----------------- LIVE MATCHES FEED SECTION (AS SEEN IN SCREENSHOT) -----------------
LIVE_MATCHES = [
    {"match": "R C Bengaluru v Kolkata Knight Riders", "league": "Indian Premier League", "time": "LIVE • 16/11/2026 8:38 am", "t1": "RC Bengaluru", "t1_odds": 1.88, "t2": "Kolkata Knight Riders", "t2_odds": 1.96},
    {"match": "Hobart Hurricanes Women v Scorchers Women", "league": "Womens Big Bash League 2026", "time": "LIVE • In-Play", "t1": "Hobart Hurricanes", "t1_odds": 2.10, "t2": "Perth Scorchers", "t2_odds": 1.74}
]

if st.session_state.active_section == "Home":
    st.markdown("### 🔥 Live Featured Matches")
    
    for idx, m in enumerate(LIVE_MATCHES):
        st.markdown(f"""
        <div class="match-card">
            <span class="live-badge">● {m['time']}</span>
            <div class="match-teams">{m['match']}</div>
            <div class="match-league">{m['league']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button(f"🔴 make Bet ({m['t1']} @ {m['t1_odds']})", key=f"bet_m_{idx}_t1", use_container_width=True):
                st.session_state.selected_bet = {"match": m["match"], "pick": m["t1"], "type": "BACK", "odds": m["t1_odds"]}
        with col_btn2:
            if st.button(f"🔴 make Bet ({m['t2']} @ {m['t2_odds']})", key=f"bet_m_{idx}_t2", use_container_width=True):
                st.session_state.selected_bet = {"match": m["match"], "pick": m["t2"], "type": "BACK", "odds": m["t2_odds"]}

# ----------------- BET SLIP MODAL -----------------
if st.session_state.selected_bet:
    bet = st.session_state.selected_bet
    with st.container(border=True):
        st.markdown(f"### 🎟️ Bet Slip")
        st.write(f"**{bet['match']}** — **{bet['pick']}** @ **{bet['odds']}**")
        stake = st.number_input("Stake Amount (₹)", min_value=100, max_value=10000, value=500, step=100)
        payout = round(stake * bet['odds'], 2)
        st.caption(f"Estimated Payout: **₹{payout:,.2f}**")
        
        bc1, bc2 = st.columns(2)
        with bc1:
            if st.button("Confirm & Place Bet", type="primary", use_container_width=True):
                if not st.session_state.logged_in:
                    st.warning("Please Login first!")
                elif stake > st.session_state.balance:
                    st.error("Insufficient balance!")
                else:
                    st.session_state.balance -= stake
                    is_win = random.choice([True, False])
                    res = f"WON ₹{payout:,.2f}" if is_win else "LOST"
                    if is_win:
                        st.session_state.balance += payout
                        st.success(f"Bet Won! +₹{payout:,.2f}")
                    else:
                        st.error("Bet Lost.")
                    
                    st.session_state.bets_history.insert(0, {
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "match": bet["match"],
                        "pick": bet["pick"],
                        "odds": bet["odds"],
                        "stake": stake,
                        "status": res
                    })
                    st.session_state.selected_bet = None
                    time.sleep(1)
                    st.rerun()
        with bc2:
            if st.button("Cancel Bet", use_container_width=True):
                st.session_state.selected_bet = None
                st.rerun()

# ----------------- FLOATING WHATSAPP BUTTON -----------------
st.markdown("""
<a href="https://wa.me/1234567890" target="_blank" class="whatsapp-float">
    <span style="font-size:20px;">💬</span>
    <span>Get The Reddy Anna ID Now</span>
</a>
""", unsafe_allow_html=True)
