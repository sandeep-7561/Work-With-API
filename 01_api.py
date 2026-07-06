import requests
import streamlit as st
url =  requests.get('https://api.coinlore.net/api/tickers/')

st.set_page_config('Coin API',layout='wide')
response = url.json()
coin_name = []
for i in range(len(response['data'])):
    coin_name.append(response['data'][i]['name'])

st.title('Coin Sandeep')

coin_confirm = st.selectbox('Select Coin',coin_name)
keys = []
values = []
for i in range(len(response['data'])):
    if coin_confirm == response['data'][i]['name']:
        for key in response['data'][i].keys():
            keys.append(key)
        for value in response['data'][i].values():
            values.append(value)
        
for i in range(len(keys)):
    st.write(f'{keys[i]} : {values[i]}')
