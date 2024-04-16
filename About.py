import streamlit as st
from st_pages import hide_pages
import streamlit as st
import Un as Un

Un.Nevigate()

#if st.button("logout"):
    #st.session_state.loggedin = ""
    


def about_bookstore():
    st.title('About Gaza library')
    about_html = '''
        <div style="font-family: 'Times New Roman', Times, serif; font-size: 20px; line-height: 1.6; color: #F0F0F0;">
            Welcome to <span style="font-weight: bold; color: #4CAF50;">GAZA Library</span>, where literature meets convenience. We're an online book rental store dedicated to providing readers with a seamless and enjoyable experience in discovering and renting their favorite books.
        </div>
        <br>
        <h3 style="font-family: 'Arial Black', Gadget, sans-serif; font-size: 24px; font-weight: bold; color: #4CAF50;">Our Mission</h3>
        <div style="font-family: 'Arial', sans-serif; font-size: 20px; line-height: 1.6; color: #F0F0F0;">
            At GAZA Library, our mission is to foster a love for reading by making books more accessible and affordable to everyone. We believe that literature has the power to inspire, educate, and entertain, and we're committed to connecting readers with the stories that resonate with them.
        </div>
        <br>
        <h3 style="font-family: 'Arial Black', Gadget, sans-serif; font-size: 24px; font-weight: bold; color: #4CAF50;">What We Offer</h3>
        <ul style="font-family: 'Arial', sans-serif; font-size: 20px; line-height: 1.6; color: #F0F0F0; list-style-type: disc; margin-left: 30px;">
            <li>Vast Selection: Explore our extensive catalog featuring a diverse range of genres, from timeless classics to contemporary bestsellers. Whether you're into fiction, non-fiction, romance, mystery, or sci-fi, we have something for every reader's taste.</li>
            <li>Convenient Rentals: Don't want to commit to buying a book? No problem! With our rental service, you can enjoy your favorite reads for a fraction of the cost. Simply choose the rental option at checkout and return the book when you're done.</li>
            <li>Secure Payments: Shop with confidence knowing that your transactions are safe and secure. We utilize state-of-the-art encryption technology to protect your personal and financial information at every step of the process.</li>
            <li>Responsive Support: Have a question or need assistance? Our dedicated customer support team is here to help. Whether it's recommending a book, tracking an order, or resolving an issue, we're committed to providing prompt and friendly assistance to ensure your satisfaction.</li>
        </ul>
        <br>
        <h3 style="font-family: 'Arial Black', Gadget, sans-serif; font-size: 24px; font-weight: bold; color: #4CAF50;">Our Story</h3>
        <div style="font-family: 'Arial', sans-serif; font-size: 20px; line-height: 1.6; color: #F0F0F0;">
            GAZA Library was founded with a passion for literature and a vision to revolutionize the way people discover and enjoy books. What started as a small idea has grown into a thriving online community of book lovers united by their shared love for reading.
        </div>
        <br>
        <h3 style="font-family: 'Arial Black', Gadget, sans-serif; font-size: 24px; font-weight: bold; color: #4CAF50;">Get in Touch</h3>
        <div style="font-family: 'Arial', sans-serif; font-size: 20px; line-height: 1.6; color: #F0F0F0;">
            We love hearing from our customers! Whether you have feedback, suggestions, or just want to say hello, we'd love to hear from you. Feel free to reach out to us via email, phone, or social media.
        </div>
        <br>
        <div style="font-family: 'Arial', sans-serif; font-size: 20px; line-height: 1.6; color: #F0F0F0;">
            Thank you for choosing <span style="font-weight: bold; color: #4CAF50;">GAZA Library</span> as your go-to destination for all things books. Happy reading!
        </div>
    '''

    st.markdown(about_html, unsafe_allow_html=True)

    st.title('Contact Information')
    st.write('Email: gazalibrary@gmail.com')
    st.write('Phone: 011-855-1231')
    st.write('Whatsapp: 0730432516')
    st.write('Website:  //////////')
    

about_bookstore()

    
    
