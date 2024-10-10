# Introducción a la Librería Pandas en Python

**Pandas** es una de las librerías más populares de Python para el análisis de datos. Ofrece estructuras de datos y funciones de alto nivel que facilitan la manipulación y análisis de grandes cantidades de información. Con Pandas, es sencillo leer, modificar, analizar y almacenar conjuntos de datos de una manera eficiente.

Pandas está construido sobre **NumPy**, lo cual significa que hereda la eficiencia y las capacidades matemáticas que caracterizan a NumPy. La librería se organiza alrededor de dos estructuras principales:

1. **Series**: Son arreglos unidimensionales, similares a listas o arreglos de NumPy, pero con la capacidad adicional de contar con un índice que facilita el acceso y la manipulación de datos.
2. **DataFrames**: Son estructuras bidimensionales (similares a una hoja de cálculo), que contienen tanto filas como columnas, y permiten un manejo más complejo y estructurado de los datos.

En este apunte, comenzaremos con **Series**, aprendiendo qué son, cómo crearlas y cómo realizar operaciones básicas con ellas.

## ¿Qué es una Serie en Pandas?

Una **Serie** es una estructura de datos unidimensional que puede almacenar datos de cualquier tipo (números, texto, booleanos, etc.). Cada elemento en una Serie tiene un **índice**, que sirve para identificar de forma única cada elemento dentro de ella. Esto es útil cuando se trabaja con datos reales, como el precio de una acción en ciertos días o las temperaturas diarias de una ciudad.

### Creación de Series

Podemos crear una Serie a partir de diferentes tipos de datos, como listas, diccionarios o incluso arreglos de NumPy. Para ello, primero debemos importar la librería Pandas:

```python
import pandas as pd
```

Veamos algunas formas de crear una Serie:

#### Creación a partir de una lista

Podemos pasar una lista directamente a la función `pd.Series()`:

```python
import pandas as pd

# Crear una Serie a partir de una lista de números
datos = [10, 20, 30, 40, 50]
serie_numerica = pd.Series(datos)
print(serie_numerica)
```

**Salida**:

