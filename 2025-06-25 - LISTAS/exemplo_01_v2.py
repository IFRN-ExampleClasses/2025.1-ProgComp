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
   
   lstValores = list()
   lstPares   = list()

   for _ in range(intN):
      # Gerando um número aleatório entre -100 e 100 
      intValor = random.randint(-100, 100)

      # Adicionando o número gerado em lstValores
      lstValores.append(intValor)

      # Adicionando o valor em lstPares se ele for par
      if intValor % 2 == 0:
         lstPares.append(intValor)

   print(lstValores)
   print(lstPares)

