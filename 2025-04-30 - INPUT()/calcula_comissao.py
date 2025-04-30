# Fazer um programa para solicitar o valor de uma venda e
# o percentual da comissão e exibir o valor da comissão

valorvenda = float(input('Digite o valor da venda (R$): '))
percentual = float(input('Informe a comissão (%)......: '))

comissao = valorvenda * percentual / 100

print(f'O Valor da comissão é R$ {comissao:.2f}')