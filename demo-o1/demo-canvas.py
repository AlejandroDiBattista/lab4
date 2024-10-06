import streamlit as st  # Librería para crear aplicaciones web interactivas
import sympy as sp  # Librería para el cálculo simbólico
import numpy as np  # Librería para cálculos numéricos
import matplotlib.pyplot as plt  # Librería para graficar
from sympy.parsing.sympy_parser import parse_expr  # Para convertir cadenas a expresiones simbólicas
from sympy import symbols, lambdify  # Funciones útiles de sympy
from matplotlib import cm  # Para colormaps en gráficos 3D

# Configuración de la aplicación
st.markdown("# :rainbow[Visualizador de Ecuaciones]")

st.write('Ingrese una ecuación matemática con las variables x e y.')

# Sidebar para la entrada de la ecuación y ajustes
st.sidebar.title('Configuración')

# Campo de entrada para la ecuación
ecuacion_entrada = st.sidebar.text_input('Ingrese la ecuación:', 'sin(a*x) + b*y*y')

# Mostrar la ecuación ingresada en formato LaTeX
st.sidebar.latex(ecuacion_entrada)

# Definir las variables simbólicas
x, y = sp.symbols('x y')

# Intentar convertir la ecuación de entrada a una expresión simbólica
try:
    # Convertir la ecuación de entrada a una expresión simbólica
    ecuacion = parse_expr(ecuacion_entrada, evaluate=False)

    # Obtener todas las variables presentes en la ecuación
    variables = ecuacion.free_symbols

    # Filtrar las variables independientes (x, y) y las constantes
    variables_independientes = variables.intersection({x, y})
    constantes = sorted(variables - variables_independientes, key=lambda c: str(c))

    # Crear sliders para las constantes
    valores_constantes = {}
    st.sidebar.write('### Constantes')
    for constante in constantes:
        # Para cada constante, crear un slider para ajustar su valor
        valor = st.sidebar.slider(f'Valor de {str(constante).upper()}', -10.0, 10.0, 1.0)
        valores_constantes[constante] = valor

    # Crear sliders para los rangos de x y y
    with st.sidebar.expander('Configurar variables'):
    
        min_x, max_x = st.slider('Rango de X', -10.0, 10.0, (-5.0, 5.0))

        if y in variables_independientes:
            min_y, max_y = st.slider('Rango de Y', -10.0, 10.0, (-5.0, 5.0))

    # Reemplazar las constantes en la ecuación con sus valores
    ecuacion_num = ecuacion.subs(valores_constantes)

    # Generar el gráfico
    st.write('### Gráfico de la Ecuación')

    # Crear la figura para el gráfico
    fig = plt.figure()

    # Si solo hay una variable independiente (x)
    if variables_independientes == {x}:
        # Crear un arreglo de valores x dentro del rango especificado
        x_vals = np.linspace(min_x, max_x, 400)

        # Convertir la ecuación simbólica a una función numérica
        f = lambdify(x, ecuacion_num, 'numpy')

        # Calcular los valores de y para cada x
        y_vals = f(x_vals)

        # Graficar la función
        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        st.pyplot(fig)

    # Si hay dos variables independientes (x, y)
    elif variables_independientes == {x, y} or variables_independientes == {y, x}:
        # Crear una malla de valores x e y dentro de los rangos especificados
        x_vals = np.linspace(min_x, max_x, 100)
        y_vals = np.linspace(min_y, max_y, 100)
        X, Y = np.meshgrid(x_vals, y_vals)

        # Convertir la ecuación simbólica a una función numérica
        f = lambdify((x, y), ecuacion_num, 'numpy')

        # Calcular los valores de Z para cada par (x, y)
        Z = f(X, Y)

        # Crear una figura 3D
        ax = fig.add_subplot(111, projection='3d')

        # Graficar la superficie 3D
        surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        # Agregar una barra de color para indicar los valores de Z
        fig.colorbar(surf, shrink=0.5, aspect=5)
        st.pyplot(fig)
    else:
        # Si hay más de dos variables independientes, mostrar un mensaje de error
        st.write('Solo se permiten ecuaciones con una o dos variables independientes (x e y).')
except Exception as e:
    # Si ocurre un error al procesar la ecuación, mostrar un mensaje amigable
    st.write('Error al procesar la ecuación. Por favor, verifique la sintaxis.')
    st.write('Detalles del error:', e)
