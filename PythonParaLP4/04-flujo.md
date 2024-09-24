# Control de Flujo

El **control de flujo** en Python permite dirigir la ejecución de un programa en función de condiciones y repeticiones. Los elementos principales del control de flujo son las **condicionales**, los **bucles**, las **funciones**, la **recursividad** y el manejo de **excepciones**.

## Condicionales

Las estructuras condicionales permiten ejecutar diferentes bloques de código según se cumplan o no ciertas condiciones. Las principales estructuras condicionales en Python son `if`, `elif` y `else`.

### Sintaxis básica

```python
if condición:
    # Bloque de código si la condición es verdadera
    ...
elif otra_condición:
    # Bloque de código si la otra condición es verdadera
    ...
else:
    # Bloque de código si ninguna condición anterior es verdadera
    ...
```

### Ejemplos

#### Uso de `if` y `else`

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
#> Eres mayor de edad.
```

#### Uso de `if`, `elif` y `else`

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
#> Aprobado
```

### Operadores de comparación y lógicos

Las condiciones suelen utilizar operadores de comparación (`==`, `!=`, `>`, `<`, `>=`, `<=`) y operadores lógicos (`and`, `or`, `not`).

```python
a = 5
b = 10

if a < b and b < 15:
    print("a es menor que b y b es menor que 15.")
#> a es menor que b y b es menor que 15.
```

### Anidación de condicionales

Es posible anidar estructuras condicionales dentro de otras para manejar múltiples condiciones.

```python
edad = 25
tiene_permiso = True

if edad >= 18:
    if tiene_permiso:
        print("Puedes conducir.")
    else:
        print("Necesitas un permiso para conducir.")
else:
    print("Eres menor de edad y no puedes conducir.")
#> Puedes conducir.
```

## Bucles

Los **bucles** permiten repetir un bloque de código múltiples veces. En Python, los bucles principales son `for` y `while`.

### Bucle `for`

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena).

#### Sintaxis básica

```python
for elemento in secuencia:
    # Bloque de código a ejecutar en cada iteración
    ...
```

#### Ejemplos

```python
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
#> manzana
#> banana
#> cereza
```

### Bucle `while`

El bucle `while` repite un bloque de código mientras una condición sea verdadera.

#### Sintaxis básica

```python
while condición:
    # Bloque de código a ejecutar mientras la condición sea verdadera
    ...
```

#### Ejemplos

```python
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
#> Contador: 0
#> Contador: 1
#> Contador: 2
#> Contador: 3
#> Contador: 4
```

### Control de bucles

Python proporciona declaraciones para controlar el flujo dentro de los bucles:

- **`break`**: Sale completamente del bucle.
- **`continue`**: Omite el resto del bloque de código y pasa a la siguiente iteración.
- **`else`**: Se ejecuta después de que el bucle finaliza normalmente (no se ejecuta si el bucle se interrumpe con `break`).

#### Ejemplos

```python
# Uso de break
for numero in range(10):
    if numero == 5:
        break
    print(numero)
#> 0
#> 1
#> 2
#> 3
#> 4

# Uso de continue
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
#> 0
#> 1
#> 3
#> 4

# Uso de else
for numero in range(3):
    print(numero)
else:
    print("Bucle completado sin interrupciones.")
#> 0
#> 1
#> 2
#> Bucle completado sin interrupciones.
```

**Nota:** En el ejemplo del uso de `continue`, el número `2` se omite en la salida porque la sentencia `continue` hace que el bucle pase a la siguiente iteración cuando `numero == 2`.

## Iteración

La **iteración** en Python se logra principalmente mediante los bucles `for` y `while`, como se describió anteriormente. Además, Python ofrece herramientas adicionales para manejar iteraciones de manera eficiente.

### Función `range()`

La función `range()` genera una secuencia de números, que es comúnmente utilizada en los bucles `for`.

#### Sintaxis

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

#### Ejemplos

```python
# Del 0 al 4
for i in range(5):
    print(i)
#> 0
#> 1
#> 2
#> 3
#> 4

# Del 2 al 6
for i in range(2, 7):
    print(i)
#> 2
#> 3
#> 4
#> 5
#> 6

# Del 0 al 10 de 2 en 2
for i in range(0, 11, 2):
    print(i)
#> 0
#> 2
#> 4
#> 6
#> 8
#> 10
```

### Comprensiones de listas

Las **comprensiones de listas** proporcionan una forma concisa de crear listas basadas en bucles.

#### Sintaxis básica

```python
[nueva_expresión for elemento in secuencia if condición]
```

#### Ejemplos

```python
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(5)]
print(cuadrados)
#> [0, 1, 4, 9, 16]

# Crear una lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares)
#> [0, 2, 4, 6, 8]
```

### Función `enumerate()`

La función `enumerate()` permite iterar sobre una secuencia y obtener el índice y el valor de cada elemento.

#### Ejemplo

```python
frutas = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
#> Índice 0: manzana
#> Índice 1: banana
#> Índice 2: cereza
```

## Funciones

Las **funciones** son bloques de código reutilizables que realizan una tarea específica. Permiten organizar el código, mejorar la legibilidad y facilitar el mantenimiento.

### Definición de una función

Se define utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden contener parámetros.

#### Sintaxis básica

```python
def nombre_de_la_funcion(parámetros):
    # Bloque de código
    ...
    return valor
```

#### Ejemplos

