# ## Condicionais

# # condicionais simples
# algoritmo "Condicional Simples" para calcular a media de duas notas e dizer se o aluno foi aprovado


# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# media = (n1 + n2) /2

# #
# if media >= 5:
#     print("Parabens, você foi aprovado!")

# print("A sua média é: {}".format(media))

# # condicionais composto
# algoritmo "Condicional Composto" para calcular a media de duas notas e dizer se o aluno foi aprovado ou reprovado

# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# media = (n1 + n2) /2

# #
# if media >= 5:
#     print("Parabens, você foi aprovado!")
# else:
#     print("Infelizmente você foi reprovado!")

# print("A sua média é: {}".format(media))

# # condicionais encadeado
# algoritmo "Condicional encadeado" para calcular a media de duas notas e dizer se o aluno foi aprovado, reprovado ou se está de recuperação

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) /2

#
if media >=7:
    print("Parabens, você foi aprovado!")
elif media >=4 and media <7:
    print("Você está de recuperação!")
else:
    print("Infelizmente você foi reprovado!")

print("A sua média é: {}".format(media))
