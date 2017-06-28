# https://wiki.python.org.br/EstruturaSequencial

s = input('Informe seu sexo ("m" ou "f" minusculo): ')
h = float(input('Informe sua altura: '))

try:
	if s == 'm':
		pesoIdeal = (72.7*h) - 58
	elif s == 'f':
		pesoIdeal = (62.1*h) - 44.7
			
	peso = float(input('Informe seu peso: '))
	
	print('-------------------------------------')
	
	if peso > pesoIdeal:
		pesoAcima = peso - pesoIdeal
		print('Voce esta %.2f kg acima do peso!' % pesoAcima)
	elif peso == pesoIdeal:
		print('Parabens, voce esta no peso correto!')
	else:
		pesoAbaixo = pesoIdeal - peso
		print('Voce esta %.2f kg abaixo do peso ideal!' % pesoAbaixo)
	print
	print('Seu peso ideal eh: %.3f' % pesoIdeal)
	print('-------------------------------------')

except:
	print('Informe "f" ou "m" minusculo!')
