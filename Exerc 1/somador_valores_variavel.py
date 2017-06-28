#CALCULO DE DESPESAS

print('CALCULO DE DESPESAS')
print
print('Para encerrar, tecle ENTER em vez de digitar um novo nome')
print

total = 0
contas = {}
while 1:
	pessoa = input('Insira o nome da pessoa: ')
	if not pessoa: 
		break
	while 1:
		resp = input('Quanto gastou %s? ' % pessoa)	
		try:
			gasto = float(resp)
			break
		except:
			print('Nro invalido!')

	contas[pessoa] = gasto
	total = total + gasto

print('...................')
num_pessoas = len(contas)
print('Quantidade de pessoas %d' % num_pessoas)
print('Total de gastros: R$ %.2f' % total)

try:
	media = total/num_pessoas
	print('Gasto medio por pessoa: R$ %.2f' % media)
except:
	print('Sem gasto medio!')
	
print('...................')

for nome in contas.keys():
	saldo = contas[nome] - media
	print('Saldo de %s: %.2f' %(nome, saldo))