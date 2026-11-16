import streamlit as st
import random
import time
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="REDDY ANNA | Live Sports & Exchange",
    page_icon="🏏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize Session State for Working Betting Engine
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
    st.session_state.show_auth = None  # "Login" or "Register"

# Custom CSS Matching Screenshot Layout, Typography & Cards
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
    background-color: #f3f4f6 !important;
}

.stApp {
    background-color: #f3f4f6 !important;
}

/* Hide default Streamlit chrome */
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
    position: relative;
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

/* Category Cards (2x2 Grid) */
.grid-card {
    border-radius: 12px;
    padding: 24px 12px;
    text-align: center;
    color: #ffffff;
    font-weight: 600;
    font-size: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    margin-bottom: 8px;
    position: relative;
    overflow: hidden;
}
.bg-cricket { background: linear-gradient(110deg, #592014 0%, #8c4838 55%, #d6c3be 100%); }
.bg-football { background: linear-gradient(110deg, #0b5e59 0%, #2b8a83 55%, #b8dbd8 100%); }
.bg-tennis { background: linear-gradient(110deg, #8f0808 0%, #b53838 55%, #e3bcbc 100%); }
.bg-horse { background: linear-gradient(110deg, #c97214 0%, #e09132 55%, #f5d8b5 100%); }

/* Full-Width Banner Cards */
.banner-card {
    border-radius: 12px;
    padding: 24px 20px;
    color: #ffffff;
    font-weight: 600;
    font-size: 17px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.14);
    margin-bottom: 10px;
}
.bg-ecricket { background: linear-gradient(95deg, #4b186e 0%, #843eb5 55%, #e4d0f2 100%); }
.bg-evolution { background: linear-gradient(95deg, #4d131a 0%, #992e3b 55%, #f0c2c7 100%); }
.bg-aviator { background: linear-gradient(95deg, #e60b1d 0%, #b80716 60%, #6e040c 100%); }
.bg-sportsbook { background: linear-gradient(95deg, #162952 0%, #2d4d8f 55%, #c5d5f5 100%); }

.banner-icon {
    font-size: 26px;
    width: 36px;
    text-align: center;
}

/* Match Odds Box */
.match-box {
    background: #ffffff;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 10px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.match-header {
    font-size: 11px;
    color: #16a34a;
    font-weight: 700;
    margin-bottom: 4px;
}
.match-title {
    font-size: 14px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 8px;
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

/* Override Streamlit Buttons to match Yellow/Compact Style */
div.stButton > button {
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    border: none !important;
    padding: 0.35rem 0.6rem !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------- TOP NAVIGATION BAR -----------------
st.markdown("""
<div class="top-navbar">
    <div style="color:white; font-size:22px; font-weight:bold;">☰</div>
    <div class="brand-logo">
        <div class="brand-main">REDDY</div>
        <div class="brand-sub-overlay">ANNA</div>
        <div class="brand-since">— SINCE 2010 —</div>
    </div>
    <div style="font-size:11px; color:#facc15; font-weight:600;">
        VIP EXCHANGE
    </div>
</div>
""", unsafe_allow_html=True)

# Top Action Controls (Login / Register / Wallet)
if not st.session_state.logged_in:
    c1, c2, c3 = st.columns([1.2, 1, 1])
    with c1:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.active_section = "Home"
            st.session_state.show_auth = None
    with c2:
        if st.button("Login", type="primary", use_container_width=True):
            st.session_state.show_auth = "Login"
    with c3:
        if st.button("Register", type="primary", use_container_width=True):
            st.session_state.show_auth = "Register"
else:
    c1, c2, c3 = st.columns([1, 1.4, 1])
    with c1:
        if st.button("🏠 Lobby", use_container_width=True):
            st.session_state.active_section = "Home"
    with c2:
        st.markdown(
            f"<div style='background:#111827; color:#facc15; padding:6px 10px; border-radius:8px; text-align:center; font-size:12px; font-weight:700;'>"
            f"💰 ₹{st.session_state.balance:,.2f}</div>",
            unsafe_allow_html=True
        )
    with c3:
        if st.button("📜 My Bets", use_container_width=True):
            st.session_state.active_section = "History"

# ----------------- AUTH MODAL (LOGIN / REGISTER) -----------------
if st.session_state.show_auth and not st.session_state.logged_in:
    with st.container(border=True):
        st.subheader(f"{st.session_state.show_auth} to Reddy Anna ID")
        user_input = st.text_input("Username / ID", placeholder="e.g. ReddyKing99")
        pass_input = st.text_input("Password", type="password", placeholder="••••••")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button(f"Confirm {st.session_state.show_auth}", type="primary", use_container_width=True):
                if user_input.strip():
                    st.session_state.logged_in = True
                    st.session_state.username = user_input.strip()
                    st.session_state.show_auth = None
                    st.rerun()
                else:
                    st.error("Enter a username.")
        with col_b:
            if st.button("Cancel", use_container_width=True):
                st.session_state.show_auth = None
                st.rerun()

# ----------------- SAMPLE LIVE MARKETS DATA -----------------
MARKETS = {
    "Cricket": [
        {"match": "India vs Australia (T20)", "time": "LIVE • In-Play", "t1": "India", "t1_back": 1.85, "t1_lay": 1.87, "t2": "Australia", "t2_back": 2.10, "t2_lay": 2.14},
        {"match": "Mumbai Indians vs CSK", "time": "Today • 19:30 IST", "t1": "Mumbai Indians", "t1_back": 1.92, "t1_lay": 1.95, "t2": "CSK", "t2_back": 2.02, "t2_lay": 2.06},
    ],
    "Football": [
        {"match": "Real Madrid vs Barcelona", "time": "LIVE • 64'", "t1": "Real Madrid", "t1_back": 2.20, "t1_lay": 2.25, "t2": "Barcelona", "t2_back": 3.10, "t2_lay": 3.20},
        {"match": "Arsenal vs Liverpool", "time": "Today • 22:00 IST", "t1": "Arsenal", "t1_back": 2.45, "t1_lay": 2.50, "t2": "Liverpool", "t2_back": 2.80, "t2_lay": 2.88},
    ],
    "Tennis": [
        {"match": "Alcaraz vs Sinner", "time": "LIVE • Set 2", "t1": "C. Alcaraz", "t1_back": 1.75, "t1_lay": 1.78, "t2": "J. Sinner", "t2_back": 2.25, "t2_lay": 2.30},
    ],
    "Horse Racing": [
        {"match": "Royal Ascot - Race 4", "time": "Starts in 12m", "t1": "Thunderbolt", "t1_back": 3.40, "t1_lay": 3.55, "t2": "Silver Arrow", "t2_back": 4.10, "t2_lay": 4.30},
    ],
    "E - Cricket": [
        {"match": "IND XI vs ENG XI (10 Overs)", "time": "LIVE • Over 6.2", "t1": "IND XI", "t1_back": 1.65, "t1_lay": 1.68, "t2": "ENG XI", "t2_back": 2.40, "t2_lay": 2.46},
    ],
    "Sportsbook": [
        {"match": "Kabaddi Pro: Patna vs Puneri", "time": "LIVE • Half 2", "t1": "Patna Pirates", "t1_back": 1.90, "t1_lay": 1.94, "t2": "Puneri Paltan", "t2_back": 2.05, "t2_lay": 2.10},
    ]
}

# ----------------- MAIN LOBBY VIEW (EXACT SCREENSHOT GRID) -----------------
if st.session_state.active_section == "Home":
    # Row 1: Cricket & Football
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="grid-card bg-cricket">Cricket</div>', unsafe_allow_html=True)
        if st.button("Open Cricket Odds", key="btn_cricket", use_container_width=True):
            st.session_state.active_section = "Cricket"
            st.rerun()
    with col2:
        st.markdown('<div class="grid-card bg-football">Football</div>', unsafe_allow_html=True)
        if st.button("Open Football Odds", key="btn_football", use_container_width=True):
            st.session_state.active_section = "Football"
            st.rerun()

    # Row 2: Tennis & Horse Racing
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="grid-card bg-tennis">Tennis</div>', unsafe_allow_html=True)
        if st.button("Open Tennis Odds", key="btn_tennis", use_container_width=True):
            st.session_state.active_section = "Tennis"
            st.rerun()
    with col4:
        st.markdown('<div class="grid-card bg-horse">Horse Racing</div>', unsafe_allow_html=True)
        if st.button("Open Racing Odds", key="btn_horse", use_container_width=True):
            st.session_state.active_section = "Horse Racing"
            st.rerun()

    st.write("")

    # Full-Width Banner 1: E - Cricket
    st.markdown('<div class="banner-card bg-ecricket"><span class="banner-icon">🏏</span><span>E - Cricket</span></div>', unsafe_allow_html=True)
    if st.button("Play E - Cricket Live", key="btn_ecricket", use_container_width=True):
        st.session_state.active_section = "E - Cricket"
        st.rerun()

    # Full-Width Banner 2: Evolution
    st.markdown('<div class="banner-card bg-evolution"><span class="banner-icon">🎲</span><span>Evolution</span></div>', unsafe_allow_html=True)
    if st.button("Enter Evolution Live Casino", key="btn_evolution", use_container_width=True):
        st.session_state.active_section = "Evolution"
        st.rerun()

    # Full-Width Banner 3: Aviator
    st.markdown('<div class="banner-card bg-aviator"><span class="banner-icon">🚀</span><span>Aviator &nbsp;&nbsp;<small style="font-size:11px; opacity:0.85;">50X &nbsp; 100X</small></span></div>', unsafe_allow_html=True)
    if st.button("Launch Aviator Crash Game", key="btn_aviator", use_container_width=True):
        st.session_state.active_section = "Aviator"
        st.rerun()

    # Full-Width Banner 4: Sportsbook
    st.markdown('<div class="banner-card bg-sportsbook"><span class="banner-icon">🏆</span><span>Sportsbook</span></div>', unsafe_allow_html=True)
    if st.button("Open Sportsbook Markets", key="btn_sportsbook", use_container_width=True):
        st.session_state.active_section = "Sportsbook"
        st.rerun()

# ----------------- SPORTS EXCHANGE ODDS VIEW -----------------
elif st.session_state.active_section in MARKETS:
    sport = st.session_state.active_section
    if st.button("← Back to All Sports"):
        st.session_state.active_section = "Home"
        st.session_state.selected_bet = None
        st.rerun()

    st.subheader(f"🔥 {sport} Live Exchange")

    for idx, m in enumerate(MARKETS[sport]):
        st.markdown(f"""
        <div class="match-box">
            <div class="match-header">● {m['time']}</div>
            <div class="match-title">{m['match']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Team 1 Back / Lay
        r1c1, r1c2, r1c3 = st.columns([2, 1, 1])
        r1c1.markdown(f"**{m['t1']}**")
        if r1c2.button(f"BACK {m['t1_back']}", key=f"{sport}_{idx}_t1b", use_container_width=True):
            st.session_state.selected_bet = {"match": m["match"], "pick": m["t1"], "type": "BACK", "odds": m["t1_back"]}
        if r1c3.button(f"LAY {m['t1_lay']}", key=f"{sport}_{idx}_t1l", use_container_width=True):
            st.session_state.selected_bet = {"match": m["match"], "pick": m["t1"], "type": "LAY", "odds": m["t1_lay"]}

        # Team 2 Back / Lay
        r2c1, r2c2, r2c3 = st.columns([2, 1, 1])
        r2c1.markdown(f"**{m['t2']}**")
        if r2c2.button(f"BACK {m['t2_back']}", key=f"{sport}_{idx}_t2b", use_container_width=True):
            st.session_state.selected_bet = {"match": m["match"], "pick": m["t2"], "type": "BACK", "odds": m["t2_back"]}
        if r2c3.button(f"LAY {m['t2_lay']}", key=f"{sport}_{idx}_t2l", use_container_width=True):
            st.session_state.selected_bet = {"match": m["match"], "pick": m["t2"], "type": "LAY", "odds": m["t2_lay"]}
        st.divider()

# ----------------- AVIATOR CRASH GAME -----------------
elif st.session_state.active_section == "Aviator":
    if st.button("← Back to Lobby"):
        st.session_state.active_section = "Home"
        st.rerun()

    st.markdown('<div class="banner-card bg-aviator"><span class="banner-icon">🚀</span><span>AVIATOR 3D CRASH</span></div>', unsafe_allow_html=True)
    stake = st.number_input("Bet Amount (₹)", min_value=100, max_value=5000, value=500, step=100)
    target_mult = st.slider("Auto Cashout Multiplier (x)", 1.20, 10.00, 2.00, 0.10)

    if st.button("🚀 Place Bet & Fly", type="primary", use_container_width=True):
        if not st.session_state.logged_in:
            st.warning("Please click Login or Register at the top first!")
        elif stake > st.session_state.balance:
            st.error("Insufficient balance!")
        else:
            st.session_state.balance -= stake
            crash_point = round(random.uniform(1.05, 6.50), 2)
            with st.spinner("Plane flying..."):
                time.sleep(1.0)
            if crash_point >= target_mult:
                win_amt = round(stake * target_mult, 2)
                st.session_state.balance += win_amt
                st.success(f"🎉 Cashed out at {target_mult}x! Plane flew to {crash_point}x. Won ₹{win_amt:,.2f}!")
                status = f"WON ₹{win_amt:,.2f}"
            else:
                st.error(f"💥 Flew away at {crash_point}x! You lost ₹{stake:,.2f}.")
                status = "LOST"

            st.session_state.bets_history.insert(0, {
                "time": datetime.now().strftime("%H:%M:%S"),
                "match": "Aviator Crash",
                "pick": f"Cashout @ {target_mult}x",
                "odds": target_mult,
                "stake": stake,
                "status": status
            })

# ----------------- EVOLUTION LIVE CASINO -----------------
elif st.session_state.active_section == "Evolution":
    if st.button("← Back to Lobby"):
        st.session_state.active_section = "Home"
        st.rerun()

    st.markdown('<div class="banner-card bg-evolution"><span class="banner-icon">🎲</span><span>EVOLUTION LIVE TABLES</span></div>', unsafe_allow_html=True)
    game_choice = st.selectbox("Select Table", ["Lightning Roulette", "Teen Patti Live", "Andar Bahar", "Dragon Tiger"])
    pick = st.radio("Choose Side", ["Red / Andar / Dragon (1.95x)", "Black / Bahar / Tiger (1.95x)"])
    casino_stake = st.number_input("Chip Value (₹)", min_value=100, max_value=5000, value=500, step=100)

    if st.button("Deal / Spin Now", type="primary", use_container_width=True):
        if not st.session_state.logged_in:
            st.warning("Please click Login or Register at the top first!")
        elif casino_stake > st.session_state.balance:
            st.error("Insufficient balance!")
        else:
            st.session_state.balance -= casino_stake
            won = random.choice([True, False])
            if won:
                payout = round(casino_stake * 1.95, 2)
                st.session_state.balance += payout
                st.success(f"🎉 Winner on {game_choice}! You won ₹{payout:,.2f}")
                status = f"WON ₹{payout:,.2f}"
            else:
                st.error(f"❌ Dealer wins this round on {game_choice}.")
                status = "LOST"

            st.session_state.bets_history.insert(0, {
                "time": datetime.now().strftime("%H:%M:%S"),
                "match": game_choice,
                "pick": pick,
                "odds": 1.95,
                "stake": casino_stake,
                "status": status
            })

# ----------------- BET HISTORY VIEW -----------------
elif st.session_state.active_section == "History":
    if st.button("← Back to Lobby"):
        st.session_state.active_section = "Home"
        st.rerun()

    st.subheader(f"📜 {st.session_state.username}'s Bet Slip History")
    if not st.session_state.bets_history:
        st.info("No bets placed yet. Select any sport or game to place a bet.")
    else:
        for b in st.session_state.bets_history:
            with st.container(border=True):
                st.markdown(f"**{b['match']}** ({b['time']})")
                st.caption(f"Selection: {b['pick']} @ {b['odds']} | Stake: ₹{b['stake']} | **{b['status']}**")

# ----------------- ACTIVE BET SLIP DRAWER -----------------
if st.session_state.selected_bet:
    bet = st.session_state.selected_bet
    with st.container(border=True):
        st.markdown(f"### 🎟️ Bet Slip ({bet['type']})")
        st.write(f"**{bet['match']}** — **{bet['pick']}** @ **{bet['odds']}**")
        bet_stake = st.number_input("Enter Stake (₹)", min_value=100, max_value=10000, value=500, step=100, key="slip_stake")
        est_return = round(bet_stake * bet['odds'], 2)
        st.caption(f"Estimated Payout: **₹{est_return:,.2f}**")

        sc1, sc2 = st.columns(2)
        with sc1:
            if st.button("✅ Place Bet", type="primary", use_container_width=True):
                if not st.session_state.logged_in:
                    st.warning("Please Login or Register first!")
                elif bet_stake > st.session_state.balance:
                    st.error("Insufficient balance!")
                else:
                    st.session_state.balance -= bet_stake
                    # Simulate instant match settlement for demo testing
                    is_win = random.choice([True, False])
                    if is_win:
                        st.session_state.balance += est_return
                        result_str = f"WON ₹{est_return:,.2f}"
                        st.success(f"Bet Matched & Settled! {result_str}")
                    else:
                        result_str = "LOST"
                        st.error("Bet Matched & Settled: Lost.")

                    st.session_state.bets_history.insert(0, {
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "match": bet["match"],
                        "pick": f"{bet['pick']} ({bet['type']})",
                        "odds": bet["odds"],
                        "stake": bet_stake,
                        "status": result_str
                    })
                    st.session_state.selected_bet = None
                    time.sleep(1.2)
                    st.rerun()
        with sc2:
            if st.button("✖ Cancel", use_container_width=True):
                st.session_state.selected_bet = None
                st.rerun()

# ----------------- FLOATING GREEN WHATSAPP BUTTON -----------------
st.markdown("""
<a href="https://wa.me/1234567890" target="_blank" class="whatsapp-float">
    <span style="font-size:20px;">💬</span>
    <span>Get The Reddy Anna ID Now</span>
</a>
""", unsafe_allow_html=True)
