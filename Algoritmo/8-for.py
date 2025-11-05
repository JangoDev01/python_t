#### Estrutura de Repetição For ####

# lista = [1,2,3,4,5,6,7,8,9,10]
# palavra = 'Sim'

# for letra in palavra:
#     print(letra)

##################################

# for numero in range(11):
#     print(numero)

##################################

# nome = input("Digite seu nome: ")

# for x in range(10):
#     print(f"{x+1} {nome}!")

##################################

# for x in range(30, 0, -2):
#     print(x)

##################################

pedras = ('Rubi', 'Esmeralda', 'Safira', 'Diamante', 'Ametista', 'Topázio', 'Quartzo')

for pedra in pedras:
    if pedra == 'Diamante':
        continue # Pula a iteração quando encontrar Diamante
    print(pedra)
