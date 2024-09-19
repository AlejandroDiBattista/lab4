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
            if token in variables:
                value = variables[token]
            else:
                raise ValueError(f"Variable no definida: {token}")
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
st.sidebar.title("CONFIGURACIÓN DE LA FUNCIÓN")

# Selección entre 2D y 3D
tipo_grafico = st.sidebar.selectbox("SELECCIONA EL TIPO DE GRÁFICO:", ["2D", "3D"])

# Sección de Parámetros
st.sidebar.subheader("PARÁMETROS")

if tipo_grafico == "2D":
    # Función por defecto para 2D
    expr = st.sidebar.text_input("INGRESA LA FUNCIÓN:", value="A*X^2 + B*X + C")
    expr = expr.upper()
    variables_independientes = ['X']
else:
    # Función por defecto para 3D
    expr = st.sidebar.text_input("INGRESA LA FUNCIÓN:", value="A*X^2 + B*Y^2 + C")
    expr = expr.upper()
    variables_independientes = ['X', 'Y']

# Extraer constantes de la expresión y ordenarlas alfabéticamente
variables_en_expr = obtener_variables(expr, variables_independientes)
constantes = {}
st.sidebar.subheader("CONSTANTES")
for var in sorted(variables_en_expr):
    constantes[var] = st.sidebar.slider(f"CONSTANTE {var}:", -10.0, 10.0, 1.0, 0.1)

# Sección de Rango de los Ejes
st.sidebar.subheader("RANGO DE LOS EJES")

paso = st.sidebar.number_input("PASO:", value=0.1)

if tipo_grafico == "2D":
    # Rango para X con sliders en la misma fila
    col1, col2 = st.sidebar.columns(2)
    rango_min1 = col1.slider("MÍN X:", -10.0, 10.0, value=-10.0, step=0.1)
    rango_max1 = col2.slider("MÁX X:", -10.0, 10.0, value=10.0, step=0.1)
else:
    # Rango para X con sliders en la misma fila
    st.sidebar.markdown("**RANGO DE X**")
    col1, col2 = st.sidebar.columns(2)
    rango_min1 = col1.slider("MÍN X:", -10.0, 10.0, value=-10.0, step=0.1)
    rango_max1 = col2.slider("MÁX X:", -10.0, 10.0, value=10.0, step=0.1)

    # Rango para Y con sliders en la misma fila
    st.sidebar.markdown("**RANGO DE Y**")
    col3, col4 = st.sidebar.columns(2)
    rango_min2 = col3.slider("MÍN Y:", -10.0, 10.0, value=-10.0, step=0.1)
    rango_max2 = col4.slider("MÁX Y:", -10.0, 10.0, value=10.0, step=0.1)

# Evaluar y mostrar el gráfico automáticamente
try:
    if tipo_grafico == "2D":
        x_vals = []
        y_vals = []
        x = rango_min1
        while x <= rango_max1:
            variables = constantes.copy()
            variables['X'] = x
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
        ax.set_xlabel('X')
        ax.set_ylabel('F(X)')
        ax.set_title('GRÁFICO DE LA FUNCIÓN')
        st.pyplot(fig)

    else:
        # Crear arrays para X y Y
        x_vals = np.arange(rango_min1, rango_max1 + paso, paso)
        y_vals = np.arange(rango_min2, rango_max2 + paso, paso)

        # Crear meshgrid
        X, Y = np.meshgrid(x_vals, y_vals)

        # Evaluar la función en cada punto
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                variables = constantes.copy()
                variables['X'] = X[i, j]
                variables['Y'] = Y[i, j]
                try:
                    Z[i, j] = evaluar_expresion(expr, variables)
                except Exception as e:
                    st.error(f"Error al evaluar la expresión en ({X[i, j]}, {Y[i, j]}): {e}")
                    Z[i, j] = np.nan

        # Crear el gráfico 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('F(X, Y)')
        ax.set_title('GRÁFICO 3D DE LA FUNCIÓN')
        st.pyplot(fig)
except Exception as e:
    st.error(f"Ocurrió un error: {e}")
