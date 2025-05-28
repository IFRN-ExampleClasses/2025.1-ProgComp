'''
   Programa que solicite ao usuário números inteiros 
   aleatoriamente até que seja informado o valor 0

   Quando for digitado o valor 0, o programa deverá informar:

   a) Quantos números inteiros foram digitados;
   b) A soma dos números inteiros positivos;
   c) A média dos números inteiros positivos;

   O valor 0 digitado não deve ser considerado em nenhum dos itens acima.
'''

intValor          = None
intSomaPositivos  = 0
intQtValores      = 0
intQtValPositivos = 0

while intValor != 0:
   try:
      intValor = int(input('Informe um valor inteiro: '))
   except ValueError:
      print('ERRO: Valor Inteiro Inválido...')
   except Exception as e:
      print(f'ERRO: {e}')
   else:
      if intValor > 0:
         intSomaPositivos  += intValor
         intQtValPositivos += 1

      if intValor != 0:
         intQtValores += 1
   
print(f'Quantos números inteiros foram digitados: {intQtValores}')
print(f'Soma dos números inteiros positivos.....: {intSomaPositivos}')
print(f'Média dos números inteiros positivos....: {intSomaPositivos/intQtValPositivos}')
