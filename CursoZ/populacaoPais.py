'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento
'''

popPaisA = 80000
popPaisB = 200000
anos = 0

while True:
    if popPaisA <= popPaisB:
        popPaisA = popPaisA * 0.03 + popPaisA
        popPaisB = popPaisB * 0.015 + popPaisB
        anos += 1
    else:
        break

print('Necessarios %d anos.' % anos)
print('Populacao final pais A: %d' % popPaisA)
print('Populacao final pais B: %d' % popPaisB)
