'''
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   PROGRAMAÇÃO  
   PROGRAMAÇÃ  
   PROGRAMAÇ
   ...  
   PROG
   PRO
   PR
   P
'''

strTexto = input('Digite um texto: ')

iPosicao = len(strTexto)

while iPosicao > 0:
   print(strTexto[0:iPosicao])
   iPosicao -= 1