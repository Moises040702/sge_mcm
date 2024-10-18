## Práctica 0401
* Crea un programa que solicite un número por pantalla al usuario y siga pidiéndolo hasta que el usuario introduzca un número válido.

```python
a = input("Dime un número: ")

while True:
    es_numero = True 
    for caracter in a:
        if caracter < '0' or caracter > '9': 
            es_numero = False
            break  

    if es_numero:  
        a = int(a)  
        break  
    else:
        print("Eso no es un número. Intenta de nuevo.")
        a = input("Dime un número: ")


print(a)
```


* Crea un programa que solicite un número n y un valor k y que muestre por la terminal los primeros k elementos de la tabla de multiplicar de n

```python
n = int(input("Dime un número: "))
k = int(input("Dime un número: "))
for k in range(1,k+1):
    print(str(n) + " * " + str(k) + " = " + str(n * k))
```
* Crea un programa que solicite un número al usuario y dibuje un triángulo con asteriscos cuya base sea el número introducido.

```python
base = int(input("Introduce un número: "))
for i in range(1,base+1):
    print("*" * i)
```
* Modifica el programa anterior para que en lugar de crear un triángulo cree una pirámide. Si el usuario introduce un número par se lo volverá a pedir hasta que introduzca un número par

```python
base = int(input("Introduce un número impar"))
while base % 2 == 0:
    print("No es un número impar")
    base = int(input("Introduce un número impar"))

for i in range(1,base+1,2):
    espacios = (base-i) //2
    print(" " * espacios + "*" * i)

```

* Crea un programa que pida al usuario que introduzca 5 números y luego le diga cuál es el mayor y el menor de todos ellos de la forma: El número mayor es <mayor> y el menor es <menor>
```python
numeros = input("Introduce 5 números separados por espacios: ").split()
numeros = [int(numero) for numero in numeros]
mayor = max(numeros)
menor = min(numeros)
print(f"El número mayor es {mayor} y el menor es {menor}")

```

* Crea un programa que convierta entre diferentes unidades de longitud (milímetros, centímetros, metros y kilómetros). El usuario introducirá primero la cantidad, luego la unidad de medida en que está y finalmente la unidad de medida a la que se va a convertir.
```python
conversiones = {
    'mm': 0.001,  
    'cm': 0.01,    
    'm': 1,        
    'km': 1000     
}

cantidad = float(input("Introduce la cantidad: "))
unidad_inicial = input("Introduce la unidad de medida inicial (mm, cm, m, km): ").lower()
unidad_final = input("Introduce la unidad de medida final (mm, cm, m, km): ").lower()

cantidad_en_metros = cantidad * conversiones[unidad_inicial]

cantidad_convertida = cantidad_en_metros / conversiones[unidad_final]

print(f"{cantidad} {unidad_inicial} es igual a {cantidad_convertida} {unidad_final}")
  ```

 * Crea un programa que genere un número aleatorio entre 0 y 100 y el usuario tenga que adivinarlo. Cada vez que el usuario introduzca un número el programa le dirá si el número es más alto o más bajo.
 ```python 
from random import randint
numero_secreto = randint(0,100)
while True:
    intento = int(input("Introduce un número del 0 al 100"))
    if intento < numero_secreto:
        print("El número es menor del deseado")
    elif intento > numero_secreto:
        print("El número es mayor del deseado")
    else:
        print("Felicidades ese es el número")
        break
```
* Crea un programa que implemente el clásico juego de piedra, papel, tijeras, lagarto y spock.
```python 
import random

opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']
reglas = {
    'piedra': ['tijera', 'lagarto'],
    'papel': ['piedra', 'spock'],
    'tijera': ['lagarto', 'papel'],
    'lagarto': ['papel', 'spock'],
    'spock': ['tijera', 'piedra']
}

jugadoruno = 0
jugadordos_puntos = 0

while jugadoruno < 5 and jugadordos_puntos < 5:
    print("\nElige una opción: piedra, papel, tijera, lagarto, spock: ")
    jugador = input("Tu elección: ").lower()

    if jugador not in opciones:
        print("Opción no válida")
        continue

    jugadordos = random.choice(opciones)
    print(f"El jugador dos eligió: {jugadordos}")

    if jugador == jugadordos:
        print("Empate")
    elif jugadordos in reglas[jugador]:
        print(f"Has ganado. {jugador} ha ganado esta ronda a {jugadordos}")
        jugadoruno += 1
    else:
        print(f"Has perdido. {jugadordos} ha ganado esta ronda a {jugador}")
        jugadordos_puntos += 1

if jugadoruno == 5:
    print("\n¡Felicidades, ganaste el juego!")
else:
    print("\nEl jugador dos ganó el juego. ¡Suerte para la próxima!")
```

 * Crea un programa que genere los primeros n números de la secuencia de Fibonacci
 ```python 

cantidad = int(input("Introduce la cantidad de números de la secuencia de Fibonacci: "))

secuencia_fibonacci = [1, 1]

for i in range(2, cantidad):
    secuencia_fibonacci.append(secuencia_fibonacci[i-2] + secuencia_fibonacci[i-1])

print(secuencia_fibonacci[:cantidad])
```