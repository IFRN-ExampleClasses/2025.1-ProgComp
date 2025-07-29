'''
   Arquivo de Funções
'''

# ----------------------------------------------------------------------
# Função que calcula a média do IFRN - v1.0
def mediaIFRN_v1(nota1:int, nota2:int) -> int:
   # Verificando se os argumentos informados são do tipo INT
   if not isinstance(nota1, int):
      raise ValueError('\nERRO: O argumento \'nota1\' deve ser do tipo INT')
   if not isinstance(nota2, int):
      raise ValueError('\nERRO: O argumento \'nota2\' deve ser do tipo INT')

   # Verificando se os valores informados estão entre 0 e 100
   if nota1<0 or nota1>100:
      raise Exception('\nERRO: O argumento \'nota1\' deve ser entre 0 e 100')
   if nota2<0 or nota2>100:
      raise Exception('\nERRO: O argumento \'nota2\' deve ser entre 0 e 100')
   
   # Calculando a média
   media = int(round((nota1*2 + nota2*3)/5,0))
   
   # Retornando o valor da média ao programa
   return media


# ----------------------------------------------------------------------
# Função que calcula a média do IFRN - v2.0
def mediaIFRN_v2(nota1:int, nota2:int) -> int:
   # Verificando se os argumentos informados são do tipo INT e 
   # estão entre 0 e 100
   for nota, nome in [(nota1, 'nota1'), (nota2, 'nota2')]:
      if not isinstance(nota, int):
         raise ValueError(f'O argumento \'{nome}\' deve ser do tipo INT')
      if nota < 0 or nota > 100:
         raise Exception(f'O argumento \'{nome}\' deve ser entre 0 e 100')
      
   # Calculando a média
   media = int(round((nota1*2 + nota2*3)/5,0))
   
   # Retornando o valor da média ao programa
   return media
