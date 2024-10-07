import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

def generar_qr(url, monto):
    """
    Genera una imagen de código QR a partir de una URL y agrega el texto "Doná $<monto>".
    """
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill='black', back_color='white')

    # Agregar el texto debajo del QR
    img_pil = img_qr.convert("RGB")
    buffer = BytesIO()
    img_pil.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def main():
    st.set_page_config(page_title="Generador de Códigos QR", layout="wide")
    st.title("Generador de Códigos QR para Donaciones")

    # Barra lateral para ingresar datos

    categorias = ["Mercado Libre", "Modo"]
    link_cobro = ['https://mpago.la/22u2j9Y','https://www.modo.com.ar/coupon/?id=41PQqxwezOO5HM48WwkXyE']

    num_montos = 3  # Número de montos a ingresar

    # Ingresar los montos una sola vez
    montos = []
    st.sidebar.header("Montos a donar")
    etiquetas = ["Mínimo", "Agradecido", "Generoso"]
    with st.sidebar:
        cols = st.columns(3)
        for i, (col, etiqueta) in enumerate(zip(cols, etiquetas), start=1):
            with col:
                monto = st.number_input(
                    f"{etiqueta}",
                    min_value=0.0,
                    step=100.0,
                    format="%.2f",
                    value=[1000.00, 2000.00, 3000.00][i-1],
                    key=f"monto_{i}"
                )
                montos.append(monto)

        # Ingresar las URLs para cada categoría en la barra lateral
        datos = {}
        for c,categoria in enumerate(categorias):
            urls = []
            st.header(f"{categoria.title()}")
            for i, monto in enumerate(montos, start=1):
                url = st.text_input(
                    f"Ingrese URL Donar ${monto:.2f}",
                    key=f"{categoria}_url_{i}",
                    value=link_cobro[c]
                )
                if url:
                    url = f"{url}?monto={monto:.2f}"
                urls.append(url)
            datos[categoria] = {"urls": urls}
    
    # Verificar que todas las URLs estén ingresadas
    for categoria in categorias:
        for idx, url in enumerate(datos[categoria]["urls"], start=1):
            if not url:
                st.warning(f"Por favor, ingresa la URL {idx} para {categoria}.")
                return

    # Crear dos columnas en la pantalla principal
    col_ml, col_modo = st.columns(2)

    with col_ml:
        st.header("Mercado Libre")
        for monto, url in zip(montos, datos["Mercado Libre"]["urls"]):
            if monto > 0 and url:
                buffer = generar_qr(url, monto)
                st.image(buffer, caption=f"Doná $ {monto:.2f}", width=300)
                st.markdown("---")  # Línea separadora

    with col_modo:
        st.header("Modo")
        for monto, url in zip(montos, datos["Modo"]["urls"]):
            if monto > 0 and url:
                buffer = generar_qr(url, monto)
                st.image(buffer, caption=f"Doná $ {monto:.2f}", width=300)
                st.markdown("---")  # Línea separadora

if __name__ == "__main__":
    main()
