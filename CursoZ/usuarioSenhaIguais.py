'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    usuario = input('Informe o usuario: ')
    senha = input('Informe a senha: ')

    if usuario != senha:
        break
    else:
        print('Informe uma senha diferente do usuario!')
