import streamlit as st


def knocking_service():
    def select_knocking_service_flip():
        st.session_state['select_knocking_service'] = select_knocking_service

    def condition_knocking_1_flip():
        st.session_state['condition_knocking_1'] = condition_knocking_1

    def condition_knocking_2_flip():
        st.session_state['condition_knocking_2'] = condition_knocking_2

    def knocking_repair_quantity_flip():
        st.session_state["knocking_repair_quantity"] = knocking_repair_quantity

    column_1_0, column_1_1 = st.columns(2)
    with column_1_0:
        st.subheader('4. Knocking')
        st.image('6340825.jpg')
    with column_1_1:
        st.subheader('10 :euro:')
        if "select_knocking_service" not in st.session_state:
            st.session_state["select_knocking_service"] = False
        if "condition_knocking_1" not in st.session_state:
            st.session_state["condition_knocking_1"] = False
        if "condition_knocking_2" not in st.session_state:
            st.session_state["condition_knocking_2"] = False
        if "knocking_repair_quantity" not in st.session_state:
            st.session_state["knocking_repair_quantity"] = 1
        select_knocking_service = st.checkbox('select service   ', value=st.session_state["select_knocking_service"], on_change=select_knocking_service_flip)
        st.session_state['select_knocking_service'] = select_knocking_service
        if select_knocking_service:
            st.markdown("---")
            condition_knocking_1 = st.checkbox('condition knocking 1', value=st.session_state["condition_knocking_1"], on_change=condition_knocking_1_flip)
            st.session_state['condition_knocking_1'] = condition_knocking_1
            condition_knocking_2 = st.checkbox('condition knocking 2', value=st.session_state["condition_knocking_2"], on_change=condition_knocking_2_flip)
            st.session_state['condition_knocking_2'] = condition_knocking_2
            if condition_knocking_1 and condition_knocking_2:
                knocking_repair_quantity = st.number_input('Quantity   ', min_value=1, max_value=10, value=st.session_state["knocking_repair_quantity"], on_change=knocking_repair_quantity_flip)
                st.session_state['knocking_repair_quantity'] = knocking_repair_quantity
                if st.button('add service    '):
                    st.toast(str(knocking_repair_quantity) + ' knocking service added')

    st.markdown("---")
