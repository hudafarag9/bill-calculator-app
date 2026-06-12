import streamlit as st

st.set_page_config(page_title="Bill Calculator", page_icon="🧾")

st.title("🧾 Bill Calculator")
st.write("Split your bill fairly with friends — service charge, VAT, and tip included!")

# --- Inputs ---
bill = st.number_input("💰 What was the total bill (LE)?", min_value=0.0, step=1.0)

service_charge = st.selectbox(
    "🍽️ What is the Service Charge at this restaurant?",
    options=[10, 12]
)

vat = st.number_input("🏛️ What is the VAT (%)?", min_value=0.0, max_value=100.0, value=14.0, step=0.5)

people = st.number_input("👥 How many people are splitting the bill?", min_value=1, step=1)

tip = st.number_input(
    "💵 Have you tipped the servers? Enter the amount (0 if no):",
    min_value=0.0, step=1.0
)

# --- Calculation ---
if st.button("Calculate 🚀"):
    if people == 0:
        st.error("Number of people can't be zero!")
    else:
        bill_with_tip = bill + tip
        service_amount = service_charge / 100 * bill
        vat_amount = vat / 100 * bill

        total_bill = bill_with_tip + service_amount + vat_amount
        bill_per_person = total_bill / people
        final_amount = round(bill_per_person, 2)

        st.success(f"✅ Total bill (with service, VAT & tip): **{round(total_bill, 2)} LE**")
        st.info(f"💸 Each person should pay: **{final_amount} LE**")
        st.write("Hehehehe have a nice day dudu :*")
