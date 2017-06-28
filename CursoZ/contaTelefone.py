#calculo da conta com valor de minuto variavel

minutos = float(input('Informe a quantidade de minutos: '))

if minutos < 200:
    valor = minutos * 0.20
elif minutos < 400:
    valor = minutos * 0.18
elif minutos < 800:
    valor = minutos * 0.15
else:
    valor = minutos * 0.08

print('O valor da sua conta é: R$ %.2f' % valor)
