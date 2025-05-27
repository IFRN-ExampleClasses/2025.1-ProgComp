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

   intMultiplicando = 1
   while intMultiplicando <= 10:
      print(f'{intMultiplicador} x  {intMultiplicando} = {intMultiplicador * intMultiplicando}')
      intMultiplicando += 1

   print('FIM DA TABUADA...')