# Integrar las clases a Python 

Todo en Python son objetos, los tipos de datos básicos son objetos, las funciones son objetos, los módulos son objetos y las clases son objetos. 

Un aspecto muy especial de Python es que nos permite crear tipos de datos personalizados y que los mismos se comporte exactamente igual que los tipos de datos básicos. Para lograrlos se utilizan metodos especiales que permiten definir el comportamiento de los objetos de una clase. Estos metodos nos ayuda a usar todo el potencial de las clases en Python.

Existen metodos especiales para convertir un objetos, realizar operaciones matematicas o de comparación, o crear colecciones entre otros.

Todos los metodos especiales se identifica por tener dos guiones bajos al principio y al final del nombre del metodo. Por ejemplo, el metodo `__init__` es un metodo especial que se utiliza para inicializar un objeto cuando se crea una instancia de una clase. Estos metodos son usado internamente por Python y no se llaman directamente en el codigo aunque se pueden llamar si es necesario. Una excepción a esto es el metodo `__init__` el cual si bien se llama interamente por Python, tambien se puede llama directamente cuando usamos herencia.

Podemos considerar que Python en realidad define una marco de trabajo para la programación orientada a objetos, esto es que ademas de las clases intrumenta un conjunto de metodos para que las clases personalizadas se comporten como los tipos de datos básicos.

## Metodos especiales

### Metodo `__init__`

El metodo `__init__` es un metodo especial que se utiliza para inicializar un objeto cuando se crea una instancia de una clase. Este metodo se llama automaticamente cuando se crea un objeto de una clase y se utiliza para inicializar los atributos de la clase.

Por ejemplo, supongamos que queremos crear una clase `Persona` que tenga los atributos `nombre`, `edad` y `altura`. Podemos definir la clase `Persona` de la siguiente manera:

```python
class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

p = Persona("Juan", 30, 1.75)

```

En este caso el metodo `__init__` recibe cuatro parametros: `self`, `nombre`, `edad` y `altura`. El parametro `self` hace referencia al objeto actual y se utiliza para acceder a los atributos y metodos de la clase. Los parametros `nombre`, `edad` y `altura` se utilizan para inicializar los atributos `nombre`, `edad` y `altura` del objeto.

### Metodo `__str__`

El metodo `__str__` es un metodo especial que se utiliza para devolver una representación en forma de cadena de un objeto. Este metodo se llama automaticamente cuando se utiliza la funcion `str()` o `print()` con un objeto de una clase.

Por ejemplo, supongamos que queremos crear una clase `Persona` que tenga los atributos `nombre`, `edad` y `altura`. Podemos definir la clase `Persona` de la siguiente manera:

```python
class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Altura: {self.altura}"

p = Persona("Juan", 30, 1.75)

print(p)  # Output: Nombre: Juan, Edad: 30, Altura: 1.75
```

En este caso, el metodo `__str__` devuelve una cadena con los atributos `nombre`, `edad` y `altura` del objeto. Cuando se utiliza la funcion `print()` con el objeto `p`, se llama automaticamente al metodo `__str__` y se imprime la cadena devuelta por el metodo.

Los mismos sucede cuando se utiliza la funcion `str()` con el objeto `p`. Por ejemplo:

```python
s = str(p)
print(s)  # Output: Nombre: Juan, Edad: 30, Altura: 1.75
```

Internamente la funcion `str()` llama al metodo `__str__` del objeto `p` y devuelve la cadena devuelta por el metodo. Esto permite utilizar el 'polimorfismo' en Python, es decir, que un objeto pueda comportarse de diferentes maneras dependiendo del contexto en el que se utilice. 

La funcion str() no sabe como convertir un objeto en un representación de cadena, pero si el objeto tiene un metodo `__str__` definido, entonces la funcion `str()` llama a ese metodo para obtener la representación en forma de cadena del objeto.

Es decir, internamente Python delega la responsabilidad de convertir un objeto en una cadena al metodo `__str__` del objeto si este metodo esta definido.

La funcion print intermanete llama a la funcion str() para obtener la representación en forma de cadena del objeto y luego imprime esa cadena en la consola. La funcion str() a su vez llama al metodo `__str__` del objeto si este metodo esta definido.

