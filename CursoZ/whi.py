#


#nro = int(input('Insira um nro: '))
#x = 1

#while x <= nro:
#    if x % 2 == 0:
#        print(x)
#        x = x + 1
#    else:
#        x = x + 1

#while x <= nro:
#    if x % 2 != 0:
#        print(x)
#    x = x + 1

#while x <= nro:
#    print(x)
#    x = x + 2

#while x <= nro:
#    if x % 3 == 0:
#        print(x)
#    x = x + 1

# soma acumulada de valores ##############################

#n = 1
#soma = 0

#while n <= 10:
#    x = int(input('Informe o peso da pessoa %d: ' % n))
#    n = n + 1
#    soma = soma + x

#print('O peso total da turma eh: %i' % soma)

# media ################################

#n = 1
#soma = 0

#while n <= 10:
#    x = int(input('Informe o valor %d: ' % n))
#    n = n + 1
#    soma = soma + x

#media = soma / 10

#print('A media dos valores eh: %.2f' % media)

# fatoria de 10 #################################
#n = 1
#vlr = int(input('Informe um nro: '))
#x = 1

#while n <= vlr:
#    x = x * n
#    print('Fat (%d) = %d' % (n, x))
#    n = n + 1

# while True #################################
#soma = 0

#while True:
#    x = int(input('Informe um valor para somar (0 para sair): '))
#    if x == 0:
#        break
#    soma = soma + x
#print('Soma: %.i' % soma)


# tabuada 1 a 10 #################################
tabuada = 1

while tabuada <= 10:
    print()
    print('Tabuada do %d' % tabuada)
    x = 1
    while x <= 10:
        valor = tabuada * x
        print('%d x %d = %d' % (tabuada, x, valor))
        x = x + 1
    tabuada = tabuada + 1

# conteudo de Repetições
# ultimo video visto TWP260 Repetições aninhadas
