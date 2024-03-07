''' Calcular precio salas de juegos '''

edad = int(input('Indique la edad: \r\n'))

if(edad < 4):
    print('La entrada es gratis')
elif edad >= 4 and edad <= 18:
    print('La entrada vale 5 €')
elif edad > 18:
    print('La entrada vale 10 €')