De esta manera las funciones creadas antes de la definición de la clase `Persona` no necesitan ser modificadas para imprimir un objeto de la clase `Persona`.

Si vamos mas al detalle en realidad str() es el contructor de la clase str. Esto lo usamos como si fuera una funcion (y lo es porque en Python las clases son `llamables` como funciones) pero en realidad es un constructor de la clase str.

```python
a = str(5)
print(a) # Output: '5'

b = str(2>1)
print(b) # Output: True

c = str([1, 2, 3]) # Output: '[1, 2, 3]'

print(5, 2>1, [1, 2, 3])     # Implitamente se llama a str() para convertir los argumentos en cadenas
# Output: 5 True [1, 2, 3]

print(str(5), str(2>1), str([1, 2, 3]))  # Llamamos explicitamente a str() para convertir 
# Output: 5 True [1, 2, 3]

```

Lo interesante es que Python es un lenguaje fuertemente tipado, pero a la vez es un lenguaje dinámico. Es fuertemente tipado porque siempre respeta las operaciones definidas para los tipos de datos, pero es dinámico porque permite que los objetos se comporten de diferentes maneras dependiendo del contexto en el que se utilicen.

Esto lo logra a través de los métodos especiales que permiten definir el comportamiento de los objetos de una clase.

### Metodo `__repr__`

El metodo `__repr__` es un metodo especial que se utiliza para devolver una representación en forma de cadena de un objeto. Este metodo se llama automaticamente cuando se utiliza la funcion `repr()` con un objeto de una clase. Es similar al metodo `__str__` pero se utiliza para obtener una representación más detallada del objeto. En cambio, el metodo `__str__` se utiliza para obtener una representación más amigable del objeto.

Por ejemplo, supongamos que queremos crear una clase `Persona` que tenga los atributos `nombre`, `edad` y `altura`. Podemos definir la clase `Persona` de la siguiente manera:

```python
class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Altura: {self.altura}"

    def __repr__(self):
        return f"Persona({self.nombre!r}, {self.edad!r}, {self.altura!r})"

a = Persona("Juan", 30, 1.75)
print(a)        # Output: Nombre: Juan, Edad: 30, Altura: 1.75    

print(repr(a))  # Output: Persona('Juan', 30, 1.75)

# f-string con !s y !r para llamar a str() y repr() respectivamente

# por defecto usa !s si no se especifica
print(f'{a}')   # Output: Nombre: Juan, Edad: 30, Altura: 1.75

# Equivalente a...
print(f'{a!s}') # Output: Nombre: Juan, Edad: 30, Altura: 1.75

# Pero si especificamos !r usa repr()
print(f'{a!r}') # Output: Persona('Juan', 30, 1.75)

```

En resumen se usa str() para obtener una representación amigable del objeto y repr() para obtener una representación más detallada del objeto.

### Metodo `__bool__`

Otro ejemplo de este comportamiento es el método `__bool__` que se utiliza para devolver un valor booleano de un objeto. Este método se llama automáticamente cuando se utiliza el operador `bool()` con un objeto de una clase.

Al comienzo vimos que en Python se considera `False` a `False`, a `0`, a `""`, a `[]`, a `{}`, a `set()` y a `None`; todo lo demás se considera `True`. 

Esto puede parecer que existen valores "mágicos", valores que tienen un valor especial en Python. Pero en realidad no es así, en Python no existen valores mágicos, sino que existen métodos especiales que permiten definir el comportamiento de los objetos de una clase.

Cuando Python quiere saber si un `int` se puede convertir a `bool` usa la función `__bool__` de la clase `int`, cuando hacemos `bool('hola')` Python llama a la función `__bool__` de la clase `str` y cuando hacemos `bool([1, 2, 3])` Python llama a la función `__bool__` de la clase `list`.

Este proceso de convercion lo hace automaticamente cuando se usa una variable en el contexto de una condición por ejemplo en un `if`, en un `while` o incluso en `and` o `or`.

