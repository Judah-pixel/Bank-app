import streamlit as st 
from savings_account import SavingsAccount 
from current_account import CurrentAccount
st.set_page_config(page_title="Savings Account")
st.title("savings Account Management")
st.session_state.account= SavingsAccount(200000)

with st.form("saving form"):
    amount=st.number_input("Enter Amount", min_value=0.0)
    operations=st.selectbox("choose operation",["Deposit","Withdraw"])
    submit=st.form_submit_button("Submit")

    if submit and operations=="Deposit":
        with st.spinner("processing"):
            st.session_state.account.deposit(amount)
            st.success(f"{amount} Deposit successful")
   
    elif submit and operations=="Withdraw":
        with st.spinner("processing"):
            if amount <= st.session_state.account.balance:
                st.session_state.account.withdraw(amount)
                st.success(f"successfully withdrew {amount}")
            else:
                st.error("insufficient funds")           

st.metric(label="Balance", value=f"#{st.session_state.account.balance:,.2f}")
