'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
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
   # Item 02
   '''
   lstValores = list()
   for _ in range(intN):
      intValor = random.randint(-100, 100)
      lstValores.append(intValor)
   '''
   lstValores = [ random.randint(-100, 100) for _ in range(intN) ]

   print(lstValores)

   # ----------------------------------------------------------------------
   # Item 03
   '''
   lstPares = list()
   for intValor in lstValores:
      if intValor % 2 == 0:
         lstPares.append(intValor)
   '''
   lstPares = [ intValor for intValor in lstValores if intValor % 2 == 0 ]
   
   print(lstPares)

