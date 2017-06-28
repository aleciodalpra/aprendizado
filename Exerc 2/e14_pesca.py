# https://wiki.python.org.br/EstruturaSequencial

limite = 50
multa = 4
excesso = 0
vlrMulta = 0

kgPesca = float(input('Informe quantos kg de peixe foi pescado: '))

if kgPesca > limite:
	excesso = kgPesca - limite
	vlrMulta = excesso * multa
	print('Excedeu o limite!!!')

else:
	print('Nao excedeu o limite.')
print('Excesso: %.2f' % excesso)
print('Multa: R$ %.2f' % vlrMulta)
	