# Variables

Las variables son usadas para almacenar información en la memoria de un programa. En Python, una variable es un nombre que se refiere a un valor.

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
- Los nombres de las variables deben ser sensibles a mayúsculas y minúsculas.

Al seguir estas reglas, se facilita la lectura y comprensión del código, lo que es fundamental para el desarrollo de programas eficientes y mantenibles.

## Tipos basicos: `int`

Los enteros (`int`) son un tipo de dato básico en Python que se utiliza para representar números enteros. Se los puede utilizar para realizar operaciones matemáticas simples, como sumas, restas, multiplicaciones y divisiones. Tienen la particularidad que no tiene limite en su tamaño (bueno, siempre hay limites pero es muy grande).

Se los identifica porque comienzan on un digito y no tienen punto decimal. Existen multiples formas de describir un entero pero mas alla de la forma de ingresarlo siempre se almacena como un numero entero.

```python
a = 100 # a es un entero en base 10 (decimal)
b = 0b10010101 # b es un entero en base 2 (binario)
c = 0o1234567 # c es un entero en base 8 (octal)
d = 0x1234567890ABCDEF # d es un entero en base 16 (hexadecimal)

print(a) # 100
print(b) # 149
print(c) # 342391
print(d) # 1311768467294899695
```

Sobre los enteros se pueden realizar las operaciones matematicas basicas como suma, resta, multiplicacion y division. Ademas se pueden realizar operaciones mas complejas como el calculo de modulo, division entera y potenciacion.

```python
# Operaciones matematicas basicas
a = 10
b = 3
c = a + b   #> 13          # Suma              __add__
d = a - b   #> 7           # Resta             __sub__
e = a * b   #> 30          # Multiplicacion    __mul__    
f = a / b   #> 3.33333333  # Division          __truediv__
g = a // b  #> 3           # Division entera   __floordiv__
h = a % b   #> 1           # Modulo (resto)    __mod__
i = a ** b  #> 1000        # Potenciacion      __pow__

# Comparaciones
j = a == b  #> False      # Igualdad          __eq__
k = a != b  #> True       # Desigualdad       __ne__
h = a < b   #> False      # Menor que         __lt__
i = a > b   #> True       # Mayor que         __gt__
l = a <= b  #> False      # Menor o igual que __le__
m = a >= b  #> True       # Mayor o igual que __ge__

a = 10_000     #> 10000  # Se pueden usar guiones bajos para separar los digitos
b = 0b1_0000   #> 16     # Se pueden usar guiones bajos para separar los digitos

print(2 ** 100)
# 1267650600228229401496703205376

# Cuantos '0' tiene el 2 ** 1000?
print(str(2 ** 1000).count('0'))
```

En Python se pueden realizar operaciones aritmeticas con los enteros sin preocuparse por el desbordamiento de los valores. Python maneja automaticamente el desbordamiento de los enteros, lo que significa que los enteros pueden crecer tanto como la memoria de la computadora lo permita.

Por ultimo, se pueden realizar conversiones entre los diferentes tipos de datos numericos en Python. Por ejemplo, se puede convertir un entero a un numero de punto flotante utilizando la funcion `float()` o un numero de punto flotante a un entero utilizando la funcion `int()`.

```python
# Conversion bool a int
int(True)  #> 1
int(False) #> 0

# Conversion float a int
int(3.14159) #> 3
int(10.9999) #> 10  (trunca el decimal)

# Conversion de cadenas a enteros
int('10')     #> 10 (base 10)
int('10', 2)  #> 2  (base 2)
int('10', 8)  #> 8  (base 8)
int('10', 16) #> 16 (base 16)
int('A', 16)  #> 10 (base 16)
int('xx', 16) #> ValueError: invalid literal for int() with base 16: 'xx'

# Conversion segura de cadenas a enteros
a = "10"

# Verificando si la cadena es un numero
if a.isnumeric(): 
    b = int(a)
    print(b)
else:
    print("No es un numero")

# Usando try-except para manejar errores
try:
    b = int(a)
    print(b)
except ValueError:
    print("No es un numero")
```

## Tipos basicos: `float`

Los números de punto flotante (`float`) son un tipo de dato básico en Python que se utiliza para representar números reales. Se los puede utilizar para realizar operaciones matemáticas más complejas, como sumas, restas, multiplicaciones y divisiones con decimales.

Se los identifica porque tienen un punto decimal o usan la notacion cientifica. Existen multiples formas de describir un numero de punto flotante pero mas alla de la forma de ingresarlo siempre se almacena como un numero real.

