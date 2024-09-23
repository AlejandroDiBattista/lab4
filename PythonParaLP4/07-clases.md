# Clases

En Python, una clase es un modelo que define las propiedades y comportamientos de un objeto. Las clases permiten crear objetos que comparten las mismas características y comportamientos.

## Definición de clases

En Python, una clase se define utilizando la palabra clave `class`, seguida del nombre de la clase y dos puntos `:`. Por ejemplo:

```python
class Persona:
    pass
```

En el ejemplo anterior, se ha definido una clase llamada `Persona` que no tiene ninguna propiedad ni comportamiento definido. La palabra clave `pass` se utiliza en Python para indicar que no hay ninguna instrucción en el bloque de código.

## Creación de objetos

Un objeto es una instancia de una clase. Para crear un objeto en Python, se utiliza el nombre de la clase seguido de paréntesis `()`. Por ejemplo:

```python
juan = Persona()
```

En el ejemplo anterior, se ha creado un objeto de la clase `Persona` y se ha asignado a la variable `juan`.

## Propiedades de los objetos

Las propiedades de un objeto son variables que almacenan información específica de cada objeto. Para definir las propiedades de un objeto en Python, se utilizan los métodos especiales `__init__` y `self`. Por ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

En el ejemplo anterior, se ha definido un método `__init__` que recibe dos parámetros `nombre` y `edad` y asigna estos valores a las propiedades `nombre` y `edad` del objeto utilizando la palabra clave `self`.

## Métodos de los objetos

Los métodos de un objeto son funciones que definen el comportamiento de un objeto. Para definir un método en Python, se utiliza la palabra clave `def` dentro de la clase. Por ejemplo:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
```

En el ejemplo anterior, se ha definido un método `saludar` que imprime un saludo con el nombre y la edad del objeto.

## Uso de objetos

Para utilizar un objeto en Python, se llama a sus métodos y se accede a sus propiedades utilizando la notación de punto `.`. Por ejemplo:

```python
juan = Persona("Juan", 30)
juan.saludar()  # Output: Hola, me llamo Juan y tengo 30 años.
```

En el ejemplo anterior, se ha creado un objeto `juan` de la clase `Persona` con el nombre `"Juan"` y la edad `30`, y se ha llamado al método `saludar` del objeto `juan`.

Las clases y los objetos son conceptos fundamentales en la programación orientada a objetos y permiten modelar el mundo real de una manera más eficiente y organizada.

## Herencia

La herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente. La nueva clase hereda las propiedades y métodos de la clase existente y puede añadir nuevas propiedades y métodos o modificar los existentes.

En Python, la herencia se define colocando el nombre de la clase base entre paréntesis después del nombre de la clase derivada. Por ejemplo:

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print(f"Estoy estudiando la carrera de {self.carrera}.")
```

En el ejemplo anterior, se ha definido una clase `Estudiante` que hereda de la clase `Persona` y añade una nueva propiedad `carrera` y un nuevo método `estudiar`.

## Polimorfismo

El polimorfismo es un concepto que permite que un objeto pueda comportarse de diferentes maneras según el contexto en el que se utilice. En Python, el polimorfismo se logra mediante el uso de métodos con el mismo nombre en diferentes clases.

Por ejemplo, si se define un método `saludar` en la clase `Persona` y en la clase `Estudiante`, cada clase puede tener su propia implementación del método `saludar`.

```python
class Persona:
    def saludar(self):
        print("Hola, soy una persona.")

class Estudiante(Persona):
    def saludar(self):
        print("Hola, soy un estudiante.")
```

En el ejemplo anterior, se ha definido un método `saludar` en las clases `Persona` y `Estudiante` con implementaciones diferentes.

El polimorfismo permite que un objeto pueda ser tratado como un objeto de su clase base o de una clase derivada, lo que facilita la reutilización del código y la creación de programas más flexibles y escalables.

## Encapsulamiento

El encapsulamiento es un concepto que permite ocultar los detalles de implementación de un objeto y exponer solo la interfaz pública. En Python, el encapsulamiento se logra utilizando métodos y propiedades privadas.

Para definir una propiedad o método privado en Python, se utiliza un guion bajo `_` al principio del nombre. Luego se utiliza el decorador `@property` para definir un método getter y el decorador `@nombre.setter` para definir un método setter.


