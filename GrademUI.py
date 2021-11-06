import streamlit as st
import random
import csv as csv
import io

# Favicon and Headings
st.set_page_config(page_title='Gradem', page_icon="💎")
st.title('Welcome to Gradem!')
st.header('Gradem is a centralized IB MYP design comments generator')

#File I/O
student = st.file_uploader("Upload student.csv file", type=['csv'])
sentences = st.file_uploader("Upload comment options", type=['csv'])

if student is not None:

    with io.TextIOWrapper(student, encoding='utf-8') as tf:
        student_reader = csv.reader(tf)
        S_Dict = {rows[0]: rows[1] for rows in student_reader}
        st.write(type(student_reader))
        st.write(S_Dict)

else:
    st.stop()

if sentences is not None: 
    with io.TextIOWrapper(sentences, encoding='utf-8') as tf2:
        sentence_reader = csv.reader(tf2)
        columnlist = list(sentence_reader)
        for i in columnlist:
            i.pop(0)
        st.write(columnlist)
else:
    st.stop()

