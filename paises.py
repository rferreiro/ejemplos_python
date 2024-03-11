import os

CARPETA = 'paises/'
EXTENSION = '.txt'

#Paises
class Pais:
    def __init__(self, nombre, capital, poblacion, moneda):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.moneda = moneda

def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = int(input('Seleccione una opción: \r\n'))

        #Ejecutar las opciones
        if opcion == 1:
            agregar_pais()
            preguntar = False
        elif opcion == 2:
            editar_pais()
            preguntar = False
        elif opcion == 3:
            ver_pais()
            preguntar=False
        elif opcion == 4:
            buscar_pais()
            preguntar=False
        elif opcion == 5:
            eliminar_pais()
            preguntar=False
        else:
            print('Opción no válida, intente de nuevo')                                                

def eliminar_pais():
    nombre = input('Seleccione el país que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n País eliminado correctamente')
    except:
        print('No existe ese contacto')

def buscar_pais():
    nombre = input('Seleccione el país que desea buscar: \r\n')

    # Probar excepciones
    try:
        with open(CARPETA + nombre + EXTENSION) as pais:
            print('\r\n Información del país: \r\n')
            for linea in pais:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El país no existe')
        print(IOError) 

def ver_pais():
    archivos = os.listdir(CARPETA)

    # Para controlar que solo sean .txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as pais:
            for linea in pais:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre países
            print('\r\n')

def editar_pais():
    print('Escribe el nombre del país a editar')
    nombre_anterior = input('Nombre del país que desea editar: \r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_pais(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            
            # Resto de los campos
            nombre_pais = input('Agrega el nuevo nombre:\r\n')
            capital_pais = input('Agrega la nueva capital:\r\n')
            poblacion_pais = input('Agrega la nueva población:\r\n')
            moneda_pais = input('Agrega la nueva moneda:\r\n')

            # instanciar
            pais = Pais(nombre_pais, capital_pais, poblacion_pais, moneda_pais)

            # Escribir en el archivo
            archivo.write('Nombre: ' + pais.nombre + '\r\n')
            archivo.write('Capital: ' + pais.capital + '\r\n')
            archivo.write('Población: ' + pais.poblacion + '\r\n')
            archivo.write('Moneda: ' + pais.moneda + '\r\n')

        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_pais + EXTENSION)

        # Mostrar un mensaje de éxito
        print('\r\n País editado correctamente \r\n')
    else:
        print('Ese país no existe')

    # Reiniciar la app
    app()


def agregar_pais():
    print('Escribe los datos para agregar el nuevo país')
    nombre_pais = input('Nombre del país: \r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_pais(nombre_pais)
    if not existe:

        with open(CARPETA + nombre_pais + EXTENSION, 'w') as archivo:
            
            # Resto de los campos
            capital_pais = input('Agrega la capital:\r\n')
            poblacion_pais = input('Agrega la población:\r\n')
            moneda_pais = input('Agrega la moneda:\r\n')

            #Instanciar la clase
            pais = Pais(nombre_pais, capital_pais, poblacion_pais, moneda_pais)

            # Escribir en el archivo
            archivo.write('Nombre: ' + pais.nombre + '\r\n')
            archivo.write('Capital: ' + pais.capital + '\r\n')
            archivo.write('Población: ' + pais.poblacion + '\r\n')
            archivo.write('Moneda: ' + pais.moneda + '\r\n')

            print('\r\n País añadido correctamente \r\n')
    else:
        print('Ese país ya existe')

    # Reiniciar la app
    app()


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

def existe_pais(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


# Llamamos a la función principal
app()