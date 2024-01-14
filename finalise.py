import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages

hide_pages(['Message'])

st.session_state['finalise'] = True

service = []
quantity = []
cost = []
total_quantity = 0
total_cost = 0

column_details_0, column_details_1 = st.columns(2)
with column_details_0:
    st.subheader(':bust_in_silhouette: Details Summary')
    st.markdown('##')
    st.text('First Name : ' + st.session_state["first_name"])
    st.text('last Name : ' + st.session_state["last_name"])
    st.text('Email : ' + st.session_state["email"])
    st.text('Whatsapp No : ' + st.session_state["mobile"])
    st.text('Address : ' + st.session_state["address"])
with column_details_1:
    if st.button('modify details'):
        switch_page('details')

st.markdown('---')

column_repairs_0, column_repairs_1 = st.columns(2)
with column_repairs_0:
    st.subheader(':shopping_trolley: Repairs Summary')
    if 'select_bat_service' in st.session_state.keys() or 'select_handle_service' in st.session_state.keys() or 'select_gutting_service' in st.session_state.keys() or 'select_knocking_service' in st.session_state.keys():
        if st.session_state["select_bat_service"]:
            if st.session_state["condition_bat_1"] and st.session_state["condition_bat_2"]:
                service.append('Bat Repair')
                quantity.append(st.session_state['bat_repair_quantity'])
                cost.append(40 * st.session_state['bat_repair_quantity'])
                total_quantity = total_quantity + st.session_state['bat_repair_quantity']
                total_cost = total_cost + (40 * st.session_state['bat_repair_quantity'])
        if st.session_state["select_handle_service"]:
            if st.session_state["condition_handle_1"] and st.session_state["condition_handle_2"]:
                service.append('Handle Repair')
                quantity.append(st.session_state['handle_repair_quantity'])
                cost.append(30 * st.session_state['handle_repair_quantity'])
                total_quantity = total_quantity + st.session_state['handle_repair_quantity']
                total_cost = total_cost + (30 * st.session_state['handle_repair_quantity'])
        if st.session_state["select_gutting_service"]:
            if st.session_state["condition_gutting_1"] and st.session_state["condition_gutting_2"]:
                service.append('Gutting')
                quantity.append(st.session_state['gutting_repair_quantity'])
                cost.append(20 * st.session_state['gutting_repair_quantity'])
                total_quantity = total_quantity + st.session_state['gutting_repair_quantity']
                total_cost = total_cost + (20 * st.session_state['gutting_repair_quantity'])
        if st.session_state["select_knocking_service"]:
            if st.session_state["condition_knocking_1"] and st.session_state["condition_knocking_2"]:
                service.append('Knocking')
                quantity.append(st.session_state['knocking_repair_quantity'])
                cost.append(10 * st.session_state['knocking_repair_quantity'])
                total_quantity = total_quantity + st.session_state['knocking_repair_quantity']
                total_cost = total_cost + (10 * st.session_state['knocking_repair_quantity'])
        if service:
            service.append('Total : ')
            quantity.append(total_quantity)
            cost.append(total_cost)
            df = pd.DataFrame(
                {'Service': service,
                 'Quantity': quantity,
                 'Cost': cost
                 })
            st.session_state['df'] = df
            st.dataframe(df.style.applymap(
                lambda _: "background-color: CornflowerBlue;", subset=([len(service)-1], slice(None))
            ), hide_index=True)
        else:
            st.text('No repair service selected')
    else:
        st.text('No repair service selected')

with column_repairs_1:
    if service:
        if st.button('modify repairs'):
            switch_page('repairs')
    else:
        if st.button('add repairs'):
            switch_page('repairs')
if service:
    st.markdown('---')
    if st.button('send service request'):
        switch_page('message')
