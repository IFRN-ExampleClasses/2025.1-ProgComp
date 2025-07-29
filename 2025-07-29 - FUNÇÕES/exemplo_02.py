import sys
from funcoes import *

try:
   intE1 = int(input('Informe a nota da Etapa 1: '))
   intE2 = int(input('Informe a nota da Etapa 2: '))
except ValueError:
   sys.exit('\nERRO: Informe valores inteiros válidos...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...')
else:
   try:
      tuplaAluno = mediaIFRN_v3(intE1, intE2)
   except Exception as erro:
      print(erro)
   else:
      print(tuplaAluno)
      print(f'\nMédia Final = {tuplaAluno[0]}')
      print(f'Situacao    = {tuplaAluno[1]}')
