import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necesario para gráficos 3D
import numpy as np  # Usado para manejar arrays en gráficos 3D

# Función para evaluar la expresión de forma segura
def evaluar_expresion(expr, variables):
    def parse_expression(tokens):
        value, remaining_tokens = parse_term(tokens)
        while remaining_tokens and remaining_tokens[0] in ('+', '-'):
            op = remaining_tokens.pop(0)
            next_value, remaining_tokens = parse_term(remaining_tokens)
            if op == '+':
                value += next_value
            elif op == '-':
                value -= next_value
        return value, remaining_tokens

    def parse_term(tokens):
        value, remaining_tokens = parse_power(tokens)
        while remaining_tokens and remaining_tokens[0] in ('*', '/'):
            op = remaining_tokens.pop(0)
            next_value, remaining_tokens = parse_power(remaining_tokens)
            if op == '*':
                value *= next_value
            elif op == '/':
                value /= next_value
        return value, remaining_tokens

    def parse_power(tokens):
        value, remaining_tokens = parse_factor(tokens)
        while remaining_tokens and remaining_tokens[0] == '^':
            remaining_tokens.pop(0)
            next_value, remaining_tokens = parse_factor(remaining_tokens)
            value = value ** next_value
        return value, remaining_tokens

    def parse_factor(tokens):
        token = tokens.pop(0)
        if token == '(':
            value, tokens = parse_expression(tokens)
            if tokens.pop(0) != ')':
                raise ValueError("Paréntesis no coinciden")
        elif token == '-':
            value, tokens = parse_factor(tokens)
            value = -value
        elif is_number(token):
            value = float(token)
        else:
            value = variables.get(token, 0)
        return value, tokens

    def tokenize(expr):
        tokens = []
        current_token = ''
        for char in expr:
            if char in '()+-*/^':
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                tokens.append(char)
            elif char.isalnum() or char == '.':
                current_token += char
            elif char == ' ':
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
            else:
                pass  # Ignorar otros caracteres
        if current_token:
            tokens.append(current_token)
        return tokens

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    tokens = tokenize(expr)
    value, remaining_tokens = parse_expression(tokens)
    return value

# Función para extraer variables de la expresión
def obtener_variables(expr, variables_independientes):
    tokens = tokenize(expr)
    variables = set()
    for token in tokens:
        if token.isalpha() and token not in variables_independientes:
            variables.add(token)
    return variables

def tokenize(expr):
    tokens = []
    current_token = ''
    for char in expr:
        if char in '()+-*/^':
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char.isalnum() or char == '.':
            current_token += char
        elif char == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ''
        else:
            pass  # Ignorar otros caracteres
    if current_token:
        tokens.append(current_token)
    return tokens

# Configuración de la barra lateral
st.sidebar.title("Configuración de la Función")

# Selección entre 2D y 3D
tipo_grafico = st.sidebar.selectbox("Selecciona el tipo de gráfico:", ["2D", "3D"])

# Sección de Parámetros
st.sidebar.subheader("Parámetros")

if tipo_grafico == "2D":
    # Función por defecto para 2D
    expr = st.sidebar.text_input("Ingresa la función:", value="a*x^2 + b*x + c")
    variable1 = st.sidebar.text_input("Nombre de la variable independiente:", value="x")
    variables_independientes = [variable1]
else:
    # Función por defecto para 3D
    expr = st.sidebar.text_input("Ingresa la función:", value="a*x^2 + b*y^2 + c")
    variable1 = st.sidebar.text_input("Nombre de la primera variable independiente:", value="x")
    variable2 = st.sidebar.text_input("Nombre de la segunda variable independiente:", value="y")
    variables_independientes = [variable1, variable2]

# Extraer constantes de la expresión y ordenarlas alfabéticamente
variables_en_expr = obtener_variables(expr, variables_independientes)
constantes = {}
st.sidebar.subheader("Constantes")
for var in sorted(variables_en_expr):
    constantes[var] = st.sidebar.slider(f"Constante {var}:", -10.0, 10.0, 1.0, 0.1)

# Sección de Rango de los Ejes
st.sidebar.subheader("Rango de los Ejes")

paso = st.sidebar.number_input("Paso:", value=0.1)

if tipo_grafico == "2D":
    # Rango para variable1 con sliders en la misma fila
    col1, col2 = st.sidebar.columns(2)
    rango_min1 = col1.slider(f"Mín {variable1}:", -10.0, 10.0, value=-10.0, step=0.1)
    rango_max1 = col2.slider(f"Máx {variable1}:", -10.0, 10.0, value=10.0, step=0.1)
else:
    # Rango para variable1 con sliders en la misma fila
    st.sidebar.markdown(f"**Rango de {variable1}**")
    col1, col2 = st.sidebar.columns(2)
    rango_min1 = col1.slider(f"Mín {variable1}:", -10.0, 10.0, value=-10.0, step=0.1)
    rango_max1 = col2.slider(f"Máx {variable1}:", -10.0, 10.0, value=10.0, step=0.1)

    # Rango para variable2 con sliders en la misma fila
    st.sidebar.markdown(f"**Rango de {variable2}**")
    col3, col4 = st.sidebar.columns(2)
    rango_min2 = col3.slider(f"Mín {variable2}:", -10.0, 10.0, value=-10.0, step=0.1)
    rango_max2 = col4.slider(f"Máx {variable2}:", -10.0, 10.0, value=10.0, step=0.1)

# Botón para mostrar gráficos
if st.sidebar.button("Mostrar Gráficos"):
    if tipo_grafico == "2D":
        x_vals = []
        y_vals = []
        x = rango_min1
        while x <= rango_max1:
            variables = constantes.copy()
            variables[variable1] = x
            try:
                y = evaluar_expresion(expr, variables)
            except Exception as e:
                st.error(f"Error al evaluar la expresión: {e}")
                break
            x_vals.append(x)
            y_vals.append(y)
            x += paso

        # Mostrar el gráfico
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel(variable1)
        ax.set_ylabel('f({})'.format(variable1))
        ax.set_title('Gráfico de la función')
        st.pyplot(fig)

    else:
        # Crear arrays para variable1 y variable2
        x_vals = np.arange(rango_min1, rango_max1 + paso, paso)
        y_vals = np.arange(rango_min2, rango_max2 + paso, paso)

        # Crear meshgrid
        X, Y = np.meshgrid(x_vals, y_vals)

        # Evaluar la función en cada punto
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                variables = constantes.copy()
                variables[variable1] = X[i, j]
                variables[variable2] = Y[i, j]
                try:
                    Z[i, j] = evaluar_expresion(expr, variables)
                except Exception as e:
                    st.error(f"Error al evaluar la expresión en ({X[i, j]}, {Y[i, j]}): {e}")
                    Z[i, j] = np.nan

        # Crear el gráfico 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel(variable1)
        ax.set_ylabel(variable2)
        ax.set_zlabel('f({}, {})'.format(variable1, variable2))
        ax.set_title('Gráfico 3D de la función')
        st.pyplot(fig)
