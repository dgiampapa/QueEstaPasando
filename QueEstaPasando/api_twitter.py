import requests
import pandas as pd

Bearer = 'AAAAAAAAAAAAAAAAAAAAAHbEOwEAAAAAOSRFS1w0Wmx%2BmnDLsTzP%2FeyEglc%3DWsmsldmU9ksMUtzwebxCHbK1GEvweui2yazIe4oMVxpY2jSM2E'

def buscar_tweets(mentions_id, cantidad_tweet=400):

    headers = {'Authorization': f'Bearer {Bearer}'} # Variable de autorizador
    url = f'https://api.twitter.com/2/users/{mentions_id}/mentions' # url de invocacion
    respuesta = '' # variable que guarda toda la respuesta
    data = pd.DataFrame()
    params = {
        'tweet.fields': 'created_at,author_id',
        'max_results':100} 
    
    for cantidad in range(int(cantidad_tweet/100)):
            respuesta = requests.get(url, params=params, headers=headers).json()
            data = data.append(respuesta['data'])
            params = {
                'tweet.fields': 'created_at,author_id',
                'pagination_token': respuesta['meta']['next_token'],
                'max_results':100} 
    
    data = data.reset_index(drop=True)


    return data

def grabar_tweets(df, ruta_archivo):
    df.to_csv(ruta_archivo)