'''
   Dado que uma Progressão Aritmética (P.A.) é uma sequência de números 
   onde a diferença entre dois termos consecutivos é sempre a mesma e que 
   essa diferença constante é chamada de razão da P.A.

   Faça um programa que:
      a) Solicite ao usuário um valor inteiro inicial e a razão da P.A.;
      b) Solicite um novo valor inteiro positivo correspondente a quantidade 
         de elementos da P.A. e exiba os valores dessa P.A.;
      c) Informe se a P.A. é constante, crescente ou decrescente;
      d) Calcule a soma dos elementos dessa P.A.;
      e) Solicite um outro valor inteiro n correspondente a enésima posição 
         de um elemento da P.A. e exibir o valor desse elemento.
'''
import sys

try:
   intValorInicial = int(input('Digite o Valor Inicial da P.A. .........: '))
   intRazao        = int(input('Digite a Razão da P.A. .................: '))
   intQtElementos  = int(input('Digite a Quantidade de Elementos da P.A.: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intRazao == 0:
      sys.exit('ERRO: A Razão deve ser diferente de ZERO...')

   if intQtElementos <= 0:
      sys.exit('ERRO: A quantidade de elementos deve ser POSITIVA...')

   intElementoPA = intValorInicial

   # Exibindo os elementos da P.A.
   print('\nElementos da P.A. :')
   print(f'{intElementoPA}, ', end = '')
   
   for _ in range(2, intQtElementos + 1):
      intElementoPA += intRazao
      print(f'{intElementoPA}, ', end = '')

   # Informando se a P.A. é constante, crescente ou decrescente
   if (intRazao == 0):
      print('\nA P.A. CONSTANTE.')
   elif (intRazao > 0):
      print('\nA P.A. CRESCENTE.')
   else:
      print('\nA P.A. DECRESCENTE.')   

   # Calculando a soma da P.A.
   floatSoma = (intQtElementos * (intValorInicial + intElementoPA)) / 2
   print(f'\n\nSoma dos termos da P.A. = {floatSoma}')

   # Exibindo o n-ésimo elemento da P.A.
   while True:
      try:
         intPosicaoN = int(input('\nInforme a posição que se deseja saber o elemento da P.A. (>0): '))
      except ValueError:
         print('ERRO: Informe um inteiro válido...')
      except Exception as e:
         print(f'ERRO: {e}')
      else:
         if intPosicaoN > 0: break

   intElementoN = intValorInicial + ((intPosicaoN - 1) * intRazao)
   print(f'\nO elemento da posição {intPosicaoN} da P.A. é {intElementoN}')