import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages

st.subheader('Personal Details')

st.session_state['details_error'] = False

if 'finalise' not in st.session_state.keys():
    hide_pages(['Finalise'])
hide_pages(['Message'])


def validate_entries():
    if st.session_state['first_name'] == '':
        st.session_state['details_error'] = True
        st.error('enter first name')
    if st.session_state['last_name'] == '':
        st.session_state['details_error'] = True
        st.error('enter last name')
    if st.session_state['email'] == '':
        st.session_state['details_error'] = True
        st.error('enter email')
    if st.session_state['mobile'] == '':
        st.session_state['details_error'] = True
        st.error('enter mobile number')
    if st.session_state['address'] == '':
        st.session_state['details_error'] = True
        st.error('enter address')


def first_name_flip():
    st.session_state["first_name"] = first_name


def last_name_flip():
    st.session_state["last_name"] = last_name


def email_flip():
    st.session_state["email"] = email


def mobile_flip():
    st.session_state["mobile"] = mobile


def address_flip():
    st.session_state["address"] = address


def agree_details_flip():
    st.session_state["agree_details"] = agree_details


column_0_0, column_0_1 = st.columns(2)
with column_0_0:
    if 'first_name' not in st.session_state:
        st.session_state["first_name"] = ''
    first_name = st.text_input('First Name', value=st.session_state["first_name"], on_change=first_name_flip)
    st.session_state['first_name'] = first_name
with column_0_1:
    if 'last_name' not in st.session_state:
        st.session_state["last_name"] = ''
    last_name = st.text_input('Last Name', value=st.session_state["last_name"], on_change=last_name_flip)
    st.session_state['last_name'] = last_name

st.markdown('##')

column_1_0, column_1_1 = st.columns(2)
with column_1_0:
    if 'email' not in st.session_state:
        st.session_state["email"] = ''
    email = st.text_input('Email', value=st.session_state["email"], on_change=email_flip)
    st.session_state['email'] = email
with column_1_1:
    if 'mobile' not in st.session_state:
        st.session_state["mobile"] = ''
    mobile = st.text_input('Whatsapp No', value=st.session_state["mobile"], on_change=mobile_flip)
    st.session_state['mobile'] = mobile

st.markdown('##')

if 'address' not in st.session_state:
    st.session_state["address"] = ''
address = st.text_input('Address', value=st.session_state["address"], on_change=address_flip)
st.session_state['address'] = address

st.markdown('##')

column_2_0, column_2_1 = st.columns(2)
with column_2_0:
    if "agree_details" not in st.session_state:
        st.session_state["agree_details"] = False
    agree_details = st.checkbox('I agree my details will used for communication purposes', value=st.session_state["agree_details"], on_change=agree_details_flip)
    st.session_state['agree_details'] = agree_details
with column_2_1:
    if agree_details:
        if st.button('proceed to finalise'):
            validate_entries()
            if not st.session_state['details_error']:
                switch_page('finalise')
