'''
   Fazer um programa que faça as seguintes operações.

   1) A partir do conteúdo do arquivo cotacao_dolar.csv gerar uma lista onde cada item
      dessa lista será uma sub-lista com os valores de cada linha do arquivo.

      a) Os valores estão separados por ";";
      b) Os dois primeiros valores são valores do tipo FLOAT;
      c) O terceiro valor é do tipo DATE;
      

   2) Gerar arquivos para cada ano. Salvar o arquivo com o mesmo nome do arquivo que 
      foi aberto na questão 1, adionando no final do nome o sufixo "_nnnn" onde "nnnn" 
      corresponde ao ano das cotações;


   3) Gerar arquivos por ano com as médias das cotações mensais. Salve os arquivos com 
      o nome "media_cotacao_nnnn.csv" onde "nnnn" corresponde ao ano. Cada linha do arquivo
      deverá ter o valor médio de compra, o valor Médio de Venda e o nome do mês. 
      Separe os valores da linha por ";";
'''
import os, sys, statistics
from datetime import datetime

# Diretório onde se encontra a aplicação
strDir = os.path.dirname(__file__)

# ----------------------------------------------------------------------
# 01 - Abrindo o arquivo e gerando uma lista com o conteúdo do arquivo
try:
   arqEntrada = open(f'{strDir}\\cotacao_dolar.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não existe...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}...')
else:
   # Lista com os cabecalhos 
   lstCabecalhos = arqEntrada.readline().strip().split(';')

   # Lista com os dados
   lstDados = list()
   while True:
      strLinha = arqEntrada.readline().strip()
      if not strLinha: break

      lstAux = strLinha.split(';')
      lstDados.append([float(lstAux[0].replace(',', '.')), 
                float(lstAux[1].replace(',', '.')),
                datetime.strptime(lstAux[2], '%d/%m/%Y').date()
               ])


# ----------------------------------------------------------------------
# Criar um set com os anos a ser usado nas questões 02 e 03 
setAnos = {dado[2].year for dado in lstDados}


# ----------------------------------------------------------------------
# 02 - Gerando os arquivos de cotações por ano
for intAno in setAnos:
   # Filtrar os dados por ano
   lstDadosAno = list(filter(lambda dado: dado[2].year == intAno, lstDados))
    
   # Ordenar os dados pela data (posição 2)
   lstDadosAno.sort(key=lambda dado: dado[2])
    
   # Criando o arquivo onde os dados serão armazenados
   arqSaida = open(f'{strDir}\\cotacao_dolar_{intAno}.csv', 'w', encoding='utf-8')

   # Escrevendo o cabeçalho
   arqSaida.write(';'.join(lstCabecalhos)+'\n')

   # Escrevendo os dados
   for dado in lstDadosAno:
      arqSaida.write(f'{dado[0]:.4f},{dado[1]:.4f},{dado[2].strftime('%d-%m-%Y')}\n')
   
   # Fechando o arquivo
   arqSaida.close()
   print(f'Arquivo \'cotacao_dolar_{intAno}.csv\' criado com sucesso!')


# ----------------------------------------------------------------------
# 03 - Gerando os arquivos de médias das cotações mensais por ano

# Nome do mês usando uma lista com os nomes dos meses
lstMeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for intAno in setAnos:
   # Filtrar os dados por ano
   lstDadosAno = list(filter(lambda dado: dado[2].year == intAno, lstDados))
    
   # Loop para processar os dados por mês
   lstMediasMensais = list()
   for intMes in range(1, 13):
      # Filtrando os dados anuais mês a mês
      lstDadosMes = list(filter(lambda dado: dado[2].month == intMes, lstDadosAno))

      # Usando statistics.mean() para calcular a média das cotações de compra e venda
      if lstDadosMes:
         fltSomaCompra = statistics.mean(dado[0] for dado in lstDadosMes)
         fltSomaVenda  = statistics.mean(dado[1] for dado in lstDadosMes)

         lstMediasMensais.append([lstMeses[intMes-1], f'{fltSomaCompra:.4f}', f'{fltSomaVenda:.4f}'])
    
      # Criar o arquivo para salvar os resultados
      arqSaida = open(f'{strDir}\\media_cotacao_{intAno}.csv', 'w', encoding='utf-8')
    
      # Escrever o cabeçalho
      arqSaida.write('Mês;Média Compra;Média Venda\n')
    
      # Escrever os dados das médias
      for media in lstMediasMensais:
         arqSaida.write(f'{media[0]};{media[1]};{media[2]}\n')
    
      # Fechar o arquivo
      arqSaida.close()
      print(f'Arquivo \'media_cotacao_{intAno}.csv\' criado com sucesso!')