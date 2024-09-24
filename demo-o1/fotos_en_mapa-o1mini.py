import os
import base64
from io import BytesIO
from PIL import Image, ExifTags
import streamlit as st
import folium
from streamlit_folium import st_folium

# Configuración de la página para usar todo el ancho disponible
st.set_page_config(layout="wide", page_title="Visualizador de Fotos Geolocalizadas")

# Función para extraer coordenadas EXIF y fecha y hora
def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None

        exif = {
            ExifTags.TAGS.get(tag, tag): value
            for tag, value in exif_data.items()
        }

        if 'GPSInfo' not in exif:
            return None

        gps_info = exif['GPSInfo']

        def get_decimal_from_dms(dms, ref):
            try:
                degrees = dms[0].numerator / dms[0].denominator
                minutes = dms[1].numerator / dms[1].denominator
                seconds = dms[2].numerator / dms[2].denominator
                decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
                if ref in ['S', 'W']:
                    decimal *= -1
                return decimal
            except AttributeError:
                return None

        lat = get_decimal_from_dms(gps_info[2], gps_info[1])
        lon = get_decimal_from_dms(gps_info[4], gps_info[3])

        # Obtener fecha y hora
        datetime_original = exif.get('DateTimeOriginal', 'No disponible')

        return {
            'lat': lat,
            'lon': lon,
            'datetime': datetime_original
        }
    except Exception as e:
        st.sidebar.error(f"Error al procesar {os.path.basename(image_path)}: {e}")
        return None

# Función para recortar la imagen al formato cuadrado
def crop_to_square(image_path, size=150):
    try:
        image = Image.open(image_path)
        width, height = image.size
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        image_cropped = image.crop((left, top, right, bottom))
        image_cropped = image_cropped.resize((size, size))
        return image_cropped
    except Exception as e:
        st.sidebar.error(f"Error al recortar {os.path.basename(image_path)}: {e}")
        return None

# Función para convertir la imagen a base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded = base64.b64encode(buffered.getvalue()).decode()
    return encoded

# Título de la aplicación
st.title("📍 Visualizador de Fotos con Geolocalización")

# Instrucciones
st.markdown("""
Esta aplicación carga todas las fotos de una carpeta específica, extrae su información de geolocalización y muestra las posiciones en un mapa interactivo. En la barra lateral, puedes seleccionar una foto para ver su miniatura, coordenadas, fecha y hora de captura. Al hacer clic en una marca del mapa, se mostrará la foto correspondiente.
""")

# Inicializar estado para la foto seleccionada
if 'selected_photo' not in st.session_state:
    st.session_state.selected_photo = None

# Barra lateral
with st.sidebar:
    st.header("🔧 Configuración")

    # Selección de carpeta con valor por defecto
    folder_path = st.text_input("📁 Ruta de la carpeta que contiene las fotos:", value="./fotos")

    if not os.path.isdir(folder_path):
        st.error("❌ La ruta proporcionada no es una carpeta válida.")
    else:
        # Obtener lista de imágenes
        supported_formats = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif')
        image_files = [
            os.path.join(folder_path, f) for f in os.listdir(folder_path)
            if f.lower().endswith(supported_formats)
        ]

        if not image_files:
            st.warning("⚠️ No se encontraron imágenes en la carpeta especificada.")
        else:
            # Extraer coordenadas y crear lista de imágenes con ubicación
            images_with_location = []
            for img_path in image_files:
                exif_data = get_exif_data(img_path)
                if exif_data and exif_data['lat'] is not None and exif_data['lon'] is not None:
                    images_with_location.append({
                        'path': img_path,
                        'lat': exif_data['lat'],
                        'lon': exif_data['lon'],
                        'name': os.path.basename(img_path),
                        'datetime': exif_data['datetime']
                    })
                else:
                    st.warning(f"⚠️ La imagen **{os.path.basename(img_path)}** no contiene información de geolocalización o datos EXIF insuficientes.")

            if not images_with_location:
                st.error("❌ Ninguna imagen contiene información de geolocalización válida.")
            else:
                # Lista de fotos cargadas en una grilla de 3 columnas
                st.subheader("📸 Fotos Cargadas")
                cols = st.columns(3)
                col_index = 0
                for img in images_with_location:
                    with cols[col_index]:
                        # Recortar y mostrar miniatura
                        cropped_image = crop_to_square(img['path'], size=100)
                        if cropped_image:
                            encoded_image = image_to_base64(cropped_image)
                            st.image(f"data:image/jpeg;base64,{encoded_image}", use_column_width=True)

                        # Botón para seleccionar la foto
                        if st.button(img['name'], key=img['path']):
                            st.session_state.selected_photo = img

                    col_index += 1
                    if col_index >= 3:
                        col_index = 0
                        cols = st.columns(3)

                # Mostrar detalles de la foto seleccionada
                if st.session_state.selected_photo:
                    st.markdown("---")
                    st.markdown("### 📄 Detalles de la Foto Seleccionada")
                    selected_img = st.session_state.selected_photo
                    cols = st.columns([1, 3])
                    with cols[0]:
                        cropped_image = crop_to_square(selected_img['path'], size=150)
                        if cropped_image:
                            encoded_image = image_to_base64(cropped_image)
                            st.image(f"data:image/jpeg;base64,{encoded_image}", use_column_width=True)
                    with cols[1]:
                        st.markdown(f"**Nombre:** {selected_img['name']}")
                        st.markdown(f"**Coordenadas:** `{selected_img['lat']:.6f}, {selected_img['lon']:.6f}`")
                        st.markdown(f"**Fecha y Hora:** {selected_img['datetime']}")

    st.markdown("---")
    st.markdown("Desarrollado por [Tu Nombre](#)")

# Verificar nuevamente si hay imágenes con ubicación
if 'images_with_location' in locals() and images_with_location:
    # Crear mapa centrado en la foto seleccionada o en la primera foto
    if st.session_state.selected_photo:
        map_center = [st.session_state.selected_photo['lat'], st.session_state.selected_photo['lon']]
        zoom_start = 14
    else:
        map_center = [images_with_location[0]['lat'], images_with_location[0]['lon']]
        zoom_start = 12

    m = folium.Map(location=map_center, zoom_start=zoom_start, tiles="OpenStreetMap")

    for img in images_with_location:
        # Recortar la imagen al formato cuadrado para el popup
        cropped_image = crop_to_square(img['path'])
        if cropped_image:
            encoded = image_to_base64(cropped_image)

            # Crear HTML para el popup
            html = f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{encoded}" width="300" height="300"><br>
                <b>{img["name"]}</b><br>
                📍 Coordenadas: {img["lat"]:.6f}, {img["lon"]:.6f}<br>
                🕒 Fecha y Hora: {img["datetime"]}
            </div>
            """

            # Añadir marcador al mapa
            folium.Marker(
                location=[img['lat'], img['lon']],
                popup=folium.Popup(html, max_width=350),
                tooltip=img['name']
            ).add_to(m)

    # Mostrar el mapa en Streamlit
    st.subheader("🗺️ Mapa de Ubicaciones de Fotos")
    folium_map = st_folium(m, width=1300, height=800)
