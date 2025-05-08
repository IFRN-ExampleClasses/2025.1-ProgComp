'''
   Programa para calcular a média de uma disciplina
   semestral no IFRN.

   As notas devem ser inteiras e entre 0 e 100 (inclusive).

   Caso a média seja igual ou superior a 60 o aluno estará
   Aprovado; Caso a média seja igual ou superior a 20 o aluno
   estará em Prova Final e os demais casos o aluno estará Reprovado. 
'''
import sys

# Informando a nota da Etapa 1
etapa1 = int(input('Informe a nota da Etapa 1: '))
if etapa1 < 0 or etapa1 > 100:
   sys.exit('ERRO: Nota Etapa 1 Inválida. Informe nota entre 0 e 100.')

# Informando a nota da Etapa 2
etapa2 = int(input('Informe a nota da Etapa 2: '))
if etapa2 < 0 or etapa2 > 100:
   sys.exit('ERRO: Nota Etapa 2 Inválida. Informe nota entre 0 e 100.')

# Calculando a média
media = int( round( (etapa1 * 2 + etapa2 * 3) / 5, 0) )
print(f'Média do Aluno: {media}')

# Verificando a situação do aluno
if media >= 60:
   print('Aluno Aprovado.')
elif media >= 20:
   print('Aluno em Prova Final.')
else:
   print('Aluno Reprovado.')