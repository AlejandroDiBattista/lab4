# Funciones

En python, una función es un bloque de código que realiza una tarea específica. Las funciones permiten dividir un programa en bloques más pequeños y fáciles de entender. Además, las funciones permiten reutilizar código y evitar la repetición de código.

Un ejemplo de uso es:
```python
nombre = "Juan"
sueldo = 5000
print("Informe de sueldo")
print(f" Nombre: {nombre}")
print(f" Sueldo: ${sueldo}")
print("")

nombre = "Ana"
sueldo = 6000
print("Informe de sueldo")
print(f" Nombre: {nombre}")
print(f" Sueldo: ${sueldo}")
print("")
```

Podemos simplificar el código anterior utilizando una función:
```python
def imprimir_informe():
    print("Informe de sueldo")
    print(f" Nombre: {nombre}")
    print(f" Sueldo: ${sueldo}")
    print("")

nombre = "Juan"
sueldo = 5000
imprimir_informe()

nombre = "Ana"
sueldo = 6000
imprimir_informe()
```

Ahora la funcion nos permite interpretar el código de manera más sencilla, ahora con el nombre de la funcion es más fácil de entender que es lo que hace.
A la vez permite reutilizar el código, si necesitamos imprimir otro informe de sueldo, solo necesitamos llamar a la función `imprimir_informe()`.

Ahora bien, esta funcion depende de las variables `nombre` y `sueldo`, si cambiamos el nombre de la variable, la función no funcionará correctamente. Para solucionar este problema, podemos pasar los valores de las variables como argumentos a la función.

```python

def imprimir_informe(nombre, sueldo):
    print("Informe de sueldo")
    print(f" Nombre: {nombre}")
    print(f" Sueldo: ${sueldo}")
    print("")

n = "Juan"
s = 5000
imprimir_informe(n, s)

imprimir_informe("Ana", 6000)
imprimir_informe("Pedro", 7000)

```

Con el paso de parametros podemos reutilizar la función para imprimir diferentes informes de sueldo. Ya no dependemos de las variables `nombre` y `sueldo`.

Sin embargo esta funcion todavia puede ser mejorada. La funcion 'imprimir_informe' le da formato a los datos y los imprime. Pero si necesitamos guardar el informe en un archivo, tendriamos que modificar la función. Para evitar esto, podemos dividir la función en dos funciones, una que le da formato a los datos y otra que imprime los datos.

```python
def generar_informe(nombre, sueldo):
    return f"""
Informe de sueldo
- Nombre: {nombre}
- Sueldo: ${sueldo}"""

informe = generar_informe("Juan", 5000)
print(informe)

informe = generar_informe("Ana", 6000)
print(informe)

informe = generar_informe("Pedro", 7000)
with open("informe.txt", "w") as archivo:
    archivo.write(informe)
```

## Pasaje de argumentos 

Python es muy flexible en cuanto al pasaje de argumentos a las funciones. Podemos pasar argumentos por posición, por nombre, y podemos tener argumentos con valores por defecto.

### Pasaje de argumentos por posición

```python
def suma(a, b):
    return a + b

print(suma(2, 3)) # Parametros por posición
#> 5
```

El pasaje de parámetros implica una asignación de las variables a los parámetros de la función en el orden en que se pasan los argumentos. Es equivalente a la asignación simultánea `a = 2` y `b = 3`, o `a, b = 2, 3`.

### Pasaje de argumentos por nombre

```python
def par(x, y):
    print(f"{x=} {y=}")

par(2, 3) # Parametros por posición
#> x=2 y=3

par(y=3, x=2) # Parametros por nombre (el orden no importa)
#> x=2 y=3

par(2, y=3) # Parametros por posición y nombre
#> x=2 y=3

# par(x=2, 3) # Error de sintaxis. Los argumentos por nombre deben ir después de los argumentos por posición
```

### Argumentos con valores por defecto

