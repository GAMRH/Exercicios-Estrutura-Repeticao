# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Digite uma nota de 0 até 10: '))

while True:
    if (nota <= 10 and nota >= 0):
        print('Esta é uma nota válida! ')
        break 
    else: 
        print('Você informou uma nota inválida! Tente novamente...')
        nota = int(input('Digite uma nota de 0 até 10: '))
