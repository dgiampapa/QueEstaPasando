from unicodedata import normalize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import string
import numpy as np
from nltk.tokenize import word_tokenize
from datetime import datetime
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
# import nltk 
#import unidecode
from sklearn.model_selection import learning_curve
#import os


class Clean_Data(object):
    def __init__(self):
        pass
        #self.ruta_archivo = ruta_archivo

    def drop_duplicates(self,data):
        data.drop_duplicates(inplace=True)
        return data

    def drop_null(self,data):
        data.dropna(axis=0, inplace=True)
        return data

    def remove_mencion(self,text):
        text = " ".join(filter(lambda x:x[0]!='@', text.split()))
        return text

    def drop_mencion(self,data):
        data['text'] = data['text'].apply(self.remove_mencion)
        return data

    def transform_date(self,data):
        data['created_at'] = pd.to_datetime(data['created_at'])
        data['created_at'] = data['created_at'].dt.strftime("%Y-%m-%d")
        data['created_at'] = pd.to_datetime(data['created_at'])
        return data

    def replace_word(self,data,word_from,word_to):
        data['text'] = data['text'].str.replace(word_from, word_to)
        return data

    def drop_space(self,data):
        data['text'] = data['text'].str.strip()
        return data

    def remove_puntuation(self,text):
        mi_puntuacion = '!¡"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}~'
        for punctuation in mi_puntuacion:
            text = text.replace(punctuation, " ")
        return text

    def drop_puntuation(self,data):
        data['text'] = data['text'].apply(self.remove_puntuation)
        return data

    def remove_lower(self,text):
        text = text.lower()
        return text

    def set_lower(self,data):
        data['text'] = data['text'].apply(self.remove_lower)
        return data

    def cambia_acentuadas(self,text):
        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
        text = normalize('NFKC', normalize('NFKD', text).translate(trans_tab))
        return text

    def change_character(self,data):
        data['text'] = data['text'].apply(self.cambia_acentuadas)
        return data

    def remove_numbers(self,text):
        text = ''.join(word for word in text if not word.isdigit())
        return text

    def drop_numbers(self,data):
        data['text'] = data['text'].apply(self.remove_numbers)
        return data

    def remove_StopWords(self,text):
        spanish_stopwords = set(stopwords.words('spanish'))
        word_tokens = word_tokenize(text)
        text = [w for w in word_tokens if not w in spanish_stopwords]
        return text

    def drop_StopWords(self,data):
        data['text'] = data['text'].apply(self.remove_StopWords)
        return data

    def remove_Lemmatize(self,text):
        lemmatizer = WordNetLemmatizer()
        lemmatized = [lemmatizer.lemmatize(word) for word in text]
        str_lemmatizer = " ".join(lemmatized)
        return str_lemmatizer

    def drop_lemmatize(self,data):
        data['text'] = data['text'].apply(self.remove_Lemmatize)
        return data

    def clean_data(self,data):
        # elimina duplicados
        data = self.drop_duplicates(data)
        # elimina los null
        data = self.drop_null(data)		
        # elimina las menciones
        data = self.drop_mencion(data)
        # transforma la data
        data = self.transform_date(data)
        # reemplaza palbras tpago
        data = self.replace_word(data,'t pago','tpago')
        # elimina espacios al inicio y al final
        data = self.drop_space(data)
        # elimina los signos de puntuacion
        data = self.drop_puntuation(data)
        # colocar todo en minuscula
        data = self.set_lower(data)
        # elimina acentos
        data = self.change_character(data)
        # elimina numeros
        data = self.drop_numbers(data)
        # elimina stopwords
        data = self.drop_StopWords(data)
        # lemmatize
        data = self.drop_lemmatize(data)
        return data

