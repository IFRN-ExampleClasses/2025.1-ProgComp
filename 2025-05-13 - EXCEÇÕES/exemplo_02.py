import sys

try:
   intDividendo = int(input('Digite o Dividendo: '))
   intDivisor   = int(input('Digite o Divisor..: '))
   fltResultado = intDividendo / intDivisor
except Exception as tipoExcecao:
   print(f'ERRO: {tipoExcecao}')
   print(f'ERRO: {sys.exc_info()}')
else:
   print(fltResultado)