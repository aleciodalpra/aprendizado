#

limite = 110
vlrMulta = 5
veloc = float(input('Qual a velocidade do veiculo: '))

if veloc > limite:
	print('Voce foi multado!')
	multa = (veloc - limite) * 5
	print('Valor da multa %.2f' % multa)