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
