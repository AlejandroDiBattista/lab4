import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Título de la aplicación
st.title('Simulador de Tiro de Baloncesto')

# Entradas del usuario para los coeficientes de la parábola
a = st.sidebar.number_input('Ingrese el coeficiente a:', value=-0.22, format="%.2f")
h = st.sidebar.number_input('Ingrese la coordenada x del vértice (h):', value=3.3735, format="%.3f")
k = st.sidebar.number_input('Ingrese la altura máxima (k):', value=5.09, format="%.2f")
st.sidebar.latex(f'f(x) = {a}(x - {h})^2 + {k}')
# Definimos la función que representa la trayectoria del tiro
def trayectoria_basketball(x):
    return a * (x - h) ** 2 + k

# Definimos el rango de x (distancia del lanzamiento al aro)
x_values = np.linspace(0, 6.75, 100)  # Desde el lanzamiento hasta la línea de tres puntos

# Calculamos las alturas correspondientes usando la función
y_values = trayectoria_basketball(x_values)

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, y_values, label='Trayectoria del tiro', color='orange')
ax.axhline(y=3.05, color='red', linestyle='--', label='Altura del aro (3.05 m)')  # Altura del aro
ax.axhline(y=2, color='green', linestyle='--', label='Altura inicial (2 m)')  # Altura de lanzamiento
ax.scatter([0, 6.75], [2, 3.05], color='blue')  # Puntos de lanzamiento y aro
ax.text(0, 2, 'Lanzamiento (2 m)', fontsize=10, verticalalignment='bottom')
ax.text(6.75, 3.05, 'Aro (3.05 m)', fontsize=10, verticalalignment='bottom')

# Etiquetas y título
ax.set_title('Trayectoria de un Tiro de Baloncesto (Triple)')
ax.set_xlabel('Distancia desde el lanzamiento (m)')
ax.set_ylabel('Altura (m)')
ax.set_xlim(-1, 8)
ax.set_ylim(0, 6)
ax.grid()
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)