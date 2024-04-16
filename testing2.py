# import pandas as pd
# import streamlit as st
# from st_pages import hide_pages

# st.set_page_config(layout='wide', page_title='Address Book', page_icon='📚', initial_sidebar_state="collapsed")

# data = pd.read_csv("/Users/da-m1-40/Downloads/lib.csv")
# hide_pages(["display"])
# hide_pages(["testing"])


# st.page_link("display.py", label="Home")

# selected_book_index = st.session_state.x
# selected_book = data.iloc[selected_book_index]
       
# print("session x")          
# image = selected_book["coverImg"]
# title = selected_book['title']
# description = selected_book['description']
# genres = selected_book['genres']            
# price = selected_book['price']

# st.image(image, width=200)
# st.markdown(title)
# st.markdown(description)
# st.markdown(genres)
# st.markdown(price)

import pandas as pd
import streamlit as st
from st_pages import hide_pages
import Un as Un

Un.Nevigate()


from streamlit_extras.switch_page_button import switch_page

data = pd.read_csv("/Users/da-m1-09/Documents/GazaLMS/pages/Lib.csv")



id = st.button("Back to Library...")
if id:
    switch_page("DisplayBooksCart")

selected_book_index = st.session_state.x
selected_book = data.iloc[selected_book_index]
       
image = selected_book["coverImg"]
title = selected_book['title']
description = selected_book['description']
genres = selected_book['genres']            
price = selected_book['price']

col1, col2 = st.columns(2)
with col1:
        st.image(image, width=400)
with col2:

    st.title(title)
    st.markdown(description)
    col1, col2 = st.columns(2)
    with col1:
         st.title("Tags:")
    with col2:
        st.markdown(genres)
        pay = st.button("Checkout To Lend A book")
        if pay:
            switch_page("Payment")
         
    st.title(price)


if "x" not in st.session_state:
        st.session_state.x = 0

x = 200
while x < 300:  # Adjusted the loop condition to stop at 0
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
                
            x += 1
        with col2:   
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
                 
            x += 1
        with col3:
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
                 
            x += 1
        with col4:
            st.image(data["coverImg"][x], width=200) 
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
                  
            x += 1
        with col5:
            st.image(data["coverImg"][x], width=200)
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
            
                
                 
                
            x += 1
            
            
      


