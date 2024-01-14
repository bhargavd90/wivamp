from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from st_pages import hide_pages
# from send_whatsapp_message import send_whatsapp_message
from send_email import send_email

hide_pages(['Information'])
hide_pages(['Repairs'])
hide_pages(['Details'])
hide_pages(['Finalise'])

# :incoming_envelope:

if 'button_disabled' not in st.session_state:
    st.session_state['button_disabled'] = False

if not st.session_state['button_disabled']:
    if "df" in st.session_state.keys():
        st.info('Upload necessary images and confirm the order by clicking the button below, This will send a message to '
                'Asantha')
        for index, row in st.session_state["df"][:-1].iterrows():
            for quantity_no in range(row[1]):
                label = row[0] + " " + str(quantity_no + 1)
                user_uploaded_images = st.file_uploader(label, accept_multiple_files=True)
                key_name = label.replace(" ", "_") + "_uploaded_images"
                st.session_state[key_name] = user_uploaded_images
                st.markdown("---")
        if st.button("confirm service request", disabled=st.session_state['button_disabled']):
            st.session_state['button_disabled'] = True
            switch_page('message')
    else:
        hide_pages(['Message'])
        st.info('this session has been closed')
else:
    send_email()
