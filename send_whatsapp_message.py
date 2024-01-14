"""
from twilio.rest import Client
import streamlit as st
from st_pages import Page, show_pages, hide_pages


def send_whatsapp_message():
    try:
        account_sid = '**************'
        auth_token = '**************'
        client = Client(account_sid, auth_token)

        body_string = ''' '''

        message = client.messages.create(
            body=body_string,
            from_='************',
            to='*************'
        )
        if message.sid:
            st.success('Thank you & you will be contacted shortly', icon="✅")
            st.balloons()
            hide_pages(['Message'])
            st.session_state.clear()
        else:
            st.error('Try again or contact Asantha')
    except:
        st.error('Could not place order, please close the browser tab and reinitiate the service request')"""
