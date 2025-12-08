#### 

n1 = [5,7,8,6,9,10,4,2]
n2 = [1,5,3,7,9,2,4,6,8]
valores = n1 + n2 # concatenar listas

## exibindo dados da listas
print(valores) # exibir a lista completa
print(valores[0:3]) # acessar os três primeiros elementos da lista apartir do índice 0
print(valores[3:10]) # acessar os elementos da lista do índice 3 ao 9
print(valores[-1]) # acessar o último elemento da lista - -2 é o penúltimo, -3 o antepenúltimo e assim por diante
print(valores[-5:]) # acessar os elementos da lista a partir do quinto elemento até o final
print(len(valores)) # tamanho da lista
print(sorted(valores, reverse=True)) # tamanho da lista em ordem decrescente
print(sorted(valores)) # ordenar a lista sem alterar a lista original
print(sum(valores)) # soma dos valores da lista
print(min(valores)) # menor valor da lista
print(max(valores)) # maior valor da lista

## manipulação de listas
valores[0] = 3 # alterar o valor do primeiro elemento da lista
valores.append(15) # adicionar um elemento ao final da lista
print(valores)
valores.pop() # remover o último elemento da lista
print(valores)
valores.pop(2) # remover o elemento do índice 2 da lista
print(valores)
valores.insert(3, 33) # inserir o valor 33 no índice 3 da lista
print(valores)
print(12 in valores) # verificar se o valor 12 está na lista
print(7 in valores) # verificar se o valor 7 está na lista


### pegando pesado
##
planetas = ['mercurio', 'venus', 'terra', 'marte', 'jupiter', 'saturno', 'urano', 'netuno', 'plutão']

for planeta in planetas:
    print(planeta)
    