```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

En este caso, la Serie tiene un índice numérico por defecto que comienza en 0.

#### Creación a partir de un diccionario

Podemos crear una Serie a partir de un diccionario, donde las claves se convierten en los **índices** y los valores se convierten en los elementos de la Serie:

```python
# Crear una Serie a partir de un diccionario
estudiantes = {'Juan': 85, 'Ana': 90, 'Pedro': 78}
serie_estudiantes = pd.Series(estudiantes)
print(serie_estudiantes)
```

**Salida**:

```
Juan     85
Ana      90
Pedro    78
dtype: int64
```

En este caso, los nombres de los estudiantes son los índices de la Serie.

### Índices en una Serie

Los **índices** permiten acceder a los elementos de una Serie de forma sencilla. Podemos definir nuestros propios índices al crear la Serie:

```python
# Crear una Serie con índices personalizados
ciudades = ['Buenos Aires', 'Córdoba', 'Rosario']
poblacion = [2890000, 1391000, 948000]
serie_ciudades = pd.Series(poblacion, index=ciudades)
print(serie_ciudades)
```

**Salida**:

```
Buenos Aires    2890000
Córdoba         1391000
Rosario          948000
dtype: int64
```

Aquí, cada ciudad es un índice que está asociado con su población.

### Acceso a elementos en una Serie

Podemos acceder a los elementos de una Serie utilizando su **índice** o su **posición**:

- **Por índice**:

```python
# Acceder al valor de Córdoba
print(serie_ciudades['Córdoba'])
```

**Salida**:

```
1391000
```

- **Por posición** (similar a una lista o arreglo):

```python
# Acceder al segundo elemento (posición 1)
print(serie_ciudades[1])
```

**Salida**:

```
1391000
```

También podemos acceder a un **subconjunto** de elementos utilizando una lista de índices:

```python
# Acceder a los valores de Buenos Aires y Rosario
print(serie_ciudades[['Buenos Aires', 'Rosario']])
```

**Salida**:

```
Buenos Aires    2890000
Rosario          948000
dtype: int64
```

### Slicing en Series

Podemos utilizar **slicing** para acceder a un rango de elementos en una Serie, ya sea por **posición** o por **índice**:

- **Slicing por posición**: Al igual que en una lista, podemos usar el operador de dos puntos `:` para acceder a un rango de posiciones.

```python
# Acceder a los elementos desde la posición 0 hasta la 1 (sin incluir la posición 2)
slice_posicion = serie_ciudades[0:2]
print(slice_posicion)
```

**Salida**:

```
Buenos Aires    2890000
Córdoba         1391000
dtype: int64
```

- **Slicing por índice**: Podemos también utilizar valores de índices personalizados para hacer slicing.

```python
# Acceder a los elementos desde 'Buenos Aires' hasta 'Córdoba'
slice_indices = serie_ciudades['Buenos Aires':'Córdoba']
print(slice_indices)
```

**Salida**:

```
Buenos Aires    2890000
Córdoba         1391000
dtype: int64
```

Es importante notar que, a diferencia del slicing por posición, el slicing por índice **incluye** el índice final especificado.

### Operaciones Básicas con Series

Las Series soportan operaciones similares a las de los arreglos de NumPy. Veamos algunas operaciones básicas:

#### Operaciones aritméticas

Podemos realizar operaciones aritméticas directamente sobre las Series:

```python
# Incrementar la población en un 10%
poblacion_incrementada = serie_ciudades * 1.10
print(poblacion_incrementada)
```

**Salida**:

```
Buenos Aires    3179000.0
Córdoba         1530100.0
Rosario         1042800.0
dtype: float64
```

#### Aplicación de funciones

Podemos aplicar funciones como `sum()`, `mean()`, etc. para obtener información útil sobre los datos:

```python
# Sumar todas las poblaciones
total_poblacion = serie_ciudades.sum()
print(f"Población total: {total_poblacion}")
```

**Salida**:

```
Población total: 5229000
```

Estas operaciones nos permiten realizar análisis de datos de manera eficiente y sencilla.

### Métodos Avanzados para Manipular Series

#### Series.apply

El método `apply()` permite aplicar una función sobre los valores de una Serie. Es muy útil cuando se necesita transformar o manipular los datos de una manera personalizada.

```python
# Aplicar una función lambda para aumentar cada valor en un 5%
aumento = serie_ciudades.apply(lambda x: x * 1.05)
print(aumento)
```

**Salida**:

```
Buenos Aires    3034500.0
Córdoba         1460550.0
Rosario          995400.0
dtype: float64
```

#### Series.agg

Los métodos `agg()` y `aggregate()` permiten realizar una o varias operaciones de agregación sobre una Serie. Podemos pasar una función o una lista de funciones.

```python
# Calcular la suma y la media de la Serie
resultado = serie_ciudades.agg(['sum', 'mean'])
print(resultado)
```

**Salida**:

```
sum     5229000.0
mean    1743000.0
dtype: float64
```

#### Series.transform

El método `transform()` permite aplicar una función sobre la Serie y devolver una Serie del mismo tamaño. Es útil cuando se necesita transformar los datos, pero manteniendo la misma estructura.

```python
# Transformar cada valor a su logaritmo natural
import numpy as np
transformada = serie_ciudades.transform(np.log)
print(transformada)
```

**Salida**:

```
Buenos Aires    14.878101
Córdoba         14.146659
Rosario         13.764979
dtype: float64
```

#### Series.map

El método `map()` permite aplicar una función o un diccionario de mapeo a los valores de una Serie. Es útil para transformar los valores según reglas definidas.

```python
# Mapear los valores a categorías
mapa_poblacion = {2890000: 'Alta', 1391000: 'Media', 948000: 'Baja'}
categorias = serie_ciudades.map(mapa_poblacion)
print(categorias)
```

**Salida**:

```
Buenos Aires    Alta
Córdoba        Media
Rosario         Baja
dtype: object
```

#### Series.groupby

El método `groupby()` permite agrupar los datos de una Serie según uno o más criterios y aplicar operaciones de agregación sobre cada grupo. Es muy poderoso cuando se trabaja con datos categóricos.

```python
# Agrupar por nivel de población y contar la cantidad de ciudades por grupo
grupo = serie_ciudades.map(lambda x: 'Alta' if x > 1000000 else 'Baja').groupby(serie_ciudades.map(lambda x: 'Alta' if x > 1000000 else 'Baja')).count()
print(grupo)
```

**Salida**:

```
Alta    2
Baja    1
dtype: int64
```

### Extracción de Elementos que Cumplen una Condición

Podemos extraer todos los elementos de una Serie que cumplan con una condición utilizando operaciones lógicas. Por ejemplo, si queremos extraer las ciudades con más de 1,000,000 de habitantes:

```python
# Extraer ciudades con más de 1,000,000 de habitantes
ciudades_mayores = serie_ciudades[serie_ciudades > 1000000]
print(ciudades_mayores)
```

**Salida**:
```
Buenos Aires    2890000
Córdoba         1391000
dtype: int64
```

### Resumen

- Una **Serie** es una estructura de datos unidimensional con un índice que facilita el acceso a los elementos.
- Podemos crear Series a partir de listas, diccionarios o arreglos de NumPy, y personalizar sus índices.
- Podemos acceder a los elementos de una Serie mediante su índice o su posición.
- Podemos utilizar **slicing** para acceder a un rango de elementos, ya sea por posición o por índice.
- Las Series soportan operaciones aritméticas y funciones estadísticas para análisis de datos.

En el próximo apunte, profundizaremos en la estructura más compleja de Pandas: el **DataFrame**.
