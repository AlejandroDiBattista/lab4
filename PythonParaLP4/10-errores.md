# Gestión de errores

En Python, un error es una situación excepcional que interrumpe la ejecución normal de un programa. Los errores pueden ser de diferentes tipos, como errores de sintaxis, errores de tiempo de ejecución y errores de lógica.

En este capítulo, aprenderemos a manejar los errores en Python utilizando las sentencias `try`, `except` y `finally`.

## Errores de sintaxis

Los errores de sintaxis ocurren cuando el intérprete de Python no puede entender el código debido a una estructura incorrecta. Por ejemplo:

```python
# Error de sintaxis
print("Hola, Mundo!)
```

## Errores de lógica

Los errores de lógica ocurren cuando un programa no produce el resultado esperado debido a un error en el diseño o la implementación del código. Por ejemplo:

```python
# Error de lógica
def sumar(a, b):
    return a - b

resultado = sumar(5, 3)

print(resultado)  # Output: 2
```

En el ejemplo anterior, se ha cometido un error de lógica al restar los números `a` y `b` en lugar de sumarlos.
En el ejemplo anterior, se ha cometido un error de sintaxis al no cerrar las comillas en la cadena de texto.

## Errores de tiempo de ejecución

Los errores de tiempo de ejecución ocurren durante la ejecución de un programa y pueden ser causados por diferentes situaciones, como divisiones por cero, acceso a índices fuera de rango, entre otros. Por ejemplo:

```python
# Error de tiempo de ejecución
resultado = 10 / 0
```

En el ejemplo anterior, se ha cometido un error de tiempo de ejecución al intentar dividir un número por cero.


## Manejo de errores

Para manejar los errores en Python, podemos utilizar las sentencias `try`, `except` y `finally`. La sentencia `try` se utiliza para probar un bloque de código en busca de errores, la sentencia `except` se utiliza para manejar los errores que se producen en el bloque `try`, y la sentencia `finally` se utiliza para ejecutar un bloque de código independientemente de si se ha producido un error o no.

Por ejemplo:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero.")
finally:
    print("El programa ha finalizado.")
```

En el ejemplo anterior, se ha utilizado la sentencia `try` para intentar dividir un número por cero. Como se produce un error de división por cero, se ejecuta el bloque `except` que imprime un mensaje de error. Finalmente, se ejecuta el bloque `finally` que imprime un mensaje de finalización del programa.

## Generacion de excepciones

En Python, también es posible generar excepciones manualmente utilizando la sentencia `raise`. Por ejemplo:

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b    

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

En el ejemplo anterior, se ha definido una función `dividir` que genera una excepción de división por cero si el segundo argumento es igual a cero. Luego, se ha utilizado la sentencia `try` para llamar a la función `dividir` con los argumentos `10` y `0`. Como se produce un error de división por cero, se ejecuta el bloque `except` que imprime un mensaje de error.

Un comportamiento interesante de la sentencia `raise` es que si se produce dentro de una función, la excepción se propaga hacia arriba en la pila de llamadas hasta que se maneja con una sentencia `try` o termina la ejecución del programa.




## Excepciones personalizadas

En Python, también es posible crear excepciones personalizadas para manejar situaciones específicas en un programa. Para crear una excepción personalizada, se debe definir una clase que herede de la clase `Exception`. Por ejemplo:

```python
class MiError(Exception):
    pass


try:
    raise MiError("Este es un mensaje de error personalizado.")
except MiError as e:
    print(f"Error: {e}")
```

En el ejemplo anterior, se ha creado una excepción personalizada llamada `MiError` que hereda de la clase `Exception`. Luego, se ha utilizado la sentencia `raise` para lanzar la excepción personalizada con un mensaje de error personalizado. Finalmente, se ha utilizado la sentencia `except` para manejar la excepción personalizada e imprimir el mensaje de error.