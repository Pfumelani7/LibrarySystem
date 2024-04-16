import streamlit as st
from streamlit_extras.switch_page_button import switch_page

total_price = sum(float(item['price']) for item in st.session_state.cart)
st.write(f"Total Price: {total_price}")
for item in st.session_state.cart:
    st.write(f"Title: {item['title']}, Price: R{item['price']}")  

if st.button("Checkout"):
    switch_page("checkout") 
