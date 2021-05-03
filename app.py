import streamlit as st
import base64

# set principal.
st.set_page_config(
    page_title="Que esta pasando?",
    page_icon="https://d1nxzqpcg2bym0.cloudfront.net/google_play/com.synergygb.megazord.MiMercantil/b3514b2e-4539-11e8-9862-35b57a16ceeb/128x128",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

# set del backgrund
@st.cache
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded

def image_tag(path):
    encoded = load_image(path)
    tag = f'<img src="data:image/png;base64,{encoded}">'
    return tag

def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <body>
    <style>
    body {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    </body>

    '''
    return style

image_path = 'images/fondo.png'
image_link = 'https://docs.python.org/3/'

st.write(background_image_style(image_path), unsafe_allow_html=True)

# Código de solicitar informacion
st.text('Analisis de sentimiento de tweets usando modelo de Machine Learning.')

# Ingresa el tweet a analizar
tweet = st.text_input('Introduza el tweet a analizar ')

if st.button('Analizar'):
    # print is visible in server output, not in the page
    if len(tweet) > 0:
        st.success('Tweet analizado con éxito')
    else:
        st.error('Debe incluir un tweet válido')


