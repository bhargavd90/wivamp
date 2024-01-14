import streamlit as st
from st_pages import hide_pages


def send_email():
    try:
        sent_email = True
        if sent_email:
            st.success('Thank you & you will be contacted shortly', icon="✅")
            st.balloons()
            hide_pages(['Message'])
            st.session_state.clear()
        else:
            st.error('Try again or contact Asantha')
    except:
        st.error('Could not place order, please close the browser tab and reinitiate the service request')
