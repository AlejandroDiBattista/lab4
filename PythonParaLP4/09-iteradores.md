# Iterador 

En muchas circunstancias, necesitamos recorrer los elementos de una colección, como una lista, tupla, conjunto o diccionario, para realizar alguna operación con cada uno de ellos. Para esto, Python proporciona una estructura llamada **iterador** que nos permite recorrer los elementos de una colección de forma secuencial.

Un **iterador** es un objeto que implementa el protocolo de iteración, lo que significa que puede ser utilizado en un bucle `for` para recorrer los elementos de una colección. Los iteradores en Python se utilizan para recorrer secuencialmente los elementos de una colección sin tener que conocer la estructura interna de la misma.

## Creación de un iterador

En Python, un iterador se crea utilizando la función `iter()` sobre una colección, como una lista, tupla, conjunto o diccionario. Por ejemplo:

```python
nombres = ["Juan", "María", "Carlos"]
iterador = iter(nombres)
```

En el ejemplo anterior, se ha creado un iterador a partir de una lista de nombres utilizando la función `iter()`. El iterador `iterador` se puede utilizar para recorrer secuencialmente los elementos de la lista `nombres`.

## Recorrido de un iterador

Para recorrer los elementos de un iterador en Python, se utiliza un bucle `for`. Por ejemplo:

```python
nombres = ["Juan", "María", "Carlos"]
iterador = iter(nombres)

for nombre in iterador:
    print(nombre)
```

En el ejemplo anterior, se ha recorrido el iterador `iterador` utilizando un bucle `for` e imprimiendo cada uno de los nombres de la lista `nombres`.

## Función `next()`

En Python, la función `next()` se utiliza para obtener el siguiente elemento de un iterador. Por ejemplo:

```python
nombres = ["Juan", "María", "Carlos"]
iterador = iter(nombres)

print(next(iterador))  # Output: Juan
print(next(iterador))  # Output: María
print(next(iterador))  # Output: Carlos
# print(next(iterador))  # Esto causaría un error: StopIteration
```

En el ejemplo anterior, se ha utilizado la función `next()` para obtener secuencialmente cada uno de los nombres de la lista `nombres` a través del iterador `iterador`. Intentar llamar a `next(iterador)` una cuarta vez causaría una excepción `StopIteration`, ya que no hay más elementos en la lista.

## Iteradores en bucles `for`

En Python, los bucles `for` utilizan iteradores para recorrer los elementos de una colección. Por ejemplo:

```python
nombres = ["Juan", "María", "Carlos"]

for nombre in nombres:
    print(nombre)
```

Un iterador muy usado es `range()`, que genera una secuencia de números enteros. Por ejemplo:

```python
for i in range(5):
    print(i)
```

La sentencia `for` busca si el objeto pasado tiene el método `__iter__`. Si no lo tiene, intenta acceder a los elementos mediante el método `__getitem__` empezando por el índice `0` hasta que se produzca una excepción `IndexError`. No utiliza `__len__`.

La ventaja de los iteradores es que permiten recorrer colecciones de elementos de manera eficiente, sin tener que cargar todos los elementos en memoria al mismo tiempo. Esto es especialmente útil cuando se trabaja con colecciones grandes o infinitas.

Python utiliza intensamente los iteradores, por ejemplo:

```python 
l = list("abracadabra")
print(l)
# Output: ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

# list usa un iterador para recorrer la cadena

s = set("abracadabra")
print(s)
# Output: {'a', 'b', 'r', 'c', 'd'}
# set usa un iterador para recorrer la cadena

for i, vocal in enumerate("aeiou"):
    print(i, vocal)
# Output: 
# 0 a
# 1 e
# 2 i
# 3 o
# 4 u

# enumerate usa un iterador para recorrer la cadena (agrega un índice a cada elemento)

d = dict(enumerate("aeiou"))
print(d)
# Output: {0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u'}

# dict usa un iterador para recorrer la cadena (agrega un índice a cada elemento)

l = list(set("abracadabra"))
print(l)
# Output: ['a', 'b', 'r', 'c', 'd']
# set usa un iterador para recorrer la cadena, y list usa un iterador para recorrer el set 

c = sum((1, 2))
print(c)
# Output: 3
# sum usa un iterador para recorrer los elementos de la tupla (1, 2)

c = sum([1, 2])
print(c)
# Output: 3

# sum usa un iterador para recorrer los elementos de la lista [1, 2]

c = sum({1, 2, 3, 1, 2, 3, 1, 3})
print(c)
# Output: 6

# sum usa un iterador para recorrer los elementos del conjunto {1, 2, 3} (eliminados los repetidos)

c = sum(range(1, 100, 2))
print(c)
# Output: 2500 
# sum usa un iterador para recorrer los elementos del rango (1, 100, 2) (1, 3, 5, ..., 99) 

m = max("aeiou")
print(m)
# Output: u

m = max([1, 2, 5, 4, 3])
print(m)
# Output: 5

cuadrados = map(lambda x: x**2, range(10))
print(list(cuadrados))
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# map usa un iterador para recorrer los elementos del rango (0, 10) y aplicar la función lambda

def par(x):   
    return x % 2 == 0

def impar(x): 
    return x % 2 != 0

def doble(x): 
    return x * 2

pares = all(map(par, range(0, 20)))
# Output: False (¿son todos pares?)

l = list(map(doble, filter(par, range(0, 20))))

# 1. Filtrar todos los pares del rango (0, 20)
# 2. Aplicar la función doble a cada elemento
# 3. Convertir el resultado en una lista

print(l)
# Output: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
```

