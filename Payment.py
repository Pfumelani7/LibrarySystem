import streamlit as st
import random
import string
import re
from datetime import datetime
import Un as Un

Un.Nevigate()
#import pricex

# Function to return a book (payment method)
    

# Function to generate a random alphanumeric reference code
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

if __name__ == '__main__':
    main()