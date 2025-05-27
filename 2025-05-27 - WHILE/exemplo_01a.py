'''
   Programa para exibir a tabuada de multiplicação de
   um determinado número inteiro positivo
'''
import sys

try:
   intMultiplicador = int(input('Informe o Multiplicador: '))
except ValueError:
   sys.exit('ERRO: Informe um valor inteiro...')
except Exception as e:
   sys.exit(f'ERRO {e}')
else:  
   if intMultiplicador <= 0:
      sys.exit('ERRO: Informe um valor inteiro positivo...')

   print(f'{intMultiplicador} x  1 = {intMultiplicador * 1}')
   print(f'{intMultiplicador} x  2 = {intMultiplicador * 2}')
   print(f'{intMultiplicador} x  3 = {intMultiplicador * 3}')
   print(f'{intMultiplicador} x  4 = {intMultiplicador * 4}')
   print(f'{intMultiplicador} x  5 = {intMultiplicador * 5}')
   print(f'{intMultiplicador} x  6 = {intMultiplicador * 6}')
   print(f'{intMultiplicador} x  7 = {intMultiplicador * 7}')
   print(f'{intMultiplicador} x  8 = {intMultiplicador * 8}')
   print(f'{intMultiplicador} x  9 = {intMultiplicador * 9}')
   print(f'{intMultiplicador} x 10 = {intMultiplicador * 10}')

   print('FIM DA TABUADA...')