Los iteradores, como cualquier objeto en Python, pueden ser pasados como argumentos a una función, devueltos por una función, asignados a una variable, etc.

```python
def doble(iterador):   
    return map(lambda x: x * 2, iterador)  # map toma un iterador y devuelve otro iterador

for a in doble(range(10)):
    print(a, end=" ")
# Output: 0 2 4 6 8 10 12 14 16 18

print(list(doble(range(10))))
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

a, b, *c = doble(range(7))
print(a, b, c)
# Output: 0 2 [4, 6, 8, 10, 12]
```

Incluso se puede combinar varios iteradores en uno solo:

```python
par = zip('aeiou', range(1, 11, 2))
print(list(par))
# Output: [('a', 1), ('e', 3), ('i', 5), ('o', 7), ('u', 9)]

numerar = zip(range(1000), 'abracadabra')  # Zip combina dos iteradores en uno solo (hasta que uno de los dos se agote)
print(list(numerar))
# Output: [(0, 'a'), (1, 'b'), (2, 'r'), (3, 'a'), (4, 'c'), (5, 'a'), (6, 'd'), (7, 'a'), (8, 'b'), (9, 'r'), (10, 'a')]

d = dict(zip(['x', 'y', 'z'], [10, 20, 30]))
print(d)
# Output: {'x': 10, 'y': 20, 'z': 30}
```

## Librería `itertools`

Esta **librería** proporciona funciones para trabajar con iteradores de forma eficiente. Por ejemplo:

```python
from itertools import * 

for i in count(10, 2):
    print(i, end=" ")
    if i > 20: break
# Output: 10 12 14 16 18 20 22

for i in cycle("aeiou"):
    print(i, end=" ")
    if i == 'u': break
# Output: a e i o u

for i in repeat("Hola", 3):
    print(i, end=" ")
# Output: Hola Hola Hola

for i in chain("aeiou", range(10)):
    print(i, end=" ")   
# Output: a e i o u 0 1 2 3 4 5 6 7 8 9

for i in combinations("abcd", 2):
    print(i, end=" ")
# Output: ('a', 'b') ('a', 'c') ('a', 'd') ('b', 'c') ('b', 'd') ('c', 'd')

for i in accumulate(range(10)):
    print(i, end=" ")
# Output: 0 1 3 6 10 15 21 28 36 45

for i in product("abc", "123"):
    print(i, end=" ")
# Output: ('a', '1') ('a', '2') ('a', '3') ('b', '1') ('b', '2') ('b', '3') ('c', '1') ('c', '2') ('c', '3')

# Agrupar las vocales y las consonantes de una cadena 

def es_vocal(x): 
    return x in "aeiou"

for k, g in groupby(sorted("hola mundo"), es_vocal):
    print(k, list(g))
# Output: 
# False [' ', 'a', 'c', 'd', 'h', 'l', 'm', 'n', 'o', 'r', 'u']
# True ['a', 'e', 'i', 'o', 'u']
```

Algunas funciones de la librería `itertools`:

- **islice**: Genera una secuencia de elementos de un iterador.
- **takewhile**: Genera una secuencia de elementos mientras se cumpla una condición.
- **dropwhile**: Genera una secuencia de elementos después de que se cumpla una condición.
- **filterfalse**: Genera una secuencia de elementos que no cumplen una condición.
- **compress**: Genera una secuencia de elementos seleccionados por una máscara.
- **count**: Genera una secuencia de números enteros.
- **cycle**: Genera una secuencia cíclica de elementos.
- **repeat**: Genera una secuencia de elementos repetidos.
- **chain**: Concatena varias secuencias en una sola.
- **combinations**: Genera todas las combinaciones posibles de una secuencia.
- **accumulate**: Genera una secuencia acumulada de elementos.
- **product**: Genera el producto cartesiano de varias secuencias.
- **permutations**: Genera todas las permutaciones posibles de una secuencia.
- **groupby**: Agrupa elementos consecutivos de una secuencia.

