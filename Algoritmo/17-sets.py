#### set

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))

# print('Ceres' in planeta_anao)

# for astro in planeta_anao:
#     print(astro)

## pegando os valores de uma lista para o nosso set
astros_lista = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(f'Lista: {astros_lista}', end=' Sets:')
astros_set = set(astros_lista)
print(astros_set)

## união de conjuntos
astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte','IO'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
print(astros1 | astros2)
print(astros1.union(astros2))

## intersecão de conjuntos ==> semelhanças entre os conjuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))

## diferença simetrica ==> diferença entre os conjuntos
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

## adicionando elementos no conjunto
astros1.add('Sol')
astros1.add('Urano')
#astros1.remove('Io') # da um erro se o elemento não estiver no set 
astros1.discard('Terra') # não da erro
astros1.pop() # remove um item aleatorio
print(astros1)