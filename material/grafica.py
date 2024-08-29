import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Gráfica de la función cuadrática")
st.sidebar.header("Coeficientes de la función cuadrática")

a = st.sidebar.slider('a', -10.0, 10.0, 0.5)
b = st.sidebar.slider('b', -10.0, 10.0, 4.0)
c = st.sidebar.slider('c', -10.0, 10.0, -1.0)
d = st.sidebar.slider('d', -10.0, 10.0, -1.0)

mostrar = st.sidebar.checkbox("Mostrar Ajuste")
def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d 

x = np.linspace(-10, 10, 201)
y = f(x)
np.random.seed(0)
yr = y + np.random.normal(0, 3, 201)

plt.plot(x, y)
plt.scatter(x, yr, c="red")
plt.title("Gráfica de la función cuadrática")
plt.xlim(-10, 10)
plt.ylim(-10, 100)


# Agregar grilla principal cada 10 unidades
plt.grid(True, which='major', linestyle='-', linewidth=0.5, color='gray')

# Agregar subgrilla cada 1 unidad
plt.grid(True, which='minor', linestyle='-', linewidth=0.2, color='lightgray')

# Configurar las marcas de la grilla
plt.minorticks_on()

# Destacar el eje x=0 y y=0 en color negro
plt.axhline(0, color='black')
plt.axvline(0, color='black')

if mostrar: 
    c = np.polyfit(x,yr,3)
    ffit = np.poly1d(c)
    yfit = ffit(x)

    plt.plot(x,yfit,'b-1')

st.pyplot(plt)