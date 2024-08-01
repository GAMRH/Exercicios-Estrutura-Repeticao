# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. 

num = int(input('Digite o número para ver a tabuada: '))
print(f'Tabuada de {num}: ')

for i in range (1,11,1):
    print(f'{num} x {i} = {num * i}')