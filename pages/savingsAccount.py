import streamlit as st
from savings_account import SavingsAccount

st.set_page_config(page_title="Savings Account")
st.title("Savings Account Management")

# state for savings account
if "Savings_account" not in st.session_state:
    st.session_state.Savings_account = SavingsAccount()

account = st.session_state.Savings_account

with st.form("savings_form"):
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
                st.error("Withdrawal failed. Check balance or limit.")

st.metric(label="Balance", value=f"#{account.get_balance():,.2f}")
