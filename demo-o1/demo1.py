import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import re

# Título de la aplicación
st.title('Visualizador de Ecuaciones Matemáticas 3D')

# Sidebar para ingresar la ecuación y los parámetros
st.sidebar.header('Configuración')

# Ingreso de la ecuación
ecuacion_input = st.sidebar.text_input('Ingresa la ecuación (usa variables x, y, z)', 'a*sin(b*x) + c*cos(d*y)')

# Variables independientes
vars_independientes = ['x', 'y', 'z']

# Funciones matemáticas permitidas
funciones_matematicas = {'sin', 'cos', 'tan', 'exp', 'sqrt', 'log', 'pi', 'arcsin', 'arccos', 'arctan'}

# Extracción de variables y parámetros de la ecuación
variables = re.findall(r'\b[a-zA-Z_]\w*\b', ecuacion_input)
variables = list(set(variables))  # Eliminar duplicados

# Identificación de parámetros (excluyendo x, y, z y funciones matemáticas)
parametros = [var for var in variables if var not in vars_independientes and var not in funciones_matematicas]
parametros.sort()  # Ordenar alfabéticamente de menor a mayor

# Creación de sliders para los parámetros
valores_parametros = {}
for param in parametros:
    valores_parametros[param] = st.sidebar.slider(f'Parámetro {param}', -10.0, 10.0, 1.0)

# Rango de variables
x_min = st.sidebar.number_input('Valor mínimo de x', value=-10.0)
x_max = st.sidebar.number_input('Valor máximo de x', value=10.0)
y_min = st.sidebar.number_input('Valor mínimo de y', value=-10.0)
y_max = st.sidebar.number_input('Valor máximo de y', value=10.0)
num_puntos = st.sidebar.number_input('Número de puntos', min_value=50, max_value=500, value=100)

# Generación de los datos
x = np.linspace(x_min, x_max, int(num_puntos))
y = np.linspace(y_min, y_max, int(num_puntos))
X, Y = np.meshgrid(x, y)

# Evaluación de la ecuación
try:
    # Definimos variables en el espacio de nombres local
    local_vars = {'x': X, 'y': Y}

    # Reemplazamos los parámetros en la ecuación utilizando expresiones regulares
    ecuacion_eval = ecuacion_input
    for param in valores_parametros:
        # Utilizamos \b para indicar límites de palabra y evitar reemplazar partes de otros nombres
        ecuacion_eval = re.sub(r'\b{}\b'.format(re.escape(param)), str(valores_parametros[param]), ecuacion_eval)

    # Definimos las funciones matemáticas permitidas
    funciones_permitidas = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'log': np.log,
        'pi': np.pi,
        'arcsin': np.arcsin,
        'arccos': np.arccos,
        'arctan': np.arctan,
        'e': np.e,
        # Agrega más funciones si es necesario
    }

    # Combinamos variables y funciones en el espacio de nombres local
    entorno_eval = {**local_vars, **funciones_permitidas}

    # Evaluamos la ecuación de manera segura
    Z = eval(ecuacion_eval, {"__builtins__": None}, entorno_eval)

    # Visualización
    st.header('Resultado')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Gráfico 3D de la ecuación')
    st.pyplot(fig)

except Exception as e:
    st.error('Error al evaluar la ecuación:')
    st.exception(e)
