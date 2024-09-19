import streamlit as st
import matplotlib.pyplot as plt

# Función para evaluar la expresión de forma segura
def evaluar_expresion(expr, variables):
    def parse_expression(expr):
        tokens = tokenize(expr)
        value, remaining_tokens = parse_term(tokens)
        while remaining_tokens and remaining_tokens[0] in ('+', '-'):
            op = remaining_tokens.pop(0)
            next_value, remaining_tokens = parse_term(remaining_tokens)
            if op == '+':
                value += next_value
            elif op == '-':
                value -= next_value
        return value

    def parse_term(tokens):
        value, remaining_tokens = parse_factor(tokens)
        while remaining_tokens and remaining_tokens[0] in ('*', '/'):
            op = remaining_tokens.pop(0)
            next_value, remaining_tokens = parse_factor(remaining_tokens)
            if op == '*':
                value *= next_value
            elif op == '/':
                value /= next_value
        return value, remaining_tokens

    def parse_factor(tokens):
        token = tokens.pop(0)
        if token == '(':
            value = parse_expression(tokens)
            tokens.pop(0)  # Remove ')'
        elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            value = float(token)
        else:
            value = variables.get(token, 0)
        return value, tokens

    def tokenize(expr):
        tokens = []
        current_token = ''
        for char in expr:
            if char in '()+-*/':
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
        if current_token:
            tokens.append(current_token)
        return tokens

    return parse_expression(expr)

# Configuración de la barra lateral
st.sidebar.title("Configuración de la Función")

# Entrada de la expresión
expr = st.sidebar.text_input("Ingresa la función:", value="a*x + b")

# Entrada de constantes
st.sidebar.subheader("Constantes")
constantes = {}
constantes['a'] = st.sidebar.number_input("Constante a:", value=1.0)
constantes['b'] = st.sidebar.number_input("Constante b:", value=0.0)

# Definición del rango de la variable independiente
st.sidebar.subheader("Variable Independiente")
variable = st.sidebar.text_input("Nombre de la variable independiente:", value="x")
rango_min = st.sidebar.number_input("Valor mínimo de x:", value=0.0)
rango_max = st.sidebar.number_input("Valor máximo de x:", value=10.0)
paso = st.sidebar.number_input("Paso:", value=0.1)

# Botón para mostrar gráficos
if st.sidebar.button("Mostrar Gráficos"):
    x_vals = []
    y_vals = []
    x = rango_min
    while x <= rango_max:
        variables = constantes.copy()
        variables[variable] = x
        y = evaluar_expresion(expr, variables)
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
