'''
   Dado que uma Progressão Geométrica (P.G.) é a uma sequência numérica 
   cujo quociente (q) ou razão entre um número e outro (exceto o primeiro) 
   é sempre igual. Vale lembrar que essa razão é sempre constante e pode 
   ser qualquer número racional (positivos, negativos, frações) exceto o 
   número zero (0).

   Faça um programa que:
      a) Solicite ao usuário um valor inteiro inicial e a razão da P.G.;
      b) Solicite um novo valor inteiro positivo correspondente a quantidade 
         de elementos da PG e exiba os valores dessa P.G.;
      c) Informe se a P.G. é constante, oscilante, crescente ou decrescente;
      d) Calcule a soma dos elementos dessa P.G.;
      e) Solicite um outro valor inteiro n correspondente a enésima posição 
         de um elemento da P.G. e exibir o valor desse elemento.
'''
import sys

try:
   intValorInicial = int(input('Digite o Valor Inicial da P.G. .........: '))
   intRazao        = int(input('Digite a Razão da P.G. .................: '))
   intQtElementos  = int(input('Digite a Quantidade de Elementos da P.G.: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intRazao == 0:
      sys.exit('ERRO: A Razão deve ser diferente de ZERO...')

   if intQtElementos <= 0:
      sys.exit('ERRO: A quantidade de elementos deve ser POSITIVA...')

   intElementoPG = intValorInicial

   # Exibindo os elementos da P.G.
   print('\nElementos da P.G. :')
   print(f'{intElementoPG}, ', end = '')

   #intSoma = intElementoPG
   for _ in range(2, intQtElementos + 1):
      intElementoPG *= intRazao
      #intSoma       += intElementoPG    
      print(f'{intElementoPG}, ', end = '')

   # Informando se a P.G. é constante, oscilante, crescente ou decrescente
   if (intRazao == 1):
      print('\nA P.G. CONSTANTE.')
   elif (intRazao < 0):
      print('\nA P.G. OSCILANTE.')
   elif (intRazao > 1) and intValorInicial > 0:
      print('\nA P.G. CRESCENTE.')   
   else:
      print('\nA P.G. DECRESCENTE.')

   # Calculando a soma da P.G.
   floatSoma = (intValorInicial * ((intRazao ** intQtElementos) - 1)) / (intRazao - 1)
   print(f'\n\nSoma dos termos da P.G. = {floatSoma}')

   # Exibindo o n-ésimo elemento da P.G.
   while True:
      try:
         intPosicaoN = int(input('\nInforme a posição que se deseja saber o elemento da P.G. (>0): '))
      except ValueError:
         print('ERRO: Informe um inteiro válido...')
      except Exception as e:
         print(f'ERRO: {e}')
      else:
         if intPosicaoN > 0: break

   intElementoN = intValorInicial * (intRazao ** (intPosicaoN - 1))
   print(f'\nO elemento da posição {intPosicaoN} da P.G. é {intElementoN}')
