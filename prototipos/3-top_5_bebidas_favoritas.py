#### Lista de 5 bebidas favoritas

bebidas = []

for i in range(5):
    nome_bebida = input(f"Digite o nome da bebida favorita {i + 1}: ") # solicitando o nome da bebida e informa quantas tem na lista
    bebidas.append(nome_bebida)

bebidas.sort() # ordenando a lista em ordem alfabética
print("\nSuas 5 bebidas favoritas são:")
for bebida in bebidas:
    print(f"- {bebida}")

print("Saúde!")
