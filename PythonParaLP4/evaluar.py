import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import ast
import operator as op
from mpl_toolkits.mplot3d import Axes3D

# Funciones y operadores permitidos
allowed_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}

allowed_functions = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'exp': np.exp,
    'log': np.log,
    'sqrt': np.sqrt,
}

# Evaluador seguro de expresiones
def safe_eval(expr, variables):
    def eval_(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.Name):
            if node.id in variables:
                return variables[node.id]
            else:
                raise ValueError(f"Variable '{node.id}' no permitida")
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            operator = allowed_operators[type(node.op)]
            return operator(eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operator = allowed_operators[type(node.op)]
            return operator(eval_(node.operand))
        elif isinstance(node, ast.Call):
            func = node.func.id
            if func in allowed_functions:
                args = [eval_(arg) for arg in node.args]
                return allowed_functions[func](*args)
            else:
                raise ValueError(f"Función '{func}' no permitida")
        else:
            raise TypeError(f"Tipo de nodo '{node}' no soportado")

    node = ast.parse(expr, mode='eval').body
    return eval_(node)

st.title("Graficador de Expresiones Aritméticas")

# Entrada de la expresión
expr = st.sidebar.text_input("Ingrese la expresión", value="a*sin(b*x)")

# Tipo de gráfica
plot_type = st.sidebar.selectbox("Seleccione el tipo de gráfica", ["2D", "3D"])

# Extraer variables y parámetros
def extract_variables(expr):
    variables = set()
    for node in ast.walk(ast.parse(expr)):
        if isinstance(node, ast.Name):
            variables.add(node.id)
    return variables

variables = extract_variables(expr)
params = variables - {'x', 'y'}

# Definir sliders para parámetros
param_values = {}
for param in params:
    param_values[param] = st.sidebar.slider(f"Valor de {param}", -10.0, 10.0, 1.0)

# Rango de variables
x_min = st.sidebar.number_input("x mínimo", value=-10.0)
x_max = st.sidebar.number_input("x máximo", value=10.0)

if plot_type == "3D":
    y_min = st.sidebar.number_input("y mínimo", value=-10.0)
    y_max = st.sidebar.number_input("y máximo", value=10.0)

# Generar datos y graficar
try:
    if plot_type == "2D":
        x = np.linspace(x_min, x_max, 400)
        variables = {'x': x}
        variables.update(param_values)
        y = np.array([safe_eval(expr, {**variables, 'x': xi}) for xi in x])

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfica 2D')
        st.pyplot(fig)

    else:
        x = np.linspace(x_min, x_max, 50)
        y = np.linspace(y_min, y_max, 50)
        X, Y = np.meshgrid(x, y)
        variables = {'x': X, 'y': Y}
        variables.update(param_values)
        Z = np.array([[safe_eval(expr, {**variables, 'x': xi, 'y': yi}) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(X, Y)])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Gráfica 3D')
        st.pyplot(fig)

except Exception as e:
    st.error(f"Error al evaluar la expresión: {e}")
