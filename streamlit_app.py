import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles

if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')


MenuButtons(get_roles())
st.header('Home page')


if ss.authentication_status:
    st.write('This content is only accessible for logged in users.')
else:
    st.write('Please log in on login page.')
