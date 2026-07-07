import requests
import streamlit as st
from india_cities import india
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY_WEATHER")

st.set_page_config('Weather WebApp: ',layout='centered')
if 'true_weather_button' not in st.session_state:
    st.session_state.true_weather_button = False
st.title('Your Today Weather')
st.divider()
state_name_input = st.selectbox('Select State Name:',[state for state in india])
city_name_input= st.selectbox(f'Select {state_name_input} City Name',[city for city in india[state_name_input]])
if st.button('See today weather') or st.session_state.true_weather_button == True:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_input}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    st.session_state.true_weather_button = True

    data = response.json()
if st.session_state.true_weather_button == True:    
    if response.status_code == 200:
        st.divider()
        st.write(f'City name : {data["name"]}')

    