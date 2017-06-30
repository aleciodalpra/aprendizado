# ver se a palavra é palíndrome
'''
palavra = input('Informe uma palavra: ')

if palavra[:] == palavra[::-1]:
    print('Eh palindrome')
else:
    print('Nao eh palindrome')

print('Escrita normal:', palavra[:])
print('Escrita inversa: ', palavra[::-1])
'''

# substituir as vogais por *
palavra = input('Informe uma palavra: ')
novaPalavra = ""
i = 0

while i < len(palavra):
    if palavra[i] in 'aeiou':
        novaPalavra = novaPalavra + '*'
    else:
        novaPalavra = novaPalavra + palavra[i]
    i += 1
        

print('Palavra:', palavra)
print('Nova Palavra: ', novaPalavra)
