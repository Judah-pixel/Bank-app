import streamlit as st
from current_account1 import CurrentAccount
from datetime import datetime

# Page config
st.set_page_config(page_title="Current Account")
st.title("🏦 Current Account Management")

# Initialize session state
if "account" not in st.session_state:
    st.session_state.account = CurrentAccount(account_number="CA001", holder_name="John Doe", balance=0.0)

if "transaction_log" not in st.session_state:
    st.session_state.transaction_log = []

# Form for deposit/withdraw
with st.form("current_form"):
    amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")
    operations = st.selectbox("Choose Operation", ["Deposit", "Withdraw"])
    submit = st.form_submit_button("Submit")

    if submit:
        with st.spinner("Processing..."):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if operations == "Deposit":
                success = st.session_state.account.deposit(amount)
                if success:
                    st.success(f"₦{amount:,.2f} deposited successfully.")
                    st.session_state.transaction_log.append({
                        "Date": timestamp,
                        "Type": "Deposit",
                        "Amount": f"₦{amount:,.2f}",
                        "Balance": f"₦{st.session_state.account.balance:,.2f}"
                    })
                else:
                    st.error("Invalid deposit amount.")

            elif operations == "Withdraw":
                success = st.session_state.account.withdraw(amount)
                if success:
                    st.success(f"₦{amount:,.2f} withdrawn successfully.")
                    st.session_state.transaction_log.append({
                        "Date": timestamp,
                        "Type": "Withdraw",
                        "Amount": f"-₦{amount:,.2f}",
                        "Balance": f"₦{st.session_state.account.balance:,.2f}"
                    })
                else:
                    st.error("❌ Withdrawal failed. Overdraft limit exceeded or invalid amount.")

# Show balance
st.metric(label="Current Balance", value=f"₦{st.session_state.account.balance:,.2f}")

# Show transaction history
st.markdown("---")
st.subheader("📜 Transaction History")

if st.session_state.transaction_log:
    st.dataframe(st.session_state.transaction_log[::-1])  # Newest first
else:
    st.info("No transactions yet.")
