# https://wiki.python.org.br/EstruturaSequencial

area = float(input('Informe a quantidade de metros quadrados: '))

# rendimento de 6 metros por litro
rendimento = 6

# descobrir quantos litros são necessários pra área informada
qtdadeLts = area/rendimento
print('Para pintar %dm sao necessarios %.2f litros de tinta.' % (area, qtdadeLts))

ltsLatao = 18
vlrLatao = 80
ltsGalao = 3.6
vlrGalao = 25
qtdadeGaloes = 0
qtdadeLatoes = 0
valorTotalG = 0
valorTotalL = 0

# se a qtdade de litros é menor que o galão, então vai 1 galão
if qtdadeLts <= ltsGalao:
	qtdadeGaloes = 1

# se a qtdade de litros é maior que 1 galão e menor que 1 latão
elif qtdadeLts > ltsGalao and qtdadeLts < ltsLatao:
        qtdadeGaloes = 1
        while qtdadeLts > ltsGalao:
                qtdadeLts = qtdadeLts - ltsGalao
                qtdadeGaloes = qtdadeGaloes + 1
        if valorTotalG > vlrLatao:
                qtdadeLatoes = 1
                qtdadeGaloes = 0
                valorTotalG = 0

# se a qtdade de litros é maior os litros do latão
elif qtdadeLts >= ltsLatao:
        qtdadeLatoes = 1
        while True:
                qtdadeLts = qtdadeLts - ltsLatao
                if qtdadeLts >= ltsLatao:
                        qtdadeLatoes = qtdadeLatoes + 1
                elif qtdadeLts > 0 and qtdadeLts < ltsLatao:
                        qtdadeGaloes = 1
                        while qtdadeLts > ltsGalao:
                                qtdadeLts = qtdadeLts - ltsGalao
                                qtdadeGaloes = qtdadeGaloes + 1
                        break
                        
valorTotalL = qtdadeLatoes * vlrLatao
valorTotalG = qtdadeGaloes * vlrGalao

print('Galoes: %d' % qtdadeGaloes)
print('Valor dos galoes: %.2f' % valorTotalG)
print('Latoes: %d' % qtdadeLatoes)
print('Valor dos latoes: %.2f' % valorTotalL)
