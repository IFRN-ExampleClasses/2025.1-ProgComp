'''
   Considerando que o fatorial de um número é dado por:

   n!= n * (n-1) * (n-2) * (n-3) * … * 1

   Faça um programa que solicite um valor inteiro ao usuário e 
   em seguida calcule e exiba o fatorial do número informado.
'''
import sys

try:
   intNumero = int(input('Informe um número: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intNumero < 0:
      sys.exit('ERRO: Não existe fatorial para números negativos ...')
   
   if intNumero < 2:
      sys.exit(f'{intNumero}! = 1')

   intFatorial = intNumero
   intAuxiliar = intNumero - 1

   while intAuxiliar >= 2:
      intFatorial *= intAuxiliar
      intAuxiliar -= 1

   print(f'{intNumero}! = {intFatorial}')