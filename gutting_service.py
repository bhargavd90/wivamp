import streamlit as st


def gutting_service():
    def select_gutting_service_flip():
        st.session_state['select_gutting_service'] = select_gutting_service

    def condition_gutting_1_flip():
        st.session_state['condition_gutting_1'] = condition_gutting_1

    def condition_gutting_2_flip():
        st.session_state['condition_gutting_2'] = condition_gutting_2

    def gutting_repair_quantity_flip():
        st.session_state["gutting_repair_quantity"] = gutting_repair_quantity

    column_1_0, column_1_1 = st.columns(2)
    with column_1_0:
        st.subheader('3. Gutting')
        st.image('6374715.jpg')
    with column_1_1:
        st.subheader('20 Euro')
        if "select_gutting_service" not in st.session_state:
            st.session_state["select_gutting_service"] = False
        if "condition_gutting_1" not in st.session_state:
            st.session_state["condition_gutting_1"] = False
        if "condition_gutting_2" not in st.session_state:
            st.session_state["condition_gutting_2"] = False
        if "gutting_repair_quantity" not in st.session_state:
            st.session_state["gutting_repair_quantity"] = 1
        select_gutting_service = st.checkbox('select service  ', value=st.session_state["select_gutting_service"], on_change=select_gutting_service_flip)
        st.session_state['select_gutting_service'] = select_gutting_service
        if select_gutting_service:
            st.markdown("---")
            condition_gutting_1 = st.checkbox('condition gutting 1', value=st.session_state["condition_gutting_1"], on_change=condition_gutting_1_flip)
            st.session_state['condition_gutting_1'] = condition_gutting_1
            condition_gutting_2 = st.checkbox('condition gutting 2', value=st.session_state["condition_gutting_2"], on_change=condition_gutting_2_flip)
            st.session_state['condition_gutting_2'] = condition_gutting_2
            if condition_gutting_1 and condition_gutting_2:
                gutting_repair_quantity = st.number_input('Quantity  ', min_value=1, max_value=10, value=st.session_state["gutting_repair_quantity"], on_change=gutting_repair_quantity_flip)
                st.session_state['gutting_repair_quantity'] = gutting_repair_quantity
                if st.button('add service   '):
                    st.toast(str(gutting_repair_quantity) + ' gutting service added')

    st.markdown("---")
