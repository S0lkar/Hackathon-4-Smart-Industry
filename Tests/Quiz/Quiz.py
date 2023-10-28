import base64
import streamlit as st
import plotly.express as px
from Nucleo import Chatbot
from PIL import Image

df = px.data.iris()
Racha = 0
Map = 1

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

page = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background: rgb(210,154,20);
background: linear-gradient(0deg, rgba(210,154,20,1) 0%, rgba(254,252,248,1) 47%, rgba(255,255,255,1) 100%);
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page, unsafe_allow_html=True)
st.title("#Nombre")
st.header("Mira tu que slogan mas apañao")
placeholder = st.empty()
with placeholder.container():
    st.image(Image.open('0.png'))

def Correcto():
    global Racha
    placeholder.empty()
    with placeholder.container():
        Racha += 1
        st.image(Image.open(str(Racha) + '.png'), caption='¡Bien hecho!')
        
def Incorrecto():
    global Racha
    placeholder.empty()
    with placeholder.container():
        Racha -= 1
        if Racha < 0:
            Racha = 0
            
        st.image(Image.open(str(Racha) + '.png'), caption='Ups...')




if st.button("A", type="primary"):
    if Map == 1:
        Correcto()
    else:
        Incorrecto()

if st.button("B", type="primary"):
    if Map == 2:
        Correcto()
    else:
        Incorrecto()
        
if st.button("C", type="primary"):
    if Map == 3:
        Correcto()
    else:
        Incorrecto()
    

