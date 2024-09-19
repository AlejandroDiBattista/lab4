import streamlit as st
import matplotlib.pyplot as plt

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
def obtener_variables(expr, variable_independiente):
    tokens = tokenize(expr)
    variables = set()
    for token in tokens:
        if token.isalpha() and token != variable_independiente:
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

# Entrada de la expresión
expr = st.sidebar.text_input("Ingresa la función:", value="a*x + b")

# Entrada de la variable independiente
st.sidebar.subheader("Variable Independiente")
variable = st.sidebar.text_input("Nombre de la variable independiente:", value="x")

# Extraer constantes de la expresión
variables_en_expr = obtener_variables(expr, variable)
constantes = {}
st.sidebar.subheader("Constantes")
for var in variables_en_expr:
    constantes[var] = st.sidebar.slider(f"Constante {var}:", -10.0, 10.0, 1.0, 0.1)

# Definición del rango de la variable independiente
st.sidebar.subheader("Rango de la Variable Independiente")
rango_min = st.sidebar.number_input(f"Valor mínimo de {variable}:", value=0.0)
rango_max = st.sidebar.number_input(f"Valor máximo de {variable}:", value=10.0)
paso = st.sidebar.number_input("Paso:", value=0.1)

# Botón para mostrar gráficos
if st.sidebar.button("Mostrar Gráficos"):
    x_vals = []
    y_vals = []
    x = rango_min
    while x <= rango_max:
        variables = constantes.copy()
        variables[variable] = x
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
    ax.set_xlabel(variable)
    ax.set_ylabel('f({})'.format(variable))
    ax.set_title('Gráfico de la función')
    st.pyplot(fig)
