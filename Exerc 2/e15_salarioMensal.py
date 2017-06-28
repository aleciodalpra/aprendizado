# https://wiki.python.org.br/EstruturaSequencial

n2 = float(input('Informe o valor da hora: '))
n1 = float(input('Informe a quantidade horas trabalhadas por mes: '))

salBruto = n1 * n2
ir = salBruto * 0.11
inss = salBruto * 0.08
sindicato = salBruto * 0.05
salLiq = salBruto - ir - inss - sindicato
print('')
print('+ Salario Bruto: R$ %.2f' % salBruto)
print('- IR: R$ %.2f' % ir)
print('- INSS: R$ %.2f' % inss)
print('- Sindicato: R$ %.2f' % sindicato)
print('= Salario Liquido: R$ %.2f' % salLiq)
print('')