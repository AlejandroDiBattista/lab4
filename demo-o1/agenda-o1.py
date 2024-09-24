import streamlit as st
import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('agenda.db', check_same_thread=False)
c = conn.cursor()

# Funciones para manipular la base de datos
def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            telefono TEXT,
            email TEXT
        )
    ''')
    conn.commit()

def add_contacto(nombre, apellido, telefono, email):
    c.execute('''
        INSERT INTO contactos (nombre, apellido, telefono, email)
        VALUES (?, ?, ?, ?)
    ''', (nombre, apellido, telefono, email))
    conn.commit()

def get_contactos():
    c.execute('SELECT * FROM contactos ORDER BY apellido, nombre')
    return c.fetchall()

def get_contacto(id_contacto):
    c.execute('SELECT * FROM contactos WHERE id = ?', (id_contacto,))
    return c.fetchone()

def update_contacto(id_contacto, nombre, apellido, telefono, email):
    c.execute('''
        UPDATE contactos
        SET nombre = ?, apellido = ?, telefono = ?, email = ?
        WHERE id = ?
    ''', (nombre, apellido, telefono, email, id_contacto))
    conn.commit()

def delete_contacto(id_contacto):
    c.execute('DELETE FROM contactos WHERE id = ?', (id_contacto,))
    conn.commit()

# Crear la tabla si no existe
create_table()

# Función principal de la aplicación
def main():
    st.title('📇 Agenda de Contactos')

    # Inicializar variables de sesión
    if 'modo' not in st.session_state:
        st.session_state['modo'] = None
    if 'contacto' not in st.session_state:
        st.session_state['contacto'] = None
    if 'actualizar' not in st.session_state:
        st.session_state['actualizar'] = False
    if 'search_query' not in st.session_state:
        st.session_state['search_query'] = ''

    # Campo de búsqueda y botón agregar
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input('Buscar Contacto', placeholder='Nombre o Apellido', key='search_input')
        st.session_state['search_query'] = search_query
    with col2:
        if st.button('Agregar Contacto'):
            st.session_state['modo'] = 'agregar'
            st.session_state['contacto'] = None

    st.markdown('---')

    # Mostrar lista de contactos filtrados
    contactos = get_contactos()

    if st.session_state['search_query']:
        contactos = [c for c in contactos if st.session_state['search_query'].lower() in c[1].lower() or st.session_state['search_query'].lower() in c[2].lower()]

    if contactos:
        for contacto in contactos:
            id_contacto = contacto[0]
            nombre = contacto[1]
            apellido = contacto[2]
            telefono = contacto[3] if contacto[3] else 'N/A'
            email = contacto[4] if contacto[4] else 'N/A'

            st.markdown(f"### {apellido}, {nombre}")
            st.write(f"**Teléfono:** {telefono}")
            st.write(f"**Email:** {email}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button('✏️ Editar', key=f'edit_{id_contacto}'):
                    st.session_state['modo'] = 'editar'
                    st.session_state['contacto'] = contacto
            with col2:
                if st.button('🗑️ Borrar', key=f'delete_{id_contacto}'):
                    delete_contacto(id_contacto)
                    st.success('Contacto eliminado.')
                    st.session_state['actualizar'] = True
                    st.experimental_set_query_params()
            st.markdown('---')
    else:
        st.info('No hay contactos para mostrar.')

    # Modo Agregar o Editar
    if st.session_state['modo'] in ['agregar', 'editar']:
        with st.sidebar:
            if st.session_state['modo'] == 'agregar':
                st.header('Agregar Contacto')
                nombre = st.text_input('Nombre', key='nombre_agregar')
                apellido = st.text_input('Apellido', key='apellido_agregar')
                telefono = st.text_input('Teléfono', key='telefono_agregar')
                email = st.text_input('Email', key='email_agregar')
                if st.button('Guardar', key='guardar_agregar'):
                    if nombre and apellido:
                        add_contacto(nombre, apellido, telefono, email)
                        st.success('Contacto agregado exitosamente.')
                        st.session_state['modo'] = None
                        st.session_state['actualizar'] = True
                        st.experimental_set_query_params()
                    else:
                        st.warning('Nombre y Apellido son obligatorios.')
            elif st.session_state['modo'] == 'editar':
                contacto = st.session_state['contacto']
                st.header('Editar Contacto')
                nombre = st.text_input('Nombre', value=contacto[1], key='nombre_editar')
                apellido = st.text_input('Apellido', value=contacto[2], key='apellido_editar')
                telefono = st.text_input('Teléfono', value=contacto[3], key='telefono_editar')
                email = st.text_input('Email', value=contacto[4], key='email_editar')
                if st.button('Actualizar', key='actualizar_editar'):
                    if nombre and apellido:
                        update_contacto(contacto[0], nombre, apellido, telefono, email)
                        st.success('Contacto actualizado exitosamente.')
                        st.session_state['modo'] = None
                        st.session_state['contacto'] = None
                        st.session_state['actualizar'] = True
                        st.experimental_set_query_params()
                    else:
                        st.warning('Nombre y Apellido son obligatorios.')
                if st.button('Cancelar', key='cancelar_editar'):
                    st.session_state['modo'] = None
                    st.session_state['contacto'] = None
                    st.experimental_set_query_params()

if __name__ == '__main__':
    main()
