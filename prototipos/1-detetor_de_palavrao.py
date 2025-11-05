#### 

palavroes = ('caralho', 'merda', 'porra', 'puta', 'bosta', 'foda', 'cu', 'cuzão', 'arrombado', 'pqp', 'vai se foder', 'puta que pariu')


while True:
    print("=======DIGITE X PARA SAIR=======")
    
    nome = input("Digite o seu nome: ")
    if nome == 'x' or nome == 'X':
        break

    msg = input("Digite a sua mensagem: ")

    for palavrao in palavroes:
        if palavrao in msg.lower(): # Verifica se há palavrões na mensagem
            print("Mensagem bloqueada! Por favor, evite usar palavrões.")
            break
    else:
        print(f"{nome}, sua mensagem foi enviada com sucesso!")