En algunas ocasiones, es útil definir valores por defecto para los argumentos de una función. Esto permite llamar a la función sin pasar todos los argumentos. 
Hace que el uso sea facil para los casos más comunes, pero permite la flexibilidad de cambiar los valores por defecto si es necesario.

```python
def suma(a, b=0, c=0, d=0):
    return a + b

print(suma(2)) # Solo pasamos un argumento
#> 2

print(suma(2, 3)) # Pasamos dos argumentos
#> 5

print(suma(2, 3, 4)) # Pasamos tres argumentos
#> 5

print(suma(2, 3, 4, 5)) # Pasamos cuatro argumentos
#> 5
```
 En este caso la funcion suma tiene 4 argumentos, pero solo uno es obligatorio, los otros tres tienen un valor por defecto de 0. Esto permite llamar a la función con un solo argumento, o con dos, tres o cuatro argumentos. Sin embargo, si se pasan más de cuatro argumentos, la función lanzará un error.

Si quiesieramos hacer mas flexible la funcion podriamos intentar que acepte un numero variable de argumentos. Para ello podriamos recibir una lista de valores en lugar de argumentos separados.

Si bien esto es una solucion hace mas dificil el uso original de la funcion, ya que ahora se necesita pasar una lista de valores en lugar de argumentos separados.

 ```python
def suma(lista):
    suma = 0
    for valor in lista:
        suma += valor
    return suma

print(suma([2])) # Solo pasamos un argumento
#> 2
print(suma([1, 2, 3, 4, 5, 6])) # Pasamos varios argumentos
#> 21

``` 

Esto es posible y es valido pero no es la mejor solucion. Python nos permite definir funciones que acepten un numero variable de argumentos. Para ello podemos usar el operador `*` para indicar que la funcion acepta un numero variable de argumentos.

```python
def suma(*args):
    suma = 0
    for valor in args:
        suma += valor
    return suma

print(suma(2)) # Solo pasamos un argumento
#> 2
print(suma(1, 2, 3, 4, 5, 6)) # Pasamos varios argumentos
#> 21
```

En este caso, la funcion `suma` acepta un numero variable de argumentos. Los argumentos se almacenan en una tupla llamada `args`. La funcion recorre la tupla y suma los valores. Ahora podemos llamar a la funcion con un solo argumento, o con varios argumentos.

Pero si tenemos los datos inicialmente en una lista, no podríamos pasar la lista directamente a la función. Para solucionar este problema, podemos usar el operador `*` para desempaquetar la lista y pasar los valores como argumentos.

```python
valores = [1, 2, 3, 4, 5, 6]
print(suma(*valores)) # Pasamos varios argumentos
#> 21
```

El operador `*` desempaqueta la lista cuando se pasa como argumento a la función. Y empaqueta los valores en una tupla cuando se recibe en la función.

Este concepto de empaquetar y desempaquetar se puede usar en una forma mas general combinando argumentos fijos, argumentos por nombre, argumentos con valores por defecto y argumentos variables.

En primer lugar pueden definirse los argumentos fijos, luego los argumentos con valores por defecto, luego los argumentos variables y finalmente los argumentos por nombre. El orden es importante, los argumentos por nombre deben ir después de los argumentos por posición.

Existe un operadador `**` que permite pasar un número variable de argumentos por nombre. Los argumentos se almacenan en un diccionario llamado `kwargs`.

```python
def parametros(a, b, *args, c=0, d=0, **kwargs):
    print(f"a={a} b={b} args={args} c={c} d={d} kwargs={kwargs}")

parametros(1, 2) # Solo pasamos dos argumentos
#> a=1 b=2 args=() c=0 d=0 kwargs={}

parametros(1, 2, 3, 4, 5, c=6, d=7) # Pasamos varios argumentos y argumentos por nombre
#> a=1 b=2 args=(3, 4, 5) c=6 d=7 kwargs={}

parametros(1, 2, 3, 4, 5, c=6, d=7, e=8, f=9) # Pasamos varios argumentos y argumentos por nombre
#> a=1 b=2 args=(3, 4, 5) c=6 d=7 kwargs={'e': 8, 'f': 9}
```

