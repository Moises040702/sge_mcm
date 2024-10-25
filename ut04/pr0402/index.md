## Práctica 0402

* Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene.
```python
def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    num_vocales = sum(1 for letra in cadena if letra in vocales)
    num_consonantes = sum(1 for letra in cadena if letra in consonantes)
    
    return num_vocales, num_consonantes

cadena = "Hola Mundo"
vocales, consonantes = contar_vocales_consonantes(cadena)
print(f"Vocales: {vocales}, Consonantes: {consonantes}")

```
* Crea un programa que invierta una cadena.
``` python
cadena = "Hola Mundo"
print(cadena[::-1])
```
* Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
```python 
cadena = "anita lava la tina"
cadena_procesada = cadena.replace(" ", "")
print(cadena_procesada == cadena_procesada[::-1])
```
* Crea una función que cuente cuántas palabras hay en una cadena, suponiendo que las palabras están separadas por espacios.
```python 
def contar_palabras(cadena):
    return len(cadena.split())
cadena = "Buenos dias, que tal"
print(contar_palabras(cadena))
```
* Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno.
```python 
def eliminar_caracteres_repetidos(cadena):
    resultado = ""
    for letra in cadena:
        if letra not in resultado:
            resultado += letra
    return resultado
cadena = "holaa"
print(eliminar_caracteres_repetidos(cadena))
```
* Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa.
```python
cadena = "Me llamo Moises"
resultado = ""
for letra in cadena:
    if letra.islower():
        resultado += letra.upper()
    elif letra.isupper():
        resultado += letra.lower()
    else:
        resultado += letra
print(resultado)
```
* Invertir palabras de una cadena
```python
cadena = "Hola Mundo"
print(cadena[::-1])
```
* Crea un programa que verifique si dos cadenas son anagramas. Se considera que dos palabras son anagramas si tienen las mismas letras en diferente orden, por ejemplo, lácteo y coleta.
```python
cadena1 = "lácteo"
cadena2 = "coleta"

cadena1 = cadena1.replace(" ", "").lower()
cadena2 = cadena2.replace(" ", "").lower()

if sorted(cadena1) == sorted(cadena2):
    print("Las cadenas son anagramas.")
else:
    print("Las cadenas no son anagramas.")
```