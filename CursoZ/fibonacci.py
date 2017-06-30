# fibonacci de um nro

nro = int(input('Informe um nro: '))

a = 1
b = 1

cont = 1

while cont <= nro - 2:
    a, b = b, a + b
    cont = cont + 1

print('Fib(%d) = %d' %(nro, b))
