#media com lista de notas
'''
notas = [6, 7, 8, 9, 9]
soma = 0
x = 0

while x < 5:#esse 5 é a quantidade de notas
    soma += notas[x]
    x += 1

print('A media eh: %d.' % (soma / 5))
'''
'''
# pedir as notas
vetor = []
x = 0

while x < 5:#esse 5 é a quantidade de notas
    n = int(input('Insira um nro: '))
    vetor.append(n)
    x += 1

print('Vetor lido: ', vetor)
'''

'''
# vetor de 10 nros e imprimir na ordem e na ordem inversa
vetor = []
x = 0
n = 1

while x < 10:#esse 5 é a quantidade de notas
    n = int(input('Insira um nro: '))
    vetor.append(n)
    x += 1

print('Vetor lido: ', vetor)

while n >= 0:
    print('Valor: %d', n)
    n = n - 1
'''

# ler 4 notas, mostrar na tela e calcular a media

notas = []
soma = 0
x = 1

while x <= 4:#esse 4 é a quantidade de notas
    n = float(input('Insira a nota: '))
    notas.append(n)
    x += 1
    soma += n

print('As notas sao: ', notas)
print('A media eh: %.2f' % (soma / 4))
