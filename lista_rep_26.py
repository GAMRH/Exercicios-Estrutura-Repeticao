# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

tot_eleitor = int(input('Digite a quantidade total de eleitores: '))
cand1 = 0
cand2 = 0
cand3 = 0
cont = 0
while (cont < tot_eleitor):
    voto = int(input('Escolha seu candidato: \n1 - João Gomes \n2 - Pedro Paulo \n3 - Frederico Evandro\n'))
    if (voto == 1):
        cand1 += 1
        cont += 1
    elif (voto == 2):
        cand2 += 1
        cont += 1
    elif (voto == 3):
        cand3 += 1
        cont += 1
    else:
        print('Você digitou uma opção errada! Corrija seu voto...')
        continue

print(f'O total de votos de cada candidato foi: ')
print(f'João Gomes {cand1}')
print(f'Pedro Paulo {cand2}')
print(f'Frederico Evandro {cand3}')