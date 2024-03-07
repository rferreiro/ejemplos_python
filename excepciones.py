''' Ejemplo de excepciones '''
a = float(input('Indique un número: '))
b = float(input('Indique otro número: '))
try:
    c = a/b
    print(f'El resultado es {c}')
except ZeroDivisionError:
    print('No se puede dividir un número por 0')