import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objects as go
from sympy.parsing.sympy_parser import parse_expr
from sympy.core.sympify import SympifyError

# Configuración de la página
st.set_page_config(page_title="Visualizador de Ecuaciones", layout="wide")

st.title("Visualizador de Ecuaciones Matemáticas")

# Entrada de la ecuación
equation_input = st.text_input(
    "Ingresa una ecuación en términos de x e y:",
    "a * x**2 + b * y + c"
)

# Función para identificar variables y constantes
def parse_equation(equation_str):
    x, y = sp.symbols('x y')
    try:
        expr = parse_expr(equation_str, evaluate=False)
        variables = expr.free_symbols
        constants = list(expr.free_symbols.symmetric_difference({x, y}))
        return expr, variables, constants, None
    except SympifyError as e:
        return None, None, None, str(e)

expr, variables, constants, error = parse_equation(equation_input)

if error:
    st.error(f"Error en la ecuación: {error}")
else:
    # Identificar si es 1D o 2D
    independent_vars = sorted(list(variables), key=lambda var: var.name)
    num_vars = len(independent_vars)

    # Crear sliders para constantes
    constant_values = {}
    if constants:
        st.sidebar.header("Constantes")
        for const in constants:
            constant_values[str(const)] = st.sidebar.slider(
                label=f"Valor de {const}",
                min_value=-10.0,
                max_value=10.0,
                value=1.0,
                step=0.1
            )
    else:
        st.sidebar.write("No hay constantes en la ecuación.")

    # Crear sliders para rangos de variables
    st.sidebar.header("Rangos de Variables")
    if sp.Symbol('x') in independent_vars:
        x_min, x_max = st.sidebar.slider(
            "Rango de x",
            min_value=-10.0,
            max_value=10.0,
            value=(-5.0, 5.0),
            step=0.1
        )
    if sp.Symbol('y') in independent_vars:
        y_min, y_max = st.sidebar.slider(
            "Rango de y",
            min_value=-10.0,
            max_value=10.0,
            value=(-5.0, 5.0),
            step=0.1
        )

    # Sustituir constantes en la expresión
    substituted_expr = expr
    for const, value in constant_values.items():
        substituted_expr = substituted_expr.subs(sp.Symbol(const), value)

    # Generar funciones numéricas
    try:
        if num_vars == 1:
            var = independent_vars[0]
            f = sp.lambdify(var, substituted_expr, modules=['numpy'])

            x_vals = np.linspace(x_min, x_max, 400)
            y_vals = f(x_vals)

            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals)
            ax.set_xlabel(str(var))
            ax.set_ylabel('f({})'.format(str(var)))
            ax.set_title('Gráfico 2D')

            st.pyplot(fig)

        elif num_vars == 2:
            x, y = sp.symbols('x y')
            f = sp.lambdify((x, y), substituted_expr, modules=['numpy'])

            x_vals = np.linspace(x_min, x_max, 100)
            y_vals = np.linspace(y_min, y_max, 100)
            X, Y = np.meshgrid(x_vals, y_vals)
            Z = f(X, Y)

            # Manejar posibles errores en la evaluación
            if np.any(np.isnan(Z)) or np.any(np.isinf(Z)):
                st.error("La ecuación produce valores no numéricos en el rango seleccionado.")
            else:
                fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
                fig.update_layout(title='Gráfico 3D', autosize=True,
                                  scene=dict(
                                      xaxis_title='x',
                                      yaxis_title='y',
                                      zaxis_title='f(x, y)'
                                  ))
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("La ecuación debe depender de al menos una variable (x o y).")
    except Exception as e:
        st.error(f"Error al evaluar la ecuación: {e}")
