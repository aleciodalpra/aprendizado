#somador de valores

print('Digite o valor para somar seguido de [ENTER].')
print('Para encerrar, digite ENTER novamente')

total = 0
while 1:
	try:
		n = float(input(':'))
		total = total + n
	except:
		break	
print('Total: %s' %total)