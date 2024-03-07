''' Clase calculadora '''

class Calculadora:

    # constructor
    def __init__(self,n1,n2):

        # variables de instancias
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        total = self.n1 + self.n2
        print(f'La suma de {self.n1} y {self.n2} es {total}')

    def restar(self):
        total = self.n1 - self.n2
        print(f'La resta de {self.n1} y {self.n2} es {total}')

    def multiplicar(self):
        total = self.n1 * self.n2
        print(f'La multiplicación de {self.n1} y {self.n2} es {total}')

    def dividir(self):
        try:
            total = self.n1 / self.n2
            print(f'La división de {self.n1} y {self.n2} es {total}')
        except ZeroDivisionError:
            print('No se puede dividir un número por 0')

    def potenciar(self):
        total = self.n1 ** self.n2
        print(f'La potencia de {self.n1} y {self.n2} es {total}')        

# Función principal
def app():
    
    # Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:          
            n1 = float(input('Introduce el primer número: '))
            n2 = float(input('Introduce el segundo número: '))
            
            suma = Calculadora(n1,n2)
            suma.sumar()

            # Reiniciar la app
            app()
            preguntar = False
        elif opcion == 2:
            n1 = float(input('Introduce el primer número: '))
            n2 = float(input('Introduce el segundo número: '))

            resta = Calculadora(n1,n2)
            resta.restar()

            # Reiniciar la app
            app()            
            preguntar = False
        elif opcion == 3:
            n1 = float(input('Introduce el primer número: '))
            n2 = float(input('Introduce el segundo número: '))

            multiplica = Calculadora(n1,n2)
            multiplica.multiplicar()
            
            # Reiniciar la app
            app()  
            preguntar = False
        elif opcion == 4:
            n1 = float(input('Introduce el primer número: '))
            n2 = float(input('Introduce el segundo número: '))

            division = Calculadora(n1,n2)
            division.dividir()

            # Reiniciar la app
            app()              
            preguntar = False
        elif opcion == 5:
            n1 = float(input('Introduce el primer número: '))
            n2 = float(input('Introduce el segundo número: '))

            potencia = Calculadora(n1,n2)
            potencia.potenciar()
            
            # Reiniciar la app
            app()              
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo')

# Función mostrar menú
def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('(1) Sumar')
    print('(2) Restar')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Potencia')

# Llamamos a la función principal
app()