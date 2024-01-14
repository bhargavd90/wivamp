import streamlit as st


def handle_service():
    def select_handle_service_flip():
        st.session_state['select_handle_service'] = select_handle_service

    def condition_handle_1_flip():
        st.session_state['condition_handle_1'] = condition_handle_1

    def condition_handle_2_flip():
        st.session_state['condition_handle_2'] = condition_handle_2

    def handle_repair_quantity_flip():
        st.session_state["handle_repair_quantity"] = handle_repair_quantity

    column_1_0, column_1_1 = st.columns(2)
    with column_1_0:
        st.subheader('2. Handle Repair')
        st.image('6408176.jpg')
    with column_1_1:
        st.subheader('30 :euro:')
        if "select_handle_service" not in st.session_state:
            st.session_state["select_handle_service"] = False
        if "condition_handle_1" not in st.session_state:
            st.session_state["condition_handle_1"] = False
        if "condition_handle_2" not in st.session_state:
            st.session_state["condition_handle_2"] = False
        if "handle_repair_quantity" not in st.session_state:
            st.session_state["handle_repair_quantity"] = 1
        select_handle_service = st.checkbox('select service ', value=st.session_state["select_handle_service"], on_change=select_handle_service_flip)
        st.session_state['select_handle_service'] = select_handle_service
        if select_handle_service:
            st.markdown("---")
            condition_handle_1 = st.checkbox('condition handle 1', value=st.session_state["condition_handle_1"], on_change=condition_handle_1_flip)
            st.session_state['condition_handle_1'] = condition_handle_1
            condition_handle_2 = st.checkbox('condition handle 2', value=st.session_state["condition_handle_2"], on_change=condition_handle_2_flip)
            st.session_state['condition_handle_2'] = condition_handle_2
            if condition_handle_1 and condition_handle_2:
                handle_repair_quantity = st.number_input('Quantity ', min_value=1, max_value=10, value=st.session_state["handle_repair_quantity"], on_change=handle_repair_quantity_flip)
                st.session_state['handle_repair_quantity'] = handle_repair_quantity
                if st.button('add service  '):
                    st.toast(str(handle_repair_quantity) + ' handle service added')

    st.markdown("---")
