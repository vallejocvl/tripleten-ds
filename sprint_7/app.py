import pandas as pd
import plotly.express as px
import streamlit as st

# Read Car Data
car_data = pd.read_csv("vehicles_us.csv")

# Add my header
st.header("Triple Ten's Sprint 7 by CVL")

# Create checkboxes instead of buttons
build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    # Display a message
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Create a histogram
    fig = px.histogram(car_data, x="odometer", title='Frecuencia de Vehiculos por Kilometraje')
    
    # Display the Plotly chart
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    # Display a message
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Create a scatter plot
    fig = px.scatter(car_data, x="odometer", y="price", title='Relación entre kilometraje y precio')
    
    # Display the Plotly chart
    st.plotly_chart(fig, use_container_width=True)