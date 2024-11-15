## Práctica 0405

* Usa filter para obtener solo los números pares de una lista de enteros.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", numeros_pares)
```
* Dada una lista de temperaturas en Celsius, usa map para convertirlas a Fahrenheit.

```python
temperaturas_celsius = [0, 20, 37, 100]
temperaturas_fahrenheit = list(map(lambda c: c * 9 / 5 + 32, temperaturas_celsius))
print("Temperaturas en Fahrenheit:", temperaturas_fahrenheit)
```

* Utiliza reduce para obtener la suma acumulativa de una lista de números.

```python
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma_acumulada = reduce(lambda x, y: x + y, numeros)
print("Suma acumulada:", suma_acumulada)
```
* Dada una lista de palabras, usa filter para encontrar las que tienen más de cinco letras y luego map para convertirlas en mayúsculas.

```python
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
palabras_largas = filter(lambda palabra: len(palabra) > 5, palabras)
palabras_mayusculas = list(map(lambda palabra: palabra.upper(), palabras_largas))
print("Palabras en mayúsculas:", palabras_mayusculas)
```
* Dada una lista de números, utiliza filter, map y reduce para obtener el producto de los números pares.

```python
from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = filter(lambda x: x % 2 == 0, numeros)
producto = reduce(lambda x, y: x * y, numeros_pares)
print("Producto de los números pares:", producto)
```
* Dada una lista de listas de enteros, usa map, filter, y reduce para obtener la suma de todos los números positivos.

```python
from functools import reduce
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
todos_los_numeros = map(lambda sublista: sublista, listas)
numeros_positivos = filter(lambda x: x > 0, [num for sublista in todos_los_numeros for num in sublista])
suma_positivos = reduce(lambda x, y: x + y, numeros_positivos)

print("Suma de los números positivos:", suma_positivos)
```
