import base64
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
from Nucleo import Chatbot
# https://codepen.io/lewismcarey/pen/GJZVoG


df = px.data.iris()
fondo = "background.png"


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64(fondo)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}


[data-testid="stSidebar"] > div:first-child {{
background: rgb(168,23,40);
background: linear-gradient(0deg, rgba(168,23,40,0.8) 0%, rgba(214,29,49,0.8) 8%, rgba(238,128,10,0.8) 82%, rgba(250,189,60,0.8) 100%);
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("")
st.sidebar.header("")

    
with st.sidebar:
    prompt = st.text_input("Infórmate de la transición energética y consigue las medallas")
    prompt = Chatbot(prompt)
    st.write('Repsolín responde: \n', prompt)
    
