''' Recibir dos números y hacer las operaciones básicas '''

numero1 = float(input('Ingrese el primer número: \r\n'))
numero2 = float(input('Ingrese el segundo número: \r\n'))

suma = numero1 + numero2
print(f'La suma de ellos es: {suma}')

resta = numero1 - numero2
print(f'La resta de ellos es: {resta}')

multiplicacion = numero1 * numero2
print(f'La multiplicación de ellos es: {multiplicacion}')


if numero2 != 0:
    division = numero1 / numero2
    print(f'La división de ellos es: {division}')
else:
    print('No se puede dividir por 0')