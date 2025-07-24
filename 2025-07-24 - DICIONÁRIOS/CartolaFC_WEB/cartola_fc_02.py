import sys, requests

from codigos_http import *

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

try:
   reqHTTP = requests.get(strURL)
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   if reqHTTP.status_code != 200:
      sys.exit(f'\nERRO: {reqHTTP.status_code} -> {dictRetornoHTTP[reqHTTP.status_code]}\n')

   dictCartola = reqHTTP.json()

   print(dictCartola)