'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''
import sys

try:
   intValorA = int(input('Digite o primeiro número inteiro positivo: '))
   intValorB = int(input('Digite o segundo número inteiro positivo.: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   # Verifica se os números são positivos
   if intValorA <=0 or intValorB <= 0:
      sys.exit('ERRO: Informe um valor positivo...')
   
   intAux_A = intValorA
   intAux_B = intValorB

   # Algoritmo de Euclides usando while
   while intAux_B != 0:
      intAux_A, intAux_B = intAux_B, intAux_A % intAux_B 
      
   # Impressão no formato desejado
   print(f'MDC({intValorA}, {intValorB}) = {intAux_A}')   