```python
a = 3.14159     # a es un numero de punto flotante
b = 1.0e-3      # b es un numero de punto flotante en notacion cientifica
c = 1_000.0     # c es un numero de punto flotante con guiones bajos para separar los digitos

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

i = math.trunc(a)       # Trunca el numero
j = math.floor(a)       # Redondea hacia abajo
k = math.ceil(a)        # Redondea hacia arriba
```

## Tipos basicos: `bool`

Los valores booleanos (`bool`) son un tipo de dato básico en Python que se utiliza para representar valores de verdad. Pueden tener dos posibles valores: `True` (verdadero) o `False` (falso).

Los valores booleanos se utilizan en expresiones lógicas y de comparación para determinar si una condición es verdadera o falsa. Por ejemplo:

```python
a = True
b = False

c = 10 > 5   #> True
d = 10 < 5   #> False
e = 10 == 5  #> False
```

En Python se consideran valores falsos los siguientes: `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `()`. Todos los demás valores se consideran verdaderos.

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

b = a OR  10/0  # True 
# 10/0 da un error de division por cero, pero como la expresion es cortocircuitada, no se evalua y no se produce el error.

c = a AND 10/0 # ZeroDivisionError: division by zero
```

Python realiza dos conversiones automaticas cuando trabaja con valores booleanos:

- Cuando se usa valores booleanos en operaciones aritmeticas, `True` se convierte en `1` y `False` se convierte en `0`.
- Cuando se expera una expresion booleana, como un un `if`, un `while` o en una `and`, `or`, `not` automáticamente se convierte en un valor booleano.

```python
# Conversion de enteros a booleanos
## Cualquier numero diferente de cero se convierte en True, el cero se convierte en False
bool(0)    # False
bool(1)    # True
bool(10)   # True

# Conversion de flotantes a booleanos
## Cualquier numero diferente de cero se convierte en True, el cero se convierte en False
bool(0.0)  # False
bool(0.1)  # True
bool(10.0) # True

# Conversion de cadenas a booleanos
## Cualquier cadena no vacia se convierte en True, la cadena vacia se convierte en False
bool('')   # False
bool('a')  # True
bool(' ')  # True

# Conversion de listas, diccionarios y tuplas a booleanos
## Cualquier secuencia no vacia se convierte en True, la secuencia vacia se convierte en False
bool([])   # False
bool([1])  # True
bool([0])  # True

bool({})   # False
bool({1})  # True

bool(())   # False
bool((1,)) # True
```

## Tipos basicos: `str`

Los `str` o cadenas en Python son un tipo de dato básico que se utiliza para representar texto. Se pueden utilizar para almacenar mensajes, nombres, direcciones, números de teléfono y cualquier otro tipo de información que se pueda representar como texto.

Las cadenas en Python se pueden definir utilizando comillas simples (`'`) o dobles (`"`). Por ejemplo:

```python
a = 'Hola, mundo!'
b = "¡Hola, mundo!"
c = '''Hola, mundo!'''
d = """¡Hola, mundo!"""
```

Tambien se pueden definir cadenas multilínea utilizando triples comillas simples (`'''`) o dobles (`"""`). Por ejemplo:

```python
a = '''Este es un ejemplo
de una cadena multilínea'''

b = """Este es otro ejemplo
de una cadena multilínea"""

print(a)
#> Este es un ejemplo
#> de una cadena multilínea
```

Existe un tipo especial de cadena que permite dar formato a los valores que se insertan en ella. Estas cadenas se conocen como cadenas de formato y se definen utilizando la letra `f` antes de las comillas de apertura. Se conocen como f-strings. o 'string interpolations'. 

Por ejemplo:

```python

nombre = "Juan"
apellido = "Perez"
mensaje = f'Hola, {nombre} {apellido}'
print(mensaje)
#> Hola, Juan Perez


a = 10
b = 20
print(f'{a} + {b} = {a + b}') # Con la f se evalua la expresion dentro de las llaves
#> 10 + 20 = 30

print('{a} + {b} = {a + b}')  #Sin la f no se evalua la expresion
#> {a} + {b} = {a + b}


# Con ':' se pueden especificar el formato de los valores
print(f'{"Hola":>10}')  # Alineado a la derecha en un campo de 10 caracteres
#>       Hola

print(f'{"Hola":<10}')  # Alineado a la izquierda en un campo de 10 caracteres
#> Hola

print(f'{"Hola":^10}')  # Alineado al centro en un campo de 10 caracteres

print(f'{3.14159:.2f}') # Redondea a 2 decimales
#> 3.14

print(f'{1000:10.2f}')  # Un campo de 10 caracteres con 2 decimales
#>   1000.00

print(f'{10:05i}')       # Rellena con ceros a la izquierda en un campo de 5 caracteres
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
#> 'Hola,'

g  = 'Hola, mundo!'[::-1]
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

k = 'Hola' * 3 # Repite la cadena 3 veces
print(k)
#> 'HolaHolaHola'

l = 'Hola, que tengas un ' + 'muy ' * 3 + 'buen dia!'
print(l)
#> 'Hola, que tengas un muy muy muy buen dia!'
```

