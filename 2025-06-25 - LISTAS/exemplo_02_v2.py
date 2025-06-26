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
   lstValores = list()
   lstRaizes  = list()

   intContador = 1
   while intContador <= intN :
      # Gerando um número aleatório entre 0 e 1000 
      intValor = random.randint(0, 1000)

      # Verificando de o valor gerado não está em lstValores
      if intValor not in lstValores:
         # Adiciona o valor em lstValores
         lstValores.append(intValor)
         # Calcula a raiz quadrada do valor gerado
         floatRaiz = math.sqrt(intValor)
         # Adiciona a raiz quadrada em lstRaizes
         lstRaizes.append(floatRaiz)
         # Incrementa o contador de números distintos gerados
         intContador += 1

   print(lstValores)

   print(lstRaizes)