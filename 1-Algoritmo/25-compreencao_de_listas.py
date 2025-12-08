#### Compreensão de listas 
# exibir o quadrado dos números em uma lista
# num_list = [1,2,3,4,5]

# quadrado = [num ** 2 for num in num_list]
# print(quadrado)

# # criar uma lista de numeros pares entre 1 e 20
# pares = [num for num in range(21) if num % 2 == 0]
# print(pares)

# # contar a quantidade de vogais em uma frase
# vogais = [
#     'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', 'à', 'è', 'ì', 'ò', 'ù', 'À', 'È', 'Ì', 'Ò', 'Ù', 'ã', 'õ', 'Ã', 'Õ', 'â', 'ê', 'ô', 'Â', 'Ê', 'Ô'
# ]
# print('Digite uma frase:')
# frase = input()
# # lista com as vogais encontradas na frase
# lista_vogais = [v for v in frase if v in vogais] 
# print(f'A frase possui {len(lista_vogais)} vogais.')
# print(f'As vogais são: {lista_vogais}')

# operações distributivas entre os valores de duas listas
distributiva = [k * m for k in [5, 2, 3] for m in [30, 20, 10]]
print(distributiva)