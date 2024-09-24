# Variables

Las variables son utilizadas para almacenar información en la memoria de un programa. En Python, una variable es un nombre que se refiere a un valor.

Los nombres de las variables en Python pueden contener letras, números y guiones bajos. Sin embargo, el nombre de una variable no puede comenzar con un número.

En Python, las variables son sensibles a mayúsculas y minúsculas. Esto significa que las variables `nombre`, `Nombre` y `NOMBRE` son consideradas diferentes.

Para asignar un valor a una variable en Python, se utiliza el operador de asignación `=`. Por ejemplo:

```python
nombre = "Juan"
edad = 30
altura = 1.75
```

En el ejemplo anterior, se han creado tres variables: `nombre`, `edad` y `altura`. La variable `nombre` almacena un valor de tipo `str`, la variable `edad` almacena un valor de tipo `int` y la variable `altura` almacena un valor de tipo `float`.

En Python es necesario declarar una variable antes de usarla. Esto se hace asignándole un valor inicial. Por ejemplo:

```python
nombre = "Juan"
print(nombre)
```

En este caso, la variable `nombre` se declara y se le asigna un valor en la misma línea. Luego, se imprime el valor de la variable utilizando la función `print()`.

Las variables tienen un tipo de dato asociado que determina el tipo de valor que pueden almacenar. Algunos de los tipos de datos más comunes en Python son:

- `int`: para números enteros.
- `float`: para números de punto flotante.
- `str`: para cadenas de texto.
- `bool`: para valores booleanos (`True` o `False`).

Es importante tener en cuenta que en Python no es necesario especificar el tipo de dato de una variable al declararla, ya que el intérprete de Python infiere automáticamente el tipo de dato en función del valor asignado.

## Reglas para nombrar variables

Al nombrar variables en Python, es importante seguir algunas reglas para garantizar que el código sea legible y fácil de entender. Algunas de las reglas más comunes son:

- Los nombres de las variables deben ser descriptivos y representativos del valor que almacenan.
- Los nombres de las variables deben comenzar con una letra o un guion bajo.
- Los nombres de las variables no pueden contener espacios en blanco.
- Los nombres de las variables no pueden ser palabras reservadas de Python, como `if`, `else`, `for`, `while`, etc.
- Los nombres de las variables son sensibles a mayúsculas y minúsculas.

Al seguir estas reglas, se facilita la lectura y comprensión del código, lo que es fundamental para el desarrollo de programas eficientes y mantenibles.

## Tipos básicos: `int`

Los enteros (`int`) son un tipo de dato básico en Python que se utiliza para representar números enteros. Se pueden utilizar para realizar operaciones matemáticas simples, como sumas, restas, multiplicaciones y divisiones. Tienen la particularidad de que no tienen límite en su tamaño (bueno, siempre hay límites pero son muy grandes).

Se identifican porque comienzan con un dígito y no tienen punto decimal. Existen múltiples formas de describir un entero, pero más allá de la forma de ingresarlo, siempre se almacena como un número entero.

```python
a = 100  # a es un entero en base 10 (decimal)
b = 0b10010101  # b es un entero en base 2 (binario)
c = 0o1234567  # c es un entero en base 8 (octal)
d = 0x1234567890ABCDEF  # d es un entero en base 16 (hexadecimal)

print(a)  # 100
print(b)  # 149
print(c)  # 342391
print(d)  # 1311768467294899695
```

Sobre los enteros se pueden realizar las operaciones matemáticas básicas como suma, resta, multiplicación y división. Además, se pueden realizar operaciones más complejas como el cálculo de módulo, división entera y potenciación.