En este caso, la función `parametros` acepta un número variable de argumentos por posición, argumentos con valores por defecto, y un número variable de argumentos por nombre. Los argumentos por posición se almacenan en una tupla llamada `args`, y los argumentos por nombre se almacenan en un diccionario llamado `kwargs`.

Asi como `*` desempaqueta una lista, `**` desempaqueta un diccionario. Por lo tanto, si tenemos un diccionario con los argumentos por nombre, podemos desempaquetar el diccionario y pasar los argumentos a la función.

```python
valores = {"c": 6, "d": 7, "e": 8, "f": 9}
parametros(1, 2, 3, 4, 5, **valores) # Pasamos varios argumentos y argumentos por nombre

def informer(nombre, sueldo):
    print(f"Nombre: {nombre} Sueldo: ${sueldo}")

empleado = {"nombre": "Juan", "sueldo": 5000}
informer(**empleado)

# Tambien funciona al reves
def listar(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

listar(nombre="Juan", sueldo=5000)
#> nombre: Juan 
#> sueldo: 5000

listar(nombre="Ana", sueldo=6000, edad=30)
#> nombre: Ana
#> sueldo: 6000
#> edad: 30
```

En este caso, el diccionario `valores` contiene los argumentos por nombre. Al pasar el diccionario a la función `parametros`, los argumentos se desempaquetan y se pasan a la función.

### Retorno de valores

Cuando una funcion termina de ejecutarse, puede devolver un valor. Para devolver un valor, se utiliza la instrucción `return`. Si no se especifica un valor de retorno, la función devuelve `None`.

```python
# Una funcion 
def suma(a, b):
    return a + b

resultado = suma(2, 3)

# Un procedimiento no devuelve nada
def imprimir_suma(a, b):
    print(f"{a} + {b} = {a + b}")

# Pero si queremos podemos usarla como una funcion

resultado = imprimir_suma(2, 3)
print(resultado) 
#> None
```

En este caso, la función `suma` devuelve la suma de los argumentos `a` y `b`. La función `imprimir_suma` no devuelve nada, por lo tanto, la variable `resultado` contiene `None`.

Las funciones pueden retornar cualquier tipo de valor, incluso colecciones o funciones.

Una forma muy comoda de retornar multiples valores es retornar una tupla.
Las tuplas tienen la ventaja de que pueden contener cualquier tipo de valor, y pueden ser desempaquetadas facilmente. Incluso no es necesaria el uso de los parentesis para crear una tupla, simplemente separar los valores con comas.

```python
def minmax(lista):
    minimo = maximo = lista[0]
    for x in lista:
        if x < minimo: minimo = x
        if x > maximo: maximo = x
    return (minimo, maximo)

valores = [1, 2, 3, 4, 5]
(minimo, maximo) = minmax(valores)
print(f"Minimo: {minimo} Maximo: {maximo}")

# Tambien se puede hacer sin parentesis
def divmod(a, b):
    return a // b, a % b

cociente, resto = divmod(10, 3)
print(f"Cociente: {cociente} Resto: {resto}")
```

En este caso, la función `minmax` devuelve una tupla con el mínimo y el máximo de una lista. La función `divmod` devuelve una tupla con el cociente y el resto de una división.

### Funciones como objetos

En Python, las funciones son objetos de primera clase. Esto significa que las funciones pueden ser asignadas a variables, almacenadas en estructuras de datos, pasadas como argumentos a otras funciones, y retornadas como valores de otras funciones.

```python
def saludar(nombre):
    return f"Hola {nombre}"

saludo = saludar
print(saludo("Juan"))
#> Hola Juan
```
Cuando definimos una funcion en realidad estamos definiendo una variable que contiene la funcion. Por lo tanto, podemos asignar la funcion a otra variable y llamar a la funcion a traves de la nueva variable.

