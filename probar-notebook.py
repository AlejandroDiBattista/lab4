from pathlib import Path
import nbformat
from nbclient import NotebookClient
import os

import contextlib
@contextlib.contextmanager
def change_directory(path):
    """Context manager for changing the current working directory"""
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

def verificar_ejecucion(origen, texto):
    # Separar la carpeta y el nombre del archivo
    origen_path = Path(origen)
    carpeta = origen_path.parent
    nombre_archivo = origen_path.name

    try:
        with cambiar_carpeta(carpeta):
            # Cargar el notebook
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)

            # Crear un cliente para ejecutar el notebook
            client = NotebookClient(nb, timeout=600, kernel_name='python3')
            client.execute()

            # Contar las ocurrencias del texto en las salidas de las celdas de código
            contador = sum(
                output.text.count(texto)
                for celda in nb.cells if celda.cell_type == 'code' and 'outputs' in celda
                for output in celda.outputs if output.output_type == 'stream' and 'text' in output
            )
            return contador
    except (nbformat.reader.NotJSONError, nbclient.exceptions.CellExecutionError) as e:
        print(f"Error al ejecutar el notebook: {e}")
        return 0

if __name__ == "__main__":
    
    origen = '/Users/adibattista/Documents/GitHub/Lab4-C5/practicos/23 - 59070 - Ladina, Maia Agostina/tp5/ejercicio.ipynb'
    r = verificar_ejecucion(origen, 'Prueba pasada exitosamente')
    if r == 6:
        print('Prueba pasada exitosamente')
    else:
        print('Prueba no pasada')