```python
# Función sin parámetros y sin valor de retorno
def saludar():
    print("¡Hola!")

saludar()
#> ¡Hola!

# Función con parámetros
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Ana")
#> ¡Hola, Ana!

# Función con valor de retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
#> 8
```

### Parámetros y argumentos

Las funciones pueden tener **parámetros** (variables en la definición) y recibir **argumentos** (valores al llamar la función).

#### Tipos de parámetros

- **Posicionales**: Se asignan según el orden.
- **Por palabra clave**: Se asignan mediante el nombre del parámetro.
- **Predeterminados**: Tienen un valor por defecto si no se proporciona uno.
- **Variables**: Permiten pasar un número variable de argumentos (`*args` y `**kwargs`).

#### Ejemplos

```python
# Parámetros posicionales
def multiplicar(a, b):
    return a * b

print(multiplicar(2, 3))
#> 6

# Parámetros por palabra clave
print(multiplicar(b=4, a=5))
#> 20

# Parámetros con valores predeterminados
def saludar(nombre, mensaje="¡Hola!"):
    print(f"{mensaje}, {nombre}.")

saludar("Carlos")
#> ¡Hola!, Carlos.
saludar("Carlos", "Buenos días")
#> Buenos días, Carlos.

# Parámetros variables (*args y **kwargs)
def funcion_variable(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

funcion_variable(1, 2, 3, nombre="Ana", edad=25)
#> Args: (1, 2, 3)
#> Kwargs: {'nombre': 'Ana', 'edad': 25}
```

### Ámbito de las variables

Las variables definidas dentro de una función tienen un **ámbito local** y no son accesibles fuera de la función. Las variables definidas fuera de cualquier función tienen un **ámbito global**.

#### Ejemplo

```python
x = 10  # Variable global

def imprimir_valor():
    y = 5  # Variable local
    print(f"x dentro de la función: {x}")
    print(f"y dentro de la función: {y}")

imprimir_valor()
#> x dentro de la función: 10
#> y dentro de la función: 5

print(x)
#> 10
# print(y)  # Esto generaría un error: NameError: name 'y' is not defined
```

### Funciones lambda

Las **funciones lambda** son funciones anónimas de una sola línea que se utilizan para operaciones simples.

#### Sintaxis básica

```python
lambda parámetros: expresión
```

#### Ejemplos

```python
# Función lambda para sumar dos números
sumar = lambda a, b: a + b
print(sumar(3, 4))
#> 7

# Uso de lambda con `map()`
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)
#> [1, 4, 9, 16]
```

## Recursividad

La **recursividad** es una técnica donde una función se llama a sí misma para resolver subproblemas más pequeños del problema original. Es útil para problemas que pueden dividirse en subproblemas similares.

### Ejemplo: Factorial

El factorial de un número `n` (denotado como `n!`) es el producto de todos los enteros positivos desde 1 hasta `n`.

#### Implementación recursiva

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
#> 120
```

### Consideraciones

- **Caso base**: Es esencial definir un caso base para evitar llamadas infinitas.
- **Eficiencia**: Las soluciones recursivas pueden ser menos eficientes en términos de memoria y tiempo comparadas con las iterativas.
- **Límites de recursión**: Python tiene un límite en la profundidad de recursión (por defecto, alrededor de 1000 llamadas).

#### Ejemplo de límite de recursión

```python
def contar_recursivo(n):
    print(n)
    return contar_recursivo(n + 1)

# contar_recursivo(1)  # Esto generará un error: RecursionError: maximum recursion depth exceeded
```

## Excepciones

Las **excepciones** son errores que ocurren durante la ejecución de un programa. Python proporciona mecanismos para manejar estos errores de manera controlada, evitando que el programa termine abruptamente.

### Manejo básico de excepciones

Se utilizan las declaraciones `try`, `except`, `else` y `finally` para manejar excepciones.

#### Sintaxis básica

```python
try:
    # Bloque de código que puede generar una excepción
    ...
except TipoDeExcepcion as e:
    # Bloque de código para manejar la excepción
    ...
else:
    # Bloque de código que se ejecuta si no ocurre ninguna excepción
    ...
finally:
    # Bloque de código que siempre se ejecuta, ocurra o no una excepción
    ...
```

#### Ejemplos

```python
# Manejo de división por cero
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Error: No se puede dividir por cero.")
#> Error: No se puede dividir por cero.
```

```python
# Uso de else
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Eso no es un número válido.")
else:
    print(f"Has ingresado el número {numero}.")
```

### Múltiples excepciones

Se pueden manejar diferentes tipos de excepciones en un solo bloque `try`.

```python
try:
    valor = int(input("Ingresa un número: "))
    resultado = 10 / valor
except ValueError:
    print("Eso no es un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print(f"El resultado es {resultado}.")
```

### Cláusula `finally`

La cláusula `finally` se ejecuta siempre, independientemente de si ocurrió una excepción o no. Es útil para liberar recursos, cerrar archivos, etc.

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print(contenido)
finally:
    archivo.close()
    print("Archivo cerrado.")
```

### Lanzar excepciones

Es posible **lanzar** excepciones de manera intencional utilizando la declaración `raise`.

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

try:
    dividir(10, 0)
except ValueError as e:
    print(e)
#> El divisor no puede ser cero.
```

### Creación de excepciones personalizadas

Se pueden crear excepciones personalizadas definiendo una clase que herede de `Exception`.

```python
class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad es inválida."""
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    print("Edad válida.")

try:
    validar_edad(-5)
except EdadInvalidaError as e:
    print(e)
#> La edad no puede ser negativa.
```