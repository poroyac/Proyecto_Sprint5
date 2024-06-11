import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #leer los datos

st.header('Dashboard de Vehiculos')

hist_button = st.button('Construir un histograma') #crear un botón

if hist_button: #al hacer clic en el botón
    #escribir mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches.')
    
    #crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')

if disp_button: #al hacer clic en el botón
    #escribir mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches.')
    
    #crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
