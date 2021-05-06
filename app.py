import streamlit as st
import base64
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sns
from QueEstaPasando import trainer_ml
import warnings
#from streamlit.script_runner import StopException, RerunException


# set principal.
st.set_page_config(
    page_title="Que esta pasando?",
    page_icon="https://d1nxzqpcg2bym0.cloudfront.net/google_play/com.synergygb.megazord.MiMercantil/b3514b2e-4539-11e8-9862-35b57a16ceeb/128x128",
    layout="centered", # wide
    initial_sidebar_state="collapsed") # collapsed

# imagen de fondo

main_bg = "images/fondo4.jpg"
main_bg_ext = "jpg"

side_bg = "images/fondo4.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
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
#st.markdown("<h1 style='text-align: center; color: black;'><br><br>Análisis de sentimiento de twitter con el procedimiento de lenguaje natural mediante el uso Machine Learning y Deep Learning</h1>", unsafe_allow_html=True)
#st.markdown("<br><h1 style='text-align: center; color: black;'>Análisis de sentimiento de twitter con el procedimiento de lenguaje natural mediante el uso Machine Learning y Deep Learning.</h1>", unsafe_allow_html=True)
#st.markdown("<style='text-align: center; color: black;'>Análisis de sentimiento de twitter con el procedimiento de lenguaje natural mediante el uso Machine Learning y Deep Learning", unsafe_allow_html=True)
st.sidebar.markdown("Menú", unsafe_allow_html=True)
my_page = st.sidebar.radio('', ['','Predicción', 'Estadísticas'])
st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
if my_page == '':
      
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.image('images/inicio.jpg')

if my_page == 'Predicción':
      
    image_path = 'images/fondo.png'
    image_link = 'https://docs.python.org/3/'

    st.write(background_image_style(image_path), unsafe_allow_html=True)

    # Código de solicitar informacion
    #titulo = st.title('Analisis de sentimiento de tweets usando modelo de Machine Learning')
    st.markdown("<h1 style='text-align: center; color: black;'>Bienvenidos al análizador de sentimientos de tweets:</h1>", unsafe_allow_html=True)

        
    # Ingresa el tweet a analizar
    st.write('''<style>
                input[type=text], select {
        width: 100%;
        height: 100px;
        }
         </style>''', unsafe_allow_html=True)

             
    st.markdown("Introduzca el tweet a analizar:")
    tweet = st.text_area('')
    

    def button():
        resultado = st.radio('Seleccione el tipo de tweet para seguir entrenando', ('','positivo', 'negativo', 'neutro'))
        if resultado == 'positivo':
            st.write('positivo')
            if st.button('Guardar'):
        # print is visible in server output, not in the page
                print('button clicked!')
                st.write('Cambio satisfactorio para entrenar 🎉')                
        elif resultado == 'negativo':
            st.write('negativo')
            if st.button('Guardar'):
        # print is visible in server output, not in the page
                print('button clicked!')
                st.write('Cambio satisfactorio para entrenar 🎉')
        elif resultado == 'neutro':
            st.write('neutro')
            if st.button('Guardar'):
        # print is visible in server output, not in the page
                print('button clicked!')
                st.write('Cambio satisfactorio para entrenar 🎉')
        return resultado  

        #if st.button('Analizar'):
        # print is visible in server output, not in the page
    if len(tweet) > 0:
        with st.spinner('Analizando...'):
            time.sleep(0.5)
        t_ml = trainer_ml.Trainer_ML()
        df = pd.DataFrame()
        df['created_at'] =['2021-04-27T07:26:38.000Z']
        df['text'] = [tweet]
        prediccion = t_ml.predict_model(df)
        if prediccion == 'pos':
            st.success('Tweet analizado como positivo')

            direction = st.radio('Esta usted deacuerdo con la validación', ('','si', 'no'))
            if direction == 'si':
                st.write('Hemos sido bien entrenados 🎉')
                if st.button('Guardar'):
            # print is visible in server output, not in the page
                    print('button clicked!')
                    st.write('Cambio satisfactorio para entrenar 🎉')
                    raise RerunException
            elif direction == 'no':
                #st.write('Sigamos entrenando 😞')
                button()

        elif prediccion == 'neu':
            st.warning('Tweet analizado como neutro')
            direction = st.radio('Esta usted deacuerdo con la validación', ('','si', 'no'))
            if direction == 'si':
                st.write('Hemos sido bien entrenados 🎉')
                if st.button('Guardar'):
            # print is visible in server output, not in the page
                    print('button clicked!')
                    st.write('Cambio satisfactorio para entrenar 🎉')
            elif direction == 'no':
                #st.write('Sigamos entrenando 😞')
                button()

        else:
            st.error('Tweet analizado como negativo')
            direction = st.radio('Esta usted deacuerdo con la validación', ('','si', 'no'))
            if direction == 'si':
                st.write('Hemos sido bien entrenados 🎉')
                if st.button('Guardar'):
            # print is visible in server output, not in the page
                    print('button clicked!')
                    st.write('Cambio satisfactorio para entrenar 🎉')
                #    raise RerunException
            elif direction == 'no':
                #st.write('Sigamos entrenando 😞')
                button()    

            
