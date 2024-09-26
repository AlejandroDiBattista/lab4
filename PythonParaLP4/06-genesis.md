---

# ¿Cómo surge la Orientación a Objetos?

Supongamos que tenemos que resolver el siguiente problema:

> **Revisar si una expresión aritmética tiene los paréntesis balanceados.**

Este es un problema que ya vimos, pero lo complicamos un poco más: digamos que la expresión aritmética puede tener paréntesis, corchetes y llaves.

> **Revisar si una expresión aritmética tiene los paréntesis, corchetes y llaves balanceados.**

A diferencia del primer problema, donde bastaba con contar la cantidad de paréntesis de apertura y cierre, ahora debemos verificar que los paréntesis, corchetes y llaves estén correctamente balanceados y anidados.

Para ello, debemos recordar cuál fue el último paréntesis, corchete o llave que abrimos y verificar que el cierre sea el correspondiente.

Para realizar esta función, debemos ir almacenando las **aperturas** y verificar que los **cierres** sean los correspondientes. La última **apertura** que se almacenó debe ser la primera en cerrarse.

```python
def parentesis_balanceados(expresion):
    pila = [None] * len(expresion)  # Crear un array con el tamaño de la expresión
    cantidad = 0                    # Inicializar el contador de elementos

    apertura = {'(': ')', '{': '}', '[': ']'}
    cierre   = {')': '(', '}': '{', ']': '['}

    for char in expresion:
        if char in apertura:
            pila[cantidad] = char   # Agregar el paréntesis de apertura a la pila
            cantidad += 1           # Incrementar el contador
        elif char in cierre:
            if cantidad == 0 or pila[cantidad - 1] != cierre[char]:
                return False        # La pila está vacía o no coincide el tipo de paréntesis
            cantidad -= 1           # Decrementar el contador

    return cantidad == 0            # La pila debe estar vacía si los paréntesis están balanceados
```

Este es un ejemplo de una función que verifica si los paréntesis, corchetes y llaves están balanceados.

Este enfoque funciona bien, pero en el código se mezclan los datos y la lógica. Una solución alternativa sería usar una estructura de datos abstracta llamada **pila**. La pila define tres funciones básicas y luego se puede usar para resolver el problema.

```python
pila = [None] * 10  # Crear una pila con capacidad para 10 elementos
cantidad = 0        # Inicializar el contador de elementos en la pila

def push(elemento):
    global cantidad
    pila[cantidad] = elemento
    cantidad += 1

def pop():
    global cantidad
    cantidad -= 1
    return pila[cantidad]

def is_empty():
    return cantidad == 0
```

Con esta estructura de datos, se puede reescribir la función anterior de la siguiente manera:

```python
def parentesis_balanceados(expresion):
    apertura = {'(': ')', '{': '}', '[': ']'}
    cierre   = {')': '(', '}': '{', ']': '['}

    for char in expresion:
        if char in apertura:
            push(char)
        elif char in cierre:
            if is_empty() or pop() != cierre[char]:
                return False

    return is_empty()
```

Esta solución es más clara y fácil de entender. La pila es una estructura de datos que se puede reutilizar en otros problemas.

La pila es un ejemplo de una estructura de datos abstracta. Una estructura de datos abstracta define un conjunto de operaciones y propiedades, pero no especifica cómo se implementan esas operaciones y propiedades.

Ahora no nos interesa cómo se implementa la pila, solo nos interesa que podemos agregar elementos, quitar elementos y verificar si está vacía.

El problema con esta implementación es que la pila es global y si se llama a la función `parentesis_balanceados` varias veces, la pila se va a mezclar entre las llamadas.

Una solución sería encapsular la pila en métodos que se encarguen de gestionar el estado interno.

```python
def Stack():    # Crear una pila vacía (constructor)
    return {'cantidad': 0, 'pila': [None] * 10}  # Usamos un diccionario para encapsular la pila

def push(pila, elemento):
    pila['pila'][pila['cantidad']] = elemento
    pila['cantidad'] += 1

def pop(pila):
    pila['cantidad'] -= 1
    return pila['pila'][pila['cantidad']]

def is_empty(pila):
    return pila['cantidad'] == 0


def parentesis_balanceados(expresion):
    pila = Stack()

    apertura = {'(': ')', '{': '}', '[': ']'}
    cierre   = {')': '(', '}': '{', ']': '['}

    for char in expresion:
        if char in apertura:
            push(pila, char)
        elif char in cierre:
            if is_empty(pila) or pop(pila) != cierre[char]:
                return False

    return is_empty(pila)
```

Ahora la pila está encapsulada en un diccionario y se pasa como argumento a las funciones que la manipulan.

Esto nos permite tener varias pilas independientes y no mezclar los datos entre llamadas a la función `parentesis_balanceados`.

Podríamos usar varias pilas para resolver problemas diferentes.

