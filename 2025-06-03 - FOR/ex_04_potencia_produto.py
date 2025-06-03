'''
   Programa para executar uma potenciação de 2 números inteiros
   utilizando apenas o operador produto (*)

   base = 2
   potencia = 10
   r = base * base * base * ...
'''
import sys

try:
   intBase     = int(input('Digite a Base....: '))
   intPotencia = int(input('Digite a Potência: '))
except ValueError:
   sys.exit('ERRO: Não foi informado um valor inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intBase <= 0:
      sys.exit('ERRO: Informe uma Base Positiva...')

   if intPotencia <= 0:
      sys.exit('ERRO: Informe uma Potência Positiva...')

   intPotenciacao = 1
   intContador    = 1
   while intContador <= intPotencia:
      intPotenciacao *=  intBase
      intContador    += 1

   print(f'{intBase} ** {intPotencia} = {intPotenciacao}')
   