'''
   Programa para classificar um triângulo quanto aos ângulos.

   - O programa deverá solicitar 3 ângulos inteiros positivos;
   - Para ser um triângulo, a soma dos ângulos deve ser igual a 180;
   
   - Retângulo..: Possui um ângulo interno reto (igual a 90).
   - Obtusângulo: Possui um ângulo interno obtuso (maior que 90).
   - Acutângulo.: Possui todos os ângulos internos agudos (menores que 90).
'''
import sys

# Solicitar os 3 ângulos do triângulo
angA = int(input('Digite o ângulo A: '))
angB = int(input('Digite o ângulo B: '))
angC = int(input('Digite o ângulo C: '))

# Verificando se os ângulos são positivos
if (angA <= 0) or (angB <= 0) or (angC <=0):
   sys.exit('ERRO: Um ou mais ângulos não são positivos.')

# Verificar se a soma dos ângulos é igual a 180
if angA + angB + angC != 180:
   sys.exit('ERRO: A soma dos ângulos deve ser 180.')

# Classificar o triângulo com base nos ângulos
if angA == 90 or angB == 90 or angC == 90:
   print('O triângulo é Retângulo.')
elif angA > 90 or angB > 90 or angC > 90:
   print('O triângulo é Obtusângulo.')
else:
   print('O triângulo é Acutângulo.')
