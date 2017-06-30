# 

a = int(input('Informe um nro para a: '))
b = int(input('Informe um nro para b: '))

while a % b != 0:
    a, b = b, a % b

print('mdc = %d' %b)
