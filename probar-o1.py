import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # Necesario para graficar en 3D

# Tokenizador y analizador de expresiones
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text.replace(' ', '')
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def generate_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isdigit() or self.current_char == '.':
                tokens.append(self.generate_number())
            elif self.current_char.isalpha():
                tokens.append(self.generate_identifier())
            elif self.current_char in '+-*/^()':
                tokens.append(Token(self.current_char, self.current_char))
                self.advance()
            else:
                raise Exception(f"Carácter inválido: '{self.current_char}'")
        return tokens

    def generate_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
            num_str += self.current_char
            self.advance()
        return Token('NUMBER', float(num_str))

    def generate_identifier(self):
        id_str = ''
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == '_'):
            id_str += self.current_char
            self.advance()
        return Token('IDENTIFIER', id_str)

# Nodos del árbol de expresiones
class Node:
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class VariableNode(Node):
    def __init__(self, name):
        self.name = name

class BinOpNode(Node):
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node

class UnaryOpNode(Node):
    def __init__(self, op_token, node):
        self.op_token = op_token
        self.node = node

# Analizador sintáctico
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        if self.current_token is None:
            return None
        result = self.expr()
        if self.current_token is not None:
            raise Exception("Token inesperado al final")
        return result

    def expr(self):
        result = self.term()
        while self.current_token is not None and self.current_token.type in ('+', '-'):
            op_token = self.current_token
            self.advance()
            result = BinOpNode(result, op_token, self.term())
        return result

    def term(self):
        result = self.power()
        while self.current_token is not None and self.current_token.type in ('*', '/'):
            op_token = self.current_token
            self.advance()
            result = BinOpNode(result, op_token, self.power())
        return result

    def power(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type == '^':
            op_token = self.current_token
            self.advance()
            result = BinOpNode(result, op_token, self.factor())
        return result

    def factor(self):
        token = self.current_token
        if token.type in ('+', '-'):
            self.advance()
            return UnaryOpNode(token, self.factor())
        elif token.type == 'NUMBER':
            self.advance()
            return NumberNode(token.value)
        elif token.type == 'IDENTIFIER':
            self.advance()
            return VariableNode(token.value)
        elif token.type == '(':
            self.advance()
            result = self.expr()
            if self.current_token is None or self.current_token.type != ')':
                raise Exception("Se esperaba ')'")
            self.advance()
            return result
        else:
            raise Exception(f"Token inesperado: {token.type}")

# Evaluador
class Interpreter:
    def __init__(self, tree, variables):
        self.tree = tree
        self.variables = variables

    def visit(self, node):
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, VariableNode):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                raise Exception(f"Variable no definida: {node.name}")
        elif isinstance(node, BinOpNode):
            if node.op_token.type == '+':
                return self.visit(node.left_node) + self.visit(node.right_node)
            elif node.op_token.type == '-':
                return self.visit(node.left_node) - self.visit(node.right_node)
            elif node.op_token.type == '*':
                return self.visit(node.left_node) * self.visit(node.right_node)
            elif node.op_token.type == '/':
                return self.visit(node.left_node) / self.visit(node.right_node)
            elif node.op_token.type == '^':
                return self.visit(node.left_node) ** self.visit(node.right_node)
        elif isinstance(node, UnaryOpNode):
            if node.op_token.type == '+':
                return +self.visit(node.node)
            elif node.op_token.type == '-':
                return -self.visit(node.node)
        else:
            raise Exception(f"Nodo desconocido: {type(node)}")

    def interpret(self):
        return self.visit(self.tree)

# Extracción de variables
def extract_variables(node, variables=set()):
    if isinstance(node, VariableNode):
        variables.add(node.name)
    elif isinstance(node, BinOpNode):
        extract_variables(node.left_node, variables)
        extract_variables(node.right_node, variables)
    elif isinstance(node, UnaryOpNode):
        extract_variables(node.node, variables)
    return variables

# Aplicación Streamlit
st.set_page_config(page_title="Graficador de Funciones", layout="centered")
st.title("Graficador de Funciones")