```python
a = Stack()  # Creo una 'instancia' de la pila
b = Stack()  # Creo otra 'instancia' de la pila

push(a, 10)  # Agrego elementos a la pila 'a'
push(b, 20)  # Agrego elementos a la pila 'b'
push(a, 30)  # Agrego otro elemento a la pila 'a'

while not is_empty(a):  # Muevo los elementos de la pila 'a' a la pila 'b'
    push(b, pop(a))

while not is_empty(b):  # Imprimo los elementos de la pila 'b'
    print(pop(b))

#> 30
#> 10
#> 20
```

Una de las ventajas de este enfoque es que el programador no tiene que pensar en cómo fue implementada la pila, solo tiene que saber cómo usarla.

Por ejemplo, si aprovechamos que en Python disponemos de listas y sus métodos `append` y `pop`, podemos reescribir la pila de la siguiente manera:

```python
def Stack():     # Crear una pila vacía (constructor)
    return []    # Usamos una lista para encapsular la pila

def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    return pila.pop()

def is_empty(pila):
    return len(pila) == 0
```

Esta implementación es más simple y utiliza las listas de Python para almacenar los elementos de la pila. No sería tan eficiente como la implementación anterior, pero es más simple y fácil de entender.

Este es un ejemplo de cómo surge la programación orientada a objetos. Se comienza a **encapsular** los datos y la lógica en estructuras de datos y funciones que operan sobre ellas.

Sin embargo, todavía tenemos un problema con esta implementación. Supongamos que tenemos que implementar una cola, que es una estructura de datos similar a una pila, pero en la que el primer elemento que se agrega es el primero en salir.

```python
def Queue():    # Crear una cola vacía (constructor)
    return []   # Usamos una lista para encapsular la cola

def enqueue(cola, elemento):
    cola.append(elemento)

def dequeue(cola):
    return cola.pop(0)

def is_empty(cola):
    return len(cola) == 0
```

Esta implementación es simple y reutilizable, pero tenemos un problema: ambas estructuras tienen un método que se llama `is_empty`, y si queremos usar ambas al mismo tiempo, vamos a tener un conflicto. En este caso puntual no es un problema grave porque si vemos la implementación de `is_empty`, es la misma para ambas estructuras.

Pero eso rompe el **encapsulamiento** de los datos y la lógica. Si queremos cambiar la implementación de `is_empty` en una de las estructuras, vamos a tener que cambiarla en todas las estructuras.

Una solución sería encapsular las estructuras en clases y definir los métodos como métodos de instancia.

Podríamos llamar a la función `is_empty` de otra manera para evitar el conflicto.

```python
def is_empty_queue(cola):
    return len(cola) == 0

def is_empty_stack(pila):
    return len(pila) == 0
```

Pero esto no es una solución elegante. Antes usábamos la función `is_empty` para saber si una estructura estaba vacía, ahora tenemos que recordar qué función usar para cada estructura.

Lo que queremos en realidad es que cada estructura tenga su propio método `is_empty` y que se llame de la misma manera. Es lo que se llama **polimorfismo**: que cada objeto se comporte de la misma manera pero adecue su conducta al tipo de datos que le corresponda.

Para esto surgen las clases y los objetos. Una clase es una plantilla que define las propiedades y los métodos de un objeto. Un objeto es una instancia de una clase.

```python
class Stack:
    def __init__(self):     # Crear una pila vacía (constructor)
        self.lista = []     # Usamos una lista para encapsular la pila

    def push(self, elemento):
        self.lista.append(elemento)

    def pop(self):
        return self.lista.pop()

    def is_empty(self):
        return len(self.lista) == 0

class Queue:
    def __init__(self):     # Crear una cola vacía (constructor)
        self.lista = []     # Usamos una lista para encapsular la cola

    def enqueue(self, elemento):
        self.lista.append(elemento)

    def dequeue(self):
        return self.lista.pop(0)

    def is_empty(self):
        return len(self.lista) == 0
```

Al definir las clases de esta manera, estamos creando funciones que se aplican a los datos de la clase. Estas funciones se llaman **métodos** y se definen dentro de la clase.

Aunque no es habitual, podemos usar las funciones directamente en la forma tradicional, solo que prefijadas por el nombre de la clase.

```python
a = Stack()

Stack.push(a, 10)
Stack.push(a, 20)
while not Stack.is_empty(a):
    print(Stack.pop(a))

b = Queue()
Queue.enqueue(b, 10)
Queue.enqueue(b, 20)
while not Queue.is_empty(b):
    print(Queue.dequeue(b))
```

Ahora no hay conflicto de nombres porque cada instancia de la clase tiene sus propios métodos.

Sin embargo, por más que esta forma de usar las clases sea válida, no es la más común. Lo más común es usar la notación de punto `.` para acceder a los métodos de una clase.

