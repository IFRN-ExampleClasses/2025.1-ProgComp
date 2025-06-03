'''
   Programa para executar um produto de 2 números inteiros
   positivos utilizando apenas o operador soma (+)

   x = 80
   y = 6
   p = y + y + y + y + y + y + y + y + ...
'''
import sys

try:
   intMultiplicador = int(input('Digite o Multiplicador: '))
   intMultiplicando = int(input('Digite o Multiplicando: '))
except ValueError:
   sys.exit('ERRO: Não foi informado um valor inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intMultiplicador <= 0:
      sys.exit('ERRO: Informe Multiplicador Positivo...')

   if intMultiplicando <= 0:
      sys.exit('ERRO: Informe Multiplicando Positivo...')

   intProduto  = 0
   intContador = 1
   while intContador <= intMultiplicador:
      intProduto  += intMultiplicando
      intContador += 1
   
   print(f'{intMultiplicador} x {intMultiplicando} = {intProduto}')