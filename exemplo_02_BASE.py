'''
   Programa para executar uma potenciação de 2 números inteiros
   utilizando apenas o operador produto (*)
'''
import sys

try:
   intBase     = int(input('Informe a Base....: '))
   intPotencia = int(input('Informe a Potência: '))
except ValueError:
   sys.exit('ERRO: Informe um valor inteiro...')
except Exception as e:
   sys.exit(f'ERRO {e}')
else:  
   if intBase < 0:
      sys.exit('ERRO: Informe um Multiplicador inteiro...')

   if intPotencia < 0:
      sys.exit('ERRO: Informe um Multiplicando inteiro...')

   intContador = 1
   intPotenciacao  = 1
   while intContador <= intPotencia:
      intPotenciacao  *= intBase
      intContador += 1

   print(f'{intBase} ** {intPotencia} = {intPotenciacao}')