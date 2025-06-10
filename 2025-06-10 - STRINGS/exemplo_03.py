'''
   Programa para verificar quantas vogais existem em uma string informada pelo usuário.
'''

strTexto = input('Digite um texto: ').upper()

strVogais = 'AEIOUÂÊÎÔÛÃÕÁÉÍÓÚÀÈÌÒÙÄËÏÖÜ'

intVogais = 0

for strLetra in strTexto:
   if strLetra in strVogais:
      intVogais += 1

print(f'O texto possui {intVogais} vogais')