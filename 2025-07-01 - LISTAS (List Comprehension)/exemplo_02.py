'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);
   
      2) Gere uma lista com N valores inteiros aleatórios entre 0 e 1.000 (inclusive)
         sem repetições;

      3) A partir da lista gerada, gere uma segunda uma lista com as raízes quadradas 
         dos valores da lista anterior;
'''
import sys, random, math

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
   # Item 2
   lstValores = random.sample(range(1001), intN)

   print(lstValores)

   # ----------------------------------------------------------------------
   # Item 3
   '''
   lstRaizes = list()
   for intValor in lstValores:
      floatRaiz = math.sqrt(intValor)

      lstRaizes.append(floatRaiz)
   '''
   lstRaizes = [ math.sqrt(intValor) for intValor in lstValores ]

   print(lstRaizes)