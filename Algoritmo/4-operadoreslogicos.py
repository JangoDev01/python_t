# Operadores Lógicos

# um algoritmo que avalia a idade e altura de uma pessoa para determinar se ela pode participar de uma atividade
# a pessoa deve ter +18 anos  e mais de 1.70m de altura

idade = 20
altura = 1.70

resultado = (idade >= 18) and (altura >= 1.70)
ms = "pode participar da atividade? " + str(resultado)

print("Idade:", idade)
print("Altura:", altura)
print(ms)