# Módulos

En Python, los **módulos** son una de las herramientas más poderosas y versátiles que permiten organizar y reutilizar el código de manera eficiente. Un módulo es simplemente un archivo que contiene definiciones y declaraciones de Python, como funciones, clases y variables. Los módulos ayudan a mantener el código limpio, modular y fácil de mantener.

## Utilidad de los Módulos

Los módulos proporcionan varias ventajas clave:

- **Reutilización de Código**: Permiten reutilizar funciones, clases y variables en diferentes programas sin necesidad de reescribir el código.
- **Organización**: Ayudan a organizar el código en archivos separados basados en su funcionalidad, lo que mejora la legibilidad y el mantenimiento.
- **Namespace**: Evitan conflictos de nombres al encapsular definiciones dentro de su propio espacio de nombres.
- **Colaboración**: Facilitan el trabajo en equipo, permitiendo que diferentes desarrolladores trabajen en diferentes módulos de un proyecto.

## Creación de un Módulo

Crear un módulo en Python es sencillo. Solo necesitas crear un archivo con la extensión `.py` y definir las funciones, clases o variables que deseas incluir.

### Ejemplo de Creación de un Módulo

Supongamos que queremos crear un módulo llamado `matematicas.py` que contiene funciones para operaciones matemáticas básicas.

```python
# matematicas.py

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Devuelve la división de dos números. Lanza un error si el divisor es cero."""
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b
```

En este ejemplo, hemos creado un módulo `matematicas.py` que define cuatro funciones básicas: `suma`, `resta`, `multiplicacion` y `division`.

## Uso de Módulos

Una vez creado un módulo, puedes utilizar sus funciones, clases y variables en otros archivos de Python mediante la instrucción `import`.

### Importar Todo el Módulo

Puedes importar todo el módulo y acceder a sus miembros utilizando la sintaxis `modulo.miembro`.

```python
# usar_matematicas.py

import matematicas

resultado_suma = matematicas.suma(5, 3)
print("Suma:", resultado_suma)  # Output: Suma: 8

resultado_resta = matematicas.resta(10, 4)
print("Resta:", resultado_resta)  # Output: Resta: 6
```

### Importar Funciones Específicas

También puedes importar funciones específicas del módulo utilizando la sintaxis `from modulo import miembro`.

```python
# usar_matematicas_especificas.py

from matematicas import multiplicacion, division

resultado_multiplicacion = multiplicacion(7, 6)
print("Multiplicación:", resultado_multiplicacion)  # Output: Multiplicación: 42

resultado_division = division(20, 4)
print("División:", resultado_division)  # Output: División: 5.0
```

### Importar con Alias

Para evitar conflictos de nombres o simplificar el acceso, puedes asignar un alias al módulo o a sus miembros.

```python
# usar_matematicas_alias.py

import matematicas as mat

resultado = mat.suma(2, 3)
print("Resultado:", resultado)  # Output: Resultado: 5

from matematicas import resta as r
print("Resta:", r(10, 5))  # Output: Resta: 5
```

## Construcción de Paquetes

Un **paquete** en Python es una forma de organizar múltiples módulos en una estructura de directorios jerárquica. Los paquetes facilitan la gestión de grandes proyectos dividiendo el código en módulos más pequeños y manejables.

### Estructura de un Paquete

Para crear un paquete, sigue estos pasos:

1. **Crear un Directorio**: Este directorio representará el paquete.
2. **Agregar un Archivo `__init__.py`**: Este archivo puede estar vacío o contener código de inicialización del paquete. Su presencia indica a Python que el directorio debe ser tratado como un paquete.
3. **Agregar Módulos**: Dentro del directorio, agrega archivos `.py` que serán los módulos del paquete.

### Ejemplo de Creación de un Paquete

Supongamos que queremos crear un paquete llamado `utilidades` que contiene módulos para matemáticas y cadenas de texto.

#### Estructura del Paquete

```
utilidades/
│
├── __init__.py
├── matematicas.py
└── cadenas.py
```

#### Contenido de `matematicas.py`

```python
# utilidades/matematicas.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
```

#### Contenido de `cadenas.py`

```python
# utilidades/cadenas.py

def mayusculas(texto):
    """Convierte el texto a mayúsculas."""
    return texto.upper()

def minusculas(texto):
    """Convierte el texto a minúsculas."""
    return texto.lower()
```

#### Contenido de `__init__.py`

```python
# utilidades/__init__.py

from .matematicas import suma, resta
from .cadenas import mayusculas, minusculas

__all__ = ['suma', 'resta', 'mayusculas', 'minusculas']
```

En este ejemplo, el archivo `__init__.py` importa las funciones de los módulos `matematicas.py` y `cadenas.py` y define la lista `__all__` para controlar qué se exporta cuando se utiliza `from utilidades import *`.

### Uso del Paquete

Una vez creado el paquete, puedes utilizarlo en otros archivos de Python de la siguiente manera:

```python
# usar_utilidades.py

from utilidades import suma, mayusculas

resultado = suma(10, 5)
print("Suma:", resultado)  # Output: Suma: 15

texto = "hola mundo"
texto_mayusculas = mayusculas(texto)
print("Texto en mayúsculas:", texto_mayusculas)  # Output: Texto en mayúsculas: HOLA MUNDO
```

## Ejemplos Prácticos

### Creación y Uso de un Módulo

1. **Crear el Módulo**

   Crea un archivo llamado `saludos.py` con el siguiente contenido:

   ```python
   # saludos.py

   def saludar(nombre):
       """Imprime un saludo personalizado."""
       print(f"Hola, {nombre}!")

   def despedir(nombre):
       """Imprime una despedida personalizada."""
       print(f"Adiós, {nombre}!")
   ```

