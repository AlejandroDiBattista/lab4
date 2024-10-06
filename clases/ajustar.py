import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Visualización Interactiva de una Función Cúbica")

# Descripción
st.markdown("""
Esta aplicación permite visualizar cómo los diferentes parámetros de una función cúbica afectan su gráfica.
Modifica los coeficientes \( a \), \( b \), \( c \), y \( d \) utilizando los controles deslizantes a continuación.
""")

# Barra lateral para los controles
st.sidebar.header("Parámetros de la Función Cúbica")

# Controles deslizantes para los coeficientes
a = st.sidebar.slider("Coeficiente a", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.sidebar.slider("Coeficiente b", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
c = st.sidebar.slider("Coeficiente c", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
d = st.sidebar.slider("Coeficiente d", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Mostrar los coeficientes seleccionados
st.sidebar.markdown("### Función Cúbica")
st.sidebar.latex(f"f(x) = {a}x^3 + {b}x^2 + {c}x + {d}")

# Generar datos para la gráfica
x = np.linspace(-10, 10, 400)
y = a * x**3 + b * x**2 + c * x + d

# Crear la gráfica
fig, ax = plt.subplots()
ax.plot(x, y, label=f"{a}x³ + {b}x² + {c}x + {d}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Gráfica de la Función Cúbica")
ax.legend()
ax.grid(True)

# Mostrar la gráfica en la aplicación
st.pyplot(fig)

# Información adicional
st.markdown("""
**Interpreta la Gráfica:**
- **Coeficiente a**: Controla la "curvatura" y la dirección de las ramas de la función.
- **Coeficiente b**: Afecta la forma general y la posición de los máximos y mínimos locales.
- **Coeficiente c**: Influye en la inclinación de la función.
- **Coeficiente d**: Desplaza la gráfica verticalmente.
""")
