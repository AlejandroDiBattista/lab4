# Colecciones

Python permite almacenar una **colección** de elementos en una sola variable. Las colecciones más comunes en Python son las **listas**, **tuplas**, **conjuntos** y **diccionarios**.

## Listas `list`

Una **lista** es una colección ordenada de elementos que se pueden modificar. En Python, una lista se define utilizando corchetes `[]` y los elementos se separan por comas `,`.

Por ejemplo:

```python
nombres = ["Juan", "María", "Carlos"]
edades = [30, 25, 35]
alturas = [1.75, 1.65, 1.80]
```

### Creación de una lista

```python
# Expresión literal de una lista
nombres = ["Juan", "María", "Carlos"]
#> ['Juan', 'María', 'Carlos']

# Creación de una lista con la función `list()`
nombres = list(["Juan", "María", "Carlos"])
#> ['Juan', 'María', 'Carlos']

# Creación de una lista vacía y agregar elementos
nombres = []  # Crear una lista vacía
nombres.append("Juan")  # Agregar un elemento a la lista
nombres.append("María")
#> ['Juan', 'María']

# Otras formas de crear una lista vacía
vacia = []       # Lista vacía
vacia = list()   # Lista vacía usando la función `list()`

# Copiar una lista
nueva = list(nombres)

# Crear una lista a partir de un diccionario (solo las claves)
d = list({'x': 1, 'y': 2})
#> ['x', 'y']

# Crear una lista a partir de una tupla
t = list((1, 2, 3))
#> [1, 2, 3]

# Crear una lista a partir de una secuencia de valores
digitos = list(range(10))   # Números del 0 al 9
#> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

vocales = list("aeiou")     # Lista con las vocales
#> ['a', 'e', 'i', 'o', 'u']
```

### Acceso a los elementos de una lista

Los elementos de una lista se acceden mediante un **índice**. El índice comienza en `0`. Si el índice es negativo, se cuenta desde el final de la lista.

```python
nombres = ["Juan", "María", "Carlos"]

print(nombres[0])    # Acceder al primer elemento
#> Juan

print(nombres[-1])   # Acceder al último elemento
#> Carlos

# Modificar un elemento de la lista
nombres[0] = "Pedro"
print(nombres)
#> ['Pedro', 'María', 'Carlos']
```

**Nota:** En Python, asignar una lista a otra variable no crea una copia de la lista, sino que crea una referencia a la lista original. Por lo tanto, si se modifica la lista original, la lista referenciada también se modificará.

```python
a = [1, 2, 3]
b = a
print(a, b)
#> [1, 2, 3] [1, 2, 3]

a[0] = 10
print(a, b)  # `b` también se modifica
#> [10, 2, 3] [10, 2, 3]

b[1] = 20
print(a, b)  # `a` también se modifica
#> [10, 20, 3] [10, 20, 3]

# Verificar si `a` y `b` son la misma lista
print(a is b)
#> True

# Para copiar una lista, usar el método `copy()`
a = [1, 2, 3]
b = a.copy()

print(a, b)
#> [1, 2, 3] [1, 2, 3]

a[0] = 10
print(a, b)  # `b` no se modifica
#> [10, 2, 3] [1, 2, 3]

b[1] = 20
print(a, b)  # `a` no se modifica
#> [10, 2, 3] [1, 20, 3]

# Otras formas de copiar una lista
b = list(a)          # Usando el constructor `list()`
b = a[:]             # Usando el operador slicing `[:]`
b = [*a]             # Usando el operador `*` para desempaquetar la lista
b = [x for x in a]   # Usando una comprensión de listas
```

### Slicing de listas

El **slicing** es una técnica en Python que permite obtener una sublista de una lista. Esta funcionalidad se puede usar tanto para extraer una sublista como para modificarla. Se puede llamar explícitamente a la función `slice()` o se puede usar la notación `[:]`, siendo esta última la más común y fácil de usar.

