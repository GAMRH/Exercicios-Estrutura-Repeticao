# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    login = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    
    if (login != senha): 
        print('Informações corretas! Login concluído!')
        break
    else: 
        print('Seu usuário não pode ser igual a sua senha \nPreencha novamente as informações!')
        continue
    
