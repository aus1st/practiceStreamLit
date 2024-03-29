import streamlit as st

st.title('Counter App with session')

if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')


if increment:
    st.session_state.count += 1
    st.success(f'Count: {st.session_state.count}')