2. **Usar el Módulo**

   Crea otro archivo llamado `uso_saludos.py` para utilizar el módulo `saludos`.

   ```python
   # uso_saludos.py

   import saludos

   saludos.saludar("Ana")    # Output: Hola, Ana!
   saludos.despedir("Ana")   # Output: Adiós, Ana!
   ```

### Creación y Uso de un Paquete

1. **Crear la Estructura del Paquete**

   ```
   mi_paquete/
   │
   ├── __init__.py
   ├── matematicas.py
   └── utilidades_cadenas.py
   ```

2. **Contenido de `matematicas.py`**

   ```python
   # mi_paquete/matematicas.py

   def multiplicar(a, b):
       return a * b

   def dividir(a, b):
       if b == 0:
           raise ValueError("El divisor no puede ser cero.")
       return a / b
   ```

3. **Contenido de `utilidades_cadenas.py`**

   ```python
   # mi_paquete/utilidades_cadenas.py

   def capitalizar(texto):
       """Capitaliza la primera letra de cada palabra."""
       return texto.title()

   def invertir(texto):
       """Invierte el texto."""
       return texto[::-1]
   ```

4. **Contenido de `__init__.py`**

   ```python
   # mi_paquete/__init__.py

   from .matematicas import multiplicar, dividir
   from .utilidades_cadenas import capitalizar, invertir

   __all__ = ['multiplicar', 'dividir', 'capitalizar', 'invertir']
   ```

5. **Usar el Paquete**

   Crea un archivo llamado `uso_paquete.py` para utilizar el paquete `mi_paquete`.

   ```python
   # uso_paquete.py

   from mi_paquete import multiplicar, capitalizar

   resultado = multiplicar(4, 5)
   print("Multiplicación:", resultado)  # Output: Multiplicación: 20

   texto = "hola mundo"
   texto_capitalizado = capitalizar(texto)
   print("Texto capitalizado:", texto_capitalizado)  # Output: Texto capitalizado: Hola Mundo
   ```

## Uso de `__init__.py`

El archivo `__init__.py` es esencial para que Python reconozca un directorio como un paquete. Puede contener código de inicialización para el paquete o simplemente estar vacío. Además, es útil para definir qué componentes del paquete estarán disponibles cuando se importe utilizando `from paquete import *`.

### Ejemplo de `__init__.py` con Código de Inicialización

```python
# mi_paquete/__init__.py

print("Paquete 'mi_paquete' cargado.")

from .matematicas import multiplicar, dividir
from .utilidades_cadenas import capitalizar, invertir

__all__ = ['multiplicar', 'dividir', 'capitalizar', 'invertir']
```

Al importar el paquete, se ejecutará el código dentro de `__init__.py`.

```python
# uso_paquete.py

import mi_paquete
# Output: Paquete 'mi_paquete' cargado.

from mi_paquete import multiplicar

resultado = multiplicar(2, 3)
print("Resultado:", resultado)  # Output: Resultado: 6
```

## Ejemplos de Paquetes

### Paquete Estándar de Python: `math`

Python incluye una amplia variedad de módulos estándar que forman parte de la biblioteca estándar. Uno de ellos es el módulo `math`, que proporciona funciones matemáticas avanzadas.

```python
# usar_math.py

import math

print("Valor de pi:", math.pi)              # Output: Valor de pi: 3.141592653589793
print("Raíz cuadrada de 16:", math.sqrt(16))  # Output: Raíz cuadrada de 16: 4.0
print("Seno de 90 grados:", math.sin(math.radians(90)))  # Output: Seno de 90 grados: 1.0
```

### Paquete de Terceros: `requests`

`requests` es un paquete de terceros ampliamente utilizado para realizar solicitudes HTTP de manera sencilla.

1. **Instalación del Paquete**

   ```bash
   pip install requests
   ```

2. **Uso del Paquete**

   ```python
   # usar_requests.py

   import requests

   respuesta = requests.get("https://api.github.com")
   print("Código de estado:", respuesta.status_code)  # Output: Código de estado: 200
   print("Contenido:", respuesta.json())
   ```

## Conclusión

Los módulos y paquetes son fundamentales para escribir código Python limpio, organizado y reutilizable. Al dividir el código en módulos, puedes gestionar mejor proyectos grandes, facilitar la colaboración y mantener una estructura lógica. Además, la capacidad de construir paquetes permite agrupar módulos relacionados, lo que mejora aún más la modularidad y escalabilidad de tus proyectos.

## Resumen

1. **Utilidad de los Módulos**:
   - Reutilización de código.
   - Organización del código.
   - Evitar conflictos de nombres.
   - Facilitar la colaboración en equipo.

2. **Creación de un Módulo**:
   - Crear un archivo `.py` con definiciones de funciones, clases y variables.

3. **Uso de Módulos**:
   - Importar el módulo completo.
   - Importar funciones o clases específicas.
   - Utilizar alias para módulos o miembros.

4. **Construcción de Paquetes**:
   - Crear un directorio con un archivo `__init__.py`.
   - Agregar módulos al paquete.
   - Importar y utilizar componentes del paquete.

5. **Ejemplos Prácticos**:
   - Creación y uso de módulos individuales.
   - Creación y uso de paquetes.
   - Uso de paquetes estándar y de terceros.

Estos conceptos y prácticas te permitirán aprovechar al máximo las capacidades de Python para desarrollar aplicaciones robustas y mantenibles.