```python
# Operaciones matemáticas básicas
a = 10
b = 3
c = a + b   #> 13          # Suma              __add__
d = a - b   #> 7           # Resta             __sub__
e = a * b   #> 30          # Multiplicación    __mul__    
f = a / b   #> 3.33333333  # División          __truediv__
g = a // b  #> 3           # División entera   __floordiv__
h = a % b   #> 1           # Módulo (resto)    __mod__
i = a ** b  #> 1000        # Potenciación      __pow__

# Comparaciones
j = a == b  #> False      # Igualdad          __eq__
k = a != b  #> True       # Desigualdad       __ne__
l = a < b   #> False      # Menor que         __lt__
m = a > b   #> True       # Mayor que         __gt__
n = a <= b  #> False      # Menor o igual que __le__
o = a >= b  #> True       # Mayor o igual que __ge__

a = 10_000     #> 10000  # Se pueden usar guiones bajos para separar los dígitos
b = 0b1_0000   #> 16     # Se pueden usar guiones bajos para separar los dígitos

print(2 ** 100)
# 1267650600228229401496703205376

# ¿Cuántos '0' tiene el 2 ** 1000?
print(str(2 ** 1000).count('0'))
```

En Python se pueden realizar operaciones aritméticas con los enteros sin preocuparse por el desbordamiento de los valores. Python maneja automáticamente el desbordamiento de los enteros, lo que significa que los enteros pueden crecer tanto como la memoria de la computadora lo permita.

Por último, se pueden realizar conversiones entre los diferentes tipos de datos numéricos en Python. Por ejemplo, se puede convertir un entero a un número de punto flotante utilizando la función `float()` o un número de punto flotante a un entero utilizando la función `int()`.

```python
# Conversión de booleanos a enteros
int(True)   #> 1
int(False)  #> 0

# Conversión de flotantes a enteros
int(3.14159)  #> 3
int(10.9999)  #> 10  (trunca el decimal)

# Conversión de cadenas a enteros
int('10')     #> 10 (base 10)
int('10', 2)  #> 2  (base 2)
int('10', 8)  #> 8  (base 8)
int('10', 16) #> 16 (base 16)
int('A', 16)  #> 10 (base 16)
int('xx', 16) #> ValueError: invalid literal for int() with base 16: 'xx'

# Conversión segura de cadenas a enteros
a = "10"

# Verificando si la cadena es un número
if a.isnumeric(): 
    b = int(a)
    print(b)
else:
    print("No es un número")

# Usando try-except para manejar errores
try:
    b = int(a)
    print(b)
except ValueError:
    print("No es un número")
```

## Tipos básicos: `float`

Los números de punto flotante (`float`) son un tipo de dato básico en Python que se utiliza para representar números reales. Se pueden utilizar para realizar operaciones matemáticas más complejas, como sumas, restas, multiplicaciones y divisiones con decimales.

Se identifican porque tienen un punto decimal o usan la notación científica. Existen múltiples formas de describir un número de punto flotante, pero más allá de la forma de ingresarlo, siempre se almacena como un número real.

```python
a = 3.14159     # a es un número de punto flotante
b = 1.0e-3      # b es un número de punto flotante en notación científica
c = 1_000.0     # c es un número de punto flotante con guiones bajos para separar los dígitos

d = .0      #> 0.0
e = 0.      #> 0.0
f = 1.      #> 1.0
g = 1e100   #> 1.0e+100
```

Existe la librería `math` que contiene funciones matemáticas que se pueden utilizar con los números de punto flotante.

```python
import math

a = 3.14159
b = math.sin(a)         # Seno
c = math.cos(a)         # Coseno
d = math.tan(a)         # Tangente

e = math.asin(a)        # Arcoseno
f = math.acos(a)        # Arcocoseno
g = math.atan(a)        # Arcotangente

i = math.trunc(a)       # Trunca el número
j = math.floor(a)       # Redondea hacia abajo
k = math.ceil(a)        # Redondea hacia arriba
```

## Tipos básicos: `bool`

Los valores booleanos (`bool`) son un tipo de dato básico en Python que se utiliza para representar valores de verdad. Pueden tener dos posibles valores: `True` (verdadero) o `False` (falso).

Los valores booleanos se utilizan en expresiones lógicas y de comparación para determinar si una condición es verdadera o falsa. Por ejemplo:

```python
a = True
b = False

c = 10 > 5   #> True
d = 10 < 5   #> False
e = 10 == 5  #> False
```

En Python, los siguientes valores son considerados falsos en un contexto booleano: `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `()`. Todos los demás valores se consideran verdaderos.

Las expresiones lógicas y de comparación en Python devuelven un valor booleano que se puede almacenar en una variable o utilizar en una estructura de control, como un `if` o un `while`.

Se pueden realizar operaciones lógicas con los valores booleanos utilizando los operadores `and`, `or` y `not`. Por ejemplo:

```python
a = True
b = False

