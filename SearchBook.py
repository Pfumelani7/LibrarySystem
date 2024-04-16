import streamlit as st
import pandas as pd
from st_pages import hide_pages
#import SearchBackEnd
import Un as Un
from streamlit_extras.switch_page_button import switch_page

Un.Nevigate()


def receivedText(keyword):    
    return keyword.strip()


def readCSV(filename):
    pd.set_option('display.max_colwidth', None)
    return pd.read_csv(filename)

    
#filename = "books_1.Best_Books_Ever.csv"
def searchKeywordOnDatabase(keyword, search_type):
    keyword = receivedText(keyword)
    df = readCSV(filename = "/Users/da-m1-09/Documents/GazaLMS/pages/Lib.csv")
    
    #database which is a DataFrame from our CSV data file
    book = df.loc[df[search_type].str.lower() ==keyword]
    if not book.empty:
        return book
    return None


def main():
    st.title("Search")

    search_options = ["bookId", "title", "author"]
    search_type = st.selectbox("Search a book by: ", search_options)
    userInput = st.text_input(f"Enter {search_type}:  ")

    if st.button("Search"):
    
        book = searchKeywordOnDatabase(receivedText(userInput.lower()),search_type)

        if book is not None:
            st.success("Book was found")
            # Display the book
            index = book["coverImg"].index[0]
            st.session_state.x =  index 
            switch_page("testing")   
        else:
            st.error("Book not found !!!")
            
st.page_link("pages/testing.py", label="View Details")
                   

if __name__ == "__main__":
    main()