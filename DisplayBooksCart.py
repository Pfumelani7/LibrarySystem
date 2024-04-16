import pandas as pd
import re
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import Un as Un

Un.Nevigate()


# Read the book data from a CSV file
data = pd.read_csv("/Users/da-m1-09/Downloads/Librarydatax.csv")

# Function to display book details
def book_description_section(title, description, ratings, genres, price):
    st.write(f"Book Title: {title}")
    st.write(f"Description: {description}")
    st.write(f"Rating: {ratings}")
    st.write(f"Genres: {genres}")
    st.write(f"Price: R{price}")

# Function to display the main page
def main():
    st.markdown("<h1 style='text-align: center; color: blue;'>📚</h1>", unsafe_allow_html=True)
    st.title("Book Store App")
    
    # Initialize the cart if it doesn't exist in session state
    if "cart" not in st.session_state:
        st.session_state.cart = []

    x = 0
    while x < 100:  # Adjusted the loop condition to stop at 0
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(data["coverImg"][x], width=200) 
            st.write(f"Book Title: {data['title'][x]}")
            st.write(f"Price: R{data['price'][x]}")
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
            if st.button("🛒", key=f"add_{x}"):
                book_details = {"title": data["title"][x], "price": data["price"][x]}
                st.session_state.cart.append(book_details)
            x += 1
        
        with col2:
            st.image(data["coverImg"][x], width=200) 
            st.write(f"Book Title: {data['title'][x]}")
            st.write(f"Price: R{data['price'][x]}")
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
            if st.button("🛒", key=f"add_{x}"):
                book_details = {"title": data["title"][x], "price": data["price"][x]}
                st.session_state.cart.append(book_details)
            x += 1

        with col3:
            st.image(data["coverImg"][x], width=200) 
            st.write(f"Book Title: {data['title'][x]}")
            st.write(f"Price: R{data['price'][x]}")
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
            if st.button("🛒", key=f"add_{x}"):
                book_details = {"title": data["title"][x], "price": data["price"][x]}
                st.session_state.cart.append(book_details)
            x += 1

        with col4:
            st.image(data["coverImg"][x], width=200) 
            st.write(f"Book Title: {data['title'][x]}")
            st.write(f"Price: R{data['price'][x]}")
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
            if st.button("🛒", key=f"add_{x}"):
                book_details = {"title": data["title"][x], "price": data["price"][x]}
                st.session_state.cart.append(book_details)
            x += 1

        with col5:
            st.image(data["coverImg"][x], width=200) 
            st.write(f"Book Title: {data['title'][x]}")
            st.write(f"Price: R{data['price'][x]}")
            id = st.button("View Details", key=x)
            if id:
                st.session_state.x = x                       
                switch_page("testing")
            if st.button("🛒", key=f"add_{x}"):
                book_details = {"title": data["title"][x], "price": data["price"][x]}
                st.session_state.cart.append(book_details)
            x += 1

# Display the cart button and total price in the sidebar
    if st.sidebar.button("View Cart"):
        total_price = sum(float(item['price']) for item in st.session_state.cart)
        st.sidebar.write(f"Total Price: {total_price}")
        for item in st.session_state.cart:
            st.sidebar.write(f"Title: {item['title']}, Price: R{item['price']}")

    # Add a Checkout button in the sidebar
    if st.sidebar.button("Checkout"):
        #st.page_link("pages/Payment.py", label="Details")
        def generate_reference_code():
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for _ in range(8))

        # Function to check if card is still valid based on expiry date
        def is_card_valid(expiry_date):
            try:
                # Parse expiry date
                expiry_date = datetime.strptime(expiry_date, '%m/%y')
                # Get current date
                current_date = datetime.now()
                # Check if expiry date is in the future
                return expiry_date >= current_date.replace(day=1)
            except ValueError:
                # Invalid date format
                return False

        # Main function
        def main():
            st.title('Payment Details')

            # Card number input limited to exactly 16 characters
            card_number = st.text_input('Card Number (16 digits)', max_chars=16)
            if card_number:
                if not re.match(r'^[0-9]{16}$', card_number):
                    st.error('Please enter a valid 16-digit card number.')

            # Expiry date input limited to (mm/yy) format
            expiry_date = st.text_input('Expiry Date (mm/yy)', max_chars=5)
            if expiry_date:
                if not re.match(r'\d{2}/\d{2}', expiry_date):
                    st.error('Please enter the expiry date in the format mm/yy.')
                elif not is_card_valid(expiry_date):
                    st.error('Card has expired or invalid expiry date.')

            # CVV input
            cvv = st.text_input('CVV',max_chars=3)
            if cvv and not re.match(r'^[0-9]{3}$', cvv):
                st.error('Please enter a valid 3-digit CVV.')

            # Submit button
            if st.button('Submit'):
                # Check if card number is exactly 16 characters and contains only digits
                if not card_number or not re.match(r'^[0-9]{16}$', card_number):
                    st.error('Please enter a valid 16-digit card number.')
                elif not expiry_date or not re.match(r'\d{2}/\d{2}', expiry_date) or not is_card_valid(expiry_date):
                    st.error('Please enter a valid expiry date.')
                elif not cvv or not re.match(r'^[0-9]{3}$', cvv):
                    st.error('Please enter a valid 3-digit CVV.')
                else:
                    # Generate reference code
                    reference_code = generate_reference_code()

                    # Show popup with reference code
                    st.success(f'Payment successful! Reference Code: {reference_code}')


# Define the checkout page
def checkout():
     st.title("Checkout")
#st.write("Please enter your payment details here.")

   

# Run the main function if the script is executed
if __name__ == "__main__":
    page = st.session_state.get("page", "main")
if page == "main":
   main()
elif page == "checkout":
    switch_page("Payment")
