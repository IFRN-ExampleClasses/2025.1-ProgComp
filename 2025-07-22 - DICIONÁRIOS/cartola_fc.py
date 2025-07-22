import os, sys, json

strDirApp = os.path.dirname(__file__)

strNomeArq = f'{strDirApp}//cartola_fc_2024.json'

try:
   arqInput = open(strNomeArq, 'r', encoding='utf-8')
   strDados = arqInput.read()
   dictCartola = json.loads(strDados)
   arqInput.close()
except  FileNotFoundError:
   sys.exit('ERRO: Arquivo não existe...')
except json.JSONDecodeError:
   sys.exit('ERRO: O conteúdo do arquivo não está no formato correto...')
except Exception as erro:
   sys.exit(f'ERRO: {erro}...')
else:
   lstChaves = list(dictCartola.keys()) # ['clubes', 'posicoes', 'status', 'atletas']

   '''
      dictCartola = { 'clubes': {...}, 'posicoes': {...}, 'status':{...}, 'atletas': [...] }

      dictCartola['clubes']    -> dicionário (k:v)
      dictCartola['posicoes']  -> dicionário (k:v)
      dictCartola['status']    -> dicionário (k:v)
      dictCartola['atletas']   -> lista (índice -> dicionário (k:v))
   '''
   # Informando o nome do Clube
   strClube = input('\nInforme o nome do Clube: ').strip().lower()

   # Obtendo o ID do clube informado

   # Listando os atletas do Clube informado

