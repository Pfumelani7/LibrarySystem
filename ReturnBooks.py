import streamlit as st
from st_pages import hide_pages
import Un as Un
import pandas as pd

Un.Nevigate()

    

def return_instructions():
    st.header("How to Return Rented Books")
    st.write("Follow these step-by-step instructions to return rented books to GAZA library:")

    steps = [
        "Log in to Your Account: Visit the GAZA library  website and log in to your account using your username and password.",
        "Ensure that the books returned are in good condition and are eligible for return(check for damages  or missing components (e.g., missing pages, torn covers)",
        "Manually enter the book's information into the system to register its return as per list below",
        "Fine Calculation:Calculate the amount due to the customer by entering the Book ID and clicking on get price",
        "After entering all the details, click on return book, the book returned successfully message will pop up.",
        ]

    for i, step in enumerate(steps, start=1):
        st.markdown(f"{i}. {step}")



def return_book():
    data = pd.read_csv("/Users/da-m1-09/Documents/GazaLMS/pages/newdata.csv")

    st.title("Return Book to Gaza Library")
    # Input fields for returning details
    book_id = st.text_input("Enter book ID of the book to return:")
    condition = st.selectbox("Pick one:", ["Good", "Moderate", "Excellent", "Poor"])
    comments = st.text_input("Enter any comments relating to the condition of the book")
    return_date = st.date_input("Enter Return Date:")
    status= st.selectbox("pick one",["available","not available"])
    # refund_deposit = st.number_input("Enter the amount due to customer")
    data2 = data[data["bookId"] == book_id]
    if len(data2) > 0: 
        refund_price =0.6*float(data2['price'].values[0])
    else:
        refund_price=0   
    
    data.loc[data["bookId"] == book_id, ["comments","condition","return_date", "refund_price","status.1"]] = [comments, condition, return_date, round(float(refund_price),2),status]
    st.write(f"Amount due to customer: R{round(float(refund_price),2)}")
    if condition and comments and return_date and book_id:
        if st.button("Return book"):
            data.to_csv("/Users/da-m1-09/Documents/GazaLMS/pages/newdata.csv",index=False)
            st.success('Book returned on the system successfully')
           
    else:
        st.write("Please enter all fields")
 # Call the function to display the return
return_instructions()
return_book()

    
