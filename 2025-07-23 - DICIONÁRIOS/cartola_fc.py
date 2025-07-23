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
   #lstChaves = list(dictCartola.keys())
   #print(lstChaves) # ['clubes', 'posicoes', 'status', 'atletas']
   '''
      dictCartola = { 'clubes':{...}, 'posicoes':{...}, 'status':{...}, 'atletas':[...] }

      dictCartola['clubes']    -> dicionário (k:v)
      dictCartola['posicoes']  -> dicionário (k:v)
      dictCartola['status']    -> dicionário (k:v)
      dictCartola['atletas']   -> lista (índice -> dicionário (k:v))
   '''

   # Informando o nome do Clube
   strNomeClube = input('\nInforme o nome do Clube: ').strip().lower()

   # Obtendo o ID do clube informado
   dictInfoClube = dict(filter(lambda clube: clube[1]['nome'].lower() == strNomeClube, 
                        dictCartola['clubes'].items())).values()

   if not dictInfoClube:
      sys.exit('\nAVISO: Não existe o clube informado...')

   intIDClube = list(dictInfoClube)[0]['id']
   print(f'O ID do {strNomeClube.title()} é {intIDClube}\n')

   # Listando os atletas do Clube informado
   lstAtletasClube = list(filter(lambda atleta: atleta['clube_id'] == intIDClube, 
                          dictCartola['atletas']))
   
   lstAtletasClube.sort(key=lambda atleta: atleta['nome'])
   
   for atleta in lstAtletasClube:
      '''
         dictCartola['posicoes']  = 
         {
            '1': {'id': 1, 'nome': 'Goleiro' , 'abreviacao': 'gol'}, 
            '2': {'id': 2, 'nome': 'Lateral' , 'abreviacao': 'lat'}, 
            '3': {'id': 3, 'nome': 'Zagueiro', 'abreviacao': 'zag'}, 
            '4': {'id': 4, 'nome': 'Meia'    , 'abreviacao': 'mei'}, 
            '5': {'id': 5, 'nome': 'Atacante', 'abreviacao': 'ata'}, 
            '6': {'id': 6, 'nome': 'Técnico' , 'abreviacao': 'tec'}
         }
      '''
      strPosicaoAtleta   = dictCartola['posicoes'][str(atleta['posicao_id'])]['nome']
      # TODO: Obter a pontuação do atleta
      fltPontuacaoAtleta = ...
      print(f'{atleta['nome']} ({atleta['apelido']}) - {strPosicaoAtleta} - {fltPontuacaoAtleta} pontos')   
