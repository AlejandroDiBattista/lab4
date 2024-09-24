import os
import base64
from PIL import Image, ExifTags
import streamlit as st
import folium
from streamlit_folium import st_folium
from io import BytesIO

# Configuración de la página para usar todo el ancho disponible
st.set_page_config(layout="wide")

# Función para convertir IFDRational a float
def rational_to_float(rational):
    if isinstance(rational, tuple):
        return float(rational[0]) / float(rational[1])
    return float(rational)

# Función para extraer coordenadas EXIF
def get_exif_location(image_path):
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
            # Convertir cada parte de DMS a float
            degrees = rational_to_float(dms[0])
            minutes = rational_to_float(dms[1])
            seconds = rational_to_float(dms[2])
            decimal = degrees + minutes / 60 + seconds / 3600
            if ref in ['S', 'W']:
                decimal *= -1
            return decimal

        lat = get_decimal_from_dms(gps_info[2], gps_info[1])
        lon = get_decimal_from_dms(gps_info[4], gps_info[3])
        return lat, lon
    except Exception as e:
        st.sidebar.error(f"Error al procesar {os.path.basename(image_path)}: {e}")
        return None

# Función para recortar la imagen al formato cuadrado
def crop_to_square(image_path, size=300):
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

# Título de la aplicación
st.title("📍 Visualizador de Fotos con Geolocalización")

# Instrucciones
st.markdown("""
Esta aplicación carga todas las fotos de una carpeta específica, extrae su información de geolocalización y muestra las posiciones en un mapa interactivo. Al hacer clic en una marca del mapa, se mostrará la foto correspondiente.
""")

# Barra lateral
with st.sidebar:
    st.header("🔧 Configuración")

    # Selección de carpeta
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
                location = get_exif_location(img_path)
                if location:
                    images_with_location.append({
                        'path': img_path,
                        'lat': location[0],
                        'lon': location[1],
                        'name': os.path.basename(img_path)
                    })
                else:
                    st.warning(f"⚠️ La imagen **{os.path.basename(img_path)}** no contiene información de geolocalización.")

            if not images_with_location:
                st.error("❌ Ninguna imagen contiene información de geolocalización.")
            else:
                # Lista de fotos cargadas
                st.subheader("📸 Fotos Cargadas")
                photo_names = [img['name'] for img in images_with_location]
                selected_photo = st.selectbox("🔍 Selecciona una foto para centrar el mapa:", options=photo_names)

                # Opcional: Mostrar detalles de la foto seleccionada
                selected_img = next((img for img in images_with_location if img['name'] == selected_photo), None)
                if selected_img:
                    st.markdown(f"**Ubicación:** ({selected_img['lat']}, {selected_img['lon']})")

# Verificar nuevamente si hay imágenes con ubicación
if 'images_with_location' in locals() and images_with_location:
    # Crear mapa centrado en la primera ubicación o en la seleccionada
    if 'selected_img' in locals() and selected_img:
        map_center = [selected_img['lat'], selected_img['lon']]
        zoom_start = 14
    else:
        map_center = [images_with_location[0]['lat'], images_with_location[0]['lon']]
        zoom_start = 12

    m = folium.Map(location=map_center, zoom_start=zoom_start, tiles="OpenStreetMap")

    for img in images_with_location:
        # Recortar la imagen al formato cuadrado
        cropped_image = crop_to_square(img['path'])
        if cropped_image:
            # Convertir la imagen a base64
            buffered = BytesIO()
            cropped_image.save(buffered, format="JPEG")
            encoded = base64.b64encode(buffered.getvalue()).decode()

            # Crear HTML para el popup
            html = f'<img src="data:image/jpeg;base64,{encoded}" width="300" height="300">'

            # Añadir marcador al mapa
            folium.Marker(
                location=[img['lat'], img['lon']],
                popup=folium.Popup(html, max_width=300),
                tooltip=img['name']
            ).add_to(m)

    # Si se seleccionó una foto, agregar un marcador destacado
    if 'selected_img' in locals() and selected_img:
        folium.Marker(
            location=[selected_img['lat'], selected_img['lon']],
            popup="📍 Foto Seleccionada",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        m.location = [selected_img['lat'], selected_img['lon']]

    # Mostrar el mapa en Streamlit
    st.subheader("🗺️ Mapa de Ubicaciones de Fotos")
    folium_map = st_folium(m, width=1300, height=800)

    # Opcional: Ajustar el zoom al marcador seleccionado
    if 'selected_img' in locals() and selected_img:
        folium_map['map'].location = [selected_img['lat'], selected_img['lon']]
        folium_map['map'].zoom_start = 14
