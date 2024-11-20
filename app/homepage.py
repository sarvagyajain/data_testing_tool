import streamlit as st
from db_utilities import user_login

st.title("Welcome to Data Testing Tool")

if 'user_state' not in st.session_state:
    st.session_state.user_state = {
        'username': '',
        'logged_in': False
    }

if not st.session_state.user_state['logged_in']:
    username = st.text_input("Enter your Username")
    password = st.text_input("Enter Password", type='password')

    col1, col2 = st.columns([1,1])

    with col1:
        if st.button("Log In"): 
            if(username and password and user_login(username, password)):
                st.session_state.user_state['username'] = username
                st.session_state.user_state['logged_in'] = True
                st.switch_page("pages/create_connection.py")
            else:  
                st.warning('Invalid User Email or Password!')
    with col2:
        if st.button("New user? Signup"):
            st.switch_page("pages/signup.py")

elif st.session_state.user_state['logged_in']: 
    st.write(f"You are logged in as {st.session_state.user_state['username']}")
    st.write('Choose from below options')
    if(st.button('Create Connection')):
        st.switch_page('pages/create_connection.py')


