import streamlit as st
import base64

#from QueEstaPasando import trainer_ml


# set principal.
st.set_page_config(
    page_title="Que esta pasando?",
    page_icon="https://d1nxzqpcg2bym0.cloudfront.net/google_play/com.synergygb.megazord.MiMercantil/b3514b2e-4539-11e8-9862-35b57a16ceeb/128x128",
    layout="centered", # wide
    initial_sidebar_state="collapsed") # collapsed

# imagen de fondo
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://cdn.hipwallpaper.com/m/80/8/OWFqjZ.jpg");
    }
    .sidebar.sidebar.sidebar-content {
        background: url("https://cdn.hipwallpaper.com/m/80/8/OWFqjZ.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
    )


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
my_page = st.sidebar.radio('Menú', ['','Predicción', 'Estadísticas'])
st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
if my_page == 'Predicción':
      
    image_path = 'images/fondo.png'
    image_link = 'https://docs.python.org/3/'

    st.write(background_image_style(image_path), unsafe_allow_html=True)

    # Código de solicitar informacion
    st.title('Analisis de sentimiento de tweets usando modelo de Machine Learning')
    
    # Ingresa el tweet a analizar
    tweet = st.text_input('Introduza el tweet a analizar ')

    def button():
        resultado = st.radio('Seleccione el tipo de tweet para seguir entrenando', ('','positivo', 'negativo', 'neutro'))
        if resultado == 'positivo':
            st.write('positivo')
            if st.button('Guardar'):
        # print is visible in server output, not in the page
                print('button clicked!')
                st.write('Cambio satisfactorio 🎉')
        elif resultado == 'negativo':
            st.write('negativo')
            if st.button('Guardar'):
        # print is visible in server output, not in the page
                print('button clicked!')
                st.write('Cambio satisfactorio 🎉')
        elif resultado == 'neutro':
            st.write('neutro')
            if st.button('Guardar'):
        # print is visible in server output, not in the page
                print('button clicked!')
                st.write('Cambio satisfactorio 🎉')
        return resultado  

    #if st.button('Analizar'):
        # print is visible in server output, not in the page
    if len(tweet) > 0:
        st.success('Tweet analizado como positivo')
        direction = st.radio('Esta usted deacuerdo con la validación', ('','si', 'no'))
        if direction == 'si':
            st.write('Hemos sido bien entrenados 🎉')
        elif direction == 'no':
            #st.write('Sigamos entrenando 😞')
            button()
            
    #else:
        #st.error('Debe incluir un tweet válido')

