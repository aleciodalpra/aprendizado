#Calculadora de despesas

print ('BALANCO DE DESPESAS')
a = input('Quanto gastou A? ')
j = input('Quanto gastou J? ')
total = float(a) + float(j)

print ('Total de gastos: R$ %s.') % total

media = total/2

print ('Media de gasto por pessoa: R$ %s.') % media
print ('.....................')
print ('ACERTO DE CONTAS')
if a < media:
	diferenca = media - a
	print ('A deve pagar R$ %s') %diferenca
elif j < media:
	diferenca = media - j
	print ('J deve pagar R$ %s') %diferenca		
else:
	print ("Ambos gastaram o mesmo valor!")