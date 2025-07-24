import sys, requests

from codigos_http import *

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

try:
   reqHTTP = requests.get(strURL)
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   dictCartola = reqHTTP.json()
   #print(dictCartola['clubes'])
   #exit()
   
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
   dictInfoClube = dict(filter(lambda clube: clube[1]['nome_fantasia'].lower() == strNomeClube, 
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
      fltPontuacaoAtleta = int(round(atleta['jogos_num'] * atleta['media_num'],0))
      print(f'{atleta['nome']} ({atleta['apelido']}) - {strPosicaoAtleta} - {fltPontuacaoAtleta} pontos')   