```python
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lista[slice(2, 7, 2)])  # Tomar del índice 2 al 7 (sin incluir) con saltos de 2
#> [30, 50, 70]
# slice(inicio, fin, salto) === lista[inicio:fin:salto]

# Si no se especifica el inicio, se toma desde el principio
print(lista[:7])  # Tomar desde el inicio hasta el índice 7 (sin incluir)
#> [10, 20, 30, 40, 50, 60, 70]

# Si no se especifica el fin, se toma hasta el final
print(lista[2:])  # Tomar desde el índice 2 hasta el final
#> [30, 40, 50, 60, 70, 80, 90]

# Si no se especifica el salto, se toma de uno en uno
print(lista[2:7])  # Tomar del índice 2 al 7 (sin incluir) de uno en uno
#> [30, 40, 50, 60, 70]

# Se pueden combinar todas las opciones
print(lista[2:7:2])  # Tomar del índice 2 al 7 (sin incluir) de dos en dos
#> [30, 50, 70]

# Si no se especifica el inicio, el fin y el salto, se toma toda la lista
print(lista[:])  # Tomar toda la lista
#> [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Se pueden usar índices negativos
print(lista[-7:-2])  # Tomar del índice -7 al -2 (sin incluir)
#> [30, 40, 50, 60, 70]

# Copiar una lista
copia = lista[:]

# Invertir una lista
invertida = lista[::-1]
```

En todos estos casos, el slicing se usa para extraer valores cuando se utiliza en el lado derecho de una asignación. Pero también se puede usar para modificar una lista cuando se utiliza en el lado izquierdo de una asignación.

```python
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lista)
#> [10, 20, 30, 40, 50, 60, 70, 80, 90]

lista[2:7] = [31, 41, 51, 61, 71]  # Modificar del índice 2 al 7 (sin incluir)
print(lista)
#> [10, 20, 31, 41, 51, 61, 71, 80, 90]

lista[2:7:2] = [32, 52, 72]  # Modificar del índice 2 al 7 (sin incluir) de dos en dos
print(lista)
#> [10, 20, 32, 41, 52, 61, 72, 80, 90]

# Se puede usar para borrar elementos
lista[2:7] = []  # Borrar del índice 2 al 7 (sin incluir)
print(lista)
#> [10, 20, 80, 90]

# Se puede usar para insertar elementos
lista[2:2] = [30, 40]  # Insertar en el índice 2
print(lista)
#> [10, 20, 30, 40, 80, 90]
```

El **slicing** es una herramienta muy poderosa y versátil, y es muy común en Python, por lo que es importante conocerla y saber usarla. El operador `:` es la forma más común de utilizarlo, pero también se puede usar la función `slice()` explícitamente.

### Recorrer una lista

Para recorrer una lista, podemos usar un bucle `for` o un bucle `while`, utilizando la función `len()` para obtener la longitud de la lista.

```python
nombres = ['Juan', 'María', 'Carlos']

# Con un bucle `while`
i = 0
while i < len(nombres):
    nombre = nombres[i]
    print(nombre, end=' ')
    i += 1
#> Juan María Carlos 

print()  # Para añadir una nueva línea

# Con un bucle `for` usando índices
for i in range(len(nombres)):
    nombre = nombres[i]
    print(nombre, end=' ')
#> Juan María Carlos 

print()

# Usando un bucle `for` directamente con los elementos
for nombre in nombres:
    print(nombre, end=' ')
#> Juan María Carlos 

print()

# Usando la función `enumerate()` para obtener el índice y el valor
for i, nombre in enumerate(nombres):
    print(i, nombre)
#> 0 Juan
#> 1 María
#> 2 Carlos
```

### Operaciones con listas

Las listas poseen métodos para agregar, eliminar y modificar elementos. Algunas de las funciones más comunes son:

- **`append()`**: Agrega un elemento al final de la lista.
- **`insert()`**: Agrega un elemento en una posición específica.
- **`pop()`**: Elimina un elemento de la lista y lo retorna.
- **`remove()`**: Elimina un elemento de la lista por su valor.
- **`index()`**: Retorna el índice de un elemento.
- **`count()`**: Cuenta la cantidad de veces que un elemento aparece en la lista.
- **`sort()`**: Ordena la lista.
- **`reverse()`**: Invierte el orden de la lista.
- **`copy()`**: Crea una copia de la lista.

