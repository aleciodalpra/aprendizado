# https://wiki.python.org.br/EstruturaSequencial

#-*- coding: utf-8 -*-

n2 = float(input('Informe o valor da hora: '))
n1 = float(input('Informe a quantidade horas trabalhadas por mês: '))

salBruto = n1 * n2
ir = salBruto * 0.11
inss = salBruto * 0.08
sindicato = salBruto * 0.05
salLiq = salBruto - ir - inss - sindicato
print('')
print('+ Salário Bruto: R$ %.2f' % salBruto)
print('- IR: R$ %.2f' % ir)
print('- INSS: R$ %.2f' % inss)
print('- Sindicato: R$ %.2f' % sindicato)
print('= Salário Liquido: R$ %.2f' % salLiq)
print('')