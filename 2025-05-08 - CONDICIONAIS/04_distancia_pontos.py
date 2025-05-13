'''
   Programa para calcular a distância entre dois pontos no plano cartesiano.

   - O programa deverá solicitar as duas coordenadas (xA,yA) do ponto A;
   - O programa deverá solicitar as duas coordenadas (xB,yB) do ponto B;

   - Calcular a distância entre os pontos (qual fórmula usar????)
'''

# Solicitar as coordenadas do ponto A
coordXA = float(input('Digite a coordenada X do ponto A: '))
coordYA = float(input('Digite a coordenada Y do ponto A: '))

# Solicitar as coordenadas do ponto B
coordXB = float(input('Digite a coordenada X do ponto B: '))
coordYB = float(input('Digite a coordenada Y do ponto B: '))

# Calcular a distância entre os pontos A e B
distancia = ((coordXB - coordXA)**2 + (coordYB - coordYA)**2)**0.5

# Exibir o resultado
print(f'A distância entre os pontos A e B é:{distancia}')
