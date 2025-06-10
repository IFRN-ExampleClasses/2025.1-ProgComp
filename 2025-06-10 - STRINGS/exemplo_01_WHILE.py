'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   R
   O
   G
   ...
   O  
'''

strTexto = input('Digite um texto: ')

'''
for strLetra in strTexto:
   print(strLetra)
'''

intPosicao = 0

while intPosicao < len(strTexto):
   print(strTexto[intPosicao])
   intPosicao += 1