# Veamos un ejemplo de estos conceptos

Supongamos que queremos modelar un producto en una tienda. Podríamos crear una clase `Producto` con las propiedades `nombre`, `precio` y `cantidad`, y un método `total` que calcule el precio total del producto.

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def total(self):
        return self._precio * self._cantidad

    def __str__(self):
        return f"{self._nombre} - ${self._precio:.2f} * {self._cantidad}u = ${self.total:.2f}"

producto = Producto("Leche", 2.50, 3)
print(producto)  # Output: Leche - $2.50 * 3u = $7.50

print(producto.nombre)  # Output: Leche
print(producto.precio)  # Output: 2.50
print(producto.cantidad)  # Output: 3
print(producto.total)  # Output: 7.50

```

Este este caso creamos lo que se conoce como un objeto inmutable, ya que no se pueden modificar sus propiedades una vez creado. El encapsulamiento permite proteger los datos de un objeto y garantizar que solo se puedan acceder y modificar a través de métodos específicos.

Si quisieramos modificar el precio y la cantidad de un producto pero que la misma no permita valores invalidos, podríamos hacerlo de la siguiente forma:

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter # Utilizamos el decorador setter para modificar el precio en forma segura
    def precio(self, nuevo_precio):
        if nuevo_precio < 0: # Validamos que el precio no sea negativo
            raise ValueError("El precio no puede ser negativo.")

        self._precio = nuevo_precio

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter # Utilizamos el decorador setter para modificar la cantidad en forma segura
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0: # Validamos que la cantidad no sea negativa
            raise ValueError("La cantidad no puede ser negativa.")

        self._cantidad = nueva_cantidad

    @property
    def total(self):
        return self._precio * self._cantidad

    def __str__(self):
        return f"{self._nombre} - ${self._precio:.2f} * {self._cantidad}u = ${self.total:.2f}"

   
```

En este caso, hemos agregado los decoradores `@precio.setter` y `@cantidad.setter` para modificar el precio y la cantidad de un producto de forma segura. Si se intenta asignar un valor negativo al precio o a la cantidad, se lanzará una excepción `ValueError` indicando que el valor no es válido.

Ahora supongamos que queremos modelar un producto que tenga un descuento. Podríamos crear una clase `ProductoDescuento` que herede de la clase `Producto` y añada una propiedad `descuento` y un método `total_descuento` que calcule el precio total con descuento.

```python
class ProductoDescuento(Producto):                  # Heredamos de la clase Producto
    def __init__(self, nombre, precio, cantidad, descuento):
        super().__init__(nombre, precio, cantidad)  # Llamamos al constructor de la clase base
        self._descuento = descuento

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter   # Utilizamos el decorador setter para modificar el descuento en forma segura
    def descuento(self, nuevo_descuento):   
        if nuevo_descuento < 0 or nuevo_descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        self._descuento = nuevo_descuento

    @property       # Calculamos el total con descuento
    def total_descuento(self):
        return super().total * (1 - self._descuento / 100) # super() nos permite acceder a el total de producto
 
    @property
    def total(self):    # Sobreescribimos el método total para incluir el descuento
        return super().total - self.total_descuento # super() nos permite acceder a los métodos de la clase base

    def __str__(self):
        return f"{self.nombre:10} - ${self.precio:.2f} * {self.cantidad}u = ${super().total:.2f} - {self._descuento}% = ${self.total:.2f}"
    
producto_descuento = ProductoDescuento("Leche", 2.50, 3, 10)
print(producto_descuento)        # Output: Leche      - $2.50 * 3u = $7.50 - 10% = $0.75

print(producto_descuento.total)  # Output: 6.75
print(producto_descuento.total_descuento)  # Output: 0.75
```

En este caso, hemos creado una clase `ProductoDescuento` que hereda de la clase `Producto` y añade una nueva propiedad `descuento` y un nuevo método `total_descuento` que calcula el precio total con descuento. Además, hemos sobrescrito el método `total` para incluir el descuento en el cálculo del precio total.

El encapsulamiento, la herencia, el polimorfismo y la composición son conceptos fundamentales de la programación orientada a objetos que permiten crear programas más flexibles, escalables y fáciles de mantener. Estos conceptos nos permiten modelar el mundo real de una manera más eficiente y organizada, y nos ayudan a reutilizar código y evitar la repetición de código.

