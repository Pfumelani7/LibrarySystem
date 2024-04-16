# import streamlit as st
# from streamlit_option_menu import option_menu
# from st_pages import hide_pages
# import Un as Un

# Un.Nevigate()

# #if st.button("logout"):
#     #st.session_state.loggedin = ""
    
             
        
        
# def update_personal_info():
#     st.header("Update Personal Information")
#     # Add input fields for updating personal information
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     contact_number= st.text_input("Contact Number")
#     address= st.text_input("address")
    
#     # Add "Submit" button
#     if st.button("Submit"):
#         st.success("Personal information successfully updated!")
    
# def update_payment_details():
#     st.header("Update Payment Details")
#     # Add input fields for updating payment details
#     card_holders_name= st.text_input("Card Holder's Name")
#     card_number = st.text_input("Card Number")
#     expiry_date = st.date_input("Expiry Date")
    
#     # Add "Submit" button
#     if st.button("Submit"):
#         st.success("Payment details successfully updated!")
    
# def change_password():
#     st.header("Change Password")
#     # Add input fields for changing password
#     current_password = st.text_input("Current Password", type="password")
#     new_password = st.text_input("New Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
    
#     # Add "Submit" button
#     if st.button("Submit"):
#         st.success("Password successfully changed!")
    
# def main():
    
#     selected_option = option_menu("Setting", ["Update Personal Information", 
#                                                   "Update Payment Details", 
#                                                   "Change Password"], 
#                                        menu_icon="cast", default_index=0)
    
#     if selected_option == "Update Personal Information":
#         update_personal_info()
#     elif selected_option == "Update Payment Details":
#         update_payment_details()
#     elif selected_option == "Change Password":
#         change_password()

# if __name__ == "__main__":
#     main()

import streamlit as st
from streamlit_option_menu import option_menu
from st_pages import hide_pages
import Un as Un
import pandas as pd
Un.Nevigate()
import psycopg2
import hashlib

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="books",
    user="postgres"
)
c = conn.cursor()
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
#if st.button("logout"):
    #st.session_state.loggedin = ""
df = pd.read_csv("/Users/da-m1-09/Downloads/Librarydatax.csv")

def update_personal_info():
    if "username" in st.session_state:
        c.execute('SELECT username FROM userstable where username = %s', (st.session_state["username"],))
        data = c.fetchone()
        
        st.header("Update Personal Information")
        # Add input fields for updating personal information
        name = st.text_input("Name", placeholder=data[0])
        email = st.text_input("Email")
        contact_number= st.text_input("Contact Number")
        address= st.text_input("address")
        
        # Add "Submit" button
        if st.button("Submit"):
            st.success("Personal information successfully updated!")
    else:
        st.write("Not Signed in")
        
def update_payment_details():
    st.header("Update Payment Details")
    # Add input fields for updating payment details
    card_holders_name= st.text_input("Card Holder's Name")
    card_number = st.text_input("Card Number")
    expiry_date = st.date_input("Expiry Date")
    
    # Add "Submit" button
    if st.button("Submit"):
        st.success("Payment details successfully updated!")
    
def change_password():
    if "username" in st.session_state:

        st.header("Change Password")
        c.execute('SELECT password FROM userstable where username = %s', (st.session_state["username"],))
        data = c.fetchone()
        # Add input fields for changing password
        current_password = st.text_input("Current Password", type="password")
        hashed_pswd = make_hashes(current_password)

        if hashed_pswd == data[0]:
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
    
        # Add "Submit" button
        if st.button("Submit"):
            if new_password == confirm_password:
                c.execute('UPDATE userstable SET password = %s WHERE username = %s', (new_password,st.session_state["username"],))
                conn.commit()
                st.success("Password successfully changed!")
    else:
        st.write("Not Signed in")
    
def main():
    
    selected_option = option_menu("Setting", ["Update Personal Information", 
                                                  "Update Payment Details", 
                                                  "Change Password"], 
                                       menu_icon="cast", default_index=0)
    
    if selected_option == "Update Personal Information":
        update_personal_info()
    elif selected_option == "Update Payment Details":
        update_payment_details()
    elif selected_option == "Change Password":
        change_password()

if __name__ == "__main__":
    main()

        
