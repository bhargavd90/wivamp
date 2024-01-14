from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from st_pages import hide_pages
# from send_whatsapp_message import send_whatsapp_message
from send_email import send_email

hide_pages(['Information'])
hide_pages(['Repairs'])
hide_pages(['Details'])
hide_pages(['Finalise'])

if 'button_disabled' not in st.session_state:
    st.session_state['button_disabled'] = False

if not st.session_state['button_disabled']:
    st.info('Upload necessary images and confirm the order by clicking the button below, This will send a message to Asantha')
    user_uploaded_images = st.file_uploader(" ", accept_multiple_files=True)
    st.session_state['user_uploaded_images'] = user_uploaded_images
    if st.button("confirm service request", disabled=st.session_state['button_disabled']):
        st.session_state['button_disabled'] = True
        switch_page('message')
else:
    send_email()
