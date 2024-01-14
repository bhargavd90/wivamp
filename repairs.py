import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages
from bat_service import bat_service
from handle_service import handle_service
from gutting_service import gutting_service
from knocking_service import knocking_service

st.subheader('Repair Services')

if 'finalise' not in st.session_state.keys():
    hide_pages(['Finalise'])
hide_pages(['Message'])

bat_service()
handle_service()
gutting_service()
knocking_service()

column_last_0, column_last_1 = st.columns(2)
with column_last_0:
    if st.button('proceed to fill personal details'):
        switch_page('details')
with column_last_1:
    if 'finalise' in st.session_state.keys():
        if st.button('proceed to finalise'):
            switch_page('finalise')
