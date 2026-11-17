import streamlit as st
import random
import time
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="REDDY ANNA | Official Exchange",
    page_icon="🏏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = "Guest"
if "balance" not in st.session_state:
    st.session_state.balance = 10000.00
if "view" not in st.session_state:
    st.session_state.view = "Home"
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False
if "menu_sub" not in st.session_state:
    st.session_state.menu_sub = None
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = None
if "selected_bet" not in st.session_state:
    st.session_state.selected_bet = None
if "bets_history" not in st.session_state:
    st.session_state.bets_history = []

# Handle URL Query Parameters for Instant Navigation
params = st.query_params
if "nav" in params:
    target = params["nav"]
    st.query_params.clear()
    if target == "toggle_menu":
        st.session_state.menu_open = not st.session_state.menu_open
        if not st.session_state.menu_open:
            st.session_state.menu_sub = None
    elif target == "sub_sports":
        st.session_state.menu_sub = None if st.session_state.menu_sub == "sports" else "sports"
    elif target == "sub_providers":
        st.session_state.menu_sub = None if st.session_state.menu_sub == "providers" else "providers"
    elif target in ["Login", "Register"]:
        st.session_state.auth_mode = target
        st.session_state.menu_open = False
    elif target == "Logout":
        st.session_state.logged_in = False
        st.session_state.view = "Home"
        st.session_state.menu_open = False
    else:
        st.session_state.view = target
        st.session_state.menu_open = False
        st.session_state.auth_mode = None
    st.rerun()

# Exact CSS Styling Matching Your Layout
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
    background-color: #f4f5f7 !important;
}
.stApp {
    background-color: #f4f5f7 !important;
}

#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 6rem !important;
    padding-left: 0.85rem !important;
    padding-right: 0.85rem !important;
    max-width: 460px !important;
}

/* Sticky Top Black Header Bar */
.top-header {
    background-color: #050505;
    padding: 12px 16px;
    margin: 0 -0.85rem 0 -0.85rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 1000;
}
.header-left {
    display: flex;
    align-items: center;
    gap: 16px;
}
.menu-icon-btn {
    color: #ffffff !important;
    font-size: 24px;
    font-weight: 500;
    text-decoration: none !important;
    line-height: 1;
    width: 24px;
    text-align: center;
}
.logo-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none !important;
    line-height: 1;
}
.logo-reddy {
    font-size: 24px;
    font-weight: 400;
    letter-spacing: 1.5px;
    color: #e6c35c;
}
.logo-anna {
    font-size: 6.5px;
    font-weight: 700;
    color: #ffffff;
    background: #050505;
    padding: 0 2px;
    margin-top: -13px;
    margin-bottom: 6px;
    letter-spacing: 0.5px;
}
.logo-since {
    font-size: 5.5px;
    color: #9ca3af;
    letter-spacing: 1.2px;
}
.header-buttons {
    display: flex;
    align-items: center;
    gap: 10px;
}
.btn-yellow {
    background-color: #fcd34d;
    color: #111827 !important;
    font-size: 13px;
    font-weight: 600;
    padding: 7px 15px;
    border-radius: 6px;
    text-decoration: none !important;
}
.wallet-pill {
    background-color: #1f2937;
    color: #fcd34d !important;
    font-size: 12px;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 6px;
    text-decoration: none !important;
    border: 1px solid #374151;
}

/* Dropdown Menu Drawer */
.nav-drawer {
    background-color: #ffffff;
    margin: 0 -0.85rem 16px -0.85rem;
    box-shadow: 0 8px 16px rgba(0,0,0,0.12);
    border-bottom: 1px solid #e5e7eb;
}
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 13px 20px;
    font-size: 15px;
    font-weight: 600;
    color: #2d3748 !important;
    text-decoration: none !important;
    border-bottom: 1px solid #f3f4f6;
}
.nav-item-active {
    background-color: #4b5563;
    color: #ffffff !important;
}
.nav-sub-list {
    background-color: #f9fafb;
    padding: 4px 0;
}
.nav-sub-item {
    display: block;
    padding: 10px 34px;
    font-size: 14px;
    font-weight: 500;
    color: #374151 !important;
    text-decoration: none !important;
    border-bottom: 1px solid #f3f4f6;
}

.main-body {
    padding-top: 18px;
}

