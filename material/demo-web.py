import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Graficador de Polinomio de Grado 3')

# Ingresar coeficientes en la barra lateral
st.sidebar.header('Coeficientes del polinomio')
a = st.sidebar.slider('Coeficiente a (x^3)', -10.0, 10.0, 1.0, 0.1)
b = st.sidebar.slider('Coeficiente b (x^2)', -10.0, 10.0, 0.0, 0.1)
c = st.sidebar.slider('Coeficiente c (x)', -10.0, 10.0, 0.0, 0.1)
d = st.sidebar.slider('Coeficiente d (constante)', -10.0, 10.0, 0.0, 0.1)

# Crear los datos del polinomio
x = np.linspace(-10, 10, 400)
y = a * x**3 + b * x**2 + c * x + d

# Crear la gráfica
plt.xkcd()
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'$y = {a}x^3 + {b}x^2 + {c}x + {d}$')
plt.title('Gráfica del polinomio de grado 3')

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Mostrar la gráfica en la aplicación
st.pyplot(plt)
