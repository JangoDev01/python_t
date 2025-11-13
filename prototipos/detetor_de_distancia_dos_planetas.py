### Detetor de distância dos planetas ao Sol
##
planetas = ['mercurio', 'venus', 'terra', 'marte', 'jupiter', 'saturno', 'urano', 'netuno', 'plutão']
distancias = [57.9, 108.2, 149.6, 227.9, 778.5, 1433.5, 2872.5, 4495.1, 5906.4] # em milhões de km

while True:
    print("-------------------------------------------------------\n")
    print("Digite 'sair' para encerrar o programa\n")
    planeta_atual = input("Em que planeta vecê está?: \n")
    if planeta_atual.lower() == 'sair':
        break
    encontrado = False

    for planeta in planetas:
        if planeta in planeta_atual.lower(): # comparando o planeta digitado com o planeta da lista
            indice = planetas.index(planeta_atual.lower()) # pegando o índice do planeta na lista
            distancia = distancias[indice] # pegando a distância do planeta na lista de distâncias
            print(f'O planeta {planeta_atual} está a {distancia} milhões de km do Sol.')
            encontrado = True
            break
    
    if not encontrado:
        print("Planeta não encontrado. Tente novamente.")
