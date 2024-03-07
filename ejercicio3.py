''' Cálculo descuento con barras de pan '''

coste = 3.49
barrasNoDia = int(input('Indique cuantas barras no son del día actual: \r\n'))
costeDescuento = coste - (coste*60)/100
costeTotal = costeDescuento*barrasNoDia

print(f'Coste normal: {coste}')
print(f'Coste barra de pan que no son del día: {costeDescuento}')
print(f'Coste total: {costeTotal}')
