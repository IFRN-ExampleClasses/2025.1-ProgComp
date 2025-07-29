import sys, funcoes

try:
   intE1 = int(input('Informe a nota da Etapa 1: '))
   intE2 = int(input('Informe a nota da Etapa 2: '))
except ValueError:
   sys.exit('\nERRO: Informe valores inteiros válidos...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...')
else:
   try:
      intMediaFinal = funcoes.mediaIFRN_v1(intE1, intE2)
   except Exception as erro:
      print(erro)
   else:
      print(f'\nMédia Final = {intMediaFinal}')