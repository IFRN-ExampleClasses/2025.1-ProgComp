'''
   Dada uma palavra chave, o programa só deve parar de pedir quando
   o usuário digitar a palavra chave

   palavra = '123Mudar'

   texto = input(...)
'''

strPalavraChave = '123Mudar'
strPalavraInfo  = ''

while strPalavraInfo != strPalavraChave:
   strPalavraInfo = input('Digite a Palavra Chave: ')

print('Você digitou a Palavra Chave...')