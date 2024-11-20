import streamlit as st
import db_utilities

st.title("This is the signup page")

username = st.text_input('Enter your Username')
email = st.text_input('Enter your email id')
password = st.text_input('Enter your password', type='password')
cnf_password = st.text_input('Confirm your password', type='password')


if st.button('Sign Up'):
    if(password == cnf_password):
        db_utilities.add_new_user(username, email, password)
        # st.switch_page('pages/create_connection.py')
        st.write('New user created!')


if st.button("Back to Homepage"):
    st.switch_page("./homepage.py")
