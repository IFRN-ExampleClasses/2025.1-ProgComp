import os, sys, statistics
from datetime import datetime
strDir = os.path.dirname(__file__)
try:
   arqEntrada = open(f'{strDir}\\cotacao_dolar.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não existe...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...')
else:
   lstCabecalhos = arqEntrada.readline().strip().split(';')
   lstDados = list()
   while True:
      strLinha = arqEntrada.readline().strip()
      if not strLinha: break
      lstAux = strLinha.split(';')
      lstDados.append([float(lstAux[0].replace(',', '.')), float(lstAux[1].replace(',', '.')), datetime.strptime(lstAux[2], '%d/%m/%Y').date()])
setAnos = {dado[2].year for dado in lstDados}
lstMeses = ['Janeiro', 'Fevereiro', 'Março'   , 'Abril'  , 'Maio'    , 'Junho',  'Julho'  , 'Agosto'   , 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for intAno in setAnos:
   lstDadosAno = list(filter(lambda dado: dado[2].year == intAno, lstDados))
   lstDadosAno.sort(key=lambda dado: dado[2])
   arqSaida = open(f'{strDir}\\cotacao_dolar_{intAno}.csv', 'w', encoding='utf-8')
   arqSaida.write(';'.join(lstCabecalhos)+'\n')
   for dado in lstDadosAno: arqSaida.write(f'{dado[0]:.4f},{dado[1]:.4f},{dado[2].strftime('%d-%m-%Y')}\n')
   arqSaida.close()
   print(f'\nArquivo \'cotacao_dolar_{intAno}.csv\' criado com sucesso!')
   lstMediasMensais = list()
   for intMes in range(1, 13):
      lstDadosMes = list(filter(lambda dado: dado[2].month == intMes, lstDadosAno))
      if lstDadosMes:
         fltSomaCompra = statistics.mean(dado[0] for dado in lstDadosMes)
         fltSomaVenda  = statistics.mean(dado[1] for dado in lstDadosMes)
         lstMediasMensais.append([f'{fltSomaCompra:.4f}', f'{fltSomaVenda:.4f}', lstMeses[intMes-1]])
      arqSaida = open(f'{strDir}\\media_cotacao_{intAno}.csv', 'w', encoding='utf-8')
      arqSaida.write('Mês;Média Compra;Média Venda\n')
      for media in lstMediasMensais: arqSaida.write(f'{media[0]};{media[1]};{media[2]}\n')
      arqSaida.close()
   print(f'Arquivo \'media_cotacao_{intAno}.csv\' criado com sucesso!')