import sys

try:
   intDividendo = int(input('Digite o Dividendo: '))
   intDivisor   = int(input('Digite o Divisor..: '))
   fltResultado = intDividendo / intDivisor
except ValueError:
   print('ERRO: Informe um valor que possa ser convertido em Inteiro.')
except ZeroDivisionError:
   print('ERRO: Não existe divisão por ZERO.')
except:
   print(f'ERRO: {sys.exc_info()}')
else:
   print(fltResultado)