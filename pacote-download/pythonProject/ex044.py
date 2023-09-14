'''

'''

#estilização
print(f'{" LOJAS JONATAS ":=^40} ')

#captura de dados
preço = float(input('Digite o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcão = int(input('Qual será a opção: '))

#condição à vista: 10% desconto
if opcão == 1:
    pre_desc = preço - (preço * (10 / 100))

    print(f'Sua compra de R${preço}, ficará no final R${pre_desc}')

#condição à vista cartão: 5% desconto
if opcão == 2:
    pre_desc = preço - (preço * (5 /100))

    print(f'Sua compra de R${preço}, ficará no final R${pre_desc}')

#condição 3x ou mais cartão: 20% juros
if opcão == 4:
    vezes = int(input('Quantas parcelas? '))
    pre_juros = preço + (preço * (20 / 100))
    va_parcela = pre_juros / vezes

    print(f'Sua compra será parcelada em {vezes}x de R${va_parcela} COM JUROS')

    print(f'Sua compra de R${preço}, ficará no final R${pre_juros}')

#condição cartão até 2x
else:
    print(f'Sua compra de R${preço}, não sofrerá nenhum juros!')