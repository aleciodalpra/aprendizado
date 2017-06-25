#somador de valores

print('Digite o valor para somar seguido de [ENTER].')
print('Para encerrar, digite zero: 0')

total = 0
while 1:
	n = float(input(':'))
	if n == 0: 
		break	
	total = total + n
print('Total: %s' %total)