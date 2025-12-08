#### Estrutura de Repetição WHILE ####

## Exemplo 1: Contador de 1 a 100

# num = 1

# while (num <= 100):
#     print(num)
#     num += 1

# print('Fim do Programa!')

##################################################

## 

nome = None

while True:
    print("Digite seu nome ou x para sair:")
    nome = input()

    if nome == 'x' or nome == 'X':
        break

    print(f"Olá, {nome}!")

print("Ate mais!")