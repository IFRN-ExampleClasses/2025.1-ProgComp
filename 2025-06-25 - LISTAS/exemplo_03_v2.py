'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista onde cada posição será 
         uma sub-lista com 3 posições:

         a) A primeira posição será o número anterior ao número da lista inicial;
         b) A segunda posição será o número da lista inicial; 
         c) A terceira posição será o número seguinte ao número da lista inicial.
'''
import sys, random

try:
   intN = int(input('Informe o valor de N: '))
except ValueError:
   sys.exit('\nERRO: Informe um valor inteiro válido...\n')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...\n')
else:
   if intN <= 0 or intN > 100:
      sys.exit('\nERRO: Informe um valor entre 1 e 100...\n')

   # ----------------------------------------------------------------------
   lstValores = list()
   lstTrios   = list()

   for _ in range(intN):
      intValor = random.randint(-100, +100)

      lstValores.append(intValor)

      lstTrios.append([intValor-1, intValor, intValor+1])

   print(lstValores)

   print(lstTrios)