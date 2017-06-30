dia, mes, ano = input('Informe a data de nascimento (dd/mm/aaaa): ').split('/')

meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

print('Data de nascimento informada:')
print('%s de %s de %s' % (dia, meses[int(mes) - 1], ano))