elif my_page == 'Estadísticas':
    st.markdown('')
    st.markdown('')
    st.markdown("<h1 style='text-align: center; color: black;'>Módulo Business Inteligence (BI)</h1>", unsafe_allow_html=True)
    my_page1 = st.sidebar.radio('', ['','Datos','Cant. Tweets x Fecha', 'Tweets x Sentimiento'])
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    if my_page1 == '':
        st.write("\n")
        st.image('images/estadisticas.jpg')
        #st.image('<div align="center"><img src="images/estadisticas.jpg"></div>')
    


    if my_page1 == 'Datos':
        fields = ['text', 'created_at', 'score']
        data_estadisticas = pd.read_csv("QueEstaPasando/data/total.csv", usecols=fields)
        data_estadisticas = data_estadisticas.assign(hack='').set_index('hack')
        st.table(data_estadisticas.head(10)) 
    if my_page1 == 'Tweets x Sentimiento':
        #st.markdown("<h1 style='text-align: center; color: black;'>prueba (BI)</h1>", unsafe_allow_html=True)
        fig=plt.figure(figsize=(3, 3))
        plt.title('Cantidad de Tweets por Sentimientos', fontsize=10)
        data_estadisticas = pd.read_csv("QueEstaPasando/data/total.csv")
        etiquetas = ['Neutro','Negativo','Positivo']
        valores = data_estadisticas['score'].value_counts()
        colores = ['orange','red','green']
        plt.pie(x=valores, colors = colores, autopct='%1.2f%%')
        plt.legend(['Neutro','Negativo','Positivo'], loc='best', fontsize=5)
        #plt.show()
        #st.write(plt.show())
        st.pyplot(fig)

    if my_page1 == 'Cant. Tweets x Fecha':
        #fig1=plt.figure(figsize=(10, 6))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        data_grafico = pd.read_csv("QueEstaPasando/data/total.csv")
        data_grafico = data_grafico[['created_at', 'text', 'score']]
        data_grafico['created_at'] = pd.to_datetime(data_grafico['created_at'])
        data_grafico['created_at'] = data_grafico['created_at'].dt.strftime("%Y-%m-%d")
        pd.get_dummies(data_grafico['score'])
        data_grafico = data_grafico.merge(pd.get_dummies(data_grafico['score']), left_index = True, right_index = True)
        data_grafico_grouped = data_grafico.groupby('created_at').agg({'neg': 'sum',
                                                                                'neu': 'sum',
                                                                                'pos': 'sum',
                                                                                'text': 'count'})
        sns.set_style("whitegrid")
        data_grafico_grouped[['neg', 'neu', 'pos']].plot(kind = 'bar',
                                                            stacked = True,
                                                            figsize = (16, 6),
                                                            color = ['orange', 'green', 'blue'])
        plt.plot(data_grafico_grouped['text'], color = 'black', label = 'Total', linestyle = 'dashed')
        plt.title('Cantidad de Tweets por Fecha', fontsize=30)
        plt.ylabel('Tweets', fontsize=18)
        plt.xlabel('Fecha', fontsize=18)
        plt.legend(loc = 'best', fontsize=15)
        sns.despine(left = True, bottom = True)
        st.pyplot()
     

    
