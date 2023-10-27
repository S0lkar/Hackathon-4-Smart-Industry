import base64
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
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
background: linear-gradient(0deg, rgba(168,23,40,0.8) 0%, rgba(214,29,49,0.8) 8%, rgba(250,250,250,0.8) 44%, rgba(238,128,10,0.8) 82%, rgba(250,189,60,0.8) 100%);
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

import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
with st.sidebar:
    prompt = st.text_input("¿Quieres saber algo más sobre la transición energética?")
    prompt = get_random_string(4)
    st.write('Repbot dice: ', prompt)
    

output = "Buenas noches"