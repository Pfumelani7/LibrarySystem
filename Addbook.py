import streamlit as st
import pandas as pd
from st_pages import hide_pages
import Un as Un

Un.Nevigate()

#if st.button("logout"):
    #st.session_state.loggedin = ""
def add_book(series, title, author, rating, description, language, isbn, genres, year, edition, pages, publisher, publishDate, characters, bookFormat, firstPublishDate, price, BookCover):
    global books_df
    book = "/Users/da-m1-09/Downloads/" + BookCover
    new_row = {
        "title": title,
        "author": author,
        "description": description,
        "language": language,
        "isbn": isbn,
        "genres": genres,
        "year": year,
        "edition": edition,
        "pages": pages,
        "publisher": publisher,
        "publishDate": publishDate,
        "series": series,
        "characters": characters,
        "bookFormat": bookFormat,
        "firstPublishDate": firstPublishDate,
        "price": price,
        "rating": rating,
        "coverImg": book,
    
    }
    books_df = books_df._append(new_row, ignore_index=True)
    # Write the updated dataset back to CSV
    books_df.to_csv("/Users/da-m1-09/Documents/GazaLMS/pages/Lib.csv", index=False)   
     
        
        
# Load the existing dataset
books_df = pd.read_csv("/Users/da-m1-09/Documents/GazaLMS/pages/Lib.csv", sep=",")

# Function to add a book to the dataset
def main():
    st.title("Gaza Library Management System")
    st.header("Add Book")
    title = st.text_input("Title:")
    author = st.text_input("Author:")
    rating = st.text_input("Rating:")
    description = st.text_area("Description:")
    language = st.text_input("Language:")
    isbn = st.text_input("ISBN:")
    genres = st.text_input("Genres (comma-separated):")
    year = st.text_input("Year:")
    edition = st.text_input("Edition:")
    pages = st.text_input("Pages:")
    publisher = st.text_input("Publisher:")
    series = st.text_input("Series:")
    price = st.text_input("Price:")
    bookFormat = st.text_input("Book Format:")
    firstPublishDate = st.text_input("First Publish Date:")
    publishDate = st.text_input("Publish Date:")
    BookCover = st.file_uploader("Choose a BookCover to upload", accept_multiple_files=True)
    for book in BookCover:
        bytes_data = book.read()
        st.write("filename:", book.name)
        BookCover = book.name



    if st.button("Add"):
        add_book(series, title, author, rating, description, language, isbn, genres, year, edition, pages, publisher, publishDate, "", bookFormat, firstPublishDate, price,BookCover)
        st.success("Book added successfully.")

    st.header("View Book Details")
    st.subheader("Basic Information")
    st.write(f"Title: {title}")
    st.write(f"Author: {author}")
    st.write(f"Description: {description}")
    st.write(f"Language: {language}")
    st.write(f"ISBN: {isbn}")
    st.write(f"Genres: {genres}")
    st.write(f"Year: {year}")
    st.write(f"Edition: {edition}")
    st.write(f"Pages: {pages}")
    st.write(f"Publisher: {publisher}")
    
    st.subheader("Dates")
    st.write(f"Publish Date: {publishDate}")
    st.write(f"First Publish Date: {firstPublishDate}")
    st.write(f"Series: {series}")
    
    st.subheader("Additional Information")
    st.write(f"Price: {price}")
    st.write(f"Rating: {rating}")
    st.write(f"Book Format: {bookFormat}")
    st.write(f"BookCover: {BookCover}")

if __name__ == "__main__":
    main()