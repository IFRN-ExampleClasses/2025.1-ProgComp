'''
   Dado que um número primo é um número que só possui dois divisores 
   (1 e ele mesmo), faça um programa que solicite ao usuário um número 
   inteiro e informe se ele é primo ou não.
'''
import sys

try:
   intNumero = int(input('Informe um número: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if intNumero < 2:
      sys.exit('ERRO: Informe um inteiro >= 2 ...')
   
   '''   
   intContDiv = 1 # Contador de Divisores
   intDivisor = 2 # Divisor inicial (considera 1 como primeiro divisor)

   while intDivisor <= intNumero:
      # Verifica se o resto da divisão do numero pelo divisor é zero.
      if intNumero % intDivisor == 0:
         intContDiv += 1
      
      # Interrompe o laço quando a quantidade de divisores passa de 2
      if intContDiv > 2: break

      intDivisor += 1
   '''
   intContDiv = 1 # Contador de Divisores

   for  intDivisor in range (2, intNumero + 1):
      # Verifica se o resto da divisão do numero pelo divisor é zero.
      if intNumero % intDivisor == 0:
         intContDiv += 1

      # Interrompe o laço quando a quantidade de divisores passa de 2
      if intContDiv > 2: break

   if intContDiv == 2:
      print(f'O número {intNumero} é Primo...')
   else:
      print(f'O número {intNumero} não é Primo...')
