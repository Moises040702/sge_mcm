## Práctica 0404

* Crea un diccionario de frutas y precios. Permite al usuario ingresar el nombre de una fruta y muestra su precio si existe en el diccionario, o un mensaje de que no está disponible en caso contrario.

```python

frutas_precios = {
    "manzana": 1.5,
    "pera": 2.0,
    "plátano": 1.2,
    "naranja": 1.8,
    "uva": 3.0
}
fruta = input("Introduce el nombre de una fruta: ").lower()
if fruta in frutas_precios:
    print(f"El precio de la {fruta} es {frutas_precios[fruta]}€ por unidad.")
else:
    print(f"Lo siento, la fruta '{fruta}' no está disponible.")

```
* Suponiendo un diccionario con al siguiente estructura, crea un programa que calcule cuántas categorías hay, cuántos productos tiene cada categoría y cuántos productos hay en total.

```python
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

num_categorias = len(productos)
productos_por_categoria = {categoria: len(lista) for categoria, lista in productos.items()}
total_productos = sum(productos_por_categoria.values())
print(f"Total de categorías: {num_categorias}")
print("\nNúmero de productos por categoría:")
for categoria, cantidad in productos_por_categoria.items():
    print(f"  {categoria}: {cantidad} productos")
print(f"\nTotal productos: {total_productos}")

```

* Escribe un programa que tome una frase y use un diccionario para contar la frecuencia de cada palabra.

```python
frase = input("Introduce una frase: ")
palabras = frase.lower().split()
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1
print("\nFrecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"  {palabra}: {frecuencia}")
```
* Supón un diccionario donde cada clave es una asignatura y el valor correspondiente una lista de estudiantes matriculados, tal como se muestra en el diccionario de ejemplo. Crea un programa que tenga un menú con tres opciones:

    * Listar estudiantes matriculados en una asignatura

    * Matricular un estudiante en una asignatura

    * Dar de baja un estudiante de una asignatura.

```python
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}
while True:
    print("\n--- MENÚ ---")
    print("1. Listar estudiantes matriculados en una asignatura")
    print("2. Matricular un estudiante en una asignatura")
    print("3. Dar de baja un estudiante de una asignatura")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        asignatura = input("\nIntroduce el nombre de la asignatura: ")
        if asignatura in asignaturas:
            print(f"\nEstudiantes matriculados en {asignatura}:")
            for estudiante in asignaturas[asignatura]:
                print(f"  {estudiante}")
        else:
            print(f"\nLa asignatura '{asignatura}' no existe.")

    elif opcion == "2":
        asignatura = input("\nIntroduce el nombre de la asignatura: ")
        estudiante = input("Introduce el nombre del estudiante: ")
        if asignatura in asignaturas:
            if estudiante not in asignaturas[asignatura]:
                asignaturas[asignatura].append(estudiante)
                print(f"\n{estudiante} ha sido matriculado en {asignatura}.")
            else:
                print(f"\n{estudiante} ya está matriculado en {asignatura}.")
        else:
            print(f"\nLa asignatura '{asignatura}' no existe.")

    elif opcion == "3":
        asignatura = input("\nIntroduce el nombre de la asignatura: ")
        estudiante = input("Introduce el nombre del estudiante: ")
        if asignatura in asignaturas:
            if estudiante in asignaturas[asignatura]:
                asignaturas[asignatura].remove(estudiante)
                print(f"\n{estudiante} ha sido dado de baja de {asignatura}.")
            else:
                print(f"\n{estudiante} no está matriculado en {asignatura}.")
        else:
            print(f"\nLa asignatura '{asignatura}' no existe.")
```

* Escribe una función que tome un diccionario y devuelva otro con las claves y valores intercambiados (lo que antes eran valores ahora son claves, y viceversa).
```python

def intercambiar_claves_valores(diccionario):
    return {valor: clave for clave, valor in diccionario.items()}
diccionario_original = {"a": 1, "b": 2, "c": 3}
diccionario_invertido = intercambiar_claves_valores(diccionario_original)

print("Diccionario original:", diccionario_original)
print("Diccionario invertido:", diccionario_invertido)
```

* Escribe un programa que tome dos diccionarios de productos y precios, y combine los productos comunes sumando sus precios, sin duplicar los elementos únicos.
```python

productos1 = {"Manzana": 1.2, "Banana": 0.8, "Naranja": 1.5}
productos2 = {"Banana": 0.7, "Pera": 1.3, "Naranja": 1.0}
productos_combinados = productos1.copy()
for producto, precio in productos2.items():
    if producto in productos_combinados:
        productos_combinados[producto] += precio
    else:
        productos_combinados[producto] = precio
print("Productos combinados:")
for producto, precio in productos_combinados.items():
    print(f"{producto}: {precio:.2f} €")
```

