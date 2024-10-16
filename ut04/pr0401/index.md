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

