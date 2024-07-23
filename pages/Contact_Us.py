import streamlit as st


with st.form(key='myemailForm'):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message here")
    button = st.form_submit_button("Submit")