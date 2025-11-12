#### módulo random em Python
import random as rd


lista = [1,2,3,44,55,6,22,6,66,45,32,11,78,77,23,90,34,12,5,8,9,10,15,27,39,48,50]

## randint
print("=========Gerar cinco números inteiros aleatórios entre 1 e 10=========")
for i  in range(3):
    n = rd.randint(1, 10)
    print(f'Número gerado aleatóriamente: {n}')

## random
print("\n=========Gerar números de ponto flutuante aleatórios=========") # com o random não é possível definir o intervalo
valor = rd.random()
print(f'Número gerado aleatóriamente: {round(valor * 10, 3)}') # multiplicando por 10 para ampliar o intervalo - round para arredondar

## uniform
print("\n=========Gerar números de ponto flutuante aleatórios entre 1 e 10=========") # com o uniform é possível definir o intervalo
valor2 = rd.uniform(1, 10)
print(f'Número gerado aleatóriamente: {round(valor2, 3)}') # round para arredondar

## choice
print("\n=========Escolher um número aleatório de uma lista=========")
valor3 = rd.choice(lista)
print(f'\nLista: {lista}')
print(f'\nNúmero aleatório escolhido da lista: {valor3}')

## sample
print("\n=========Escolher números aleatórios de uma lista=========")
valor4 = rd.sample(lista, 3) # escolhe 3 números aleatórios da lista
print(f'\nLista: {lista}')
print(f'\nNúmeros aleatórios escolhidos da lista: {valor4}')

## shuffle
print("\n=========Embaralhar uma lista=========")
print(f'\nLista original: {lista}')
valor5 = rd.shuffle(lista) # embaralha a lista
print(f'\nLista embaralhada: {lista}')