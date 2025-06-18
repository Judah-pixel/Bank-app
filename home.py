import streamlit as st
st.set_page_config(page_title="Cryio Bank", layout="wide",
                   initial_sidebar_state="expanded")

st.title("Welcome to Cryo Bank")
st.markdown("""
            This is **Cryo Bank**, where you can deposit and withdraw""")
#Animations and U/I
st.balloons()

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/savingsaccount.py", label="💰 Savings Account", help="Manage your savings")
with col2:
    st.page_link("pages/currentaccount.py", label="🏦 Current Account", help="Manage your current account")

st.markdown("---")
st.markdown("Contact us: support@cryio-bank.com | 📞 080-CRYO-BANK")
# navigation
st.toast("Welcome to Cryio Bank!") 
st.sidebar.title("Socials")
st.sidebar.markdown("Follow us on:")
st.sidebar.markdown("- [Twitter](https://twitter.com/cryio_bank)")
st.sidebar.markdown("- [Facebook](https://facebook.com/cryio_bank)")
st.sidebar.markdown("All rights reserved. © 2024 Cryio Bank")