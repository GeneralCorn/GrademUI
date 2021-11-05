import streamlit as st

st.set_page_config(page_title='Gradem', page_icon="💎")
st.title('Welcome to Gradem!')
st.header('Gradem is a centralized IB MYP design comments generator')


student = st.file_uploader("Upload student.csv file", type=['csv'])

sentences = st.file_uploader("Upload comment options", type=['csv'])
