# Ejercicio de manejo de cadenas
nombre = input('Dime tu nombre: \r\n')
apellidos = input('Dime tus apellidos: \r\n')
inicial = nombre[0]
print(inicial)
final = nombre [-1]
print(final)

dosPosiciones = nombre[0:2]
print(dosPosiciones)
print(nombre[3:1:-1])

# Print nombres
nombreEntero = nombre +' '+ apellidos
print(f'Nombre Completo: {nombreEntero}')
longitud = len(nombreEntero)
print(f'La longitud total es de: {longitud} caracteres' )
print(f'Nombre completo en mayúsculas:{nombreEntero.upper()}')

# Nombre en minúsculas
print(f'Nombre completo en minúsculas:{nombreEntero.lower()}')

# Probar más posiciones 
cincoPosiciones = nombre[0:5]
print(cincoPosiciones)