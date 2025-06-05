'''
   Os primeiros dois números consecutivos que podem ser decompostos 
   como apenas dois fatores primos são 14 = (2 * 7) e 15 = (3 * 5).

   Faça um programa que recebe a quantidade n de fatores primos que 
   um número pode ter. 
   
   O programa deve listar os primeiros n números consecutivos que 
   atendem ao critério.
'''
import sys, math

try:
   intQtFatores = int(input('Digite a quantidade de fatores primos que um número pode ter: '))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
	...