```python

if 10:                      # Convierte (implicitamente) 10 a bool
    print('10 es True')
else:
    print('10 es False')

# Output: 10 es True

#Equivale a 
if bool(10):                # Convierte (explicitamente) 10 a bool
    print('10 es True')
else:
    print('10 es False')

# Output: 10 es True

# que a la vez equivale a
if int.__bool__(10):        # Convierte (explicitamente usando __bool__) 10 a bool
    print('10 es True')
else:
    print('10 es False')

# Output: 10 es True

```

Volvamos a nuestra clase `Producto` y veamos cómo se comporta en un contexto de condición.

```python

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def __bool__(self):
        return self.precio > 0

p = Producto("Laptop", 1000)
if p:
    print('Lo podemos vender')
else:
    print('No lo podemos vender')

# Output: Lo podemos vender

p = Producto("Mouse", 0)
if p:
    print('Lo podemos vender')
else:
    print('No lo podemos vender')

# Output: No lo podemos vender

```

En este caso, el método `__bool__` devuelve `True` si el precio del producto es mayor que cero y `False` en caso contrario. Cuando se utiliza el objeto `p` en un contexto de condición, se llama automáticamente al método `__bool__` y se evalúa si el producto se puede vender o no.

En la tienda, podríamos tener una lista de productos y querer saber si podemos vender todos los productos de la lista. Podemos hacer esto de la siguiente manera:

```python

class Tienda:
    #...
    def mostrar(self):
        for p in self.productos:
            if p:
                print(p)
    #...
```

En este caso, el método `mostrar` recorre la lista de productos de la tienda y utiliza cada producto en un contexto de condición para determinar si se puede vender o no. Si el producto se puede vender, se imprime el producto en la consola.

De esta manera, podemos utilizar el polimorfismo en Python para que los objetos de una clase se comporten de diferentes maneras dependiendo del contexto en el que se utilicen.

### Metodo `__len__`

El método `__len__` es un método especial que se utiliza para devolver la longitud de un objeto. Este método se llama automáticamente cuando se utiliza la función `len()` con un objeto de una clase.

A diferencia de otros lenguajes, para averiguar la longitud de una lista en Python se usa la función `len()` en lugar de 'a.length' o 'a.size()' como en otros lenguajes.

Esto es así porque la función `len()` llama al método `__len__` del objeto `a` para obtener la longitud del objeto. Si el método `__len__` no está definido para el objeto `a`, se produce un error.

Sigamos con el caso de la clase Tienda, si quisiéramos saber cuántos productos hay en la tienda podríamos hacer lo siguiente:

```python

class Tienda:
    #...
    def __len__(self):
        return len(self.productos)
    #...

t = Tienda()
t.agregar(Producto("Laptop", 1000))
t.agregar(Producto("Mouse", 0))

print(f'Hay {len(t)} productos en la tienda')  
# Output: Hay 2 productos en la tienda

```

En este caso, el método `__len__` devuelve la longitud de la lista de productos de la tienda. Cuando se utiliza la función `len()` con el objeto `t`, se llama automáticamente al método `__len__` y se obtiene la cantidad de productos en la tienda. Se podría haber hecho lo mismo con la función `len(t.productos)` pero de esta manera se encapsula la lógica de la longitud de la lista de productos en la clase `Tienda`.

Si vamos más al detalle, podemos ver que Python usa la función `len()` para determinar si un objeto es vacío o no. Por ejemplo, si hacemos `if len(t):` Python llama al método `__len__` de la clase `Tienda` para determinar si la tienda tiene productos o no.

Si observamos bien, veremos que cuando convertíamos a `bool()`, las cadenas, las listas, los diccionarios, las tuplas y los conjuntos se consideraban `False` si estaban vacíos y `True` si tenían elementos. Esto es porque Python llama al método `__len__` de la clase correspondiente para determinar si el objeto está vacío o no cuando no encuentra un método `__bool__` definido.

Por ejemplo en la clase `Tienda` podriasmos usarla en un contexto de condición para saber si la tienda tiene productos o no.

```python


t = Tienda()
t.agregar(Producto("Laptop", 0))
t.agregar(Producto("Mouse", 0))

if t:
    print(f'La tienda tiene productos {len(t)} productos disponibles')
else:
    print('La tienda no tiene productos para vender')

```

### Metodo `__getitem__`

