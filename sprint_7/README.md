# Análisis de Vehículos Usados

Este proyecto forma parte del Sprint 7 del bootcamp de ciencia de datos de **TripleTen**. El objetivo principal es practicar el uso de herramientas como **Streamlit**, **Plotly Express** y realizar el despliegue de la aplicación en **Render.com**.

## Descripción del Proyecto
La aplicación web permite visualizar de forma sencilla dos gráficos principales basados en datos de vehículos usados:

1. **Histograma**: Muestra la distribución de kilometraje de los vehículos.
2. **Gráfico de dispersión (scatter plot)**: Relaciona el precio de los vehículos con su kilometraje.

Esta aplicación permite explorar visualmente los datos para identificar patrones o tendencias en el mercado de autos usados.

## Datos Utilizados
Los datos fueron proporcionados por **TripleTen** durante el Sprint 7. Contienen información sobre:
- **Precio** del vehículo.
- **Año del modelo**.
- **Kilometraje**.
- **Condición del vehículo**.
- **Tipo de combustible**.
- **Transmisión**.
- Otros atributos.

## Requisitos
Para ejecutar la aplicación localmente, es necesario tener instaladas las siguientes dependencias:

```plaintext
pandas
plotly_express
streamlit
```

O puedes instalar todas las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecución de la Aplicación
Para ejecutar la aplicación en tu entorno local, usa el siguiente comando:

```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador predeterminado. Si realizas cambios en el código, deberás reiniciar la aplicación o refrescar la página para verlos reflejados.

## Despliegue
El despliegue de esta aplicación se realizó a través de **Render.com**. Se puede encontrar en el siguiente link **https://sprint7-cvl-vehiculos-usados.onrender.com**