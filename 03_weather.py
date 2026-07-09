import requests
import streamlit as st
from india_cities import india
from dotenv import load_dotenv
import os
import plotly.express as px
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

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
    temp_of_state = []
    temp_of_state_name = []
    for i in india[state_name_input]:
        if city_name_input == i:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_input}&appid={API_KEY}&units=metric"
        else:
            city_temp_url = f"https://api.openweathermap.org/data/2.5/weather?q={i}&appid={API_KEY}&units=metric"
            response_temp = requests.get(city_temp_url)
            data_temp = response_temp.json()
            if response_temp.status_code == 200:
                temp_of_state.append(data_temp['main']['temp'])
                temp_of_state_name.append(i)



    response = requests.get(url)
    st.session_state.true_weather_button = True

    data = response.json()
    temp_of_state.append(data['main']['temp'])
    temp_of_state_name.append(data['name'])
if st.session_state.true_weather_button == True:    
    if response.status_code == 200:
        st.divider()
        col1,col2,col3 = st.columns(3)
        with col1:
            st.metric('City',data['name'])
        with col2:
            st.metric("Temp",f'{data["main"]["temp"]} °C')
        with col3:
            st.metric('Weather' ,data["weather"][0]["main"])

        new_dict_for_graph = {}
        for key,value in zip(temp_of_state,temp_of_state_name):
            new_dict_for_graph[value] = key
        
        df = pd.DataFrame({
            'City':new_dict_for_graph.keys(),
            'Temperature':new_dict_for_graph.values()
        })
        fig = px.line(df,x='City',y='Temperature',title=f'Temperature of {state_name_input} States:')
        st.plotly_chart(fig,use_container_width=True)       
        
        #m is a map object
        m = folium.Map(
            location=[22.9734, 78.6569],
            zoom_start=5
        )
        
        folium.Marker(
            location=[23.0225,72.5714],
            popup="Ahmedabad"
        ).add_to(m)

        st_folium(
            m,
            width=700,
            height=500
        )