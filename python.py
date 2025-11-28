import streamlit as st

# -------------------- SESSION STATE INIT --------------------
if "Pin" not in st.session_state:
    st.session_state.Pin = ""
if "Balance" not in st.session_state:
    st.session_state.Balance = 0


class Atm:

    def __init__(self):
        self.Pin = st.session_state.Pin
        self.balance = st.session_state.Balance

    def menu(self, choice):
        if choice == "Create PIN":
            self.create_pin()
        elif choice == "Change PIN":
            self.change_pin()
        elif choice == "Check Balance":
            self.chek_balance()
        elif choice == "Withdraw":
            self.withdraw()

    # Create pin
    def create_pin(self):
        user_pin = st.text_input("Enter your pin:", key="create_pin_input")
        user_balance = st.number_input("Enter your balance:", min_value=0, key="create_balance_input")

        if st.button("Create"):
            st.session_state.Pin = user_pin
            st.session_state.Balance = user_balance
            st.success("Pin created successfully!")

    # Change pin
    def change_pin(self):
        old_pin = st.text_input("Enter old pin:", key="old_pin_input")
        new_pin = st.text_input("Enter new pin:", key="new_pin_input")

        if st.button("Change"):
            if old_pin == st.session_state.Pin:
                st.session_state.Pin = new_pin
                st.success("Pin changed successfully!")
            else:
                st.error("Wrong old pin!")

    # Check balance
    def chek_balance(self):
        user_pin = st.text_input("Enter your pin:", key="check_pin_input")

        if st.button("Check"):
            if user_pin == st.session_state.Pin:
                st.info(f"Your balance is: {st.session_state.Balance}")
            else:
                st.error("Cannot check balance (wrong PIN)!")

    # Withdraw
    def withdraw(self):
        user_pin = st.text_input("Enter your pin:", key="with_pin_input")
        amount = st.number_input("Enter amount:", min_value=0, key="with_amt_input")

        if st.button("Withdraw"):
            if user_pin == st.session_state.Pin:
                if amount <= st.session_state.Balance:
                    st.session_state.Balance -= amount
                    st.success(f"Withdraw successful! Balance is: {st.session_state.Balance}")
                else:
                    st.error("Insufficient balance")
            else:
                st.error("Wrong PIN!")


# --------------------- STREAMLIT UI ---------------------
st.title("💳 ATM Machine ")

atm = Atm()

choice = st.sidebar.radio(
    "Menu",
    ["Create PIN", "Change PIN", "Check Balance", "Withdraw"]
)

atm.menu(choice)

