import streamlit as st

st.set_page_config(page_title="Cryo Bank Dashboard", layout="wide")
st.title("🏦 Welcome to Cryo Bank")

st.markdown("---")
st.subheader("💼 Choose a transaction to begin")

# Center the buttons using 5 columns
col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col2:
    if st.button("💰 Deposit"):
        st.session_state.next_action = "Deposit"

with col4:
    if st.button("🏧 Withdraw"):
        st.session_state.next_action = "Withdraw"

# If a button is clicked, show account options
if "next_action" in st.session_state:
    st.markdown(f"### 👉 You chose to **{st.session_state.next_action}** money")

    # Use similar column layout for radio and proceed button
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
    with col3:
        account_type = st.radio("Select Account Type", ["Savings Account", "Current Account"])

    with col3:
        if st.button("Proceed"):
            st.session_state.account_type = account_type

            # Navigate to the appropriate page
            if account_type == "Savings Account":
                st.switch_page("pages/savings_account.py")
            elif account_type == "Current Account":
                st.switch_page("pages/current_account.py")
