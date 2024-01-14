import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages


def do_stuff_on_page_load():
    # To set the page layout to wide on page load
    st.set_page_config(layout="wide")


do_stuff_on_page_load()


show_pages([
    Page("main.py", "Information"),
    Page("repairs.py", "Repairs"),
    Page("details.py", "Details"),
    Page("finalise.py", "Finalise"),
    Page("message.py", "Message"),
])

if 'finalise' not in st.session_state.keys():
    hide_pages(['Finalise'])
hide_pages(['Message'])

st.title("WEVAMP REPAIRS")
st.markdown("##")
st.header("This page if for bat repairs")
st.subheader('This page if for bat repairs')
st.markdown("##")
st.markdown("##")
st.markdown("##")
if st.button('proceed to details'):
    switch_page('repairs')
