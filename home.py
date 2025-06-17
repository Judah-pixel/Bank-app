import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cryo Bank", layout="wide", initial_sidebar_state="expanded")

# --- BACKGROUND IMAGE SETUP ---
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1588776814546-ec7e23619645?auto=format&fit=crop&w=1650&q=80");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: center;
        }
        .overlay {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# --- MAIN CONTENT WITH OVERLAY ---
st.markdown('<div class="overlay">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🏦 Welcome to Cryo Bank</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 18px; color: #f0f0f0;'>
Where your money stays cool ❄️<br>
Deposit and withdraw securely and instantly!
</div>
""", unsafe_allow_html=True)

# --- CENTERED BUTTONS ---
spacer1, col_deposit, spacer2, col_withdraw, spacer3 = st.columns([1, 2, 1, 2, 1])

with col_deposit:
    if st.button("💰 Deposit Money"):
        st.success("Redirecting to deposit page...")

with col_withdraw:
    if st.button("🏧 Withdraw Money"):
        st.warning("Redirecting to withdraw page...")

st.markdown('</div>', unsafe_allow_html=True)  # End overlay

# --- SIDEBAR MENU ---
with st.sidebar:
    st.header("🏦 Cryo Bank Menu")
    st.button("💼 Account Summary")
    st.button("📈 Transaction History")
    st.button("⚙️ Settings")