```python
nombres = ["Juan", "María", "Carlos"]

# Agregar un elemento al final
nombres.append("Ana")
print(nombres)
#> ['Juan', 'María', 'Carlos', 'Ana']

# Insertar un elemento en una posición específica
nombres.insert(1, "Luis")
print(nombres)
#> ['Juan', 'Luis', 'María', 'Carlos', 'Ana']

# Eliminar el último elemento y retornarlo
ultimo = nombres.pop()
print(ultimo)  # Ana
#> Ana
print(nombres)
#> ['Juan', 'Luis', 'María', 'Carlos']

# Eliminar un elemento por su valor
nombres.remove("Luis")
print(nombres)
#> ['Juan', 'María', 'Carlos']

# Obtener el índice de un elemento
indice = nombres.index("María")
print(indice)
#> 1

# Contar cuántas veces aparece un elemento
cantidad = nombres.count("Carlos")
print(cantidad)
#> 1

# Ordenar la lista
nombres.sort()
print(nombres)
#> ['Carlos', 'Juan', 'María']

# Invertir el orden de la lista
nombres.reverse()
print(nombres)
#> ['María', 'Juan', 'Carlos']

# Copiar la lista
nombres_copia = nombres.copy()
print(nombres_copia)
#> ['María', 'Juan', 'Carlos']
```

## Diccionarios `dict`

Los **diccionarios** permiten mantener una colección **desordenada** de valores heterogéneos que se pueden acceder mediante una **clave**. En Python, un diccionario se define utilizando llaves `{}` y los pares clave-valor se separan por comas `,`.

Las claves pueden ser cualquier valor inmutable y hashable, como una cadena, un número o una tupla cuyos elementos también sean inmutables. Los valores pueden ser de cualquier tipo de dato.

### Creación de un diccionario

```python
# Expresión literal de un diccionario
persona = {"nombre": "Juan", "edad": 30}

# Creación de un diccionario con la función `dict()`
persona = dict(nombre="Juan", edad=30)

# Creación de un diccionario a partir de una lista de tuplas
persona = dict([("nombre", "Juan"), ("edad", 30)])

# Creación de un diccionario vacío y agregar elementos
persona = {}  # Diccionario vacío
persona["nombre"] = "Juan"  # Agregar un elemento
persona["edad"] = 30
```

### Acceso a los elementos de un diccionario

Para acceder a un elemento de un diccionario usamos la **clave** entre corchetes `[]`. Si accedemos a una clave inexistente, se generará un error `KeyError`. Para evitar este error, podemos usar el método `get()` o verificar la existencia de la clave con el operador `in`.

```python
persona = {'nombre': 'Juan', 'edad': 30}

# Acceder a un valor usando la clave
print(persona['nombre'])
#> Juan

# Usar el método `get()` para acceder a un valor
print(persona.get('nombre'))
#> Juan

# Intentar acceder a una clave inexistente con `get()`, retorna `None`
print(persona.get('apellido'))
#> None

# Intentar acceder a una clave inexistente con `get()`, retornando un valor por defecto
print(persona.get('apellido', '(anónimo)'))
#> (anónimo)

# Verificar si una clave existe usando el operador `in`
if 'apellido' in persona:
    print(persona['apellido'])
else:
    print('(anónimo)')
#> (anónimo)
```

### Métodos adicionales de diccionarios

Además de los métodos básicos, los diccionarios en Python ofrecen una variedad de métodos útiles para manejar sus elementos:

- **`keys()`**: Retorna una vista de las claves del diccionario.
- **`values()`**: Retorna una vista de los valores del diccionario.
- **`items()`**: Retorna una vista de los pares clave-valor.
- **`update()`**: Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable.
- **`pop()`**: Elimina el elemento con la clave especificada y lo retorna.
- **`clear()`**: Elimina todos los elementos del diccionario.

```python
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Obtener todas las claves
claves = persona.keys()
print(claves)
#> dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener todos los valores
valores = persona.values()
print(valores)
#> dict_values(['Juan', 30, 'Madrid'])

# Obtener todos los pares clave-valor
items = persona.items()
print(items)
#> dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])

# Actualizar el diccionario
persona.update({"edad": 31, "profesion": "Ingeniero"})
print(persona)
#> {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Eliminar un elemento con `pop()`
edad = persona.pop("edad")
print(edad)
#> 31
print(persona)
#> {'nombre': 'Juan', 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Eliminar todos los elementos
persona.clear()
print(persona)
#> {}
```

## Conjuntos `set`

Los **conjuntos** son colecciones desordenadas de elementos únicos. Se utilizan para almacenar elementos sin duplicados y para realizar operaciones matemáticas como la unión, intersección y diferencia.