c = a and b  #> False
d = a or b   #> True
e = not a    #> False
```

Las expresiones lógicas en Python se evalúan de izquierda a derecha y se detienen tan pronto como se determina el resultado, evitando evaluar innecesariamente el resto. Esto se llama cortocircuito y es útil para prevenir errores en expresiones complejas.

```python
a = True

b = a or 10/0  # True 
# 10/0 da un error de división por cero, pero como la expresión es cortocircuitada, no se evalúa y no se produce el error.

# c = a and 10/0  # ZeroDivisionError: division by zero
```

Python realiza dos conversiones automáticas cuando trabaja con valores booleanos:

- Cuando se usan valores booleanos en operaciones aritméticas, `True` se convierte en `1` y `False` se convierte en `0`.
- Cuando se espera una expresión booleana, como en un `if`, un `while` o en una `and`, `or`, `not`, automáticamente se convierte en un valor booleano.

```python
# Conversión de enteros a booleanos
# Cualquier número diferente de cero se convierte en True, el cero se convierte en False
bool(0)    # False
bool(1)    # True
bool(10)   # True

# Conversión de flotantes a booleanos
# Cualquier número diferente de cero se convierte en True, el cero se convierte en False
bool(0.0)  # False
bool(0.1)  # True
bool(10.0) # True

# Conversión de cadenas a booleanos
# Cualquier cadena no vacía se convierte en True, la cadena vacía se convierte en False
bool('')   # False
bool('a')  # True
bool(' ')  # True

# Conversión de listas, diccionarios y tuplas a booleanos
# Cualquier secuencia no vacía se convierte en True, la secuencia vacía se convierte en False
bool([])    # False
bool([1])   # True
bool([0])   # True

bool({})    # False
bool({1})   # True

bool(())    # False
bool((1,))  # True
```

## Tipos básicos: `str`

Los `str` o cadenas en Python son un tipo de dato básico que se utiliza para representar texto. Se pueden utilizar para almacenar mensajes, nombres, direcciones, números de teléfono y cualquier otro tipo de información que se pueda representar como texto.

Las cadenas en Python se pueden definir utilizando comillas simples (`'`) o dobles (`"`). Por ejemplo:

```python
a = 'Hola, mundo!'
b = "¡Hola, mundo!"
c = '''Hola, mundo!'''
d = """¡Hola, mundo!"""
```

También se pueden definir cadenas multilínea utilizando comillas triples simples (`'''`) o dobles (`"""`). Por ejemplo:

```python
a = '''Este es un ejemplo
de una cadena multilínea'''

b = """Este es otro ejemplo
de una cadena multilínea"""

print(a)
#> Este es un ejemplo
#> de una cadena multilínea
```

Existe un tipo especial de cadena que permite dar formato a los valores que se insertan en ella. Estas cadenas se conocen como cadenas de formato y se definen utilizando la letra `f` antes de las comillas de apertura. Se conocen como f-strings o 'string interpolations'. 

Por ejemplo:

```python
nombre = "Juan"
apellido = "Perez"
mensaje = f'Hola, {nombre} {apellido}'
print(mensaje)
#> Hola, Juan Perez

a = 10
b = 20
print(f'{a} + {b} = {a + b}')  # Con la f se evalúa la expresión dentro de las llaves
#> 10 + 20 = 30

print('{a} + {b} = {a + b}')   # Sin la f no se evalúa la expresión
#> {a} + {b} = {a + b}

# Con ':' se pueden especificar el formato de los valores
print(f'{"Hola":>10}')  # Alineado a la derecha en un campo de 10 caracteres
#>       Hola

print(f'{"Hola":<10}')  # Alineado a la izquierda en un campo de 10 caracteres
#> Hola     

print(f'{"Hola":^10}')  # Alineado al centro en un campo de 10 caracteres
#>    Hola   

print(f'{3.14159:.2f}')  # Redondea a 2 decimales
#> 3.14

print(f'{1000:10.2f}')   # Un campo de 10 caracteres con 2 decimales
#>   1000.00

print(f'{10:05d}')       # Rellena con ceros a la izquierda en un campo de 5 caracteres
#> 00010
```

