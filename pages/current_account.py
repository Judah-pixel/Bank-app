import streamlit as st
from current_accounts import CurrentAccount

st.title("Current Accounts")

if 'accounts' not in st.session_state or not st.session_state.accounts:
    st.warning("No accounts found!")
else:

    current_accounts = {acc_num: acc for acc_num, acc in st.session_state.accounts.items() 
                        if isinstance(acc, CurrentAccount)}
    
    if not current_accounts:
        st.warning("No current accounts found!")
    else:
        account_numbers = list(current_accounts.keys())
        selected_acc_num = st.selectbox("Select Account", account_numbers, 
            format_func=lambda acc_num: f"{acc_num} - {current_accounts[acc_num].holder_name}")
        
        selected_account = current_accounts[selected_acc_num]
        
        st.subheader(f"Account Number: {selected_acc_num}")
        st.write(f"Holder: {selected_account.holder_name}")
        st.write(f"Current Balance: {selected_account.get_balance()}")
        
        # Deposit form
        with st.form("deposit_form"):
            deposit_amount = st.number_input("Deposit Amount", min_value=0.0, step=100.0)
            deposit_submit = st.form_submit_button("Deposit")
            if deposit_submit:
                if selected_account.deposit(deposit_amount):
                    st.success(f"Deposited {deposit_amount}. New Balance: {selected_account.get_balance()}")
                else:
                    st.error("Invalid deposit amount")
        
        # Withdraw form
        with st.form("withdraw_form"):
            withdraw_amount = st.number_input("Withdraw Amount", min_value=0.0, step=100.0)
            withdraw_submit = st.form_submit_button("Withdraw")
            if withdraw_submit:
                if selected_account.withdraw(withdraw_amount):
                    st.success(f"Withdrew {withdraw_amount}. New Balance: {selected_account.get_balance()}")
                else:
                    st.error("Withdrawal failed. Overdraft limit exceeded or invalid amount.")
