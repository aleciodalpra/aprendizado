#somador de valores

print('Digite o valor para somar seguido de [ENTER].')
print('Para encerrar, digite zero: 0')
n = float(input(':'))
total = n 
while n != 0:
	n = float(input(':'))
	total = total + n
print('Total: %s' %total)