Los `str` son una secuencia de caracteres, puede ser tratada como una lista de caracteres. Se puede acceder a los caracteres individuales de una cadena utilizando la notación de corchetes `[]` y el índice del carácter que se desea acceder. Por ejemplo:

```python
a = 'Hola, mundo!'
print(a[0])   #> 'H'    # Primer caracter
print(a[1])   #> 'o'    # Segundo caracter
print(a[-1])  #> '!'    # Ultimo caracter

for i in range(len(a)): # Recorre la cadena e imprime cada caracter
    print(a[i], end=' ')
#> H o l a ,   m u n d o !

l = list('Hola, mundo!') # Convierte la cadena en una lista de caracteres
print(l)
#> ['H', 'o', 'l', 'a', ',', ' ', 'm', 'u', 'n', 'd', 'o', '!']

print(a[6:8]) 
#> 'mu'
```

En python todos los tipos se pueden convertir a string, es decir siempre se puede hacer una representación de un valor como una cadena. Para convertir un valor a una cadena se puede utilizar la función `str()`. Esta funcion esta definida para todos los tipos de datos en Python. Para los tipos creados (clases) se pueden proveer una funcion para convertir a cadena.

```python
# Conversion de enteros a cadenas
a = str(10)    #> '10'
b = str(1000)  #> '1000'

# Conversion de flotantes a cadenas
c = str(3.14159)  #> '3.14159'
d = str(10.9999)  #> '10.9999'

# Conversion de booleanos a cadenas
e = str(True)   #> 'True'
f = str(False)  #> 'False'

# Conversion de listas, diccionarios y tuplas a cadenas
g = str([1, 2, 3])       #> '[1, 2, 3]'
h = str({'a': 1, 'b': 2}) #> "{'a': 1, 'b': 2}"
i = str((1, 2, 3))       #> '(1, 2, 3)'
```

Python realiza conversiones automaticas a cadena cuando se necesita. Por ejemplo, cuando se imprime un valor, se convierte a cadena automaticamente. Tambien se puede concatenar una cadena con un valor que no es una cadena, Python convierte el valor a cadena antes de concatenarlo.

```python
print(10, 1 > 2, "Hola", [1, 2, 3])                 # Llamada a str en forma implicita
#> 10 False Hola [1, 2, 3]

print(str(10), str(1 > 2), "Hola" , str([1, 2, 3])) # Llamada a str en forma explicita
#> 10 False Hola [1, 2, 3]

print(f"{10} {1 > 2} Hola {[1, 2, 3]}")             # Llamada a str en forma implicita
#> 10 False Hola [1, 2, 3]
```

Existe otra funcion para convertir un objeto en una cadena, `repr()`. Esta funcion devuelve una representacion de cadena del objeto que es mas cercana a la representacion interna del objeto. Es util para depurar y para mostrar objetos de forma mas detallada. Se puede decir que `str()` es para mostrar al usuario y `repr()` es para mostrar al programador.


```python
from datetime import datetime

# Crear un objeto datetime
now = datetime.now()

# Usar str() para convertir el objeto a una cadena (representacion legible)
print(f'str: {str(now)}')
#> str: 2022-03-06 10:00:00.123456

# Usar repr() para convertir el objeto a una cadena (representacion detallada)
print(f'repr: {repr(now)}')
#> repr: datetime.datetime(2022, 3, 6, 10, 0, 0, 123456)

print(f'{now}') # Llamada a str() en forma implicita
#> 2022-03-06 10:00:00.123456
```

En este ejemplo, `str(now)` devuelve una representación legible del objeto `datetime`, mientras que `repr(now)` devuelve una representación más detallada y precisa del objeto, que incluye información adicional sobre la clase y el módulo.

## Tipos basicos: `None`

El valor `None` es un tipo de dato especial en Python que se utiliza para representar la ausencia de un valor. Se puede utilizar para inicializar variables, devolver valores nulos desde funciones o métodos, y representar la falta de un valor en una estructura de datos.

Las llamadas a funcion que no retornan un valor explicito, retornan `None`. Por ejemplo:

```python
def saludar(nombre):
    print(f'Hola, {nombre}!')

saludo = saludar('Juan')
print(saludo) #> None
```