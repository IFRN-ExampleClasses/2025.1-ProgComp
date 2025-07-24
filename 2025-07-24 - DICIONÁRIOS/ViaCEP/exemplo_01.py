import requests, sys

strCEP = input('Informe o CEP: ')

try:
   reqHTTP = requests.get(f'https://viacep.com.br/ws/{strCEP}/json/')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   if reqHTTP.status_code != 200:
      sys.exit('\nErro na Requisição...')

   print(f'\n{reqHTTP}')
   print(f'\n{reqHTTP.json()}')