Si se usa la variable con parentesis, se llama a la funcion, si se usa sin parentesis, se accede a la funcion.

```python
def suma(a, b): return a + b
def producto(a, b): return a * b

# Aplica la funcion a cada elemento de la lista en forma acumulativa 
def reducir(funcion, lista):
    resultado = lista[0]
    for x in lista[1:]:
        resultado = funcion(resultado, x)
    return resultado

valores = [1, 2, 3, 4, 5]
print(reducir(suma, valores))
#> 15

print(reducir(producto, valores))
#> 120

nombres = ["Juan", "Ana", "Pedro"]
print(reducir(lambda a, b: a + " " + b, nombres))
#> Juan Ana Pedro

print(sorted(nombres))
#> ['Ana', 'Juan', 'Pedro']
def longitud(nombre):
    return len(nombre)

print(sorted(nombres, key = longitud))
#> ['Ana', 'Juan', 'Pedro']

print(sorted(nombres, key = lambda nombre: len(nombre)))
#> ['Ana', 'Juan', 'Pedro']

print(sorted(nombres, key = len)
#> ['Ana', 'Juan', 'Pedro']

```

En este caso, la función `reducir` recibe una función y una lista, y aplica la función a cada elemento de la lista en forma acumulativa. La función `sorted` recibe una lista y un argumento `key` que indica la función que se debe aplicar a cada elemento de la lista antes de ordenarla.

### Funciones anónimas

En Python, las funciones anónimas son funciones que no tienen nombre. Se definen con la palabra clave `lambda`, seguida de los argumentos y el cuerpo de la función. Las funciones anónimas son útiles para definir funciones simples en una sola línea.

```python
suma = lambda a, b: a + b
print(suma(2, 3))

producto = lambda a, b: a * b
print(producto(2, 3))
```

La ventaja de las funciones anónimas es que son concisas y se pueden definir en una sola línea. La desventaja es que son menos legibles que las funciones normales, y no pueden contener múltiples instrucciones.

Las funciones anónimas son útiles cuando se necesita una función temporal, o cuando se necesita una función simple para pasar como argumento a otra función.

```python
valores = [1, 2, 3, 4, 5]
print(reducir(lambda a, b: a + b, valores))
#> 15

print(reducir(lambda a, b: a * b, valores))
#> 120

nombres = ["Juan", "Ana", "Pedro"]
print(reducir(lambda a, b: a + " " + b, nombres))
#> Juan Ana Pedro

print(sorted(nombres, key = lambda nombre: len(nombre)))
#> ['Ana', 'Juan', 'Pedro']
```

### Parametros por referencia

En python toda asignacion de variables es por referencia. Esto significa que cuando se pasa una variable a una funcion, se pasa la referencia a la variable, no una copia de la variable. Por lo tanto, si se modifica la variable dentro de la funcion, se modifica la variable original.

```python
def duplicar(lista):
    for i in range(len(lista)):
        lista[i] *= 2

valores = [1, 2, 3, 4, 5]
duplicar(valores)
print(valores)
#> [2, 4, 6, 8, 10]
```

En este caso, la función `duplicar` recibe una lista y multiplica cada elemento por 2. Como la lista se pasa por referencia, la lista original se modifica.

Si se necesita modificar una variable dentro de una función sin modificar la variable original, se puede hacer una copia de la variable antes de modificarla.

```python
def duplicar(lista):
    lista = lista.copy()
    for i in range(len(lista)):
        lista[i] *= 2
    return lista

valores = [1, 2, 3, 4, 5]
valores_duplicados = duplicar(valores)
print(valores)
#> [1, 2, 3, 4, 5]
print(valores_duplicados)
#> [2, 4, 6, 8, 10]
``` 

### Funciones anidadas 

En Python, las funciones pueden definirse dentro de otras funciones. Las funciones anidadas pueden acceder a las variables de la función externa, y pueden devolverse como valores de la función externa.