/* 2x2 Sports Grid */
.sports-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 18px;
}
.sport-card {
    border-radius: 12px;
    height: 76px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    text-decoration: none !important;
    color: #ffffff !important;
    font-size: 15px;
    font-weight: 600;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
}
.sport-card span {
    z-index: 2;
    text-shadow: 0 1px 3px rgba(0,0,0,0.3);
}
.sport-pattern {
    position: absolute;
    right: -4px;
    top: -4px;
    bottom: -4px;
    width: 55%;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    align-items: center;
    gap: 4px;
    font-size: 22px;
    opacity: 0.24;
    z-index: 1;
    pointer-events: none;
}

.card-cricket { background: linear-gradient(105deg, #592014 0%, #8e4b3b 55%, #d9c8c4 100%); }
.card-football { background: linear-gradient(105deg, #0b635e 0%, #2f8f88 55%, #beded9 100%); }
.card-tennis { background: linear-gradient(105deg, #990808 0%, #bf3b3b 55%, #e6c1c1 100%); }
.card-horse { background: linear-gradient(105deg, #cf7715 0%, #e39639 55%, #f5dbb8 100%); }

/* 4 Full-Width Feature Banners */
.banner-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
}
.banner-item {
    border-radius: 12px;
    height: 78px;
    padding: 0 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    text-decoration: none !important;
    color: #ffffff !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.13);
}
.banner-left {
    display: flex;
    align-items: center;
    gap: 20px;
    z-index: 2;
}
.banner-svg {
    width: 28px;
    height: 28px;
    fill: #ffffff;
    flex-shrink: 0;
}
.banner-title {
    font-size: 16px;
    font-weight: 600;
}
.banner-right-art {
    z-index: 1;
    font-size: 46px;
    opacity: 0.35;
    display: flex;
    align-items: center;
}
.aviator-right {
    display: flex;
    align-items: center;
    gap: 10px;
    z-index: 2;
}
.aviator-mults {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    line-height: 1.1;
}
.mult-100 {
    font-size: 16px;
    font-weight: 800;
    color: #ffffff;
    transform: rotate(-12deg);
}
.mult-50 {
    font-size: 9px;
    font-weight: 700;
    color: #fecaca;
    margin-right: 26px;
}
.aviator-badge-box {
    text-align: center;
    line-height: 1;
}
.aviator-logo-txt {
    font-size: 14px;
    font-weight: 800;
    font-style: italic;
    letter-spacing: 0.5px;
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}
.aviator-3d-txt {
    font-size: 9px;
    font-weight: 800;
    color: #fca5a5;
}

.banner-ecricket { background: linear-gradient(95deg, #4f1875 0%, #863fb8 55%, #e6d3f5 100%); }
.banner-evolution { background: linear-gradient(95deg, #4f131b 0%, #9c2f3d 55%, #f2c4ca 100%); }
.banner-aviator { background: linear-gradient(95deg, #eb0c1e 0%, #bd0817 60%, #75040d 100%); }
.banner-sportsbook { background: linear-gradient(95deg, #172b57 0%, #305296 55%, #c8d7f7 100%); }

/* Floating WhatsApp Pill */
.whatsapp-pill {
    position: fixed;
    bottom: 18px;
    right: 16px;
    background-color: #25d366;
    color: #ffffff !important;
    padding: 11px 20px;
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none !important;
    box-shadow: 0 6px 16px rgba(37, 211, 102, 0.45);
    z-index: 1001;
    display: flex;
    align-items: center;
    gap: 10px;
}
</style>
""", unsafe_allow_html=True)

# ----------------- TOP HEADER BAR -----------------
menu_symbol = "✕" if st.session_state.menu_open else "☰"

if not st.session_state.logged_in:
    right_controls = """
    <div class="header-buttons">
        <a href="?nav=Login" target="_self" class="btn-yellow">Login</a>
        <a href="?nav=Register" target="_self" class="btn-yellow">Register</a>
    </div>
    """
else:
    right_controls = f"""
    <div class="header-buttons">
        <a href="?nav=History" target="_self" class="wallet-pill">₹{st.session_state.balance:,.0f}</a>
        <a href="?nav=Logout" target="_self" class="btn-yellow" style="padding:6px 10px; font-size:11px;">Logout</a>
    </div>
    """

st.markdown(f"""
<div class="top-header">
    <div class="header-left">
        <a href="?nav=toggle_menu" target="_self" class="menu-icon-btn">{menu_symbol}</a>
        <a href="?nav=Home" target="_self" class="logo-wrap">
            <div class="logo-reddy">REDDY</div>
            <div class="logo-anna">ANNA</div>
            <div class="logo-since">— SINCE 2010 —</div>
        </a>
    </div>
    {right_controls}
</div>
""", unsafe_allow_html=True)

# ----------------- DROPDOWN MENU DRAWER -----------------
if st.session_state.menu_open:
    sports_sub_html = ""
    if st.session_state.menu_sub == "sports":
        sports_sub_html = """
        <div class="nav-sub-list">
            <a href="?nav=Cricket" target="_self" class="nav-sub-item">🏏 Cricket</a>
            <a href="?nav=Football" target="_self" class="nav-sub-item">⚽ Football</a>
            <a href="?nav=Tennis" target="_self" class="nav-sub-item">🎾 Tennis</a>
            <a href="?nav=Horse Racing" target="_self" class="nav-sub-item">🏇 Horse Racing</a>
            <a href="?nav=E - Cricket" target="_self" class="nav-sub-item">🎮 E - Cricket</a>
            <a href="?nav=Evolution" target="_self" class="nav-sub-item">🎲 Evolution</a>
            <a href="?nav=Aviator" target="_self" class="nav-sub-item">🚀 Aviator</a>
            <a href="?nav=Sportsbook" target="_self" class="nav-sub-item">🏆 Sportsbook</a>
        </div>
        """

    providers_sub_html = ""
    if st.session_state.menu_sub == "providers":
        providers_sub_html = """
        <div class="nav-sub-list">
            <a href="?nav=Cricket" target="_self" class="nav-sub-item">Diamond Exchange</a>
            <a href="?nav=Cricket" target="_self" class="nav-sub-item">Lotus365 VIP</a>
            <a href="?nav=Cricket" target="_self" class="nav-sub-item">SkyExchange Official</a>
        </div>
        """

    st.markdown(f"""
    <div class="nav-drawer">
        <a href="?nav=Home" target="_self" class="nav-item nav-item-active">Home</a>
        <a href="?nav=sub_sports" target="_self" class="nav-item">Reddy Anna Sports &nbsp;▾</a>
        {sports_sub_html}
        <a href="?nav=sub_providers" target="_self" class="nav-item">ID Providers &nbsp;▾</a>
        {providers_sub_html}
        <a href="?nav=ReddyAnnaID" target="_self" class="nav-item">Reddy Anna ID</a>
        <a href="?nav=AboutUs" target="_self" class="nav-item">About Us</a>
    </div>
    """, unsafe_allow_html=True)

# ----------------- AUTHENTICATION MODAL -----------------
if st.session_state.auth_mode and not st.session_state.logged_in:
    st.write("")
    with st.container(border=True):
        st.subheader(f"{st.session_state.auth_mode} to Reddy Anna ID")
        u = st.text_input("Username / ID", placeholder="Enter your ID")
        p = st.text_input("Password", type="password", placeholder="••••••")
        ac1, ac2 = st.columns(2)
        with ac1:
            if st.button(f"Confirm {st.session_state.auth_mode}", type="primary", use_container_width=True):
                if u.strip():
                    st.session_state.logged_in = True
                    st.session_state.username = u.strip()
                    st.session_state.auth_mode = None
                    st.rerun()
                else:
                    st.error("Please enter a username.")
        with ac2:
            if st.button("Cancel", use_container_width=True):
                st.session_state.auth_mode = None
                st.rerun()

# ----------------- HOME VIEW -----------------
if st.session_state.view == "Home":
    grid_html = ""
    if not st.session_state.menu_open:
        grid_html = """
        <div class="sports-grid">
            <a href="?nav=Cricket" target="_self" class="sport-card card-cricket">
                <span>Cricket</span>
                <div class="sport-pattern">🏏 ⚾ 🏏 ⚾</div>
            </a>
            <a href="?nav=Football" target="_self" class="sport-card card-football">
                <span>Football</span>
                <div class="sport-pattern">⚽ ⚽ ⚽ ⚽</div>
            </a>
            <a href="?nav=Tennis" target="_self" class="sport-card card-tennis">
                <span>Tennis</span>
                <div class="sport-pattern">🎾 🎾 🎾 🎾</div>
            </a>
            <a href="?nav=Horse Racing" target="_self" class="sport-card card-horse">
                <span>Horse Racing</span>
                <div class="sport-pattern">🏇 🏇 🏇 🏇</div>
            </a>
        </div>
        """

    st.markdown(f"""
    <div class="main-body">
        {grid_html}

        <!-- 4 Full-Width Feature Banners with Custom SVG Icons -->
        <div class="banner-list">
            <!-- E - Cricket -->
            <a href="?nav=E - Cricket" target="_self" class="banner-item banner-ecricket">
                <div class="banner-left">
                    <svg class="banner-svg" viewBox="0 0 24 24">
                        <path d="M18.5 2.5L21.5 5.5L9.5 17.5L6.5 14.5L18.5 2.5ZM5 16L8 19L4 21L3 20L5 16ZM16 18C17.1 18 18 18.9 18 20C18 21.1 17.1 22 16 22C14.9 22 14 21.1 14 20C14 18.9 14.9 18 16 18Z"/>
                    </svg>
                    <div class="banner-title">E - Cricket</div>
                </div>
                <div class="banner-right-art">🏏</div>
            </a>

            <!-- Evolution -->
            <a href="?nav=Evolution" target="_self" class="banner-item banner-evolution">
                <div class="banner-left">
                    <svg class="banner-svg" viewBox="0 0 24 24">
                        <path d="M12 2C16.5 2 20 5.2 20 9.2C20 11.5 18.7 13.5 16.8 14.7C18.5 15.6 19.6 17.2 19.6 19.1C19.6 21.8 16.5 23 12 23H7V18H12C13.8 18 15 17.3 15 16.2C15 15.1 13.8 14.4 12 14.4H8V10.4H12C13.8 10.4 15 9.7 15 8.6C15 7.5 13.8 6.8 12 6.8H7V2H12Z"/>
                    </svg>
                    <div class="banner-title">Evolution</div>
                </div>
                <div class="banner-right-art">🃏🎲</div>
            </a>

            <!-- Aviator -->
            <a href="?nav=Aviator" target="_self" class="banner-item banner-aviator">
                <div class="banner-left">
                    <svg class="banner-svg" viewBox="0 0 24 24">
                        <path d="M13.13 22.19L11.5 18.36C13.07 17.78 14.54 17 15.9 16.09L13.13 22.19ZM5.64 12.5L1.81 10.87L7.91 8.1C7 9.46 6.22 10.93 5.64 12.5ZM21.61 2.39C21.61 2.39 16.66 .269 11 5.93C8.81 8.12 7.5 10.53 6.65 12.64C6.37 13.39 6.56 14.21 7.11 14.77L9.24 16.89C9.79 17.45 10.61 17.63 11.36 17.35C13.5 16.53 15.88 15.19 18.07 13C23.73 7.34 21.61 2.39 21.61 2.39ZM14.54 9.46C13.76 8.68 13.76 7.41 14.54 6.63C15.32 5.85 16.59 5.85 17.37 6.63C18.14 7.41 18.14 8.68 17.37 9.46C16.59 10.24 15.32 10.24 14.54 9.46Z"/>
                    </svg>
                    <div class="banner-title">Aviator</div>
                </div>
                <div class="aviator-right">
                    <div class="aviator-mults">
                        <span class="mult-100">100X</span>
                        <span class="mult-50">50X</span>
                    </div>
                    <div class="aviator-badge-box">
                        <div style="font-size:22px;">✈️</div>
                        <div class="aviator-logo-txt">AVIATOR</div>
                        <div class="aviator-3d-txt">3D</div>
                    </div>
                </div>
            </a>

            <!-- Sportsbook -->
            <a href="?nav=Sportsbook" target="_self" class="banner-item banner-sportsbook">
                <div class="banner-left">
                    <svg class="banner-svg" viewBox="0 0 24 24">
                        <path d="M18 2H6V4H2V9C2 11.21 3.79 13 6 13H6.62C7.42 15.05 9.29 16.58 11.5 16.92V19H8V21H16V19H12.5V16.92C14.71 16.58 16.58 15.05 17.38 13H18C20.21 13 22 11.21 22 9V4H18V2ZM4 9V6H6V11C4.9 11 4 10.1 4 9ZM20 9C20 10.1 19.1 11 18 11V6H20V9Z"/>
                    </svg>
                    <div class="banner-title">Sportsbook</div>
                </div>
                <div class="banner-right-art">🏟️</div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ----------------- LIVE MARKETS VIEW -----------------
elif st.session_state.view in ["Cricket", "Football", "Tennis", "Horse Racing", "E - Cricket", "Sportsbook"]:
    sport = st.session_state.view
    st.write("")
    if st.button("← Back to All Sports"):
        st.session_state.view = "Home"
        st.session_state.selected_bet = None
        st.rerun()

    st.subheader(f"🔴 {sport} Live Markets")
    ALL_MARKETS = {
        "Cricket": [
            ("R C Bengaluru v Kolkata Knight Riders", "Indian Premier League", "RC Bengaluru", 1.88, "Kolkata Knight Riders", 1.96),
            ("Hobart Hurricanes Women v Scorchers Women", "Womens Big Bash League 2026", "Hobart Hurricanes", 2.10, "Perth Scorchers", 1.74),
            ("India vs Australia (1st Test)", "International Series", "India", 1.45, "Australia", 2.90),
        ],
        "Football": [
            ("Real Madrid vs Barcelona", "La Liga", "Real Madrid", 2.15, "Barcelona", 3.10),
            ("Arsenal vs Liverpool", "Premier League", "Arsenal", 2.45, "Liverpool", 2.80),
        ],
        "Tennis": [
            ("Carlos Alcaraz vs Jannik Sinner", "ATP Tour Finals", "C. Alcaraz", 1.75, "J. Sinner", 2.20),
            ("Iga Swiatek vs Aryna Sabalenka", "WTA Finals", "I. Swiatek", 1.85, "A. Sabalenka", 2.05),
        ],
        "Horse Racing": [
            ("Royal Ascot - Race 4 (1400m)", "UK Racing", "Thunderbolt", 3.40, "Silver Arrow", 4.10),
            ("Bangalore Turf Club - Derby", "Indian Racing", "Deccan Star", 2.60, "Royal Mysore", 3.80),
        ],
        "E - Cricket": [
            ("IND XI vs ENG XI (10 Overs T10)", "Virtual Cricket League", "IND XI", 1.65, "ENG XI", 2.40),
            ("AUS XI vs SA XI (Super Over)", "E-Cricket Blitz", "AUS XI", 1.90, "SA XI", 1.95),
        ],
        "Sportsbook": [
            ("Pro Kabaddi: Patna Pirates vs Puneri Paltan", "PKL 2026", "Patna Pirates", 1.90, "Puneri Paltan", 2.05),
            ("NBA: LA Lakers vs Boston Celtics", "Basketball", "LA Lakers", 2.30, "Boston Celtics", 1.68),
        ],
    }

    for idx, (m_name, league, t1, o1, t2, o2) in enumerate(ALL_MARKETS[sport]):
        with st.container(border=True):
            st.caption(f"🟢 LIVE • {league}")
            st.markdown(f"**{m_name}**")
            b1, b2 = st.columns(2)
            if b1.button(f"🔴 make Bet ({t1} @ {o1})", key=f"bet_{sport}_{idx}_1", use_container_width=True):
                st.session_state.selected_bet = {"match": m_name, "pick": t1, "odds": o1}
            if b2.button(f"🔴 make Bet ({t2} @ {o2})", key=f"bet_{sport}_{idx}_2", use_container_width=True):
                st.session_state.selected_bet = {"match": m_name, "pick": t2, "odds": o2}

# ----------------- AVIATOR CRASH GAME -----------------
elif st.session_state.view == "Aviator":
    st.write("")
    if st.button("← Back to Lobby"):
        st.session_state.view = "Home"
        st.rerun()
    st.subheader("🚀 Aviator 3D Crash")
    stake = st.number_input("Bet Amount (₹)", 100, 5000, 500, 100)
    mult = st.slider("Auto Cashout Multiplier (x)", 1.2, 10.0, 2.0, 0.1)
    if st.button("🚀 Place Bet & Fly", type="primary", use_container_width=True):
        if not st.session_state.logged_in:
            st.warning("Tap Login or Register at the top first!")
        elif stake > st.session_state.balance:
            st.error("Insufficient balance!")
        else:
            st.session_state.balance -= stake
            crash = round(random.uniform(1.05, 6.0), 2)
            if crash >= mult:
                win = round(stake * mult, 2)
                st.session_state.balance += win
                st.success(f"🎉 Cashed out at {mult}x! Plane reached {crash}x. Won ₹{win:,.2f}")
                status = f"WON ₹{win:,.2f}"
            else:
                st.error(f"💥 Flew away at {crash}x! Lost ₹{stake:,.2f}")
                status = "LOST"
            st.session_state.bets_history.insert(0, {
                "time": datetime.now().strftime("%H:%M:%S"),
                "match": "Aviator 3D", "pick": f"Cashout @ {mult}x", "odds": mult, "stake": stake, "status": status
            })

# ----------------- EVOLUTION CASINO -----------------
elif st.session_state.view == "Evolution":
    st.write("")
    if st.button("← Back to Lobby"):
        st.session_state.view = "Home"
        st.rerun()
    st.subheader("🎲 Evolution Live Tables")
    table = st.selectbox("Choose Live Table", ["Lightning Roulette", "Teen Patti Live", "Andar Bahar", "Dragon Tiger"])
    stake = st.number_input("Chip Value (₹)", 100, 5000, 500, 100)
    if st.button("Deal / Spin Now", type="primary", use_container_width=True):
        if not st.session_state.logged_in:
            st.warning("Tap Login or Register at the top first!")
        elif stake <= st.session_state.balance:
            st.session_state.balance -= stake
            won = random.choice([True, False])
            if won:
                win = round(stake * 1.95, 2)
                st.session_state.balance += win
                st.success(f"🎉 Won ₹{win:,.2f} on {table}!")
                status = f"WON ₹{win:,.2f}"
            else:
                st.error(f"❌ Dealer won this round on {table}.")
                status = "LOST"
            st.session_state.bets_history.insert(0, {
                "time": datetime.now().strftime("%H:%M:%S"),
                "match": table, "pick": "Main Hand", "odds": 1.95, "stake": stake, "status": status
            })

# ----------------- INFO & HISTORY PAGES -----------------
elif st.session_state.view == "ReddyAnnaID":
    st.write("")
    if st.button("← Back"):
        st.session_state.view = "Home"
        st.rerun()
    st.subheader("🆔 Reddy Anna ID")
    st.info("Get your official Reddy Anna VIP Exchange ID in under 2 minutes via our 24/7 WhatsApp desk.")

elif st.session_state.view == "AboutUs":
    st.write("")
    if st.button("← Back"):
        st.session_state.view = "Home"
        st.rerun()
    st.subheader("ℹ️ About Reddy Anna")
    st.write("Operating since 2010, Reddy Anna provides live sports markets across Cricket, Football, Tennis, Horse Racing, E-Cricket, Evolution Casino, and Aviator.")

elif st.session_state.view == "History":
    st.write("")
    if st.button("← Back to Lobby"):
        st.session_state.view = "Home"
        st.rerun()
    st.subheader(f"📜 {st.session_state.username}'s Bet History")
    if not st.session_state.bets_history:
        st.info("No bets placed yet.")
    for b in st.session_state.bets_history:
        with st.container(border=True):
            st.markdown(f"**{b['match']}** ({b['time']})")
            st.caption(f"Pick: {b['pick']} @ {b['odds']} | Stake: ₹{b['stake']} | **{b['status']}**")

# ----------------- BET SLIP DRAWER -----------------
if st.session_state.selected_bet:
    bet = st.session_state.selected_bet
    with st.container(border=True):
        st.markdown(f"### 🎟️ Bet Slip")
        st.write(f"**{bet['match']}** — **{bet['pick']}** @ **{bet['odds']}**")
        s_amt = st.number_input("Stake (₹)", 100, 10000, 500, 100, key="slip_amt")
        payout = round(s_amt * bet['odds'], 2)
        st.caption(f"Estimated Payout: **₹{payout:,.2f}**")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Confirm Bet", key="confirm_slip", type="primary", use_container_width=True):
                if not st.session_state.logged_in:
                    st.warning("Please Login or Register first!")
                elif s_amt > st.session_state.balance:
                    st.error("Insufficient balance!")
                else:
                    st.session_state.balance -= s_amt
                    won = random.choice([True, False])
                    if won:
                        st.session_state.balance += payout
                    st.session_state.bets_history.insert(0, {
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "match": bet["match"], "pick": bet["pick"], "odds": bet["odds"],
                        "stake": s_amt, "status": f"WON ₹{payout:,.2f}" if won else "LOST"
                    })
                    st.session_state.selected_bet = None
                    st.rerun()
        with c2:
            if st.button("Cancel", key="cancel_slip", use_container_width=True):
                st.session_state.selected_bet = None
                st.rerun()

# ----------------- FLOATING WHATSAPP PILL -----------------
st.markdown("""
<a href="https://wa.me/1234567890" target="_blank" class="whatsapp-pill">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="white">
        <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824z"/>
    </svg>
    <span>Get The Reddy Anna ID Now</span>
</a>
""", unsafe_allow_html=True)
