## Proyecto
 ```python
 import csv
import datetime
def cargar_tareas():
    tareas = []
    try:
        with open("tareas.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila['Fecha límite'] = datetime.datetime.strptime(fila['Fecha límite'], '%Y-%m-%d').date()
                fila['Completada'] = fila['Completada'] == 'True'
                tareas.append(fila)
    except FileNotFoundError:
        print("No se encontró un archivo de tareas. Se comenzará con una lista vacía.")
    return tareas
def guardar_tareas(tareas):
    with open("tareas.csv", "w", newline="") as archivo:
        campos = ['Nombre', 'Prioridad', 'Fecha límite', 'Completada']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for tarea in tareas:
            tarea['Fecha límite'] = tarea['Fecha límite'].strftime('%Y-%m-%d')
            escritor.writerow(tarea)
def añadir_tarea(tareas):
    nombre = input("Nombre de la tarea: ")
    prioridad = input("Prioridad (alta, media, baja): ")
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    fecha_limite = datetime.datetime.strptime(fecha_limite, '%Y-%m-%d').date()
    tarea = {
        'Nombre': nombre,
        'Prioridad': prioridad,
        'Fecha límite': fecha_limite,
        'Completada': False
    }
    tareas.append(tarea)
    print("Tarea añadida correctamente.")
def listar_tareas(tareas):
    print("\nLista de Tareas:")
    hoy = datetime.date.today()
    for i, tarea in enumerate(tareas):
        estado = "Vencida" if not tarea['Completada'] and tarea['Fecha límite'] < hoy else "Pendiente"
        print(f"{i}. {tarea['Nombre']} - Prioridad: {tarea['Prioridad']} - Fecha límite: {tarea['Fecha límite']} - Estado: {'Completada' if tarea['Completada'] else estado}")
    print()
def marcar_tarea_completada(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("Introduce el número de la tarea a marcar como completada: "))
        if 0 <= indice < len(tareas):
            tareas[indice]['Completada'] = True
            print("Tarea marcada como completada.")
        else:
            print("Índice no válido.")
    except ValueError:
        print("Entrada inválida. Debes introducir un número.")
def eliminar_tarea(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("Introduce el número de la tarea a eliminar: "))
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['Nombre']}' eliminada.")
        else:
            print("Índice no válido.")
    except ValueError:
        print("Entrada inválida. Debes introducir un número.")
def notificar_tareas_vencidas(tareas):
    hoy = datetime.date.today()
    tareas_vencidas = [tarea for tarea in tareas if not tarea['Completada'] and tarea['Fecha límite'] < hoy]
    if tareas_vencidas:
        print("\nTareas Vencidas:")
        for tarea in tareas_vencidas:
            print(f"{tarea['Nombre']} - Prioridad: {tarea['Prioridad']} - Fecha límite: {tarea['Fecha límite']}")
        print()
def menu():
    tareas = cargar_tareas()
    while True:
        print("\nGestión de Tareas")
        print("1. Añadir tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Notificar tareas vencidas")
        print("6. Salir y guardar")

        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            añadir_tarea(tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            marcar_tarea_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            notificar_tareas_vencidas(tareas)
        elif opcion == '6':
            guardar_tareas(tareas)
            print("Tareas guardadas. Saliendo...")
            break
        else:
            print("Opción no válida, por favor elige una opción del menú.")
if __name__ == "__main__":
    menu()
```