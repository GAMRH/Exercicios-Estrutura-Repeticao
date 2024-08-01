#Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.
cont = 0
tot_alunos = 0

qtd_turma = int(input('Qual a quantidade de turmas? '))

while (cont < qtd_turma):
   qtd_alunos = int(input(f'Quantos alunos temos na turma {cont+1}? '))
   
   if (qtd_alunos > 40):
       print('A quantidade de alunos não é válida!')
       continue
       
   cont += 1
   tot_alunos += qtd_alunos
   
print(f'A média de alunos por turma é: {tot_alunos // qtd_turma}')
   


