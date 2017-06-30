letras = []
i = 1

while i <= 10:
    letras.append(input('Insira uma letra: '))
    i += 1
print('Conteudo capturado: ', letras)

i = 0
cons = 0
while i <= 9:
    if letras[i] not in 'aeiou':
        cons += 1
    i += 1

print('Consoantes lidas: %d' % cons)
