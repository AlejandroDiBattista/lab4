import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import re
import ast

st.title('Graficador Interactivo de Ecuaciones en 2D y 3D')

# Sidebar inputs
st.sidebar.header('Configuración')

# Seleccionar el tipo de gráfica
tipo_grafica = st.sidebar.selectbox('Selecciona el tipo de gráfica', ['2D', '3D'])

# Ingresar la ecuación en la barra lateral
if tipo_grafica == '2D':
    st.sidebar.subheader('Ecuación en función de x')
    ecuacion = st.sidebar.text_input('Ingresa una ecuación en función de x (por ejemplo, a*x + b):', 'a*x + b')
else:
    st.sidebar.subheader('Ecuación en función de x e y')
    ecuacion = st.sidebar.text_input('Ingresa una ecuación en función de x e y (por ejemplo, a*x + b*y):', 'a*x + b*y')

# Encontrar las constantes en la ecuación
# Excluyendo 'x', 'y' y funciones matemáticas comunes
funciones_permitidas = ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt']
tokens = re.findall(r'[a-zA-Z_]\w*', ecuacion)
constantes = set(tokens) - {'x', 'y'} - set(funciones_permitidas)

# Crear sliders para las constantes en la barra lateral
st.sidebar.subheader('Ajustar Constantes')
valores_constantes = {}
for const in constantes:
    valores_constantes[const] = st.sidebar.slider(f'Valor de {const}', -10.0, 10.0, 1.0)

# Definir el rango de x y y
if tipo_grafica == '2D':
    x = np.linspace(-10, 10, 400)
    entorno = {'x': x, 'np': np}
else:
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    entorno = {'x': X, 'y': Y, 'np': np}

# Añadir funciones matemáticas permitidas al entorno
for func in funciones_permitidas:
    entorno[func] = getattr(np, func)

entorno.update(valores_constantes)

# Evaluador de expresiones seguro
class EvaluadorSeguro(ast.NodeVisitor):
    def __init__(self, variables):
        self.variables = variables

    def visit(self, node):
        if isinstance(node, ast.Num):  # Números
            return node.n
        elif isinstance(node, ast.BinOp):  # Operaciones binarias
            left = self.visit(node.left)
            right = self.visit(node.right)
            return self.operar(node.op, left, right)
        elif isinstance(node, ast.UnaryOp):  # Operaciones unarias
            operand = self.visit(node.operand)
            return self.operar_unario(node.op, operand)
        elif isinstance(node, ast.Name):  # Variables
            if node.id in self.variables:
                return self.variables[node.id]
            else:
                raise ValueError(f"Uso de variable no permitida: {node.id}")
        elif isinstance(node, ast.Call):  # Funciones
            func_name = node.func.id
            if func_name in funciones_permitidas:
                args = [self.visit(arg) for arg in node.args]
                return self.variables[func_name](*args)
            else:
                raise ValueError(f"Uso de función no permitida: {func_name}")
        else:
            raise ValueError(f"Expresión no permitida: {ast.dump(node)}")

    def operar(self, op, left, right):
        if isinstance(op, ast.Add):
            return left + right
        elif isinstance(op, ast.Sub):
            return left - right
        elif isinstance(op, ast.Mult):
            return left * right
        elif isinstance(op, ast.Div):
            return left / right
        elif isinstance(op, ast.Pow):
            return left ** right
        else:
            raise ValueError(f"Operador no permitido: {op}")

    def operar_unario(self, op, operand):
        if isinstance(op, ast.UAdd):
            return +operand
        elif isinstance(op, ast.USub):
            return -operand
        else:
            raise ValueError(f"Operador unario no permitido: {op}")

def evaluar_expresion(expr, variables):
    try:
        node = ast.parse(expr, mode='eval').body
        evaluador = EvaluadorSeguro(variables)
        return evaluador.visit(node)
    except Exception as e:
        raise ValueError(f"Error al evaluar la expresión: {e}")

# Evaluar la ecuación de forma segura
try:
    y = evaluar_expresion(ecuacion, entorno)
    # Graficar la ecuación
    if tipo_grafica == '2D':
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Gráfica de la Ecuación en 2D')
        st.pyplot(fig)
    else:
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, y, cmap='viridis')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Gráfica de la Ecuación en 3D')
        st.pyplot(fig)
except Exception as e:
    st.error(f'Error al evaluar la ecuación: {e}')
