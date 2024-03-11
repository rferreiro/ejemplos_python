import os

CARPETA = 'paises/'

def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menú de opciones
    mostrar_menu()

def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('(1) Agregar país')
    print('(2) Editar país')
    print('(3) Ver país')
    print('(4) Buscar país')
    print('(5) Eliminar país')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)

# Llamamos a la función principal
app()