El método `__getitem__` es un método especial que se utiliza para obtener un elemento de un objeto mediante su índice. Este método se llama automáticamente cuando se utiliza la indexación con corchetes `[]` en un objeto de una clase.

Por ejemplo, si queremos listar los `Productos` de la `Tienda` podriamos aprovechar que sabemos que se implmento con una lista de productos y recorrerlo asi:

```python
t = Tienda()
t.agregar(Producto("Laptop", 1000))
t.agregar(Producto("Mouse", 0))

for i in range(len(t.productos)):
    p = t.productos[i]
    print(p)

# o incluso 
for p in t.productos:
    print(p)    

```

Pero este enfoque rompe el encapsulamiento de la clase `Tienda` ya que estamos accediendo directamente a la lista de productos. Podemos mejorar esto implementando el método `__getitem__` en la clase `Tienda` de la siguiente manera:

```python
class Tienda :
    #...
    def __len__(self):
        return len(self.productos)

    def __getitem__(self, i):
        return self.productos[i]
    #...

# Ahora podemos listar los productos de la tienda de la siguiente manera:
t = Tienda()
t.agregar(Producto("Laptop", 1000))
t.agregar(Producto("Mouse", 0))

for i in range(len(t)):
    p = t[i]
    print(p)

# o incluso
for p in t:
    print(p)

```

Esto es asi porque Python llama al método `__getitem__` de la clase `Tienda` para obtener el elemento de la lista de productos en la posición `i`. De esta manera, podemos utilizar la indexación con corchetes `[]` en un objeto de la clase `Tienda` para obtener un producto de la tienda.

Es decir podemos usar `Tienda` como si fuera una lista de productos y tratarla como tal. Esto es un ejemplo de polimorfismo en Python, es decir, que un objeto pueda comportarse de diferentes maneras dependiendo del contexto en el que se utilice.

Esta es una de las razones por las que Python es un lenguaje tan poderoso y flexible, ya que nos permite definir el comportamiento de los objetos de una clase de acuerdo a nuestras necesidades.

Esto tiene implicancias muy interesantes, por ejemplo:

```python

t = Tienda()
t.agregar(Producto("Laptop", 1000))
t.agregar(Producto("Mouse", 0))
t.agregar(Producto("Teclado", 500))

print(t[0])     # Output: Laptop - $1000
print(t[1])     # Output: Mouse - $0
print(t[-1])    # Output: Teclado - $500

parte = t[1:]  # usamos slicing para obtener una parte de la lista de productos
print(parte)   # Output: [Mouse - $0, Teclado - $500]

parte = t[:2]  # 
print(parte)   # Output: [Laptop - $1000, Mouse - $0]

sorted_tienda = sorted(t)  # Usamos la función sorted() para ordenar los productos de la tienda

precios 

```

### Metodo `__setitem__`

El método `__setitem__` es un método especial que se utiliza para asignar un valor a un elemento de un objeto mediante su índice. Este método se llama automáticamente cuando se utiliza la indexación con corchetes `[]` en un objeto de una clase en el lado izquierdo de una asignación.

Por ejemplo, si queremos modificar un `Producto` de la `Tienda` podriamos aprovechar que sabemos que se implmento con una lista de productos y modificarlo asi:

```python
t = Tienda()
t.agregar(Producto("Laptop", 1000))

t.productos[0] = Producto("Mouse", 0)

for p in t.productos:
    print(p)

```

Pero este enfoque rompe el encapsulamiento de la clase `Tienda` ya que estamos accediendo directamente a la lista de productos. Podemos mejorar esto implementando el método `__setitem__` en la clase `Tienda` de la siguiente manera:

```python
class Tienda :
    #...
    def __setitem__(self, i, p):
        self.productos[i] = p
    #...

# Ahora podemos modificar un producto de la tienda de la siguiente manera:
t = Tienda()
t.agregar(Producto("Laptop", 1000))

t[0] = Producto("Mouse", 0)

for p in t:
    print(p)

```

Esto es así porque Python llama al método `__setitem__` de la clase `Tienda` para asignar un producto a la lista de productos en la posición `i`. De esta manera, podemos utilizar la indexación con corchetes `[]` en un objeto de la clase `Tienda` para modificar un producto de la tienda.