Los `str` en Python son inmutables, lo que significa que una vez que se crea una cadena, no se puede modificar. Sin embargo, se pueden realizar operaciones con las cadenas, como concatenarlas, dividirlas, reemplazar partes de ellas, etc.

```python
a = 'Hola, '
b = 'mundo!'
c = a + b  
print(c)
#> 'Hola, mundo!'

d = 'Hola, mundo!'.split(', ')  
print(d)
#> ['Hola', 'mundo!']

e = 'Hola, mundo!'.replace('mundo', 'Python')  
print(e)
#> 'Hola, Python!'

f = 'Hola, mundo!'[0:5]  
print(f)
#> 'Hola'

g = 'Hola, mundo!'[::-1]
print(g)
#> '!odnum ,aloH'

h = 'Hola, mundo!'.upper()
print(h)
#> 'HOLA, MUNDO!'

i = 'Hola, mundo!'.lower()
print(i)
#> 'hola, mundo!'

j = 'Hola, mundo!'.title()
print(j)
#> 'Hola, Mundo!'

k = 'Hola' * 3  # Repite la cadena 3 veces
print(k)
#> 'HolaHolaHola'

l = 'Hola, que tengas un ' + 'muy ' * 3 + 'buen día!'
print(l)
#> 'Hola, que tengas un muy muy muy buen día!'
```

Los `str` son una secuencia de caracteres y pueden ser tratados como una lista de caracteres. Se puede acceder a los caracteres individuales de una cadena utilizando la notación de corchetes `[]` y el índice del carácter que se desea acceder. Por ejemplo:

```python
a = 'Hola, mundo!'
print(a[0])   #> 'H'    # Primer carácter
print(a[1])   #> 'o'    # Segundo carácter
print(a[-1])  #> '!'    # Último carácter

for i in range(len(a)):  # Recorre la cadena e imprime cada carácter
    print(a[i], end=' ')
#> H o l a ,   m u n d o !

l = list('Hola, mundo!')  # Convierte la cadena en una lista de caracteres
print(l)
#> ['H', 'o', 'l', 'a', ',', ' ', 'm', 'u', 'n', 'd', 'o', '!']

print(a[6:8]) 
#> 'mu'
```

En Python, todos los tipos se pueden convertir a cadena, es decir, siempre se puede obtener una representación de un valor como una cadena. Para convertir un valor a una cadena se puede utilizar la función `str()`. Esta función está definida para todos los tipos de datos en Python. Para los tipos creados (clases), se puede proveer una función para convertir a cadena.

```python
# Conversión de enteros a cadenas
a = str(10)    #> '10'
b = str(1000)  #> '1000'

# Conversión de flotantes a cadenas
c = str(3.14159)  #> '3.14159'
d = str(10.9999)  #> '10.9999'

# Conversión de booleanos a cadenas
e = str(True)   #> 'True'
f = str(False)  #> 'False'

# Conversión de listas, diccionarios y tuplas a cadenas
g = str([1, 2, 3])        #> '[1, 2, 3]'
h = str({'a': 1, 'b': 2}) #> "{'a': 1, 'b': 2}"
i = str((1, 2, 3))        #> '(1, 2, 3)'
```

Python realiza conversiones automáticas a cadena cuando es necesario. Por ejemplo, cuando se imprime un valor, se convierte a cadena automáticamente. Sin embargo, para concatenar una cadena con un valor que no es una cadena, es necesario convertirlo explícitamente o utilizar formatos.

```python
print(10, 1 > 2, "Hola", [1, 2, 3])                 # Llamada a str en forma implícita
#> 10 False Hola [1, 2, 3]

print(str(10), str(1 > 2), "Hola", str([1, 2, 3]))  # Llamada a str en forma explícita
#> 10 False Hola [1, 2, 3]

print(f"{10} {1 > 2} Hola {[1, 2, 3]}")             # Llamada a str en forma implícita
#> 10 False Hola [1, 2, 3]
```

