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
    image = Image.open(image_path)
    exif_data = image._getexif()
    if not exif_data:
        return None

    exif = {
        ExifTags.TAGS.get(tag, tag): value
        for tag, value in exif_data.items()
    }

    if 'GPSInfo' not in exif or 'DateTimeOriginal' not in exif:
        return None

    gps_info = exif['GPSInfo']

    def get_decimal_from_dms(dms, ref):
        degrees = dms[0].numerator / dms[0].denominator
        minutes = dms[1].numerator / dms[1].denominator
        seconds = dms[2].numerator / dms[2].denominator
        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
        if ref in ['S', 'W']:
            decimal *= -1
        return decimal

    lat = get_decimal_from_dms(gps_info[2], gps_info[1])
    lon = get_decimal_from_dms(gps_info[4], gps_info[3])
    datetime_original = exif.get('DateTimeOriginal', 'No disponible')

    return {
        'lat': lat,
        'lon': lon,
        'datetime': datetime_original
    }

# Función para recortar la imagen al formato cuadrado con tamaño variable
def crop_to_square(image_path, size=100):
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

# Función para convertir la imagen a base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded = base64.b64encode(buffered.getvalue()).decode()
    return encoded

# Agregar estilos CSS para las miniaturas y la foto seleccionada
st.markdown("""
    <style>
    .thumbnail {
        border-radius: 5px;
        border: 2px solid transparent;
        cursor: pointer;
        object-fit: cover;
    }
    .selected {
        border: 3px solid red;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la aplicación
st.title("📍 Visualizador de Fotos con Geolocalización")

# Inicializar estado para la foto seleccionada
if 'selected_photo' not in st.session_state:
    st.session_state.selected_photo = None

# Barra lateral
with st.sidebar:
    st.header("📸 Fotos Cargadas")
    folder_path = "./fotos"  # Ruta por defecto

    # Obtener lista de imágenes
    supported_formats = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif')
    image_files = [
        os.path.join(folder_path, f) for f in os.listdir(folder_path)
        if f.lower().endswith(supported_formats)
    ]

    images_with_location = []
    for img_path in image_files:
        exif_data = get_exif_data(img_path)
        if exif_data:
            images_with_location.append({
                'path': img_path,
                'lat': exif_data['lat'],
                'lon': exif_data['lon'],
                'name': os.path.basename(img_path),
                'datetime': exif_data['datetime']
            })

    # Mostrar miniaturas en una grilla de 3 columnas
    if images_with_location:
        cols = st.columns(3)
        col_index = 0
        for img in images_with_location:
            with cols[col_index]:
                cropped_image = crop_to_square(img['path'], size=100)
                encoded_image = image_to_base64(cropped_image)
                # Determinar si la foto está seleccionada para aplicar estilos
                if st.session_state.selected_photo and st.session_state.selected_photo['path'] == img['path']:
                    st.markdown(f"""
                        <img src="data:image/jpeg;base64,{encoded_image}" class="thumbnail selected" width="100" height="100">
                        """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <img src="data:image/jpeg;base64,{encoded_image}" class="thumbnail" width="100" height="100" onclick="window.location.href='?selected={img['path']}'">
                        """, unsafe_allow_html=True)
                # Botón invisible sobre la imagen para detectar el clic
                if st.button("", key=img['path']):
                    st.session_state.selected_photo = img
            col_index += 1
            if col_index >= 3:
                col_index = 0
                cols = st.columns(3)

        # Detalles de la foto seleccionada
        if st.session_state.selected_photo:
            st.markdown("---")
            st.markdown("### 📄 Detalles de la Foto Seleccionada")
            selected_img = st.session_state.selected_photo
            cols = st.columns([1, 3])
            with cols[0]:
                cropped_image = crop_to_square(selected_img['path'], size=150)
                encoded_image = image_to_base64(cropped_image)
                st.markdown(f"""
                    <img src="data:image/jpeg;base64,{encoded_image}" class="thumbnail selected" style="width:150px; height:150px;">
                    """, unsafe_allow_html=True)
            with cols[1]:
                st.markdown(f"**Nombre:** {selected_img['name']}")
                st.markdown(f"**Coordenadas:** `{selected_img['lat']:.6f}, {selected_img['lon']:.6f}`")
                st.markdown(f"**Fecha y Hora:** {selected_img['datetime']}")

    st.markdown("---")
    st.markdown("Desarrollado por [Tu Nombre](#)")

# Mapa principal
if images_with_location:
    if st.session_state.selected_photo:
        map_center = [st.session_state.selected_photo['lat'], st.session_state.selected_photo['lon']]
        zoom_start = 14
    else:
        map_center = [images_with_location[0]['lat'], images_with_location[0]['lon']]
        zoom_start = 12

    m = folium.Map(location=map_center, zoom_start=zoom_start, tiles="OpenStreetMap")

    for img in images_with_location:
        # Aumentar el tamaño de la imagen para el popup (e.g., 300 píxeles)
        cropped_image = crop_to_square(img['path'], size=300)
        encoded = image_to_base64(cropped_image)
        html = f"""
        <div style="text-align: center;">
            <img src="data:image/jpeg;base64,{encoded}" width="300" height="300"><br>
            <b>{img["name"]}</b><br>
            📍 Coordenadas: {img["lat"]:.6f}, {img["lon"]:.6f}<br>
            🕒 Fecha y Hora: {img["datetime"]}
        </div>
        """
        folium.Marker(
            location=[img['lat'], img['lon']],
            popup=folium.Popup(html, max_width=350),
            tooltip=img['name']
        ).add_to(m)

    st.subheader("🗺️ Mapa de Ubicaciones de Fotos")
    st_folium(m, width=1300, height=800)
