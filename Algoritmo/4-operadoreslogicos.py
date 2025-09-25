# ## Operadores Lógicos

# # um algoritmo que avalia a idade e altura de uma pessoa para determinar se ela pode participar de uma atividade
# a pessoa deve ter +18 anos  e mais de 1.70m de altura

# idade = 20
# altura = 1.70

# resultado = (idade >= 18) and (altura >= 1.70)
# msg = "pode participar da atividade? " + str(resultado)

# print("Idade:", idade)
# print("Altura:", altura)
# print(msg)

# # um algoritmo de disparo de alarme
# o alarme dispara se a porta ou a janela forem abertas

# porta = 'f'
# janela = 'f'

# alarme = (porta == 'a') or (janela == 'a')
# msg = "Alarme disparado? " + str(alarme)

# print(msg)

# # um algoritmo que verifica se uma pessoa tem ou não dinheiro para comprar um produto

tem_dinheiro = True

msg = "Tem dinheiro? " + str(not tem_dinheiro)
print(msg)