```python
a = Stack()
a.push(10)
a.push(20)
while not a.is_empty():
    print(a.pop())

b = Queue()
b.enqueue(10)
b.enqueue(20)
while not b.is_empty():
    print(b.dequeue())
```

Ahora el código es más claro y fácil de entender. Se puede ver que `a` es una pila y `b` es una cola, y se pueden usar de la misma manera.

En resumen, la programación orientada a objetos es un paradigma de programación que se basa en el concepto de objetos, que son instancias de clases. Las clases definen las propiedades y los métodos de los objetos y permiten encapsular los datos y la lógica en una estructura coherente y reutilizable.

Observemos algunos elementos de la sintaxis de Python que nos permiten trabajar con clases y objetos.

### Método `__init__`

El primero es que se usa un nombre especial para inicializar los valores de la clase: `__init__`. Este método se llama **constructor** y se utiliza para inicializar los valores de los objetos cuando se crean.

Si vamos muy al detalle, en realidad no es un constructor, sino un inicializador. En Python, los objetos se crean primero y luego se inicializan con el método `__init__`, pero a efectos prácticos, se puede considerar un constructor.

Existen muchos **métodos especiales** que se pueden definir en una clase para modificar el comportamiento de los objetos. Por ejemplo, el método `__str__` se utiliza para definir la representación en forma de cadena de un objeto. Estos métodos los usa Python para realizar operaciones internas y no es necesario llamarlos directamente. Veremos algunos de estos métodos más adelante.

### Parámetro `self`

El segundo elemento es que cada **método** recibe un primer parámetro que se llama `self`. Este parámetro se utiliza para referenciar al objeto que se está manipulando. Es una convención en Python utilizar `self` como nombre de este parámetro, pero se puede utilizar cualquier nombre.

### Acceso a Propiedades y Métodos

El tercer elemento es que se puede acceder a las propiedades y los métodos de un objeto utilizando la notación de punto `.`. Por ejemplo, si tenemos un objeto `a` de la clase `Stack`, podemos llamar a los métodos `a.push()`, `a.pop()` y `a.is_empty()`.

### Definición de Propiedades

El cuarto elemento es que se pueden definir propiedades de un objeto utilizando la palabra clave `self`. Por ejemplo, si queremos definir una propiedad `lista` en la clase `Stack`, esta propiedad se crea al asignarle un valor y puede ser accedida y modificada utilizando la notación de punto `.`.

Python permite acceder a las propiedades de un objeto desde fuera de la clase. Si bien esto es posible, no es recomendable ya que se pierde el encapsulamiento de los datos y la lógica. Es mejor definir métodos para acceder y modificar las propiedades de un objeto.

```python
a = Stack()
print(a.lista)  # Output: []
a.push(10)
a.push(20)
print(a.lista)  # Output: [10, 20]

a.lista.clear()  # Se puede acceder a la propiedad lista y modificarla directamente
print(a.is_empty())  # Output: True
```

El quinto elemento es que se pueden definir **métodos estáticos** y **de clase** en una clase. Un método estático es un método que no recibe el parámetro `self` y se puede llamar sin crear una instancia de la clase. Un método de clase es un método que recibe el parámetro `cls` en lugar de `self` y se puede llamar utilizando la clase en lugar de un objeto.

```python
class Stack:
    @staticmethod
    def is_empty_list(lista):
        return len(lista) == 0

    @classmethod
    def from_list(cls, lista):
        stack = cls()
        stack.lista = lista
        return stack

a = Stack.from_list([10, 20])
print(Stack.is_empty_list(a.lista))  # Output: False
```

Este tipo de métodos se usan para aprovechar que los nombres están definidos dentro de la clase y de esta manera no entran en conflicto con otros nombres definidos fuera de la clase. La distinción entre un método de clase y un método estático es sutil y se puede utilizar según la necesidad. Pero la idea es que se pueden llamar sin crear una instancia de la clase.

Nótese que en el método `from_list` se crea una instancia de la clase `Stack` y se inicializa la propiedad `lista` con el valor pasado como argumento. Este es un ejemplo de un método de clase que se utiliza para crear instancias de la clase.

### Decoradores en Clases

En ambos casos se usa un **decorador** para indicarle a Python el comportamiento especial del método. Los decoradores son una característica avanzada de Python que permite modificar el comportamiento de una función o método.

Otro decorador que se puede utilizar en una clase es `@property`. Este decorador se utiliza para definir propiedades de solo lectura en una clase. Por ejemplo, en lugar de usar un método para averiguar si una pila está vacía, podríamos usar una propiedad de solo lectura.

```python
class Stack:
    def __init__(self):
        self.lista = []

    def push(self, elemento):
        self.lista.append(elemento)

    def pop(self):
        return self.lista.pop()

    @property
    def empty(self):
        return len(self.lista) == 0

a = Stack()
a.push(10)
a.push(20)
while not a.empty:
    print(a.pop())
```

