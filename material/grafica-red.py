import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers, models

st.title("Gráfica de la función cuadrática")
st.sidebar.header("Coeficientes de la función cuadrática")

a = st.sidebar.slider('a', -10.0, 10.0, 0.5)
b = st.sidebar.slider('b', -10.0, 10.0, 4.0)
c = st.sidebar.slider('c', -10.0, 10.0, -1.0)
d = st.sidebar.slider('d', -10.0, 10.0, -1.0)

e = st.sidebar.slider('epoc', 10, 100, 10)

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

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(1,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Crear una barra de progreso
progress_bar = st.progress(0)
for i in range(e):
    # Actualizar la barra de progreso
    progress_bar.progress((i + 1) / e)
    history = model.fit(x, y, epochs=5, verbose=0)

# Predicciones
y_pred = model.predict(x)

# Graficar los resultados
plt.plot(x, y_pred, color='green', linewidth=5,  label='Ajuste con red neuronal')


st.pyplot(plt)