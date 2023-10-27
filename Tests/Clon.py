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

components.html("""
<div class="ticker-wrap">
<div class="ticker">
  <div class="ticker__item">¡Repsol es chupiguay!</div>
  <div class="ticker__item">¡La descarbonizacion mola!</div>
  <div class="ticker__item">Buenos días</div>
</div>
</div>
""")

with open('rotatorio.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("")
st.sidebar.header("")