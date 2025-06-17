import streamlit as st
from savings_account1 import SavingsAccount
from datetime import datetime

# Page config
st.set_page_config(page_title="Savings Account")
st.title("💰 Savings Account Management")

# Initialize session state
if "account" not in st.session_state:
    st.session_state.account = SavingsAccount(0)

if "transaction_log" not in st.session_state:
    st.session_state.transaction_log = []

# Form for deposit/withdraw
with st.form("saving_form"):
    amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")
    operations = st.selectbox("Choose Operation", ["Deposit", "Withdraw"])
    submit = st.form_submit_button("Submit")

    if submit:
        with st.spinner("Processing..."):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if operations == "Deposit":
                st.session_state.account.deposit(amount)
                st.success(f"₦{amount:,.2f} deposited successfully.")

                # Log transaction
                st.session_state.transaction_log.append({
                    "Date": timestamp,
                    "Type": "Deposit",
                    "Amount": f"₦{amount:,.2f}",
                    "Balance": f"₦{st.session_state.account.balance:,.2f}"
                })

            elif operations == "Withdraw":
                if amount <= st.session_state.account.balance:
                    st.session_state.account.withdraw(amount)
                    st.success(f"₦{amount:,.2f} withdrawn successfully.")

                    st.session_state.transaction_log.append({
                        "Date": timestamp,
                        "Type": "Withdraw",
                        "Amount": f"-₦{amount:,.2f}",
                        "Balance": f"₦{st.session_state.account.balance:,.2f}"
                    })
                else:
                    st.error("❌ Insufficient funds")

# Show balance
st.metric(label="Current Balance", value=f"₦{st.session_state.account.balance:,.2f}")

# Show transaction history
st.markdown("---")
st.subheader("📜 Transaction History")

if st.session_state.transaction_log:
    st.dataframe(st.session_state.transaction_log[::-1])  # Show newest first
else:
    st.info("No transactions yet.")