## Generadores

Existe una forma muy simple de generar iteradores en Python, utilizando funciones generadoras. Una función generadora es una función que contiene la palabra clave `yield` en lugar de `return`. 
Cuando en una función se encuentra con la palabra clave `yield`, retorna un valor y se suspende la ejecución de la función. Cuando se llama a la función nuevamente, la ejecución se reanuda en el punto donde se suspendió.

```python
# Genera tres valores: 1, 2, 3
def tres():
    yield 1
    yield 2
    yield 3

for i in tres():
    print(i, end=" ")
# Output: 1 2 3

# Genera los números del 1 al n
def contar(n):
    for i in range(n):
        yield i+1

for i in contar(5):
    print(i, end=" ")
# Output: 1 2 3 4 5

# También se puede usar `next()` para obtener los valores de un generador de uno en uno

c = contar(3)
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
# print(next(c))  # Esto causaría un error: StopIteration
```

La maravilla de los generadores es que trabajan en forma perezosa (lazy), es decir, no generan todos los valores de una vez, sino que los generan a medida que se necesitan. Esto es especialmente útil cuando se trabaja con colecciones grandes o infinitas, ya que no es necesario cargar todos los elementos en memoria al mismo tiempo.

Por ejemplo, el siguiente generador produce los números primos de forma indefinida:

```python
def primos():
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0: 
                break  # Si es divisible por alguno, no es primo
        else:
            yield n  # Si no es divisible por ninguno, es primo
        n += 1

p = primos()

# Se los puede traer uno a uno con `next()`
print(next(p))  # 2
print(next(p))  # 3
print(next(p))  # 5
print(next(p))  # 7
print(next(p))  # 11
# print(next(p))  # Continuar según se necesite

from itertools import * 

def menor100(x): 
    return x < 100 

for i in takewhile(menor100, primos()):  # Tome los primos mientras sean menores a 100
    print(i, end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

# o más breve aún 
print(list(takewhile(menor100, primos())))  # Tome los primos mientras sean menores a 100
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(list(islice(primos(), 2, 20, 3)))  # Dame una lista de los primos desde el índice 2 hasta el 20, saltando de 3 en 3
# Output: [5, 11, 17, 23, 31, 41, 47, 59, 67, 79, 89]

print(list(zip(range(10), primos())))  # Empareja los primos con los primeros 10 números
# Output: [(0, 2), (1, 3), (2, 5), (3, 7), (4, 11), (5, 13), (6, 17), (7, 19), (8, 23), (9, 29)]
```

Se pueden realizar operaciones muy interesantes como concatenar generadores, filtrarlos, etc., usando `yield from`:

```python
# Forma tradicional de concatenar dos generadores
def concatenar(a, b):
    for i in a: 
        yield i
    for i in b: 
        yield i

print(list(concatenar(range(3), range(5, 7))))
# Output: [0, 1, 2, 5, 6]

# Forma moderna de concatenar dos generadores
def concatenar(a, b):
    yield from a
    yield from b

print(list(concatenar(range(3), range(5, 7))))
# Output: [0, 1, 2, 5, 6]

# Forma tradicional de filtrar un generador
def filtrar(a, condicion):
    for i in a:
        if condicion(i):
            yield i

print(list(filtrar(range(10), lambda x: x % 2 == 0)))
# Output: [0, 2, 4, 6, 8]
```

Por último, hay una forma muy interesante de generar generadores usando una **expresión generadora**. Las expresiones generadoras son similares a las listas por comprensión, pero en lugar de devolver una lista, devuelven un generador. Por ejemplo:

```python
# Dame los cuadrados de los números entre 0 y 100 que sean múltiplos de 32
g = (x**2 for x in range(100) if x % 32 == 0)
print(list(g))
# Output: [0, 1024, 4096, 9216]

# Se puede usar una expresión generadora en cualquier lugar donde se espera un generador

print(sum(x**2 for x in range(10)))
# Output: 285

def filtrar(a, condicion):
    return (i for i in a if condicion(i))

print(list(filtrar(range(10), lambda x: x % 2 == 0)))
# Output: [0, 2, 4, 6, 8]
```