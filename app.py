import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #leer los datos

st.header('Dashboard de Vehiculos')

build_histogram = st.checkbox('Construir un histograma') #crear checkbox de histograma

if build_histogram: #al hacer clic en el botón
    #escribir mensaje
    st.write('Histograma de Vehiculos de anuncios de venta de coches.')
    
    #crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.checkbox('Construir gráfico de dispersión') #crear checkbox de dispersion

if build_dispersion: #al hacer clic en el botón
    #escribir mensaje
    st.write('Gráfico de dispersión de anuncios de venta de coches.')
    
    #crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
