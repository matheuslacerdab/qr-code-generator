#Importing the libraries
import pyqrcode
import streamlit as st

#Function for QR-Code generation
def gen_qrcode(link):
    qr_code = pyqrcode.create(link)
    qr_code.png('src/qr-code-link.png', scale=3)

    st.image('src/qr-code-link.png')

#Streamlit Form
with st.form("my_form", clear_on_submit=True):
    st.write('Gerador de QR-Code')
    link = st.text_input('Link:')
    submitted = st.form_submit_button('Gerar QR-Code')

    if submitted:
        if link:
            gen_qrcode(link)
        else:
            st.write('Insira algum link!')