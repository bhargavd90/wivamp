import streamlit as st


def bat_service():
    def select_bat_service_flip():
        st.session_state['select_bat_service'] = select_bat_service

    def condition_bat_1_flip():
        st.session_state['condition_bat_1'] = condition_bat_1

    def condition_bat_2_flip():
        st.session_state['condition_bat_2'] = condition_bat_2

    def bat_repair_quantity_flip():
        st.session_state["bat_repair_quantity"] = bat_repair_quantity

    column_1_0, column_1_1 = st.columns(2)
    with column_1_0:
        st.subheader('1. Bat Repair')
        st.image('6340825.jpg')
    with column_1_1:
        st.subheader('40 :euro:')
        if "select_bat_service" not in st.session_state:
            st.session_state["select_bat_service"] = False
        if "condition_bat_1" not in st.session_state:
            st.session_state["condition_bat_1"] = False
        if "condition_bat_2" not in st.session_state:
            st.session_state["condition_bat_2"] = False
        if "bat_repair_quantity" not in st.session_state:
            st.session_state["bat_repair_quantity"] = 1
        select_bat_service = st.checkbox('select service', value=st.session_state["select_bat_service"], on_change=select_bat_service_flip)
        st.session_state['select_bat_service'] = select_bat_service
        if select_bat_service:
            st.markdown("---")
            condition_bat_1 = st.checkbox('condition bat 1', value=st.session_state["condition_bat_1"], on_change=condition_bat_1_flip)
            st.session_state['condition_bat_1'] = condition_bat_1
            condition_bat_2 = st.checkbox('condition bat 2', value=st.session_state["condition_bat_2"], on_change=condition_bat_2_flip)
            st.session_state['condition_bat_2'] = condition_bat_2
            if condition_bat_1 and condition_bat_2:
                bat_repair_quantity = st.number_input('Quantity', min_value=1, max_value=10, value=st.session_state["bat_repair_quantity"], on_change=bat_repair_quantity_flip)
                st.session_state['bat_repair_quantity'] = bat_repair_quantity
                if st.button('add service '):
                    st.toast(str(bat_repair_quantity) + ' bat service added')

    st.markdown("---")
