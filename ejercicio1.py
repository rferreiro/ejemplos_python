'''Pedir 3 números por teclado y comprobar si todos son menores de 10'''
numero1 = int(input('Ingrese el primer número: \r\n'))
numero2 = int(input('Ingrese el segundo número: \r\n'))
numero3 = int(input('Ingrese el tercer número: \r\n'))

if numero1 < 10 and numero2 < 10 and numero3 < 10:
    print('Todos los números son menores de 10')
else:
    print('Algún número no cumple la condición')