Una observación interesante, la clase `str` en realidad es una lista de caracteres, por lo que podemos usar indexación y slicing en una cadena de texto. En dicha clase se implementó `__len__` y `__getitem__` pero no `__setitem__`. Esto es porque las cadenas de texto son inmutables, es decir, no se pueden modificar una vez creadas.

### Otros métodos de colección:

- `__contains__`: Se utiliza para determinar si un objeto contiene un elemento. Este método se llama automáticamente cuando se utiliza el operador `in` con un objeto de una clase.
- `__delitem__`: Se utiliza para eliminar un elemento de un objeto mediante su índice. Este método se llama automáticamente cuando se utiliza la instrucción `del` con un objeto de una clase.
- `__iter__`: Se utiliza para devolver un iterador de un objeto. Este método se llama automáticamente cuando se utiliza la función `iter()` con un objeto de una clase.

### Metodo `__add__` , `__sub__`, `__mul__`, `__truediv__`, etc. 

Estos son metodos que se usan para realizar operaciones matematicas con objetos de una clase. Cuando se usa un operador matematico con un objeto de una clase, Python llama al metodo correspondiente para realizar la operación. 

Para `+` se llama a `__add__`, para `-` se llama a `__sub__`, para `*` se llama a `__mul__`, para `/` se llama a `__truediv__` etc.

Es por esta razon que podemos sumar dos cadenas de texto, dos listas o dos enteros. Python llama al metodo `__add__` de la clase `str`, `list` o `int` respectivamente para realizar la suma.

Esta es una caracetistica que hace muy expresivo al lenguaje. Por ejemplo, estas son las implementaciones de los metodos `__add__` y `__mul__` en la clase `str`:

```python
class str:
    #...
    def __add__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return self.join([self, other])

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.join([self]*other)
    #...

a = ('Hola ' + 'Mundo! ') * 3 
print(a)  # Output: Hola Mundo! Hola Mundo! Hola Mundo! 

# Incluso podemos hacer algo como esto
b = ('Hola, ' + 'muy ' * 3 + 'buenos dias!' + '\n' ) * 3

# usa los parentesis para separar las operaciones y hacerlo mas legible, ejecuta primero '* 3' y luego '+ 'buenos dias!' + '\n' '
print(b) 
# Output:
# Hola, muy muy muy buenos dias!
# Hola, muy muy muy buenos dias!
# Hola, muy muy muy buenos dias!

```
En el caso de str el `+` concatena las cadenas y el `*` repite la cadena.

Podriamos hacer un ejemplo similar con la clase `Producto` para sumar cantidades y incrementar los precios.

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Producto(self.nombre, self.precio, self.cantidad + other.cantidad)

    def __mul__(self, aumento):
        if not isinstance(other, int, float):
            return NotImplemented
        return Producto(self.nombre, self.precio * (1 + aumento / 100 ), self.cantidad)

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - {self.cantidad} unidades"

    def __repr__(self):
        return f"Producto('{self.nombre}', {self.precio}, {self.cantidad})"
    
    def __bool__(self):
        return self.precio > 0 and self.cantidad > 0

p = Producto("Laptop", 1000, 10)
print(repr(p))  # Output: Producto('Laptop', 1000, 10)

p = p + 10      # Agrega 10 unidades
print(repr(p))  # Output: Producto('Laptop', 1000, 20)

p += 10
print(repr(p))  # Output: Producto('Laptop', 1000, 30)

p = p * 10     # Incrementa el precio un 10%
print(repr(p))  # Output: Producto('Laptop', 1100, 30)

p *= 10
print(repr(p))  # Output: Producto('Laptop', 1210, 30)

