#Importing the libraries
from sklearn.preprocessing import scale
import pyqrcode
import streamlit as st
import base64

#Function for QR-Code generation
def gen_qrcode(link):
    qr_code = pyqrcode.create(link)
    #qr_code.show()
    #qr_code.png('qr-code-link.png', scale=3)
    img = base64.b64decode(qr_code.png_as_base64_str(scale=3))

    st.image(img)

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