En Python, un conjunto se define utilizando llaves `{}` para conjuntos con elementos o la función `set()`.

### Creación de un conjunto

```python
# Usando llaves con elementos
frutas = {"manzana", "banana", "cereza"}

# Usando la función `set()`
numeros = set([1, 2, 3, 4, 5])

# Crear un conjunto vacío
vacio = set()  # No se puede usar {} porque crea un diccionario vacío
```

**Nota:** Para crear un conjunto vacío se debe usar `set()`. Usar `{}` creará un diccionario vacío.

### Operaciones con conjuntos

- **Agregar elementos**: `add()`
- **Eliminar elementos**: `remove()` o `discard()`
- **Unión**: `union()` o `|`
- **Intersección**: `intersection()` o `&`
- **Diferencia**: `difference()` o `-`
- **Diferencia simétrica**: `symmetric_difference()` o `^`

```python
# Agregar un elemento
frutas.add("naranja")
print(frutas)
#> {'banana', 'manzana', 'naranja', 'cereza'}

# Eliminar un elemento
frutas.remove("banana")
print(frutas)
#> {'manzana', 'naranja', 'cereza'}

# Unión de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(union)
#> {1, 2, 3, 4, 5}

# Intersección de conjuntos
interseccion = set1.intersection(set2)
print(interseccion)
#> {3}

# Diferencia de conjuntos
diferencia = set1.difference(set2)
print(diferencia)
#> {1, 2}

# Diferencia simétrica
diff_simetrica = set1.symmetric_difference(set2)
print(diff_simetrica)
#> {1, 2, 4, 5}
```

### Métodos adicionales de conjuntos

- **`issubset()`**: Verifica si un conjunto es subconjunto de otro.
- **`issuperset()`**: Verifica si un conjunto es superconjunto de otro.
- **`copy()`**: Crea una copia del conjunto.
- **`clear()`**: Elimina todos los elementos del conjunto.

```python
set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}

# Verificar subconjunto
print(set1.issubset(set2))
#> True

# Verificar superconjunto
print(set2.issuperset(set1))
#> True

# Copiar un conjunto
set3 = set1.copy()
print(set3)
#> {1, 2}

# Eliminar todos los elementos
set3.clear()
print(set3)
#> set()
```

## Tuplas `tuple`

Las **tuplas** son colecciones ordenadas e **inmutables** de elementos. Son similares a las listas, pero una vez creadas, no pueden modificarse (no se pueden agregar, eliminar ni cambiar sus elementos).

En Python, una tupla se define utilizando paréntesis `()` o simplemente separando los elementos por comas.

### Creación de una tupla

```python
# Usando paréntesis
coordenadas = (10, 20)

# Sin usar paréntesis
colores = "rojo", "verde", "azul"

# Crear una tupla vacía
vacia = ()

# Tupla con un solo elemento (necesita una coma)
solo_un_elemento = (5,)
```

### Acceso a los elementos de una tupla

Al igual que las listas, los elementos de una tupla se acceden mediante índices.

```python
colores = ("rojo", "verde", "azul")

print(colores[0])
#> rojo

print(colores[-1])
#> azul

# Intentar modificar un elemento generará un error
# colores[0] = "amarillo"  # TypeError: 'tuple' object does not support item assignment
```

### Operaciones con tuplas

Aunque las tuplas son inmutables, se pueden realizar operaciones como concatenación y repetición.

```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenación
concatenada = tupla1 + tupla2
print(concatenada)
#> (1, 2, 3, 4, 5, 6)

# Repetición
repetida = tupla1 * 2
print(repetida)
#> (1, 2, 3, 1, 2, 3)

# Verificar la existencia de un elemento
print(2 in tupla1)
#> True

# Obtener el índice de un elemento
print(tupla1.index(3))
#> 2

# Contar la cantidad de veces que aparece un elemento
print(tupla1.count(2))
#> 1
```

### Métodos adicionales de tuplas

Las tuplas ofrecen métodos que facilitan su manipulación:

- **`count()`**: Cuenta cuántas veces aparece un elemento.
- **`index()`**: Retorna el índice de la primera aparición de un elemento.

```python
tupla = (1, 2, 3, 2, 4, 2)

# Contar la cantidad de veces que aparece el número 2
print(tupla.count(2))
#> 3

# Obtener el índice de la primera aparición del número 2
print(tupla.index(2))
#> 1
```