```

Observe que en este caso cuando se suma o multiplica un `Producto` con un entero, se devuelve un nuevo `Producto` con la cantidad o el precio modificado. De esta manera, podemos utilizar los operadores matemáticos con objetos de la clase `Producto` de manera similar a como lo hacemos con los tipos de datos básicos. 

Esto es lo que se llama una clase inmutable, es decir, una clase cuyos objetos no se pueden modificar una vez creados. En este caso, los objetos de la clase `Producto` son inmutables porque no se pueden modificar una vez creados. De esta manera están implementadas las clase int, float, str, tuple, etc.

### Metodo `__eq__`, `__lt__`, `__gt__`, `__le__`, `__ge__`, `__ne__`

Estos son metodos que se usan para realizar comparaciones con objetos de una clase. Cuando se usa un operador de comparación con un objeto de una clase, Python llama al metodo correspondiente para realizar la comparación.

- `__eq__` se llama cuando se usa el operador `==` para comparar dos objetos.
- `__lt__` se llama cuando se usa el operador `<` para comparar dos objetos.
- `__gt__` se llama cuando se usa el operador `>` para comparar dos objetos.
- `__le__` se llama cuando se usa el operador `<=` para comparar dos objetos.
- `__ge__` se llama cuando se usa el operador `>=` para comparar dos objetos.
- `__ne__` se llama cuando se usa el operador `!=` para comparar dos objetos.

Por ejemplo, si queremos comparar dos `Productos` por su precio podríamos hacer lo siguiente:

```python

class Producto:
    #...
    def __eq__(self, other):
        return self.precio == other.precio

    def __lt__(self, other):
        return self.precio < other.precio
    #...

p1 = Producto("Laptop", 1000)
p2 = Producto("Mouse", 500)

if p1 == p2:
    print('Los productos tienen el mismo precio')
elif p1 < p2:
    print('El producto 1 es más barato que el producto 2')
else:
    print('El producto 1 es más caro que el producto 2')

```

En este caso, el método `__eq__` devuelve `True` si el precio del producto 1 es igual al precio del producto 2 y `False` en caso contrario. El método `__lt__` devuelve `True` si el precio del producto 1 es menor que el precio del producto 2 y `False` en caso contrario.

De esta manera, podemos utilizar los operadores de comparación con objetos de la clase `Producto` de manera similar a como lo hacemos con los tipos de datos básicos.

### Metodo `__call__`

El método `__call__` es un método especial que se utiliza para llamar a un objeto como si fuera una función. Este método se llama automáticamente cuando se utiliza el objeto con paréntesis `()`.

Por ejemplo, si queremos calcular el precio total de un producto podríamos hacer lo siguiente:

```python

class Producto:
    #...
    def __call__(self, cantidad):
        return self.precio * cantidad
    #...

p = Producto("Laptop", 1000)
total = p(10)
print(f'El precio total es ${total}')

```

En este caso, el método `__call__` recibe un parámetro `cantidad` y devuelve el precio total del producto. Cuando se utiliza el objeto `p` con paréntesis `()`, se llama automáticamente al método `__call__` y se calcula el precio total del producto.

De esta manera, podemos utilizar los objetos de la clase `Producto` como si fueran funciones para calcular el precio total del producto.

### Metodo `__iter__` y `__next__`

Vimos que con el método `__len__` y `__getitem__` podemos hacer que un objeto de una clase se comporte como una lista. Pero no siempre se puede hacer esto, por ejemplo, si queremos recorrer los números pares de 0 a 10 no podemos hacerlo con una lista. 

En este caso, podemos implementar el método `__iter__` y `__next__` para crear un iterador que nos permita recorrer los números pares de 0 a 10.

Supongamos que queremos hacer un contador (similiar a `range(1, n)`) es puede implementar de la siguiente manera:

```python
class Contador:
    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration # Se lanza una excepción para indicar que se ha alcanzado el final de la secuencia
        self.i += 1      # Incrementa el contador
        return self.i

    def __iter__(self): # Devuelve el objeto iterador para el bucle for
        return self

c = Contador(10)
print(next(c))  # Output: 1
print(next(c))  # Output: 2
print(next(c))  # Output: 3
while True:
    try:
        print(next(c))
    except StopIteration:
        break
# Output: 4 5 6 7 8 9 10
for i in Contador(10):
    print(i, end=' ')

# Output: 1 2 3 4 5 6 7 8 9 10


```

En este caso, el método `__next__` devuelve el siguiente número par en la secuencia de 0 a 10. Cuando se utiliza el objeto `c` en un contexto de iteración, se llama automáticamente al método `__iter__` y `__next__` para recorrer los números pares de 0 a 10.

De esta manera, podemos utilizar los objetos de la clase `Contador` como si fueran iteradores para recorrer los números pares de 0 a 10.
