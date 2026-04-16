# Estrutura de repetição While:

# Números até 10

# i = 1

# while 1 <= 10:
#     print(i)
#     i += 1

# Exemplo 2:
    
# n = 1
# soma = 0
# while n != 0:
#     n = int(input('Digite um número: '))
#     soma += n
# print(f'O total foi: {soma}')


# Exemplo 3:

# resposta = 'S'
# soma = 0
# while resposta != 'N':
#     n = int(input('Informe um número: '))
#     soma += n

#     resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]

# print(f'O total da soma é: {soma}')


resposta = 'S'
valor_venda = 0

while resposta != 'N':
    valor_venda = float(input('Digite o valor da venda: '))

    if valor_venda >= 1000.0:
        desconto = valor_venda * 0.1
        print(f'O valor da venda foi de: {valor_venda - desconto}')
        print(f'O valor do desconto foi de: {desconto}')
    else:
        print(valor_venda)

    resposta = input('Deseja prosseguir? [S/N] ').upper().strip()[0]
print('Programa encerrado.')


