'''
   Fazer um programa que solicite ao usuário nomes de pessoas.

   O programa deverá parar de solicitar nomes quando o usuário digitar 'FIM'.

   No final o programa deverá listar os nomes informados.
'''

# Cria a variável do tipo lista
lstNomes = list()

while True:
   # Solicita o nome, removendo espaços em branco a esqueda e a direita
   strNome = input('Digite um nome: ').strip()

   # Verifica se foi digitado 'FIM' (compara em minúscula) para interromper o laço
   if strNome.lower() == 'fim': 
      break

   # Se houver caracteres na variável o seu conteúdo será adicionado na lista
   if len(strNome) > 0: 
      lstNomes.append(strNome)

# Imprime a lista
print(lstNomes)