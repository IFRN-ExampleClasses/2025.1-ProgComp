'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   P
   PR
   PRO
   PROG
   ...
   PROGRAMAÇÃO  
'''

strTexto = input('Digite um texto: ')

iPosicao = 0

while iPosicao < len(strTexto):
   print(strTexto[0:iPosicao + 1])
   iPosicao += 1