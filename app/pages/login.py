import streamlit as st
from db_utilities import user_login

st.title("This is the login page")

email = st.text_input("Enter email")
# if username:
#     st.write("the username is: ", username)
password = st.text_input("Enter a Password", type='password')
# Password encryption code
# if password:
#     st.write("Show Encrypted password")


col1, col2 = st.columns([1,1])

with col1:
    if (st.button("Log In")):
        if(email and password and user_login(email, password)):
            st.switch_page("pages/create_connection.py")
        else:  
            st.warning('Invalid User Email or Password!')
    
with col2:
    if st.button("New user? Signup"):
        st.switch_page("pages/signup.py")