# Sidebar para la entrada de datos
st.sidebar.header("Configuración")

# Selección de dimensión (2D o 3D)
dimension = st.sidebar.selectbox("Selecciona la dimensión de la gráfica:", ["2D", "3D"])

# Ingreso de la expresión
if dimension == "2D":
    expr_input = st.sidebar.text_input("Ingresa una expresión en función de 'x':", "a * x^2 + b * x + c")
else:
    expr_input = st.sidebar.text_input("Ingresa una expresión en función de 'x' e 'y':", "a * x^2 + b * y^2 + c")

# Tokenización y parsing
try:
    lexer = Lexer(expr_input)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()

    # Extracción de variables
    variables = extract_variables(tree)
    variables = variables - {'x', 'y'}  # Excluir 'x' e 'y' de las variables
except Exception as e:
    st.error(f"Error al analizar la expresión: {e}")
    st.stop()

# Ingreso de valores para variables
st.sidebar.subheader("Variables")
var_values = {}
for var in sorted(variables):
    val = st.sidebar.number_input(f"Ingresa el valor para '{var}':", value=1.0)
    var_values[var] = val

# Selección del rango de 'x' y 'y'
st.sidebar.subheader("Rango de variables independientes")
x_min = st.sidebar.number_input("Valor mínimo de 'x':", value=-10.0)
x_max = st.sidebar.number_input("Valor máximo de 'x':", value=10.0)

if dimension == "3D":
    y_min = st.sidebar.number_input("Valor mínimo de 'y':", value=-10.0)
    y_max = st.sidebar.number_input("Valor máximo de 'y':", value=10.0)

# Botón para graficar
if st.sidebar.button("Graficar"):
    if x_min >= x_max:
        st.error("El valor mínimo de 'x' debe ser menor que el valor máximo.")
    elif dimension == "3D" and y_min >= y_max:
        st.error("El valor mínimo de 'y' debe ser menor que el valor máximo.")
    else:
        if dimension == "2D":
            # Generación de valores de 'x'
            x_values = [x_min + i * (x_max - x_min) / 400 for i in range(401)]
            y_values = []
            for x in x_values:
                try:
                    local_vars = var_values.copy()
                    local_vars['x'] = x
                    interpreter = Interpreter(tree, local_vars)
                    y = interpreter.interpret()
                    y_values.append(y)
                except Exception as e:
                    st.error(f"Error al evaluar la función en x={x}: {e}")
                    break

            if len(y_values) == len(x_values):
                # Configuración de la gráfica
                fig, ax = plt.subplots()
                ax.plot(x_values, y_values, label=expr_input)

                ax.set_xlabel('x')
                ax.set_ylabel('f(x)')
                ax.set_title('Gráfica de la Función')
                ax.legend()
                ax.grid(True)

                # Mostrar la gráfica en Streamlit
                st.pyplot(fig)
        else:
            # Generación de valores de 'x' e 'y'
            x_values = [x_min + i * (x_max - x_min) / 50 for i in range(51)]
            y_values = [y_min + i * (y_max - y_min) / 50 for i in range(51)]
            X, Y = [], []
            Z = []
            for x in x_values:
                row_z = []
                for y in y_values:
                    try:
                        local_vars = var_values.copy()
                        local_vars['x'] = x
                        local_vars['y'] = y
                        interpreter = Interpreter(tree, local_vars)
                        z = interpreter.interpret()
                        row_z.append(z)
                    except Exception as e:
                        st.error(f"Error al evaluar la función en x={x}, y={y}: {e}")
                        break
                Z.append(row_z)
            # Preparar datos para la gráfica
            X, Y = np.meshgrid(x_values, y_values)
            Z = np.array(Z).T  # Transponer para que coincidan las dimensiones

            # Configuración de la gráfica 3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, Y, Z, cmap='viridis')

            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('f(x, y)')
            ax.set_title('Gráfica de la Función 3D')

            # Mostrar la gráfica en Streamlit
            st.pyplot(fig)
