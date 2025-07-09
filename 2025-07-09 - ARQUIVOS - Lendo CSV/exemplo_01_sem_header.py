import os, sys

# Obtendo o diretório onde o programa está salvo
strDir = os.path.dirname(__file__)

# Abrindo e lendo o arquivo
try:
   arqLeitura = open(f'{strDir}\\times.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   lstTimes = list()
   while True:
      # Lendo a linha e armazendo na variável
      strLinha = arqLeitura.readline().strip()   
      # Interrompe o laço quando não há conteúdo na linha (EOF)
      if not strLinha: break
      # Transforma a string em uma lista convertendo os valores para inteiro
      lstAux = [int(i) if i.isdigit() else i for i in strLinha.split(';')]
      # Adicionando os dados na lista
      lstTimes.append(lstAux)
   arqLeitura.close()

# Adionando a pontuação e o saldo de gols
for time in lstTimes:
   time.insert(4, time[1]*3 + time[2])
   time.append(time[5] - time[6])

# Classificando os times
lstTimes.sort(key=lambda time: (time[4], time[1], time[7], time[5]), reverse=True)

# Imprimindo o conteúdo da lista
for time in lstTimes:
   print(time)