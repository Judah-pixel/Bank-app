import streamlit as st
from Current_account import CurrentAccount  # Corrected import (case-sensitive)

st.set_page_config(page_title="Current Account")
st.title("Current Account Management")

# Initialize session state for current account
if "current_account" not in st.session_state:
    st.session_state.current_account = CurrentAccount("CA-001", "Jane Doe", 1000, overdraft_limit=50000)

account = st.session_state.current_account

st.subheader(f"Account Number: {account.account_number}")
st.write(f"Holder: {account.holder_name}")

with st.form("current_form"):
    amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")
    operation = st.selectbox("Choose operation", ["Deposit", "Withdraw"])
    submit = st.form_submit_button("Submit")

    if submit:
        if amount <= 0:
            st.warning("Amount must be greater than zero.")
        elif operation == "Deposit":
            if account.deposit(amount):
                st.success(f"Deposited {amount:.2f} successfully!")
            else:
                st.error("Deposit failed.")
        elif operation == "Withdraw":
            if account.withdraw(amount):
                st.success(f"Withdrew {amount:.2f} successfully!")
            else:
                st.error("Withdrawal failed. Check balance or overdraft limit.")

st.metric(label="Balance", value=f"#{account.get_balance():,.2f}")