Existe otra función para convertir un objeto en una cadena, `repr()`. Esta función devuelve una representación de cadena del objeto que es más cercana a la representación interna del objeto. Es útil para depurar y para mostrar objetos de forma más detallada. Se puede decir que `str()` es para mostrar al usuario y `repr()` es para mostrar al programador.

```python
from datetime import datetime

# Crear un objeto datetime
now = datetime.now()

# Usar str() para convertir el objeto a una cadena (representación legible)
print(f'str: {str(now)}')
#> str: 2023-10-05 14:30:00.123456

# Usar repr() para convertir el objeto a una cadena (representación detallada)
print(f'repr: {repr(now)}')
#> repr: datetime.datetime(2023, 10, 5, 14, 30, 0, 123456)

print(f'{now}')  # Llamada a str() en forma implícita
#> 2023-10-05 14:30:00.123456
```

En este ejemplo, `str(now)` devuelve una representación legible del objeto `datetime`, mientras que `repr(now)` devuelve una representación más detallada y precisa del objeto, que incluye información adicional sobre la clase y el módulo.

## Tipos básicos: `None`

El valor especial `None` en Python representa la ausencia de un valor o un valor nulo. Es un tipo de dato único que se utiliza para indicar que una variable no tiene ningún valor asignado o que una función no devuelve ningún valor explícitamente.

El tipo de dato de `None` es `NoneType`. Solo existe una instancia de `None` en todo el programa, lo que significa que es un singleton. Se puede utilizar `None` en diversas situaciones, como inicializar variables que aún no tienen un valor, o para indicar que una función no devuelve nada.

Por ejemplo:

```python
a = None  # Inicializar una variable sin valor
print(a)  #> None

def saludo(nombre):
    print(f"Hola, {nombre}!")

b = saludo("Juan")  # La función imprime un saludo pero no devuelve nada
print(b)            #> None
```

En este ejemplo, la variable `a` se inicializa con `None`, indicando que no tiene un valor específico. La función `saludo` imprime un mensaje pero no devuelve ningún valor explícito, por lo que `b` se asigna el valor `None`.

Es importante destacar que `None` no es lo mismo que `False`, `0` o una cadena vacía `''`. Aunque todos estos valores son considerados falsos en un contexto booleano, representan conceptos diferentes.

Para comprobar si una variable es `None`, se debe utilizar el operador `is` en lugar de `==`. Esto se debe a que `None` es un singleton, y se recomienda comparar identidades en lugar de valores.

Por ejemplo:

```python
a = None

if a is None:
    print("a es None")
else:
    print("a no es None")
```

También se puede utilizar `is not` para comprobar que una variable no es `None`:

```python
b = 10

if b is not None:
    print("b tiene un valor")
else:
    print("b es None")
```

### Uso de `None` en funciones

En Python, si una función no tiene una sentencia `return` o la sentencia `return` no devuelve ningún valor, la función devuelve implícitamente `None`.

```python
def sin_retorno():
    pass

resultado = sin_retorno()
print(resultado)  #> None
```

En este ejemplo, la función `sin_retorno` no devuelve ningún valor, por lo que `resultado` es `None`.

### Contexto booleano de `None`

En un contexto booleano, como en una condición `if`, el valor `None` se considera falso. Esto permite utilizar `None` para comprobar si una variable tiene un valor asignado o no.

```python
a = None

if not a:
    print("a es falso o None")
else:
    print("a tiene un valor verdadero")
```

Sin embargo, es recomendable utilizar `is None` o `is not None` para verificar explícitamente si una variable es `None`, ya que otros valores como `0`, `False` o cadenas vacías también se consideran falsos.

### Conversión de `None` a otros tipos

Intentar convertir `None` a otros tipos puede generar errores. Por ejemplo, convertir `None` a una cadena con `str()` es posible y devuelve la cadena `'None'`. Sin embargo, convertir `None` a un entero o a un número de punto flotante genera un error.

```python
a = None

print(str(a))  #> 'None'

# int(a)  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# float(a)  # TypeError: float() argument must be a string or a number, not 'NoneType'
```

### Resumen

El valor `None` es un tipo especial en Python que representa la ausencia de valor. Es útil para inicializar variables sin asignarles un valor específico, indicar que una función no devuelve nada o para comprobar si una variable no tiene un valor asignado.