```python

def operacion(operador):
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    if operador == "+":
        return suma
    elif operador == "-":
        return resta

funcion = operacion("+")
print(funcion(2, 3))
#> 5

funcion = operacion("-")
print(funcion(2, 3))
#> -1
```

### Funciones recursivas

En Python, una función puede llamarse a sí misma. Esto se conoce como recursión. La recursión es útil para resolver problemas que pueden dividirse en subproblemas más pequeños.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def suma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma(lista[1:])

valores = [1, 2, 3, 4, 5]
print(suma(valores))
#> 15

# Busqueda lineal
def buscar(lista, valor):
    if len(lista) == 0:
        return False
    elif lista[0] == valor:
        return True
    else:
        return buscar(lista[1:], valor)

```
En este caso, la función `factorial` calcula el factorial de un número utilizando recursión. 

En la funcion `suma` y `buscar` se usa la recursion para recorrer una lista. Esto reemplaza el uso de un ciclo `for` para recorrer la lista.

Una curiosidad... es 1930, el matemático Kurt Gödel demostró que cualquier función computable puede ser calculada mediante recursión. Esto se conoce como la tesis de Church-Turing.

### Funciones generadoras

En Python, una función generadora es una función que devuelve un generador. Un generador es un tipo especial de iterador que permite recorrer una secuencia de valores de uno en uno.

```python
def contador(n):
    for i in range(n):
        yield i

for i in contador(5):
    print(i)
```
La funciones generadores usan `yield` en lugar de `return` para devolver valores. Cuando se llama a una función generadora, se obtiene un generador. Un generador es un iterador que permite recorrer los valores de uno en uno.

Cuando encuentra un `yield`, la función generadora se detiene y devuelve el valor. Cuando se llama al generador nuevamente, la función generadora se reanuda en el `yield` y continúa la ejecución.

```python
def tres():
    yield 1
    yield 2
    yield 3

for i in tres():
    print(i, end=" ")
#> 1 2 3

def cuenta_regresiva(n):
    while n > 0:
        yield n
        n -= 1
    yield "Despegue!"
for i in contar(5):
    print(i, end=" ")
#> 5 4 3 2 1 Despegue!
``` 

En este caso, la función `contador` es una función generadora que devuelve un generador. El generador permite recorrer los valores de 0 a `n-1`. La función `tres` es una función generadora que devuelve un generador que permite recorrer los valores 1, 2 y 3. La función `cuenta_regresiva` es una función generadora que devuelve un generador que permite recorrer los valores de `n` a 1, y finalmente el valor "Despegue!".

### Funciones de orden superior

En Python, una función de orden superior es una función que recibe una o más funciones como argumentos, o devuelve una función como resultado.

```python
def aplicar(funcion, valor):
    return funcion(valor)

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

print(aplicar(cuadrado, 2))
#> 4

print(aplicar(cubo, 2))

def multiplicador(n):
    def funcion(x):
        return x * n
    return funcion

duplicar = multiplicador(2)
print(duplicar(3))
#> 6

triplicar = multiplicador(3)
print(triplicar(3))
#> 9
```

En este caso, la función `aplicar` es una función de orden superior que recibe una función y un valor, y aplica la función al valor. 

La función `multiplicador` es una función de orden superior que recibe un número y devuelve una función que multiplica un valor por ese número.

Con la funcion `multiplicador` se puede crear una función que multiplica por 2 y otra que multiplica por 3.

### Decoradores

En Python, un decorador es una función que recibe una función como argumento, y devuelve otra función. Los decoradores se utilizan para modificar o extender el comportamiento de una función sin modificar su código.

```python
def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print(f"Antes de llamar a {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"Despues de llamar a {funcion.__name__}")
        return resultado
    return nueva_funcion

@decorador
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Juan"))
#> Antes de llamar a saludar
#> Hola Juan
#> Despues de llamar a saludar
```







