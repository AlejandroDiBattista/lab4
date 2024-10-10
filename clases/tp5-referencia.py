# %% [markdown]
# ## Productos
# - `codigo`: 4 digitos
# - `nombre`: 1 a 100 caracteres
# - `precio`: 10 a 10000
# - `tipo`: 0 a 20 caracteres
# - `cantidad`: 0 a 100 

# %%
class Producto:
    def __init__(self, codigo, nombre, precio, tipo, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo   = tipo
        self.cantidad = cantidad
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        if 10 <= precio <= 10000: self._precio = precio
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        if 0 <= cantidad <= 100 : self._cantidad = cantidad
    
    @property
    def valorTotal(self):
        return self.precio * self.cantidad


# %%
## NO MODIFIQUE ESTE CODIGO ##

# Prueba de la clase Producto

p1 = Producto('0001', 'Coca Cola', 1500, 'gaseosa', 10)

assert p1.codigo == '0001'
assert p1.nombre == 'Coca Cola'
assert p1.precio == 1500

# Calcula el valor total 
assert p1.valorTotal == 15000 

# Asegura que los valores de precio y cantidad sean validos
p1.precio = -200
assert p1.precio == 1500    # Rechaza el valor negativo

p1.precio = 2000 
assert p1.precio == 2000

p1.cantidad = -5
assert p1.cantidad == 10    # Rechaza el valor negativo

p1.cantidad = 50
assert p1.cantidad == 50
assert p1.valorTotal == 100000

print("Prueba pasada exitosamente!")

# %% [markdown]
# # Ofertas
# Debe permitir aplicar oferctas a codigos espeficicos de productos y a tipos de productos
# - `descripcion`: 1 a 100 caracteres
# - `codigos`: lista de codigos de productos
# - `tipos`: lista de tipo de producto
# - `esAplicable(producto, cantidad)`: retorna si la oferta es aplicable a ese producto
# - `calcularDescuento(producto, cantidad)`: calcula el descuento que se aplica a ese producto
# 

# %%
class Oferta:
    def __init__(self,descripcion, codigos = None, tipos = None):
        self.descripcion = descripcion
        self.codigos = codigos if codigos else []
        self.tipos   = tipos if tipos else []

    def esAplicable(self, producto, cantidad):
        return producto.codigo in self.codigos or producto.tipo in self.tipos
    
    def calcularDescuento(self, producto, cantidad):
        return 0


class OfertaDescuento(Oferta):
    def __init__(self, descuento, *args, **kwargs):
        super().__init__(f"Descuento {descuento}%", *args, **kwargs)
        self.descuento = descuento

    def calcularDescuento(self, producto, cantidad):
        if not self.esAplicable(producto, cantidad): return 0
        return producto.precio * cantidad * (self.descuento / 100)
    
    
class Oferta2x1(Oferta):
    def __init__(self, *args, **kwargs):
        super().__init__("Oferta 2x1", *args, **kwargs)
        
    def esAplicable(self, producto, cantidad):
        return super().esAplicable(producto, cantidad) and cantidad >= 2
    
    def calcularDescuento(self, producto, cantidad):
        if not self.esAplicable(producto, cantidad): return 0
        return producto.precio * (cantidad // 2)

# %%
## NO MODIFICAR ESTE CODIGO ##

p1 = Producto('1234', 'Coca Cola', 1000, 'gaseosa', 10)
p2 = Producto('1235', 'Oreo',      2300, 'galleta', 10)

o10d = OfertaDescuento(10, codigos=['1234'])
assert o10d.calcularDescuento(p1, 10) == 1000 
assert o10d.calcularDescuento(p1, 1) == 100

assert o10d.calcularDescuento(p2, 10) == 0

o2x1 = Oferta2x1(tipos=['galleta'])
assert o2x1.calcularDescuento(p1, 10) == 0

assert o2x1.calcularDescuento(p2, 1) == 0
assert o2x1.calcularDescuento(p2, 2) == 2300
assert o2x1.calcularDescuento(p2, 3) == 2300
assert o2x1.calcularDescuento(p2, 4) == 4600
assert o2x1.calcularDescuento(p2, 5) == 4600

print("Prueba pasada exitosamente!")

# %% [markdown]
# # Catalogo
# - `leer(archivo) `    : Carga los productos desde el archivo
# - `guardar(archivo)`  : Guarda los productos en el archivo
# - `agregar(producto)` : Agrega un producto al catalogo
# - `buscar(codigo)`    : Busca un producto por codigo o None si no existe
# - `registrarOferta(oferta)`  : Registra una oferta
# - `buscarOferta(producto, cantidad)`: Busca una oferta por codigo o None si no existe
# - `calcularDescuento(producto, cantidad)`: Calcula el descuento de una oferta
# - `cantidadProductos`: Retorna la cantidad de productos en el catalogo
# - `cantidadUnidades`: Retorna la cantidad de unidades en el catalogo
# - `valorTotal`: retorna el valor total del catalogo sin descuentos
# - `informe()`: retorna un string con el informe del catalogo 

# %%
from collections import defaultdict

class Catalogo:
    def __init__(self):
        self.productos = []
        self.ofertas   = []

    @staticmethod
    def leer(origen):
        catalogo = Catalogo()
        with open(origen) as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:]:
                codigo, nombre, precio, tipo, cantidad = linea.strip().split(',')
                producto = Producto(codigo, nombre, float(precio), tipo, int(cantidad))
                catalogo.agregar(producto)
            return catalogo
    
    def guardar(self, destino): 
        with open(destino, 'w') as archivo:
            archivo.write("codigo,nombre,precio,tipo,cantidad\n")
            for producto in self.productos:
                archivo.write(f"{producto.codigo},{producto.nombre},{producto.precio},{producto.tipo},{producto.cantidad}\n")

    def agregar(self, *productos):
        self.productos.extend(productos)

    def vender(self, producto, cantidad): 
        producto.cantidad -= cantidad

    def buscar(self, codigo): 
        for producto in self.productos:
            if producto.codigo == codigo: 
                return producto
        return None

    def registrarOferta(self, oferta): 
        self.ofertas.append(oferta)
    
    def buscarOfertas(self, producto, cantidad):
        for oferta in self.ofertas:
            if oferta.esAplicable(producto, cantidad):
                return oferta
        return None 
    
    def calcularDescuento(self, producto, cantidad):
        oferta = self.buscarOfertas(producto, cantidad)
        if oferta: 
            return oferta.calcularDescuento(producto, cantidad)
        return 0
    
    @property 
    def cantidadProductos(self): 
        return len(self.productos)

    @property 
    def cantidadUnidades(self): 
        return sum(producto.cantidad for producto in self.productos) 

    @property
    def valorTotal(self): 
        return sum(producto.valorTotal for producto in self.productos)
    
    def informe(self):

        tipos = defaultdict(lambda: {'unidades': 0, 'total': 0})

        for producto in self.productos:
            tipos[producto.tipo]['unidades'] += producto.cantidad
            tipos[producto.tipo]['total']    += producto.precio * producto.cantidad

        informe_tipos = "\n".join(
            f"  - {tipo:20}: {d['unidades']:3}u x ${d['total'] / d['unidades']:8.2f}" for tipo, d in tipos.items()
        )

        ofertas = "\n".join(f"  - {oferta.descripcion}" for oferta in self.ofertas)
# INFORME CATALOGO 
# Cantidad de productos:   <cantidad productos>
# Cantidad de unidades:    <cantidad unidades>
# Precio promedio:       $ <precio promedio>
# Valor total:           $ <valor total>
# Tipos de productos: 
#   - <tipo>              :  <unidades>u x $ <precio promedio>
#   - ...
# Ofertas:
#   - <descripción oferta>
#   - ...
        return f"""
INFORME CATALOGO 
Cantidad de productos:  {self.cantidadProductos:10}
Cantidad de unidades:   {self.cantidadUnidades:10}
Precio Promedio:       ${self.valorTotal / self.cantidadUnidades:10.2f}
Valor total:           ${self.valorTotal:10.2f}
Tipos de productos: 
{informe_tipos}
Ofertas:
{ofertas}
"""

# %%
## NO MODIFIQUE ESTE CODIGO ##

# Prueba del catálogo 

catalogo = Catalogo()
p1 = Producto('0001', 'Coca Cola',  1500, 'gaseosa', 10)
p2 = Producto('0002', 'Pepsi Cola', 1200, 'gaseosa', 20)
p3 = Producto('0003', 'Sonrisa',    1200, 'galleta', 30)
p4 = Producto('0004', 'Oreo',       2300, 'galleta', 40)

## Agregar productos al catalogo 
catalogo.agregar(p1)
catalogo.agregar(p2)
catalogo.agregar(p3)
catalogo.agregar(p4)

assert catalogo.cantidadProductos == 4
assert catalogo.cantidadUnidades  == 100

assert catalogo.valorTotal == 167000

## Calcular descuentos segun las ofertas registradas
assert catalogo.calcularDescuento(p1, 5) == 0
assert catalogo.calcularDescuento(p2, 5) == 0

# Ofertas no acumulables 
catalogo.registrarOferta(Oferta2x1(tipos=['galleta']))
catalogo.registrarOferta(OfertaDescuento(10, codigos=['0001', '0003']))

assert catalogo.calcularDescuento(p1, 5) == 750
assert catalogo.calcularDescuento(p2, 5) == 0
assert catalogo.calcularDescuento(p3, 5) == 2400

assert catalogo.valorTotal == 167000.0
catalogo.guardar('catalogo-prueba.csv') ## Guardar datos antes de vender

# Vender afecta la cantidad de unidades y el valor total
catalogo.vender(p3, 3)   

# Verificar que el informe se genere correctamente

informe = catalogo.informe()
assert "Cantidad de productos: " in informe
assert "Cantidad de unidades: "  in informe
assert "Precio Promedio: "       in informe
assert "Valor total: "           in informe
assert "Tipos de productos: "    in informe
assert "gaseosa"                 in informe
assert "galleta"                 in informe
assert "Ofertas:"                in informe 
assert "Oferta 2x1"              in informe
assert catalogo.cantidadUnidades == 97
assert catalogo.valorTotal == 163400

# Buscar por código
assert catalogo.buscar('0001') == p1
assert catalogo.buscar('0002') == p2
assert catalogo.buscar('0099') is None 

# Recuperar los datos guardados  
c2 = Catalogo.leer('catalogo-prueba.csv')

assert c2.cantidadProductos == 4
assert c2.cantidadUnidades == 100

# Valor antes de guardar
assert c2.valorTotal == 167000.0
print(catalogo.informe())
print("Prueba pasada exitosamente!")

# %% [markdown]
# # Cliente
# - `nombre`: 1 a 100 caracteres
# - `cuit`: 11 digitos
# 

# %%
class Cliente: 
    def __init__(self, nombre, cuit):
        self.nombre = nombre
        self.cuit = cuit
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor:
            self._nombre = valor

    @property
    def cuit(self):
        return self._cuit

    @cuit.setter
    def cuit(self, valor):
        partes = valor.split('-')
        # if re.match(r'^\d{2}-\d{8}-\d{1}$', valor):
        if (len(partes) == 3 and # 
            partes[0].isdigit() and len(partes[0]) == 2 and 
            partes[1].isdigit() and len(partes[1]) == 8 and 
            partes[2].isdigit() and len(partes[2]) == 1):
            self._cuit = valor


# %%
## NO MODIFICAR ESTE CODIGO ##

# Prueba de la clase Cliente #

c1 = Cliente('Juan Perez', '20-12345678-1')

assert c1.nombre == 'Juan Perez'
assert c1.cuit   == '20-12345678-1'

c1.nombre = ''
assert c1.nombre == 'Juan Perez' # Rechaza el valor vacio

c1.nombre = 'Juana Perez'        # Acepta el nuevo valor
assert c1.nombre == 'Juana Perez'

# CUIT debe tener el formato correcto
# 13 digitos, con guiones en las posiciones correctas

c1.cuit = '1234567890123'
assert c1.cuit == '20-12345678-1' # Debe tener los giones

c1.cuit = 'CC-12345678-1'
assert c1.cuit == '20-12345678-1' # Solo números y guiones

print("Prueba pasada exitosamente!")

# %%
import datetime  as dt 

class Factura:
    ultimoNumero = 0

    @staticmethod
    def ultimaFactura(inicial):
        Factura.ultimoNumero = inicial
    
    @staticmethod
    def nuevoNumero():
        Factura.ultimoNumero += 1
        return Factura.ultimoNumero
        
    def __init__(self, catalogo, cliente):
        self.numero   = Factura.nuevoNumero()
        self.fecha    = dt.datetime.now()
        self.catalogo = catalogo
        self.cliente  = cliente
        self.items    = []

    def agregar(self, producto, cantidad): 
        for item in self.items:
            if item[0].codigo == producto.codigo:
                item[1] += cantidad
                break
        else:
            self.items.append([producto, cantidad])
        producto.cantidad -= cantidad

    @property
    def cantidadProductos(self): 
        return len(self.items)
    
    @property
    def cantidadUnidades(self): 
        return sum([cantidad for _, cantidad in self.items])

    @property
    def subtotal(self): 
        return sum(producto.precio * cantidad for producto, cantidad in self.items)
    
    @property
    def descuentos(self): 
        return sum(catalogo.calcularDescuento(producto, cantidad) for producto, cantidad in self.items)
    
    @property
    def total(self): 
        return self.subtotal - self.descuentos

    def imprimir(self): 
        items = []
        for item in self.items:
            producto, cantidad = item
            descuento = self.catalogo.calcularDescuento(producto, cantidad)
            
            items.append(f"- {cantidad:2} {producto.nombre:20}  x ${producto.precio:8.2f} = ${producto.precio * cantidad:8.2f}")
            
            oferta = self.catalogo.buscarOfertas(producto, cantidad)
            if oferta is not None: 
                descuento = oferta.calcularDescuento(producto, cantidad)
                items.append(f"     {oferta.descripcion:32}  - ${descuento:8.2f}")
            items.append('')
# Factura: <numero>
# Fecha  : <fecha>
# Cliente: <nombre cliente> (<CUIT>)

# - <cantidad>u <nombre producto>            x $<precio> = $<subtotal>
#       <descripción oferta>                             - $<descuento>
# - ...

#                                              Subtotal:   $<subtotal general>
#                                              Descuentos: $<total descuentos>
#                                              -----------------------
#                                              Total:      $<total>

        return f"""
Factura: {self.numero}
Fecha  : {self.fecha:%d/%m/%Y %H:%M:%S}
Cliente: {self.cliente.nombre} ({self.cliente.cuit})

{'\n'.join(items)}
                           Subtotal:     ${self.subtotal:8.2f}
                           Descuentos: - ${self.descuentos:8.2f}
                           -----------------------
                           TOTAL:        ${self.total:8.2f}
"""

# %%
## NO MODIFICAR ESTE CODIGO ##
# Prueba de la clase Factura

# Creo un catalogo con productos
catalogo = Catalogo()
p1 = Producto('0001', 'Coca Cola',  1500, 'gaseosa', 10)
p2 = Producto('0002', 'Pepsi Cola', 1200, 'gaseosa', 20)
p3 = Producto('0003', 'Sonrisa',    1200, 'galleta', 30)
p4 = Producto('0004', 'Oreo',       2300, 'galleta', 40)
catalogo.agregar(p1,p2,p3,p4)

# Registro ofertas
catalogo.registrarOferta(Oferta2x1(tipos=['galleta']))
catalogo.registrarOferta(OfertaDescuento(10, codigos=['0001', '0003']))

# Creo un cliente
cliente = Cliente('Juan Perez', '20-12345678-9')

# Creo una factura
Factura.ultimaFactura(100)
assert Factura.nuevoNumero() == 101
assert Factura.nuevoNumero() == 102

f1 = Factura(catalogo, cliente)
f1.agregar(p1, 5)
f1.agregar(p3, 3)

assert f1.numero == 103
assert f1.cantidadProductos == 2
assert f1.cantidadUnidades  == 8

# Agrega unidades de un producto ya agregado
f1.agregar(p1, 5)
assert f1.cantidadProductos == 2
assert f1.cantidadUnidades == 13

assert f1.subtotal   == 18600
assert f1.descuentos == 2700.0
assert f1.total == 15900.0

impresion = f1.imprimir()

assert "Juan Perez"    in impresion
assert "10 Coca Cola"  in impresion
assert "Sonrisa"       in impresion
assert "Descuento 10%" in impresion
assert "Oferta 2x1"    in impresion
assert "TOTAL:"        in impresion
assert "15900.00"      in impresion

print("Prueba pasada exitosamente!")

# %%
## NO MODIFICAR ESTE CODIGO ##

# Prueba de integración #

# Cargamos los datos
catalogo = Catalogo.leer('catalogo.csv')
juan  = Cliente('Juan Perez', '20-12345678-9')
maria = Cliente('Maria Lopez', '27-87654321-3')

o2x1 = Oferta2x1(tipos=['galleta'], codigos=['0002', '0003','0010'])
od20 = OfertaDescuento(20, codigos=['0001', '0002'], tipos=['gaseosa', 'arroz'])
od10 = OfertaDescuento(10, tipos=['fideo'])

catalogo.registrarOferta(o2x1)
catalogo.registrarOferta(od20)
catalogo.registrarOferta(od10)

# Controlo que la carga este correcta
assert catalogo.cantidadProductos == 30
assert catalogo.cantidadUnidades == 1000
assert catalogo.valorTotal == 2000000

Factura.ultimaFactura(10000)

# Crear una factura
f1 = Factura(catalogo, juan)
f1.agregar(catalogo.buscar('0001'), 5)
f1.agregar(catalogo.buscar('0002'), 3)
f1.agregar(catalogo.buscar('0003'), 2)

assert f1.numero == 10001
assert f1.cantidadProductos == 3
assert f1.cantidadUnidades == 10
assert f1.subtotal == 13450.0
assert f1.descuentos == 3890.0
assert f1.total == 9560.0

assert catalogo.cantidadUnidades == 990

f2 = Factura(catalogo, maria)
f2.agregar(catalogo.buscar('0010'), 5)
f2.agregar(catalogo.buscar('0010'), 3)
f2.agregar(catalogo.buscar('0020'), 2)
f2.agregar(catalogo.buscar('0030'), 2)

assert f2.numero == 10002
assert f2.cantidadProductos == 3
assert f2.cantidadUnidades == 12
assert f2.subtotal == 23900.00
assert f2.descuentos == 8860.00
assert f2.total == 15040.00

assert catalogo.cantidadUnidades == 978

print("Prueba pasada exitosamente!")


