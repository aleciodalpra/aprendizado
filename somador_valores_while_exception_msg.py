#somador de valores

print('Digite o valor para somar seguido de [ENTER].')
print('Para encerrar, digite ENTER novamente')

total = 0
while 1:
	try:
		linha = input(':')
		n = float(linha)
		total = total + n
	except:
		if len(linha) == 0:
			break
		elif ',' in linha:
			print('Use ponto (.) como separador decimal')
		else:
			print('Insira apenas numeros')
print('Total: %s' %total)