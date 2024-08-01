while True:
    login = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    
    if (login != senha): 
        print('Informações corretas! Login concluído!')
        break
    else: 
        print('Seu usuário não pode ser igual a sua senha \nPreencha novamente as informações!')
        continue
    
