# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário

preco_pao = float(input('Informe o preço do produto: '))

print('Panificadora Pão de Ontem - Tabela de preços')

for i in range(1,51,1):
    por_tabela = i * preco_pao
    print(f'{i} - R$ {por_tabela}')