En este caso, la propiedad `empty` se define utilizando el decorador `@property` y se puede acceder a ella como si fuera un atributo de la clase. Sin embargo, no se puede modificar la propiedad `empty` directamente, ya que es de solo lectura.

Este concepto de propiedades de solo lectura es útil para definir propiedades que se calculan a partir de otras propiedades o métodos de la clase, pero también se puede usar para proteger propiedades de la clase de modificaciones no deseadas.

### Protección de Propiedades con Getters y Setters

Veamos un ejemplo de cómo usar propiedades para proteger el acceso a las propiedades de una clase.

Supongamos que tenemos que modelar un producto en una tienda y queremos asegurarnos de que el precio del producto sea siempre mayor que cero. Podríamos guardar el precio en una variable interna `_precio` y acceder al mismo a través de un método `get_precio` y modificarlo a través de un método `set_precio`. De esta manera, podemos controlar que el precio sea siempre mayor que cero.

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.set_precio(precio)

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.get_precio()}"

producto = Producto("Laptop", 1000)
print(producto)                # Output: Laptop: $1000
print(producto.get_precio())   # Output: 1000

producto.set_precio(1500)      # Modifica el precio del producto
print(producto)                # Output: Laptop: $1500
print(producto.get_precio())   # Output: 1500

# Si intentamos modificar el precio a un valor inválido, se lanza una excepción
# producto.set_precio(-1000)   # ValueError: El precio debe ser mayor que cero.
```

Esto soluciona el problema del acceso y modificación de las propiedades de la clase. Ahora el precio del producto es una propiedad protegida que solo se puede modificar a través del método `set_precio`. En realidad, se sigue pudiendo acceder a la propiedad `_precio` directamente, pero se desaconseja hacerlo. Python no tiene un mecanismo para proteger las propiedades de una clase de modificaciones no deseadas, pero usa la convención de que las propiedades que comienzan con un guion bajo `_` son privadas y no deben ser accedidas directamente.

Este patrón de diseño se llama **getter** y **setter** y se utiliza para controlar el acceso y la modificación de las propiedades de una clase. En Python, se puede utilizar el decorador `@property` para definir un getter y el decorador `@<nombre_propiedad>.setter` para definir un setter.

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

producto = Producto("Laptop", 1000)
print(producto)          # Output: Laptop: $1000
print(producto.precio)   # Output: 1000

producto.precio = 1500   # Modifica el precio del producto
print(producto)          # Output: Laptop: $1500
print(producto.precio)   # Output: 1500

# Si intentamos modificar el precio a un valor inválido, se lanza una excepción
# producto.precio = -1000  # ValueError: El precio debe ser mayor que cero.
```

Recuerda que en Python, las propiedades de una clase se pueden acceder y modificar directamente, pero es una buena práctica utilizar métodos getter y setter para controlar el acceso y la modificación de las propiedades de una clase. Mantenemos la elegancia del código y, a la vez, podemos proteger el acceso a las propiedades de la clase manteniendo el encapsulamiento.

Estos son algunos de los elementos básicos de la programación orientada a objetos en Python. La programación orientada a objetos es un paradigma de programación poderoso que permite modelar el mundo real de una manera más natural y reutilizable.

En los próximos capítulos, veremos cómo utilizar la programación orientada a objetos para resolver problemas más complejos y cómo aprovechar las características avanzadas de Python para crear aplicaciones más eficientes y organizadas.

## Repaso de las Ideas Principales

- La programación orientada a objetos es un paradigma de programación que se basa en el concepto de **objetos**, que son instancias de **clases**.
- Una **clase** es una plantilla que define las propiedades y los métodos de un objeto.
- Un **objeto** es una instancia de una clase y encapsula los datos y la lógica en una estructura coherente y reutilizable.
- Los objetos se crean utilizando la palabra clave `class` seguida del nombre de la clase y dos puntos `:`.
- Los **métodos** de una clase se definen utilizando la palabra clave `def` dentro de la clase y reciben un parámetro `self` que se refiere al objeto que se está manipulando.
- Las **propiedades** de un objeto se definen utilizando la palabra clave `self` y se pueden acceder y modificar utilizando la notación de punto `.`.
- Los **métodos estáticos** y **de clase** se definen utilizando los decoradores `@staticmethod` y `@classmethod`, respectivamente.
- El decorador `@property` se utiliza para definir propiedades de solo lectura en una clase. Con `@<nombre_propiedad>.setter` se define un setter para la propiedad.
- Los **métodos getter** y **setter** se utilizan para controlar el acceso y la modificación de las propiedades de una clase.
- La programación orientada a objetos es un paradigma poderoso que permite modelar el mundo real de una manera más natural y reutilizable.