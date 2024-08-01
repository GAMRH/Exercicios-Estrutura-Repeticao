# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.
par = impar = 0

for i in range (1,11,1):
    num = int(input(f'Digite o {i} número inteiro: '))
    if (num % 2 == 0):
        par += 1
    else: 
        impar += 1

print(f'A quantidade de números pares é: {par}')
print(f'A quantidade de números ímpares é: {impar}')