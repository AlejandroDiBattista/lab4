import json
import difflib


if __name__ == "__main__":
    ruta_original   = '../Lab4/practicos/tp1/ejercicio.ipynb'
    
    ruta_modificado = '../Lab4-C2/practicos/15 - 59268 - Cordoba, Pedro Josue/tp1/ejercicios.ipynb'

    original   = cargar_cuaderno(ruta_original)
    modificado = cargar_cuaderno(ruta_modificado)

    print(comparar_cuadernos(original, modificado))
