import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Ajuste de una función cúbica a puntos de muestra")

# Inicializamos variables en session_state
if 'a' not in st.session_state:
    st.session_state['a'] = 0.0
if 'b' not in st.session_state:
    st.session_state['b'] = 0.0
if 'c' not in st.session_state:
    st.session_state['c'] = 0.0
if 'd' not in st.session_state:
    st.session_state['d'] = 0.0
if 'adjustment_factor' not in st.session_state:
    st.session_state['adjustment_factor'] = 0.1
if 'error' not in st.session_state:
    st.session_state['error'] = None
if 'auto_adjust' not in st.session_state:
    st.session_state['auto_adjust'] = False
if 'x_data' not in st.session_state:
    # Generamos valores de x
    st.session_state['x_data'] = np.linspace(-10, 10, 200)
    # Coeficientes verdaderos de la función cúbica
    a_true = 1.0
    b_true = -2.0
    c_true = 1.0
    d_true = 0.5
    # Generamos valores de y con ruido
    np.random.seed(42)  # Para reproducibilidad
    noise = np.random.normal(0, 10, size=st.session_state['x_data'].shape)
    st.session_state['y_data'] = a_true * st.session_state['x_data'] ** 3 + b_true * st.session_state['x_data'] ** 2 + c_true * st.session_state['x_data'] + d_true + noise

x_data = st.session_state['x_data']
y_data = st.session_state['y_data']

# Parámetros ajustables en el Sidebar
st.sidebar.header("Ajusta los parámetros de la función cúbica")

if not st.session_state['auto_adjust']:
    st.session_state['a'] = st.sidebar.slider('Coeficiente a', -5.0, 5.0, st.session_state['a'], 0.1)
    st.session_state['b'] = st.sidebar.slider('Coeficiente b', -5.0, 5.0, st.session_state['b'], 0.1)
    st.session_state['c'] = st.sidebar.slider('Coeficiente c', -5.0, 5.0, st.session_state['c'], 0.1)
    st.session_state['d'] = st.sidebar.slider('Coeficiente d', -5.0, 5.0, st.session_state['d'], 0.1)
    if st.sidebar.button("Ajustar automáticamente"):
        st.session_state['auto_adjust'] = True
else:
    st.sidebar.write(f"Coeficiente a: {st.session_state['a']:.4f}")
    st.sidebar.write(f"Coeficiente b: {st.session_state['b']:.4f}")
    st.sidebar.write(f"Coeficiente c: {st.session_state['c']:.4f}")
    st.sidebar.write(f"Coeficiente d: {st.session_state['d']:.4f}")
    if st.sidebar.button("Detener ajuste"):
        st.session_state['auto_adjust'] = False
        st.session_state['adjustment_factor'] = 0.1  # Reiniciamos el factor de ajuste

# Calculamos la función con los parámetros ajustados
def calculate_model(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d

# Contenedores para actualizar la gráfica y el error
plot_placeholder = st.empty()
error_placeholder = st.empty()

if st.session_state['auto_adjust']:
    adjustment_factor = st.session_state['adjustment_factor']
    error = float('inf')

    while error > 10 and adjustment_factor >= 0.001 and st.session_state['auto_adjust']:
        for param in ['a', 'b', 'c', 'd']:
            if not st.session_state['auto_adjust']:
                break  # Salimos si el usuario detiene el ajuste

            original_value = st.session_state[param]

            # Calcular el error con el valor original
            y_model_original = calculate_model(
                st.session_state['a'],
                st.session_state['b'],
                st.session_state['c'],
                st.session_state['d'],
                x_data
            )
            error_original = np.sum((y_model_original - y_data) ** 2)

            # Calcular el error al sumar el factor de ajuste
            st.session_state[param] = original_value + adjustment_factor
            y_model_plus = calculate_model(
                st.session_state['a'],
                st.session_state['b'],
                st.session_state['c'],
                st.session_state['d'],
                x_data
            )
            error_plus = np.sum((y_model_plus - y_data) ** 2)

            # Calcular el error al restar el factor de ajuste
            st.session_state[param] = original_value - adjustment_factor
            y_model_minus = calculate_model(
                st.session_state['a'],
                st.session_state['b'],
                st.session_state['c'],
                st.session_state['d'],
                x_data
            )
            error_minus = np.sum((y_model_minus - y_data) ** 2)

            # Encontrar el mínimo error y actualizar el parámetro si corresponde
            errors = [error_original, error_plus, error_minus]
            min_error = min(errors)
            min_index = errors.index(min_error)

            if min_index == 0:
                # El error mínimo es con el valor original, no actualizamos el parámetro
                st.session_state[param] = original_value
            elif min_index == 1:
                # El error mínimo es al sumar el factor de ajuste
                st.session_state[param] = original_value + adjustment_factor
            elif min_index == 2:
                # El error mínimo es al restar el factor de ajuste
                st.session_state[param] = original_value - adjustment_factor

            # Actualizamos el error
            error = min_error
            st.session_state['error'] = error

            # Actualizamos la gráfica y el error
            with plot_placeholder:
                fig, ax = plt.subplots()
                ax.scatter(x_data, y_data, color='blue', label='Puntos de muestra', s=10)
                y_model = calculate_model(
                    st.session_state['a'],
                    st.session_state['b'],
                    st.session_state['c'],
                    st.session_state['d'],
                    x_data
                )
                ax.plot(x_data, y_model, color='red', label='Función ajustada', linewidth=2)
                ax.legend()
                st.pyplot(fig)

            with error_placeholder:
                st.write(f"Error (suma de los cuadrados de las diferencias): {error:.2f}")

            # Actualizamos los coeficientes en el Sidebar
            st.sidebar.write(f"Coeficiente a: {st.session_state['a']:.4f}")
            st.sidebar.write(f"Coeficiente b: {st.session_state['b']:.4f}")
            st.sidebar.write(f"Coeficiente c: {st.session_state['c']:.4f}")
            st.sidebar.write(f"Coeficiente d: {st.session_state['d']:.4f}")

            time.sleep(0.1)  # Pausa para simular animación

            # Si el error mínimo es con el valor original, dejamos de ajustar este parámetro
            if min_index == 0:
                break  # Salimos del ajuste de este parámetro

        # Reducimos el factor de ajuste a la mitad
        adjustment_factor /= 2
        st.session_state['adjustment_factor'] = adjustment_factor

    st.session_state['auto_adjust'] = False  # Detenemos el ajuste automático una vez finalizado
    st.success("Ajuste automático completado.")
else:
    # Calculamos y mostramos la gráfica y el error cuando no hay ajuste automático
    y_model = calculate_model(
        st.session_state['a'],
        st.session_state['b'],
        st.session_state['c'],
        st.session_state['d'],
        x_data
    )
    error = np.sum((y_model - y_data) ** 2)
    st.session_state['error'] = error

    with plot_placeholder:
        fig, ax = plt.subplots()
        ax.scatter(x_data, y_data, color='blue', label='Puntos de muestra', s=10)
        ax.plot(x_data, y_model, color='red', label='Función ajustada', linewidth=2)
        ax.legend()
        st.pyplot(fig)

    with error_placeholder:
        st.write(f"Error (suma de los cuadrados de las diferencias): {error:.2f}")