El encapsulamiento nos permite proteger los datos de un objeto y garantizar que solo se puedan acceder y modificar a través de métodos específicos. 

La herencia nos permite crear una nueva clase a partir de una clase existente y heredar las propiedades y métodos de la clase base. 

El polimorfismo nos permite que un objeto pueda comportarse de diferentes maneras según el contexto en el que se utilice. 

Ahora supongamos que queremos modelas una tienda que tiene una coleccion de productos. Podríamos crear una clase `Tienda` que tenga una lista de productos y métodos para agregar, eliminar y mostrar los productos de la tienda.

```python
class Tienda:
    def __init__(self):
        self._productos = []

    def agregar(self, producto):
        self._productos.append(producto)

    def eliminar(self, producto):
        self._productos.remove(producto)

    def mostrar(self):
        print("Productos en la tienda:")
        for producto in self._productos:
            print(" ", producto)

tienda = Tienda()
tienda.agregar(Producto("Leche", 2.50, 3))
tienda.agregar(ProductoDescuento("Pan", 1.50, 5, 20))
tienda.mostrar()
# Output:
# Productos en la tienda:
#   Leche     - $2.50 * 3u = $7.50
#   Pan       - $1.50 * 5u = $7.50 - 20% = $6.00

```

En este caso, hemos creado una clase `Tienda` que tiene una lista de productos y métodos para agregar, eliminar y mostrar los productos de la tienda. Hemos agregado un producto de tipo `Producto` y un producto de tipo `ProductoDescuento` a la tienda y hemos mostrado los productos en la tienda.

La composición nos permite combinar objetos de diferentes clases para crear objetos más complejos y completos. En este caso, hemos combinado objetos de las clases `Producto` y `ProductoDescuento` en la clase `Tienda` para modelar una tienda que tiene una colección de productos.

Decimos que la tienda esta compuesta por productos porque usa objetos de la clase Producto y ProductoDescuento para modelar su comportamiento. La composición nos permite crear objetos más complejos y completos combinando objetos más simples y reutilizables.

Una observación importante es que gracias a la herencia y al polimorfismo, podemos tratar a los objetos de las clases `Producto` y `ProductoDescuento` de la misma manera en la clase `Tienda`, ya que ambas clases comparten la misma interfaz pública. Esto nos permite reutilizar el código y crear programas más flexibles y escalables.

Esto nos permitia agregar productos de diferentes tipos a la tienda y mostrarlos de la misma manera, independientemente de si son productos normales o productos con descuento. Esto nos permite reutilizar el código y crear programas más flexibles y escalables.

Agregemos una nueva oferta, esta fue creada despues que se creo la tienda pero podemos usarla en la tienda si problema. Por ejemplo agregemos 2x1 como oferta.

```python
class Producto2x1(ProductoOferta):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad, 100) # 100% de descuento en la segunda unidad o 2x1 
        self._cantidad_minima = 2   # Cantidad minima para aplicar la oferta

    @property
    def descuento(self):
        if self._cantidad < self._cantidad_minima:
            return 0
        
        return self._descuento * (self._cantidad // self._cantidad_minima)

    @descuento.setter
    def descuento(self, nuevo_descuento):
        raise ValueError("No se puede modificar el descuento de un producto 2x1.")

```

Ahora podemo usar la tienda para agregar productos de tipo `Producto2x1` y mostrarlos de la misma manera que los otros productos.

```python
tienda.agregar(Producto2x1("Galletas", 1.00, 3))
tienda.mostrar()

# Output:
# Productos en la tienda:
#   Leche     - $2.50 * 3u = $7.50
#   Pan       - $1.50 * 5u = $7.50 - 20% = $6.00
#   Galletas  - $1.00 * 3u = $3.00 - 1.00 = $2.00
```

En este caso, hemos creado una clase `Producto2x1` que hereda de la clase `ProductoOferta` y añade una nueva propiedad `cantidad_minima` que indica la cantidad mínima de unidades para aplicar la oferta 2x1. Hemos sobrescrito el método `descuento` para calcular el descuento de la oferta 2x1 y el método `total` para incluir el descuento en el cálculo del precio total.

