'''
   Arquivo de Funções
'''

__all__ = ['mediaIFRN_v1', 'mediaIFRN_v2', 'mediaIFRN_v3']

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


# ----------------------------------------------------------------------
# Função que retorna a situação final do aluno
def _situacaoFinal(media: int) -> str:
   # Verificando se o argumento informado é do tipo INT
   if not isinstance(media, int):
      raise ValueError('\nERRO: O argumento \'media\' deve ser do tipo INT')

   # Verificando se o valor informado está entre 0 e 100
   if media<0 or media>100:
      raise Exception('\nERRO: O argumento \'media\' deve ser entre 0 e 100')

   # Verificando a situação do aluno
   if media >= 60:
      situacao = 'Aprovado'
   elif media >= 20:
      situacao = 'Prova Final'
   else:
      situacao = 'Reprovado'

   # Retornando a situacao ao programa
   return situacao


# ----------------------------------------------------------------------
# Função que calcula a média do IFRN - v3.0
def mediaIFRN_v3(nota1:int, nota2:int) -> int:
   # Verificando se os argumentos informados são do tipo INT e 
   # estão entre 0 e 100
   for nota, nome in [(nota1, 'nota1'), (nota2, 'nota2')]:
      if not isinstance(nota, int):
         raise ValueError(f'O argumento \'{nome}\' deve ser do tipo INT')
      if nota < 0 or nota > 100:
         raise Exception(f'O argumento \'{nome}\' deve ser entre 0 e 100')
      
   # Calculando a média
   media = int(round((nota1*2 + nota2*3)/5,0))
   
   # Obtendo a situação final do aluno
   situacao = _situacaoFinal(media)

   # Retornando o valor da média ao programa
   return (media, situacao)
